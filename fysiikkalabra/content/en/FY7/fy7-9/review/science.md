VERDICT: FAIL
CONTENT-HASH: bcc7ac600a1daa68

## Blocking
- assets/sims/fy7/fy7-9/sim.js:150 — (A, internal consistency; owner rule "en must have no Finnish words visible to students") the canvas region label is hard-coded `$\text{infrapuna}$`, so the English simulation labels the infrared region in Finnish (seen in review/shots/fy7-9-sim-1280.png) while the lesson, table and readout say "infrared". Every other canvas/readout string goes through `__()`. — Route it through the i18n strings: add a key (e.g. `ir`) to `sims.fy7-9` in lang/fi.json ("infrapuna"), lang/fi-easy.json ("infrapuna") and lang/en.json ("infrared") and draw `` `$\\text{${__('ir')}}$` ``. The fi/fi-easy pages are unchanged in content.

## Polish
- inquiry.json:90 (ennuste-huone, the "does not radiate" option) — "the stone just radiates infrared" can be read as "only infrared"; "the stone radiates mainly infrared" matches the lesson ("almost only infrared") and the correct option.

## Checked
- Every number in lesson.md, inquiry.json, exercises and solutions is identical to the passed Finnish version (number-by-number diff); JSON structure, correct flags, numeric answers, mistakes, tolerances, initial/locked/vary identical.
- Recomputed in one script: Wien examples 9.66/9.44/3.62 µm, 502 nm ↔ 5773 K, 900 °C → 2.47 µm vs 3.22 µm, bT = 2.61 m·K², siirto 1072.08 nm (mistakes 1192.59, 1.07208), lava 1380 K → 1106.85 °C (mistakes 1380, 1653.15), 5800/307 ≈ 19, curve peaks 483/580/724 nm at ≈100/40/13 MW/(m²·µm).
- Translation keeps every stated condition: black-body assumption in example, siirto and tarkistus-2; absolute temperature; Wien "approximately" for real bodies; accelerated charge as the source; "model values" wording in feedback and conclusion.
- Prediction options: exactly one correct each; distractor feedback physics right in English.
- Experiments: koe-1 short range 0–3000 nm shows peaks 966–483 nm; koe-2 long range 0–30 µm shows 9.66 µm at 300 K; measured key lmax present.
- Sim readout strings (en lang file) translate peak region, visible share, glow colours correctly; decimal point localised.
- Exit ticket: order radio > IR > visible > X-ray and the factor 1/3 correct.
