# Prodensa

Client hub for tailored Global Leadership workshops. Policies: [`../POLICIES.md`](../POLICIES.md). Do **not** publish into `global-leadership-preview` or `go2-view`.

Open [`site/index.html`](site/index.html). Logos: [`site/assets/`](site/assets/) (`vendor_logo.py Prodensa`).

| Engagement | Channel | Where |
| --- | --- | --- |
| Comunicación efectiva — HTML review | `html` | [`site/workshops/comunicacion-efectiva/`](site/workshops/comunicacion-efectiva/) |
| Comunicación efectiva — M01 demos T1–T4 | `egregor` | `global-leadership/jobs/demo/prodensa/ce-t{1-4}-m01-es/` |
| Discover briefs / locks | `local` | [`workshops/comunicacion-efectiva/`](workshops/comunicacion-efectiva/), [`LOCKS.md`](LOCKS.md) |

| Path | Role |
| --- | --- |
| [`site/`](site/) | Vercel publish root · hub lists `workshops/` |
| [`site/workshops/comunicacion-efectiva/`](site/workshops/comunicacion-efectiva/) | Review page from `brief-platform*` |
| [`scripts/render_briefs_html.py`](scripts/render_briefs_html.py) | MD → `site/` |
| [`LOCKS.md`](LOCKS.md) | Locked grain for Comunicación efectiva |
| [`workshops/comunicacion-efectiva/`](workshops/comunicacion-efectiva/) | Workshop folder (title slug). Code `CE` is inside `ce/` |
| [`config/workshops.json`](config/workshops.json) | Tenant registry for GL tickets |
| [`AUTHORING.md`](AUTHORING.md) | How to regenerate / scaffold demos |
| [`scripts/run_demo_factory.py`](scripts/run_demo_factory.py) | Batch M01 demos → `global-leadership/jobs/` |
| [`VIEW.md`](VIEW.md) | Render + ship `site/` |

**Active workshop:** [`workshops/comunicacion-efectiva/`](workshops/comunicacion-efectiva/) (`CE`).

Regenerate demos: `python3 scripts/run_demo_factory.py --force`.  
Regenerate the review site: `python3 scripts/render_briefs_html.py`.
