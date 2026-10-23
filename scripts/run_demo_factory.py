#!/usr/bin/env python3
"""Batch Prodensa CE demo tickets (+ assets) via GL factory.

  cd special-projects/Prodensa
  python3 scripts/run_demo_factory.py --dry-run
  python3 scripts/run_demo_factory.py --skip-assets
  python3 scripts/run_demo_factory.py --force
  python3 scripts/run_demo_factory.py --tiers T2 --force
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

PRODENSA = Path(__file__).resolve().parents[1]
WORKSPACE = PRODENSA.parents[1]  # egregor-content
DEFAULT_CODE = "CE"
DEFAULT_TIERS = ["T1", "T2", "T3", "T4"]
CODEBOOK = PRODENSA / "config" / "workshops.json"


def gl_root() -> Path:
    env = os.environ.get("GL_ROOT")
    if env:
        return Path(env).resolve()
    candidate = WORKSPACE / "global-leadership"
    if candidate.is_dir():
        return candidate
    raise SystemExit(
        f"Cannot find global-leadership (set GL_ROOT). Tried {candidate}"
    )


def run(cmd: list[str], *, cwd: Path, dry_run: bool = False) -> int:
    print("+", " ".join(cmd))
    if dry_run:
        return 0
    return subprocess.run(cmd, cwd=cwd).returncode


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Prodensa → GL demo factory batch")
    p.add_argument("--code", default=DEFAULT_CODE, help="Workshop code (default: CE)")
    p.add_argument(
        "--tiers",
        default=",".join(DEFAULT_TIERS),
        help="Comma list of tiers, e.g. T1,T2,T3,T4",
    )
    p.add_argument("--locale", default="es")
    p.add_argument("--module", default="M01")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--skip-assets", action="store_true", help="Write tickets only")
    p.add_argument("--force", action="store_true")
    p.add_argument(
        "--assets",
        default="",
        help="Optional comma list for gen_module_assets --assets (default: all subset)",
    )
    args = p.parse_args(argv)

    code = args.code.strip().upper()
    if not code:
        raise SystemExit("No code")
    tiers = [t.strip().upper() for t in args.tiers.split(",") if t.strip()]
    if not tiers:
        raise SystemExit("No tiers")
    if not CODEBOOK.is_file():
        raise SystemExit(f"Missing {CODEBOOK}")
    registry = json.loads(CODEBOOK.read_text(encoding="utf-8"))
    entry = registry.get(code) or next(
        (v for k, v in registry.items() if str(k).upper() == code), None
    )
    if not isinstance(entry, dict) or not str(entry.get("folder") or "").strip():
        raise SystemExit(f"{code} has no folder slug in {CODEBOOK.name}")
    briefs = PRODENSA / "workshops" / str(entry["folder"]).strip()
    if not briefs.is_dir():
        raise SystemExit(f"Missing {briefs}")

    spine = briefs / code.lower() / "spine-lock.md"
    if not spine.is_file():
        raise SystemExit(f"Missing spine {spine}")

    gl = gl_root()
    write_ticket = gl / "pipeline" / "scripts" / "write_run_ticket.py"
    gen_assets = gl / "pipeline" / "scripts" / "gen_module_assets.py"
    if not write_ticket.is_file():
        raise SystemExit(f"Missing {write_ticket}")

    py = sys.executable
    failed = 0
    for tier in tiers:
        cmd = [
            py,
            str(write_ticket),
            "--code",
            code,
            "--tier",
            tier,
            "--locale",
            args.locale,
            "--module",
            args.module,
            "--lane",
            "tailored",
            "--phase",
            "demo",
            "--evidence-mode",
            "brief_only",
            "--codebook",
            str(CODEBOOK),
            "--briefs-dir",
            str(briefs),
        ]
        if args.force:
            cmd.append("--force")
        rc = run(cmd, cwd=gl, dry_run=args.dry_run)
        if rc != 0:
            failed += 1
            continue
        if args.skip_assets:
            continue
        if not gen_assets.is_file():
            print(f"error: missing {gen_assets}", file=sys.stderr)
            failed += 1
            continue
        job_id = (
            f"{code.lower()}-{tier.lower()}-{args.module.lower()}-demo-{args.locale.lower()}"
        )
        acmd = [py, str(gen_assets), "--job-id", job_id]
        if args.assets.strip():
            acmd.extend(["--assets", args.assets.strip()])
        if args.force:
            acmd.append("--force")
        if args.dry_run:
            print(f"(skip gen dry-run without ticket for {job_id})")
            continue
        rc = run(acmd, cwd=gl, dry_run=False)
        if rc != 0:
            failed += 1

    if failed:
        print(f"done with {failed} error(s)", file=sys.stderr)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
