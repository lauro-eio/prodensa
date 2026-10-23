# Authoring — Prodensa

Policies: [`../POLICIES.md`](../POLICIES.md) (§6a workshop Egregor).

## Platform briefs → Demo book (`egregor`)

Pack: [`workshops/comunicacion-efectiva/ce/`](workshops/comunicacion-efectiva/ce/) (`brief-platform*`). Upload:

```bash
# from egregor-api-demo
python scripts/upload_content.py -f ../special-projects/Prodensa/workshops/comunicacion-efectiva/ce \
  --target-book DEMO_BOOK_UUID --preview
```

## Demo factory (`egregor`)

```bash
cd special-projects/Prodensa
python3 scripts/run_demo_factory.py --force
```

Jobs: `global-leadership/jobs/demo/prodensa/ce-t{1-4}-m01-es/`. Upload into the **Demo** book (separate units from the brief). List job-ids in README — **not** on the hub.

## Brand / logos

Shared: [`../assets/prodensa/`](../assets/prodensa/). Publish copy:

```bash
python3 ../scripts/vendor_logo.py Prodensa
```

## HTML review (`html`)

```bash
cd special-projects/Prodensa
python3 scripts/render_briefs_html.py
```

Writes `site/index.html` (list of workshop folders) and `site/workshops/comunicacion-efectiva/index.html` from `brief-platform*`. Factory `brief-a*` / `brief-merged.md` stay off the page. Egregor job ids stay off the page.

## Do not

- Nest git remotes
- Put briefs under `site/`
- List `egregor` rows on the Vercel hub
- Upload factory `brief-a*` as client chrome (use `brief-platform*`)
- Mix Demo / fridge into the production Workshop book
- Name the workshop folder with the code (`ce`)
