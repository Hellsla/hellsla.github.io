VERDICT: FAIL
CONTENT-HASH: 6a1e34abe8699d59

## Blocking
- [Major] fig-4 (rontgen) at 390 px — the label "bone" is cut off at the right edge ("bon") — the English word is longer than the Finnish one — shorten to "bone" with a smaller offset or move the label left / widen the viewBox.
- [Major] fig-6 (pet) at 390 px — "source on the segment" is cut off ("source on the segr") — fix: shorten to "source on line" or wrap onto two lines.
- [Major] fig-10 (mittari) at 390 px — "controller" is cut off ("controll") — move the box left or widen the viewBox.
- [Major] lab-1280-1 (experiment panel) — Finnish words appear in the English page: "potilas: one tumour, ilmaisu: koinsidenssi" and "Kept constant: potilas, ilmaisu" (inquiry.json `names`, `values`) — translate to "patient", "detection", "coincidence".
- [Major] sim-390 / sim-1280 — a duplicate disclosure "Assumptions of the model and explanation" appears above the three boxes, and the orange-dot/segment legend line is missing (present in fi-easy) — remove the duplicate; restore the legend text.

## Polish
- [Minor] lab-1280-1 — readings table header "through tumour (%)" is cut off; make the overflow visible.
- [Minor] sim canvas — the "-15" y tick collides with the detector ring; shift the label.
- [Minor] fig-12 — "soft tissue" label sits on the curve; move it above.

## Checked
- Opened: top via contact-1, sim-390, sim-1280, lab-1280-1, fig-4, fig-6, fig-8, fig-10, fig-12, open-exercises 1 and L3-2.
- Sim canvas and figures contain no Finnish text; only the experiment panel does.
- Maths: LaTeX units and decimal point consistent.

## Scores
illustrations 3 · typography 4 · Finnish n/a (English; leaks 2) · accessibility 4
