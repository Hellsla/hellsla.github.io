VERDICT: FAIL
CONTENT-HASH: 6bf178eaf366b56f

## Blocking
- [Major] inquiry.json koe-1 and koe-2 (captures exp-koe-1-390-1, exp-koe-2-390-1, lab-1280) — the experiment panel's "Initial state / Kept constant" line shows the Finnish variable name "laite" ("Initial state: laite: car petrol engine ... Kept constant: laite, input power"), and test prediction 2 shows the Finnish value "hehkulamppu" — an English reader meets untranslated Finnish at the exact point where they set up the experiment — translate `names.laite` ("device") and `values.laite.lamppu` ("incandescent lamp") in the English inquiry.json.

## Polish
- [Minor] Simulation panel (sim-390, exp-koe-*-390) — two near-identical accordions, "Assumptions of the model and explanation" and "Assumptions of the model", plus "How the calculation works" — merge or rename so the labels differ.
- [Minor] Experiment tables (lab-1280, exp-koe-1-390-2) — column heads render the subscripts as italic (E_o, E_a, E_h) while the text uses upright subscripts (E_o) — use \text{o}, \text{a}, \text{h} in measure labels (units J upright).
- [Minor] Tarkista feedback (open-tarkista-1280-1/2) — "Suggestion: one answer does not show everything you can do, but review the theory summary…" reads awkwardly — e.g. "One answer is not enough to judge, but review the theory summary and do the core exercises."
- [Minor] exp-koe-1-390-1 — in the small sim canvas the "P_o = 60 kW" label touches the incoming arrow — nudge the label up.

## Checked
- contact-1..3; top-390, top-1280/intro-1280, fig-1/2/3-390 (hero, lamp, pair: legible, arrow thicknesses to scale 60:10 W, green/orange consistent), fig-row, theory-1280-1..3, example-390-1, sim-390, sim-1280, lab-1280, exp-koe-1/2-390, open-ennusta-1280, open-tarkista-1280-1..4, open-exit-1280. Lesson text read in full. Maths typography (aligned blocks, \cdot, colon division, thin-space units, % spacing) clean.

## Scores
illustrations 5 · typography 4 · Finnish (English prose) 4 · accessibility 4
