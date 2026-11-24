VERDICT: PASS
CONTENT-HASH: 4767acb6926783d8

## Blocking

## Polish
- lesson.md:170 — the caption says the cooled lava surface "looks grey because it radiates almost only infrared". This gets the cause wrong. We see the grey from reflected daylight; the infrared emission only explains why the surface does not glow. — Suggested wording: "The cooled surface does not glow, because it radiates almost only infrared; it looks grey in reflected daylight."
- lesson.md:175 — "much hotter than red-glowing lava": sparkler sparks (about 1000–1600 °C, iron burning locally hotter) are hotter than lava at about 1100–1200 °C, but not "much" hotter in every case. The colour argument still holds. — "hotter than".
- inquiry.json tarkistus-2 hint 3 — the hint already gives $1380\,\text{K}$, so only the Celsius step is left (this is for pedagogy to judge, not physics). — Optionally stop at the substitution.

## Checked
- I recomputed every number in one script with my own formulas (c = fλ; Wien; Planck's law with Wien's root x = 4.965 for the model peaks): 7.5/4.3·10¹⁴ Hz, 3.0 m, 12 cm, 966/483/9659 nm, 9.7/9.4/3.6 µm, 502 nm, 5773 K, 2.47 vs 3.22 µm, 2.61 m, 1072 nm (mistake values 1193 nm and 1.07), 1380 K → 1107 °C (mistake values 1380 and 1653), Sun/skin ratio 19, Stefan–Boltzmann ×16. All of them match the lesson.
- Curves figure (says it is to scale): peak positions 189.8/207.8/234.7 px and heights 82.4/206.6/262.7 px from Planck agree with the SVG (6000 K ≈ 100, 5000 K ≈ 40, 4000 K ≈ 13 MW/(m²·µm)). The visible band at 380–750 nm is placed correctly.
- Spectrum figure: the logarithmic scale (97.5 px per factor 1000) puts the 750 nm, 380 nm, 10 nm and 0.01 nm boundaries at the drawn x values, the zoom ticks at 700–400 nm are linear and correct, and the table matches the figure.
- Wave figure: E and B are in phase and perpendicular, and E × B points along +x (the direction of travel) at both crests. Antenna figure: E is parallel to the rods, reverses every half wavelength, and λ is marked between like crests.
- sim.js: exact Planck exitance (with π, consistent with σT⁴); a golden-section peak search over 50 nm–50 µm that is unimodal over the slider's 200–10 000 K; visible share = band integral / σT⁴ (300 K: 7·10⁻²²%, so "under 0.01 %" is right); the axis unit is W/(m²·µm) with an SI prefix; glow starts at 800 K. The model box states the black-body assumption, that reflected light and radiation from the surroundings are left out, and that the readings are model values.
- koe-1 (short range locked, T varied 3000–6000 K, peaks inside 0–3000 nm) and koe-2 (long range locked, 300 K and 600–900 K, peaks inside 0–30 µm) each isolate T. `simState.lmax` gives the measured key.
- Predictions: exactly one correct option in each, and every distractor's feedback gives the right reason and the model values. Find the error, check-1 (an accelerating charge radiates; a charge at constant velocity or at rest does not) and the exit ticket are correct.
- Worked example and the siirto/tarkistus-2 solutions: solved symbolically first, conversions to K and m correct, significant figures justified, and the reasonableness checks are real checks.
- Scope: classical source (accelerating charge), no photon (FY8), Stefan–Boltzmann only as a qualitative proportionality, Planck named only as later quantum physics.
- Consistency: theory, summary, glossary, sim boxes, conclusion model answer and tarkistus-3 (5800 K vs 5772 K is fine) agree. The check results show no physics lint warnings.
