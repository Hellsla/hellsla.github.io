VERDICT: FAIL
CONTENT-HASH: 9d3ad72f000cfde4

## Blocking
- [Major] Tarkista task 3 (inquiry.json check-2), solution "Sijoitus" (capture open-tarkista-1280-3) — `\theta_0 = 27\,°C - \dfrac{100}{\tfrac13\,\tfrac{1}{°C}}` sets a \tfrac inside a \dfrac denominator: the fraction-in-fraction renders at sub-script size and is cramped and hard to read (also `\tfrac{1}{°C}` in Muunnokset drops below the baseline) — a student cannot follow the key step of the extrapolation — write the slope as `k = 0{,}33\,\tfrac{1}{{}^\circ\text{C}}` (or `\tfrac13\,{}^\circ\text{C}^{-1}`) and the step as `\theta_0 = 27\,{}^\circ\text{C} - 100 \cdot 3\,{}^\circ\text{C}`, or take the unit out of the denominator.

## Polish
- [Minor] Tarkista hint 2 and the check-2 solution — `27\,\text{°C}` renders a small text degree sign unlike `{}^\circ\text{C}` everywhere else — use `{}^\circ\text{C}`.
- [Minor] sim-390 / sim-1280 — the canvas labels (600 K, 100 K, V) are about 8 px at 390 px, and the readout shows "p ≈ 0" or a low value just after loading while "teoria 100" is shown; ")," wraps onto its own line at 390 px — larger canvas type; settle the first reading.
- [Minor] Example, "Pystyakseli…" paragraph and Vaihe 1 — "7–8 kPa" and "−300 °C:n" can break at the dash, so "–8" can read as a negative number — keep the range together (non-breaking).
- [Minor] Prose numbers with units (`90,0 kPa`, `2,0 dm³`, `120 kPa`) are plain text beside KaTeX `°C`, so two typefaces share one sentence — set them as inline maths (NOTES §1).

## Checked
- contact-1…4; fig-1…6-390 (hero, system, micro-model, kelvin-scale, scene, extrapolation: all legible, no clipping, scale figure is to scale); top-390, intro-1280, theory-1280-1/2, fig description text.
- example-390-1/2 (table scrolls by design; aligned rows read well), sim-390, sim-1280, lab-1280, exp-exp-2-390.
- open-ennusta-1280-1 (models layout OK), open-tarkista-1280-2/3, open-exit-1280 via contact-4.
- Figure descriptions give the same information as the figures.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
