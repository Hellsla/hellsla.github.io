# FY14 — brief for a unit developer

You write one or more course units of FY14 *Road to Fusion* (English-language CLIL course: physics + English +
beginner French; authors Lauri Hellsten and Marjo Inkala). Work in `fysiikkalabra/`.

## Read first (in this order)
1. `docs/fy14/brief.md` — the teacher's brief, verbatim: the section on your chapter(s) is your specification.
   Everything it lists for your chapter must be covered somewhere in your units.
2. `docs/fy14/writing-guide.md` — the yardstick the three reviewers use. Follow it exactly.
3. `docs/FY14_PLAN.md` — chapters, verified facts that may change, limitations.
4. `scripts/units.py` (docstring) — the unit format; `docs/inquiry.md` — activity types of `inquiry.json`.
5. The two reviewed pilot units as models of form and quality: `content/en/units/fy14-photoelectric/`
   (physics with a simulation) and `content/en/units/fy14-fr-bonjour/` (language), with
   `lessons/units/<id>/figures.py`. Copy their structure, not their text.
6. The header comment of every component you use (`assets/units/fy14/fx/<kind>.js`): `match`, `order`, `gapfill`,
   `say`, `dialogue`, `video`, `timeline` (data `units/fy14/data/timeline.json`), `map` (`facilities.json`),
   `isotopes`, `binding`, `reaction` (`nuclides.json`), `reactors`, `iter` (`iter.json`). Simulations:
   `fy14/photoelectric`, `fy14/magnetic` (`assets/sims/fy14/<name>/sim.js` header; a unit uses one with
   `"sim": "fy14/<name>"` in unit.json and a `sim` activity, as the photoelectric unit does). Build a small demo of a
   component if you are unsure how it looks: put it in a unit and build.

## What you write (only these)
- `content/en/units/<id>/unit.json`, `unit.md`, `inquiry.json`, `teacher.md`; `lessons/units/<id>/figures.py`
  (then `python3 scripts/units.py figures <id>`); `content/en/units/<id>/review/developer.md`.
- The unit ids, chapters and titles are fixed in `local-courses.json` (FY14 → chapters → units); `unit.json`
  `chapter` and `order` follow that list. Do not rename ids or edit `local-courses.json`.
- Never edit shared files: `scripts/`, `templates/`, `assets/units/fy14/` (components, css, data), the sims, other
  units, `site/`, `lang/`. A bug, a missing feature or a wrong fact in a shared file goes in your report under
  "Shared issues" with file, place and the fix you propose; work around it in your unit meanwhile.
- Do not commit. Do not run the full `python3 scripts/build.py` (it rewrites site/); build only your units.

## Content rules that reviewers fail most often
- Every fact, date, name and number verified with reliable sources (WebFetch: iter.org, en.wikipedia.org,
  nobelprize.org, iaea.org, euro-fusion.org, ukaea, pppl.gov, lab sites, original papers; Wikimedia Commons and
  hs.fi are blocked). Every number computed in Python with exact constants before you write it. Sources with
  `checked` dates in unit.json.
- LaTeX for every symbol and number-with-unit, `\cdot`, `\overline{F}`, decimal point, units upright with `\ `.
  Complete seven-step solution for every worked example and numeric task.
- Inquiry: Think about it → Predict (committed, revealed later by evidence) → Investigate → Theory summary → Apply →
  Check (2–3 choice checks with misconception feedback, correct option not longest, varied). One 75-minute lesson
  per unit; optional extensions marked `"optional": true`.
- CLIL: word bank and sentence starters for every harder speaking/writing task; at least one pair or group
  discussion; one short written task with model answer and criteria; B1–B2 English, key terms bold and explained.
- French corner at the end of every non-French unit (`lang="fr"` on French text, a `say` component where
  pronunciation matters).
- Opening illustration (`hero`) for every unit, original SVG in figures.py; never draw real people (faceless herolib
  figures only); photographs: leave `<!-- photo: <subject> -->` where an authentic photo would help (a later pass
  adds licensed photos).
- Teacher notes (`teacher.md`): 75-minute timing, organisation, preparation, assessment criteria, difficulties,
  extensions.
- Changing facts (ITER schedule, records, device status, companies) carry their date ("as of November 2026").
  Distinguish results, institutional plans and corporate claims. Scientific gain $Q$ is not electricity.

## Lessons from the pilot reviews (2026-11-01)
- **Never give away a prediction.** The hook text, the *Why* line, the opening illustration and any component placed
  before a prediction must not show or state its answer. Every `prediction` has a `reveal` tied to the evidence
  that answers it (an experiment, a theory section, a source); feedback appears only then.
- Correct options are not the longest: keep all options of a choice within about ±30 % of each other in length.
- Sentence starters next to every argue/explain task, not only the first one.
- One 75-minute lesson: a theory summary of at most about 500 words; biographies and extras `optional`.
- French tips for Finnish learners compare with Finnish sounds (French *u* ≈ Finnish *y*), not German.
- `teacher.md` includes a plan for fast pairs and for running out of time.
- The opening illustration has **no text** (no speech bubbles with words); labels in other figures at least 14 px at
  390 px width (in a 1200-wide SVG that means about 48 units).
- Experiment tables: put the unit in the quantity name (`"names": {"lambda": "wavelength λ (nm)"}`) and in every
  measure label (`$U\;(\text{V})$`); a column without a unit fails the visual review. Simulation canvas text ≥ 14 px.
- A display equation never splits a sentence; no `\dfrac` inline.
- Respellings of French pronunciation are plain English-alphabet hints in one consistent style, not tagged `lang="fr"`.
- `screenshot.py` captures only the first step of a staged worked example and closed solutions: open them yourself
  in the browser and look.
- `scripts/test_inquiry.py` and `check_choices.py` do not know units yet: test the inquiry mechanics yourself in
  the browser (predictions lock, reveals open at the right point, model answers stay closed until the student writes).

## Checks before you hand over (each unit)
`python3 scripts/units.py check` (no errors) · `python3 scripts/build.py <id>` → `preview/en/<id>.html` ·
`python3 scripts/check_layout.py <id> --width 360` and `--width 1280` (all OK) · `python3 scripts/screenshot.py <id>`
and look at the captures yourself (fix what looks wrong) · open the page with Playwright (`scripts/_browser.launch(pw)`;
plain `chromium.launch()` fails here), answer every task once and confirm no console errors and no raw `$` or
`.katex-error`.

`review/developer.md`: `VERDICT: DONE` on line 1, then files, facts verified with sources, numbers computed,
open questions, Shared issues. Report back briefly (under 200 words): units done, open questions, shared issues.
