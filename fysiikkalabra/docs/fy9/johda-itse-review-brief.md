# FY9 — delta review: derived results as "Johda itse" tasks (teacher 2026-11-12)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial) and the units you review.

## What changed
The teacher decided that the FY9 review book gives as formulas only the laws of the MAFY formula tables (what students
have in the exam). A result the course exam asks students to *derive* from those laws is no longer a formula row of
its own. In each such place the theory text of `unit.md` now has:
- the formula table (```kaavat, `name :: LaTeX`, `scripts/kaavat.py`) with the MAFY laws only;
- one or two short sentences that state the model or situation and its quantities, without the derived result;
- a **Johda itse** task, a ```johda fence: the question, a line `---`, then the derivation in paragraphs and display
  equations. The page shows the question in view and the derivation behind a closed *Näytä johto* button
  (`kaavat.johda_html`, `.johda` in `templates/site.css`), like a task's solution: the student tries first;
- where the derivation needs a situation the unit did not draw, a new figure (`lessons/units/<id>/figures.py`), and the
  unit's concept map (`kartta`) lists only the remaining formulas.

Only the theory text (`unit.md`), figures.py and the figure translations (`figures.json`) changed; inquiry, tasks,
exit tickets and Sovella sets did not. Each unit changed in fi, fi-easy (selkeä suomi) and en.
The diff since the reviewed version: `git diff b32fa4e7 -- content/<lang>/units/<id>/unit.md content/<lang>/units/<id>/figures.json lessons/units/<id>/figures.py`
(ignore `review/` folders). Every unit was reviewed in full before (its `review/<role>.md`); judge only the change and
what it touches.

## What to judge (delta)
- **Science**: each derivation is correct, complete and starts from laws that are in MAFY's tables (or stated in the
  unit), with its assumptions (constant deceleration, point source, Ohmic resistor, …); every symbol is defined with
  units; the model sentence states the situation correctly; nothing left in the text, the figures or the unit's own
  tasks/inquiry now uses a removed formula as if it were given without saying where it comes from (a task's solution
  may derive it: that is fine); new figures are physically right; fi-easy and en say the same physics as fi.
- **Pedagogy**: a 16–19-year-old revising for the course exam can follow the model sentence, try the question
  first and learn the method from the derivation; the question says exactly what to derive and from what; the text
  still reads as a coherent review without the removed formulas; the Johda itse tasks are not too many or too long
  for a review unit; fi-easy is clear Finnish (short sentences, every derivation step kept).
- **Visual & editorial**: build with `python3 scripts/build.py <id>` → `preview/<id>.html` (fi; `preview/fi-easy/`,
  `preview/en/` for the others) and look at the theory section at 390 and 1280 px with the Johda itse boxes closed
  and open (Playwright: `node` with `require('playwright')`; open them with
  `document.querySelectorAll('.johda details').forEach(d => d.open = true)`): the box, the question, the derivation's
  maths (upright subscripts, spacing, display equations that fit a phone), the new figures (labels readable on a
  phone, nothing overlapping, the palette and strokes of the unit's other figures), the concept map's text fits its
  boxes, Finnish/English language of the new sentences.

## Output
For each unit-language pair you were given write `content/<lang>/units/<id>/review/<science|pedagogy|visual>.md`
(overwrite your role's previous report), starting exactly
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id> --lang <lang>>
```
(or FAIL), then a line "Delta review (Johda itse, 2026-11-12) of the version passed at <old hash from your role's
previous report>." and numbered findings, Blocking first, then Polish, each with the file, the place and a concrete
fix (under 300 words per report). Blocking = a physics error, a derivation that does not hold or skips a needed step,
an undefined symbol, a contradiction a student would meet, broken layout. Do not edit anything else and do not
commit. Report back in under 200 words: verdicts per unit-language and every Blocking finding.

## Round 2 (teacher 2026-11-12, later): what changed since the reviewed version 3ec8cc24
- Esimerkit worked solutions (`inquiry.json`) that gave a removed result under "Kaava:" now derive it first in one or
  two steps from MAFY laws (tasavirta [13] [15] [19] [20], moderni [16], liike [13], energia [14], magnetismi-valo [15],
  sahkokentta [7] [19], sailymislait [14], ympyraliike [15] [16]); every number is unchanged.
- Two formulas the teacher calls extra information are given again, marked **Lisätieto** in the formula table (a line
  `+ <formula>`; the name column shows the word Lisätieto in italics) with a sentence that the exam gives it when a
  task needs it: moderni H = Ḣt, sahkokentta η = P/(GA) (light perpendicular to the cell). Their Johda itse tasks are gone.
- ympyraliike: the first Johda itse is split in two (ΣF = mv²/r; the car in a flat curve), and the derivation of g says
  "Ilmanvastus jätetään huomioimatta."
Judge only this change: `git diff 3ec8cc24 -- fysiikkalabra/content/<lang>/units/<id>/ fysiikkalabra/lessons/units/<id>/`
(ignore review/). Your report's second line names the version passed at your role's previous hash.
