VERDICT: PASS
CONTENT-HASH: 4af3dd4a3bd89dae
SCOPE: delta added-exercise from 3b30a01720987360 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- solutions.md fy6-14-L2-09 Järkevyys — "luvun paneelin suurin teho (0,92 W)" assumes the reader knows this is the same panel; it is (same model in figures.py), so say "saman paneelin suurin teho" to make the comparison explicit.

## Checked
- fy6-14-L2-09 recomputed from the figure's model in figures.py (M_PV 0,40 V, I_sc 0,200 A, U_oc 6,0 V): I(4,0 V) = 198,7 mA ≈ 200 mA gridline; P = 4,0 V · 0,200 A = 0,80 W (model 0,795 W); matches answers.py and exercises.json (unit W, tolerance 0,04).
- Same model gives the maximum power 0,918 W at 4,96 V, consistent with the brief's 0,92 W at about 5,0 V and 184 mA, so 0,80 W < P_max holds.
- Physics: panel as a DC source, P = UI at the operating point fixed by the load's voltage; the check that I_sc · U_oc (1,2 W) is not reached at once matches the brief's misconception section.
- Figure fy6-14/ex-kenno: curve on a 1 V / 50 mA grid, nothing marked; alt text says the curve stays near 200 mA up to about 4 V, which gives the needed reading; no power shown.
- Irradiance stated constant in the task; solution complete (reading, P = UI, mA → A, substitution, rounding reason, check).
- Content hash checked at start and end.
