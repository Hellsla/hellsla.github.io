# FY9 — delta review: formulas in MAFY form (teacher 2026-11-12, "Kirjoita mafy muodossa")

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial).

## What changed
The teacher asked that the FY9 formulas be written as in the formula tables of mafytaulukot.fi ("MAFY"). In the
theory sections (```kaavat blocks, `name :: LaTeX`, see `scripts/kaavat.py`) 13 units changed in three languages
(fi, fi-easy, en): each formula whose form or symbols differed from MAFY is now MAFY's form, rows were added where
MAFY has two formulas (four Doppler rows, ydinreaktion massaero, voiman impulssi), the sentence after each block
defines the new symbols, and the units' formula maps (figures.py `kaavakartta`) show the same forms. Tasks, inquiry
activities, exit tickets and Sovella sets were not changed. `docs/fy9/kaavanimet.tsv` lists every formula, its name,
English name and source (MAFY page, or "ehdotus" for a formula MAFY does not have).

The units: aallot, energia, kaasut, koe, lampo, liike, magnetismi-valo, moderni, sahkokentta, sailymislait,
tasavirta, voimat, ympyraliike (ids `fy9-<name>`), each in `content/fi/`, `content/fi-easy/`, `content/en/` `units/`.
The diff since the reviewed version: `git diff da7970e24 -- content/fi/units content/fi-easy/units content/en/units lessons/units`
(ignore `review/` folders). Every unit was reviewed in full before (its `review/<role>.md`); judge only the change and
what it touches.

## What to judge (delta)
- Science: each new formula is correct and equals MAFY's law with its conditions (sign conventions: kaasut now
  ΔU = Q + W with W done on the gas; heikennyslaki as I = I0 e^{−μx}, hajoamislaki as N = N0 e^{−λt}); every symbol of a
  new form is defined in the sentence after it, with units; no statement in the unit's text, figures or the unit's own
  inquiry/exit ticket/Sovella now contradicts the theory (a task may use its own, defined symbols — report only a real
  contradiction or a confusing clash as Polish); the fi-easy and en versions say the same physics as fi.
- Pedagogy: does the change keep the review unit coherent for a student (new symbols introduced where used, nothing
  taught in a form the unit's tasks then contradict without explanation)? Is the half-life form still available
  where the tasks need it?
- Visual & editorial: build with `python3 scripts/build.py <id>` → `preview/<id>.html` (fi; `preview/fi-easy/`,
  `preview/en/` for the others) and look at the theory section's formula tables and the formula maps at 390 and 1280 px
  (Playwright: `node` with `require('playwright')`, or `scripts/_browser.py`): typography of the new LaTeX (upright
  subscripts, \overline vectors, spacing), no overflow, the formula map's text fits its boxes, Finnish/English language
  of the new sentences.

## Output
For each of the 39 unit-language pairs write `content/<lang>/units/<id>/review/<science|pedagogy|visual>.md`
(overwrite your role's previous report), starting exactly
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id> --lang <lang>>
```
(or FAIL), then a line "Delta review (formulas in MAFY form, 2026-11-12) of the version passed at <old hash>." and
numbered findings, Blocking first, then Polish, each with the file, the place and a concrete fix (under 300 words per
report). Blocking = a physics error, an undefined symbol, a contradiction a student would meet, broken layout.
Do not edit anything else and do not commit. Report back in under 200 words: verdicts per unit-language and every
Blocking finding.
