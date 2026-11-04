VERDICT: FAIL
CONTENT-HASH: bcc7ac600a1daa68

## Blocking
- [Major] Simulation canvas (`sim-390`, `sim-1280`, `lab-1280-1`, `exp-koe-1-390-1`) — the graph shows the Finnish word "infrapuna" in the plot area (hard-coded `$\text{infrapuna}$` at assets/sims/fy7/fy7-9/sim.js:150; the strings block has no key for it) — standing decision: en must show no Finnish words to students; the same label is correctly "infrared" in the lesson's own figures — add a `region_ir` key ("infrared"/"infrapuna") to the sim's strings in lang/en.json and lang/fi*.json and draw `__('region_ir')`.

## Polish
- [Minor] Simulation legend — the en `selite` string is 18 words; sim-embed folds a legend over 15 words behind a second box, so the page has "Assumptions of the model and explanation" beside "Assumptions of the model" (as in FY4 reviews), and the colour-band/dashed-line legend is hidden — shorten to 15 words or fewer, e.g. "The colour band is visible light; the dashed line marks the peak."
- [Minor] inquiry.json experiment intros — "The wavelength range is short wavelengths" reads awkwardly — "The wavelength range is set to short wavelengths".
- [Minor] Spectrum table at 390 px — "microwaves" breaks as "mi-crowaves" in a narrow first column — acceptable, the table scrolls by design.

## Checked
- contact-1..3; top-390, intro-1280, sim-390, sim-1280, lab-1280-1, exp-koe-1-390-1
- figures fig-5 (wave), fig-7 (antenna), fig-9 (spectrum), fig-11 (curves) at 390; fig-2 hero
- theory-1280-2 (table and spectrum figure), open-ennusta-1280, example-390 (contact sheet), exit-1280
- check_layout.py fy7-9 --width 340: OK (no formula overflow)
- Language: read all lesson, inquiry, exit-ticket text in English; fluent, terms consistent.

## Scores
illustrations 4 · typography 5 · Finnish 4 (English reads naturally) · accessibility 4
