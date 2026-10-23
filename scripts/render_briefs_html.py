#!/usr/bin/env python3
"""Render the Prodensa hub and one page per workshop folder.

Hub: site/index.html lists workshops/{title-slug}/ (a list of one is still a list).
Page: site/workshops/{title-slug}/index.html from brief-platform* in that folder.
Factory brief-a* stays off the site.

Usage (from Prodensa hub root):
  python3 scripts/render_briefs_html.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"
CODEBOOK = ROOT / "config" / "workshops.json"
WORKSHOPS = ROOT / "workshops"

# Upload order. Same files inside workshops/{slug}/{code}/.
SECTIONS = [
    ("diseno", "Diseño", "brief-platform.md"),
    ("problema", "Problema", "brief-platform-a1.md"),
    ("modulos", "Módulos", "brief-platform-a2.md"),
    ("filtros", "Filtros", "brief-platform-a3.md"),
    ("secuencia", "Secuencia", "brief-platform-spine.md"),
]

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
    '  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600'
    '&family=IBM+Plex+Sans:wght@400;600;700&family=IBM+Plex+Serif:wght@600;700'
    '&display=swap" rel="stylesheet" />'
)


def inline_md(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def is_table_sep(line: str) -> bool:
        s = line.strip()
        return bool(re.match(r"^\|?[\s:-]+\|[\s|:-]+$", s))

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            close_lists()
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                if is_table_sep(row):
                    i += 1
                    continue
                cells = [c.strip() for c in row.strip("|").split("|")]
                rows.append(cells)
                i += 1
            if not rows:
                continue
            out.append("<table>")
            out.append(
                "<thead><tr>"
                + "".join(f"<th>{inline_md(c)}</th>" for c in rows[0])
                + "</tr></thead>"
            )
            if len(rows) > 1:
                out.append("<tbody>")
                for row in rows[1:]:
                    out.append(
                        "<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in row) + "</tr>"
                    )
                out.append("</tbody>")
            out.append("</table>")
            continue

        if stripped == "---":
            close_lists()
            out.append("<hr />")
            i += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            # Page h1 is the workshop title. # → h2, ## → h3.
            tag = {1: "h2", 2: "h3"}.get(level, "h4")
            out.append(f"<{tag}>{inline_md(heading.group(2))}</{tag}>")
            i += 1
            continue

        ul = re.match(r"^[-*]\s+(.*)$", stripped)
        if ul:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(ul.group(1))}</li>")
            i += 1
            continue

        ol = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if ol:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(ol.group(2))}</li>")
            i += 1
            continue

        if not stripped:
            close_lists()
            i += 1
            continue

        close_lists()
        chunk = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt == "---"
                or nxt.startswith("|")
                or re.match(r"^#{1,4}\s+", nxt)
                or re.match(r"^[-*]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
            ):
                break
            chunk.append(nxt)
            i += 1
        para = " ".join(chunk)
        emph = len(para) > 2 and para.startswith("_") and para.endswith("_")
        if emph:
            para = para[1:-1]
        rendered = inline_md(para)
        if emph:
            rendered = f"<em>{rendered}</em>"
        out.append(f"<p>{rendered}</p>")

    close_lists()
    return "\n".join(out)


def page_shell(*, title: str, css_href: str, body: str, lang: str = "es") -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{html.escape(title)}</title>
  {FONT_LINK}
  <link rel="stylesheet" href="{css_href}" />
</head>
<body>
{body}
</body>
</html>
"""


def load_workshops() -> list[tuple[str, str, dict]]:
    if not CODEBOOK.is_file():
        raise SystemExit(f"Missing {CODEBOOK}")
    data = json.loads(CODEBOOK.read_text(encoding="utf-8"))
    rows: list[tuple[str, str, dict]] = []
    for code, entry in data.items():
        if not isinstance(entry, dict):
            continue
        slug = str(entry.get("folder") or "").strip()
        if not slug:
            raise SystemExit(f"{code} has no folder slug in {CODEBOOK.name}")
        rows.append((code.upper(), slug, entry))
    if not rows:
        raise SystemExit(f"No workshops in {CODEBOOK}")
    return rows


def render_workshop(code: str, slug: str, entry: dict) -> None:
    pack = WORKSHOPS / slug / code.lower()
    if not pack.is_dir():
        raise SystemExit(f"Missing brief pack: {pack}")
    title = str(entry.get("program_title") or slug)
    nav = []
    sections = []
    for sid, label, filename in SECTIONS:
        src = pack / filename
        if not src.is_file():
            raise SystemExit(f"Missing {src}")
        nav.append(f'      <a href="#{sid}">{html.escape(label)}</a>')
        sections.append(
            f'    <section id="{sid}">\n{md_to_html(src.read_text(encoding="utf-8"))}\n    </section>'
        )
    body = f"""  <div class="wrap">
    <div class="mast"><img src="../../assets/banner.png" alt="Prodensa" /></div>
    <div class="brand"><img src="../../assets/egregor-logo.png" alt="Egregor" /></div>
    <p class="badge">Prodensa · {html.escape(title)}</p>
    <p class="back"><a href="../../">Talleres</a></p>
    <h1>{html.escape(title)}</h1>
    <div class="meta">
      <span class="chip">es</span>
      <span class="chip">M01–M09</span>
      <span class="chip">primer envío T2</span>
    </div>
    <p class="lede">Diseño del taller para revisión. No es el paquete del participante.</p>
    <div class="step-nav">
{chr(10).join(nav)}
    </div>
    <article class="article">
{chr(10).join(sections)}
    </article>
  </div>
"""
    out = SITE / "workshops" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        page_shell(
            title=f"{title} · Prodensa",
            css_href="../../assets/site.css",
            body=body,
        ),
        encoding="utf-8",
    )
    print(f"wrote site/workshops/{slug}/index.html")


def render_hub(rows: list[tuple[str, str, dict]]) -> None:
    cards = []
    for _code, slug, entry in rows:
        title = str(entry.get("program_title") or slug)
        cards.append(
            "      <a class=\"card\" href=\"workshops/"
            + html.escape(slug)
            + "/\">\n"
            "        <div class=\"code\">html</div>\n"
            f"        <h2>{html.escape(title)}</h2>\n"
            "        <p>es · M01–M09</p>\n"
            "      </a>"
        )
    body = f"""  <div class="wrap">
    <div class="mast"><img src="assets/banner.png" alt="Prodensa" /></div>
    <div class="brand"><img src="assets/egregor-logo.png" alt="Egregor" /></div>
    <h1>Prodensa</h1>
    <p class="lede">Talleres para revisión.</p>
    <div class="grid">
{chr(10).join(cards)}
    </div>
  </div>
"""
    SITE.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(
        page_shell(
            title="Prodensa",
            css_href="assets/site.css",
            body=body,
        ),
        encoding="utf-8",
    )
    print("wrote site/index.html")


def main() -> None:
    rows = load_workshops()
    for code, slug, entry in rows:
        render_workshop(code, slug, entry)
    render_hub(rows)


if __name__ == "__main__":
    main()
