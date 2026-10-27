VERDICT: PASS
CONTENT-HASH: f9d3b98d3c037ea9

## Blocking

## Polish
- lessons/FY1/fy1-4/figures.py:71-72 — `reading()` says "patikoijan matka" and id 'lue-kuvaajasta', but the embedded figure (inquiry.json:311) and task are a cyclist at 15 km/h (id `kuvaajasta`); regenerating would label a 15 km/h hiker. — Say "pyöräilijän" and the right id.
- inquiry.json ennuste-1 correct option — shortened to "Origon kautta kulkeva suora, jonka molemmin puolin on pisteitä"; the glossary's other criterion (lähellä kaikkia pisteitä) is gone, so a too-steep line through the cloud also qualifies. — Consider restoring "lähellä kaikkia pisteitä".

## Checked
- Round-1 blocking fixed: tarkistus-2 now a patikkaretki, 3,0 km/h consistent with its check; mistake 5,5 h = (25 − 3,0)/4,0 with correct feedback; 8,3 h and 7,0 h recomputed.
- Round-1 polish fixed: ennuste-2 names k = 0,80 g/ml; L3-03 rounding justified from exact Δx ratio; L3-01 states the extrapolation assumption.
- New task `kuvaajasta`: SVG measured to scale (X 106,9 px/h, Y 4 px/km); line s = 15t + 5 passes (1, 20) and (3, 50); answer 15 km/h, mistakes 16,7 (50/3) and 0,067 (Δt/Δs) correct; solution symbolic first, third-point check (2,0 h; 35 km) true; 15 km/h realistic cycling.
- koe-3 (now core): b locked at 80, best k = −1,90, d = 5,80 °C; residuals +10,0 −0,9 −5,7 −6,2 −3,7 +0,9 +6,9 (LS fit same pattern), so the correct option "ylhäällä päissä, alhaalla keskellä" holds; new wrong options' feedback correct.
- virhe item: reworded options keep correct physics (Δs/Δt, far points on fitted line give 0,50 m/s).
- L2-04 rewording: ratio 29,0/16,5 = 1,76 → 1,8 within 3 %.
- answers.py rerun: all 12 values unchanged and matching exercises.json; comment numbers correct.
- Unchanged content (worked example, figures 1–4, sim.js, exit ticket) as verified in round 1; hash identical at start and end.
