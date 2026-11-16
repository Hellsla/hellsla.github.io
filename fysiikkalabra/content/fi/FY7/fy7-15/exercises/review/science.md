VERDICT: PASS
CONTENT-HASH: 18b7d27b5621721b

## Blocking

## Polish
- exercises.json:318 (L2-09) — the reflection from glass is clearly polarised only when the window is viewed obliquely (Fresnel, n = 1,50: degree of polarisation 0,04 at 10°, 0,83 at 45°, 1 at 56°); head-on the filter does nothing. The task gives the dimming as an observation, so nothing is wrong — add "vinosti" to the situation or one sentence to the model answer.
- exercises.json:359 (L3-04) — still carries "Aineisto on esimerkkiaineisto." while the same sentence was removed from L2-05 and L2-06; make the three consistent.
- solutions.md (L2-05, L2-08, L1-10) — the "hyvä vastaus" ranges end slightly outside the tolerance: 309 lx (1,6 % against 1,5 %), 46° (4,1 % against 3 %), 280 W/m² (4,3 % against 4 %). Narrow the ranges or widen the tolerances.

## Checked
- Hash identical at the start and the end (18b7d27b5621721b).
- All 22 numeric answers recomputed in one script from the task texts with my own formulas (L2-04 through Snell's law, L3-04 by scanning for the maximum, both fits by least squares): all agree with exercises.json and answers.py.
- L2-05 fit: slope 313,9 lx, intercept 6,9 lx. L2-08 fit: 14,64 lx + 360,7 lx · cos²θ, 200 lx → 44,2°; the figure's description matches.
- L1-09: D 100 < E 125 < A 150 < B 200 < C 240 W/m². L3-04 model values 0, 30, 90, 120, 90, 30, 0 W/m² fit the table's scatter.
- L3-05: Sun's height 36,9°, 7,14 W/m², break-even tilt 33,2°. L3-02: 36,9° is below the critical angle 48,8°.
- L1-11: crown glass 1,520 is the verified MAFY value (docs/mafy-arvot.tsv).
- L2-09 (new, core): qualitative, inside "polarisaatio kvalitatiivisesti"; no Malus or Brewster needed. Direction right (reflection partly polarised parallel to the surface, the s component reflects more strongly), blocked when the filter's axis is perpendicular to it, a quarter turn restores it, unpolarised light halved in every position, the residual reflection explained by partial polarisation. Agrees with the lesson's summary, the glossary and L1-06.
- L2-05 and L2-06 without the "(esimerkkiaineisto)" sentence: no number, datum or answer changed; solutions still valid (L2-06 linear interpolation 51,6°, inside the 3 % tolerance).
- Core path: only L1-01, L1-06 and L2-09 are core, and none of them is marked syventävä.
