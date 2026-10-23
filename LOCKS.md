# Prodensa — Comunicación efectiva (locked grain)

**Status:** Locked (2026-10-15). Change only with an explicit unlock note here.  
**Source temario:** [`workshops/comunicacion-efectiva/temario.md`](workshops/comunicacion-efectiva/temario.md)  
**Factory pattern:** Global Leadership workshop factory (discover briefs → spine → tickets → assets). Pattern reference only — do not overwrite GL catalog packs.

---

## Grain (do not collapse)

| Prodensa | Global Leadership analogue |
| --- | --- |
| **Comunicación efectiva** (this engagement) | One **workshop** (catalog-code grain: ATC, GTY, …) |
| Modules inside the title | **Modules** (`M01`…) of that workshop — not separate workshops |

**Rejected:** treating “Comunicación efectiva” as a rename of Sanmina **Comunicación asertiva** (`CA`). Related topic, different problem spine.

---

## Workshop index

| # | Workshop title (client) | Code |
| :---: | --- | --- |
| 1 | Comunicación efectiva | `CE` |

---

## Briefs

- **One workshop → one discover brief pack** (A1 → A2 → A3 → merged).
- Spine: provisional **M09** under [`workshops/comunicacion-efectiva/ce/spine-lock.md`](workshops/comunicacion-efectiva/ce/spine-lock.md).

---

## Locale / tier

| Field | Value |
| --- | --- |
| Language | **Spanish** (`es`) for source + primary locale |
| Discover | One spine × T1–T4 lenses (no exclusive tier-only modules) |
| Demo intent | One M01 demo **per tier** (T1–T4) after spine lock — separate jobs, same spine |
| First-ship priority (discover) | `T2` |

---

## Egregor surfaces (locked · POLICIES §6a)

| Book | Contents |
| --- | --- |
| **Demo / preview** | `brief-platform*` + M01 demos T1–T4 |
| **Workshop / production** | Full finish after client yes |

Factory `brief-a*` / spine = authoring. Upload `brief-platform*` only.

---

## Factory registry + demo ship

| Piece | Path |
| --- | --- |
| Tenant registry | [`config/workshops.json`](config/workshops.json) |
| Batch script | [`scripts/run_demo_factory.py`](scripts/run_demo_factory.py) |
| Demo jobs (live) | `global-leadership/jobs/ce-t{1-4}-m01-demo-es/` |

Demo defaults: **es · M01 · brief_only · lane=tailored**. Regenerate: `python3 scripts/run_demo_factory.py --force`.
