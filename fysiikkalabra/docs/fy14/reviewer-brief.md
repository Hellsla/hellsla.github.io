# FY14 — brief for a unit reviewer (science, pedagogy, or visual & editorial)

Work in `fysiikkalabra/`. Your prompt names your role and the units to review.

## Read first
1. Your role file: `../.claude/agents/<science-reviewer|pedagogy-reviewer|visual-editorial-reviewer>.md` (where it
   speaks of Finnish lessons, read English course units of FY14).
2. `docs/fy14/writing-guide.md` (the yardstick, §8 for your role), `docs/fy14/developer-brief.md` ("Lessons from the
   pilot reviews" is now part of the standard), `docs/fy14/brief.md` (the teacher's brief: the chapter's
   specification), `docs/FY14_PLAN.md`.
3. Two units that passed all three reviews, as the bar: `content/en/units/fy14-photoelectric/` and
   `content/en/units/fy14-fr-bonjour/` (with their `review/*.md`).

## For each unit
- Sources: `content/en/units/<id>/{unit.json,unit.md,inquiry.json,teacher.md,review/developer.md}`,
  `lessons/units/<id>/figures.py`, components used (`assets/units/fy14/fx/<kind>.js`, data in
  `assets/units/fy14/data/`), simulation if any (`assets/sims/fy14/<name>/`).
- Build: `python3 scripts/build.py <id>` → `preview/en/<id>.html`. Captures: `python3 scripts/screenshot.py <id>`
  → `review/shots/` (they do not open staged worked examples or closed solutions: open those yourself).
- Browser: Playwright with `scripts/_browser.launch(pw)` (plain `chromium.launch()` fails). Serve `preview/` over HTTP
  (`python3 -m http.server` in `preview/` in the background) if a component shows "could not be loaded" from `file:`.
- Science: recompute every number with exact constants in Python; verify facts and dates with WebFetch (iter.org,
  en.wikipedia.org, nobelprize.org, iaea.org, euro-fusion.org work; hs.fi and Wikimedia do not); changing facts dated.
- Pedagogy: predictions never answered before they are asked, each revealed by its evidence; CLIL support;
  75 minutes; feedback; option lengths; model answers closed until the student writes.
- Visual & editorial: every capture at 390 and 1280; figures, LaTeX, labels ≥ 14 px, English and French.

## Output
Write `content/en/units/<id>/review/<science|pedagogy|visual>.md`, starting exactly
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id>>
```
(or FAIL), then numbered findings, Blocking first, then Polish, each with file, place and a concrete fix. Do not
edit anything else and do not commit. A problem in a shared file (component, css, data, script) goes under
"Shared issues" at the end; it blocks the unit only if the unit is wrong for the student because of it.
Report back in under 150 words: verdict per unit, blocking findings in one line each, shared issues.
