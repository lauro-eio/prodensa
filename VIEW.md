# Prodensa HTML → Vercel

Publish root is **`site/`** ([`../POLICIES.md`](../POLICIES.md)).

| Piece | Path |
| --- | --- |
| Hub | [`site/index.html`](site/index.html) — lists `workshops/` |
| Workshop page | [`site/workshops/comunicacion-efectiva/`](site/workshops/comunicacion-efectiva/) |
| Styles | [`site/assets/site.css`](site/assets/site.css) |
| Source MD | [`workshops/comunicacion-efectiva/ce/`](workshops/comunicacion-efectiva/ce/) `brief-platform*` |
| Render | [`scripts/render_briefs_html.py`](scripts/render_briefs_html.py) |
| Vercel | [`vercel.json`](vercel.json) → `outputDirectory: site` |

## Render

```bash
cd special-projects/Prodensa
python3 scripts/render_briefs_html.py
```

## Local preview

```bash
python3 -m http.server 8765 --directory site
```

## Ship

```bash
cd special-projects/Prodensa
git add site
git commit -m "Update Prodensa site"
git push
```

Vercel: one project on `lauro-eio/prodensa`, output = **`site`**.  
Do **not** publish into `global-leadership-preview` or `go2-view`.
