VERDICT: FAIL
CONTENT-HASH: 23d615651bb8e7b6

## Blocking
- [Major] inquiry.json experiments koe-1, koe-2, koe-3 (capture exp-koe-*-390, lab-1280) — the "Initial state" and "Kept constant" lines show the untranslated Finnish word "aineisto" ("aineisto = 1", "Kept constant: aineisto, constant term b"), while the simulation calls it "Data set" — a student cannot tell what is being set or kept constant, and the English page reads as unfinished — change the `names` entry `"aineisto"` to "data set" in all three experiments (and the matching table header).
- [Major] simulation locked-control hints (exp-koe-1/2/3-390, lab-1280) — the greyed controls carry the Finnish caption "(vakio)" under "Data set", "Constant term b" and "Slope k" — untranslated UI text in an English lesson — localise the caption ("fixed") in the template or its English string table.

## Polish
- [Minor] lesson.md Linear model — "The measurements show that the model holds only in the range that was measured." overstates what data show — "The measurements support the model only in the range that was measured." (for science: confirm.)
- [Minor] lesson.md / Summary — "the constant term b is the point where the line crosses the vertical axis": b is a value, not a point — "b is the value of y where the line crosses the vertical axis."
- [Minor] fig-5 (kettle, 390) — tick labels "2" and "2.5" nearly touch, and the worked-example figure already marks 2.5 min before the solution reaches it — widen the label gap; (for pedagogy: the figure gives the answer away).
- [Minor] worked example, Given and find (390) — a line wraps leaving ". We need" starting a line after inline maths — keep the full stop attached (non-breaking).
- [Minor] sim canvas at 390 — axis titles and tick numbers are about 7 px; the readout carries the information, but enlarge canvas text on narrow screens. (for science: "mean deviation" is a root-mean-square value.)

## Checked
- hash at start and end; contact sheets 1–3; fig-1, fig-3, fig-4, fig-5, fig-6 at 390; intro-1280; theory-1280-2; lab-1280-1; sim-390; exp-koe-1-390-1; open-ennusta-1280-1; open-tarkista-1280-3. Not opened one by one: contact sheets 4–6, the remaining theory and open-state parts (seen only in the contact sheets).

## Scores
illustrations 4 · typography 4 · Finnish 3 (English: 3, the Finnish leaks) · accessibility 4
