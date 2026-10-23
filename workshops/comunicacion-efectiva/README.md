# Comunicación efectiva

Grain: [`../../LOCKS.md`](../../LOCKS.md). This folder is **one workshop** (not a module). The code `CE` is inside [`ce/`](ce/).

## Factory (authoring only)

| File | Role |
| --- | --- |
| `brief-a1.md` | Knowledge core (problem, frameworks, taxonomy, evidence) |
| `brief-a2.md` | 6 core units + complement pool |
| `brief-a3.md` | Filters + factory handoff |
| `brief-merged.md` | A1–A3 concatenated for authoring (not the HTML page) |
| `spine-lock.md` | Provisional M09 module order (feeds GL tickets) |

## Platform (Egregor client chrome)

Spanish, uniform MD (`#` / `##`, bold, lists/tables). Folder upload ships **all** of these in order (POLICIES §6a):

| File | Role |
| --- | --- |
| `brief-platform.md` | Overview — diseño del taller |
| `brief-platform-a1.md` | Problema y marcos |
| `brief-platform-a2.md` | Módulos del taller |
| `brief-platform-a3.md` | Filtros y límites |
| `brief-platform-spine.md` | Secuencia de módulos (M01–M09) |

Hand-tuned reference pack. Regenerator (overwrite): `python3 ../../../scripts/gen_brief_platform.py Prodensa --codes ce --force`.

**Locale:** `es` · **evidence_mode:** `brief_only` · **first-ship tier priority:** `T2` (spine remains T1–T4).

**Demo intent:** after spine lock, ship **M01 demos for T1–T4** (separate jobs, same spine) into the **Demo** book; full workshop → separate production book.

**Upload:** from `egregor-api-demo`, `-f` at the pack folder or GUI **Choose brief pack…**. Unit title: `Comunicación efectiva`. Prefer **GL-Demos** / client Demo book — not GL-Catalog.

**Reupload:** delete previous platform-brief sections in the target unit, then Choose brief pack… → same unit → Upload.

```bash
python scripts/upload_content.py -f ../special-projects/Prodensa/workshops/comunicacion-efectiva/ce \
  --target-book DEMO_BOOK_UUID --preview
```

**Demo jobs (live):** `global-leadership/jobs/demo/prodensa/ce-t{1-4}-m01-es/` — regenerate via [`../../scripts/run_demo_factory.py`](../../scripts/run_demo_factory.py).
