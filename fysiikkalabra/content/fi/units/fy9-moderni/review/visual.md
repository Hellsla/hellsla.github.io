VERDICT: PASS
CONTENT-HASH: 115941f6cb5f4383
SCOPE: delta: new tasks s8 and s9 and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- [Minor] s8 and s9 figures at 390 px (fy8-13/vaimennus, fy8-16/hubble-t): the catalogue figures scale to about 55 %, so the tick numbers are very small and the pale grid (`#e3dccb`) is hard to see; in s9 the x ticks (50 100 150 200 250 300) nearly touch. The task relies on "ruudukon piste" (250 Mpc; 18 000 km/s). Shared catalogue figures, so no change here; for a later figure-fix: tick numbers every 100 Mpc and a darker grid.
- [Minor] s8 rubric c, calculation row: the display ends in a comma ($\approx 2{,}2\,\text{mSv},$ then "joka on yli"); move the clause out of the maths.
- [Minor] s8 rubric a: $\ln(80 : 5{,}0)$ has no units while the model solution has them; harmless.

## Checked
- Opened (fi) stage-exercises-390-60, -61, -62, -63 (end of s7, start of s8), -64 (s8 text and figure), -65, -66 (model solution a), -71 to -73 (rubric rows), -74, -75, -78 (s9 figure, solution a, d), intro-390.
- s8 and s9 figure SVGs: aria-label names match the task's ($\dot{H}$, $d$, $v$); axes carry quantity and unit; data points distinct from the fitted line; no answer marked on either figure.
- Task text does not name the solution structure beyond the given models $\dot{H} = \dot{H}_0 e^{-\mu d}$ and $v = H_0 d$; results rounded to the data's precision (6,6 µSv/h, 24 cm, 72, 1,4 · 10^10 a); calculation chains as aligned rows; unit fields language-neutral (1/cm, µSv/h, km/s/Mpc, a).
- Intro: "Yhdeksän ... Tehtävissä 8 ja 9 työskennellään kuvaajan kanssa" matches the set and reads fluently.
- No horizontal overflow or clipped formula visible at 390 px in the opened captures; check_layout result taken as given.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
