VERDICT: PASS
CONTENT-HASH: 302f1baa0ebd6ce9

## Blocking

## Polish
- [Minor] greenhouse figure at 390 px — the whole figure renders only about 300 px wide, so the labels "näkyvä valo", "infrapuna" and "CO₂" are small — enlarge the label font or the figure's scale a little.
- [Minor] sim-spec.md (not student-facing) keeps plain "n_a", "E_n" — fine as a spec, no action unless it is shown to students.

## Checked
- Delta: aria-label of the greenhouse figure (now says two photons, one down, one up-right). Opened the figure with Playwright (preview/fy8-2.html, 390 px, every details box opened): two re-emitted infrared photons are drawn, one down toward the ground and one up-right, matching the label. Orange visible light, red infrared, nothing clipped or overlapping. The previous Minor is fixed.
- Opened exp-koe-1-390-1: the Alkutila line and the readout now show n_a, n_y as upright-subscript maths ($n_\text{a}$), consistent with the text; the table labels in koe-2 use the same names.
- Text changes read in the diff: "pieni osa vetyatomeista" (fluent, correct case), the model answer's added sentence on $E_n$ (formula and units well formed, one idea), and the Etsi virhe prompt, where the doubled `\\n` became real newlines, so the situation, display chain and question now separate as intended (checked in the source diff, JSON valid, build and inquiry checks ok).
- Not opened individually: other captures, since the diff touches nothing else.

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
