VERDICT: FAIL
CONTENT-HASH: 01c745ba4b9d5511

## Blocking
1. [Major] Figure `plan` (`lessons/units/fy14-fr-cadarache/figures.py` → `unit.md` `data-fig="plan"`, viewBox 800 wide): every room label is 30 units, which renders at **13.4 px at 390 px**. The standard (pilot lessons) asks for at least 14 px. These labels are the content of the *Follow the directions* task. Fix: set the label size to 32 units (14.3 px). The rooms are about 280 units wide, so *la bibliothèque* and *la salle de conférence* still fit. Also darken the grey *le couloir* label to the normal ink colour.

## Polish
1. [Minor] Figure `map`: the label *le Rhône* (x 17, y 262) floats in empty land about 100 units below the point where the Rhône line leaves the left edge (y ≈ 155). Fix: move the label next to the drawn line, around (20, 120), for example `f.tex(*P(…≈43.9 N), …)`.
2. [Minor] Figure `map`: the blue ellipse (Étang de Berre) has no label and is not in the aria-label, so it reads as an unexplained lake. Fix: label it *l'étang de Berre* or remove it.
3. [Minor] The summary table at 390 auto-hyphenates English ("ask a sim-ple question", "under-stood"). This comes from the shared `td{hyphens:auto}` rule; an optional fix is `th:first-child{width:30%}`.
4. [Minor] The feedback "France: the ground floor is the rez-de-chaussée …" has its French untagged. Fix: `{fr}rez-de-chaussée{/fr}`.

## Checked
- Contact sheets 1–6.
- The map at 390 and 1280. The scale checks out: Aix–Marseille 27 km, Aix–ITER 37 km, Manosque–ITER 15 km, Avignon–Aix 70 km. The labels are 14.6 px at 390.
- The plan at 390 and 1280, with label sizes measured.
- The hero at 390 and 1280: blank signboards, no faces.
- Directions table, dialogue, both order components, both gapfills and the role-play cards at 390 and 1280.
- A word-break audit at 360, 390 and 1280: French breaks only at real hyphens.
- All three model answers, opened after writing.
- No console errors, no `.katex-error`.
- Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English/French 4 · accessibility 3
