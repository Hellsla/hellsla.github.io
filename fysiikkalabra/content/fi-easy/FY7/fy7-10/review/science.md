VERDICT: PASS
CONTENT-HASH: 6ae8f5d003acc8f8

## Blocking

## Polish
- lesson.md:152 — the fix introduced a duplicated clause: "Huoneesta lasiin osuva valo heijastuu osittain takaisin, ja huoneesta lasiin osuva valo heijastuu osittain takaisin." The physics is right, but the text is broken (editorial, for the visual reviewer). Fix: "Huoneesta lasiin osuva valo heijastuu osittain takaisin."
- lesson.md:150 — "järven pinta peilaa iltaisin rannan puut": "iltaisin" suggests the time of day is the cause; the cause is the grazing view far across the lake ("kun pintaa katsoo loivasti kauas"). Carried from round 1, C if left.

## Checked
- Round-1 blocking fixed: line 152 no longer says "Samasta syystä"; the window reflection is now explained by little light coming from outside while ~4 % of the room light is reflected, which is the right mechanism at near-normal incidence.
- One script (scratchpad sci/recompute_r2.py): example 38.02° and 2.256·10⁸ m/s; ennuste-1 28.9°; ennuste-2 22.1° → 40.6° (×1.84), limits 48.8°/24.4°; ratios 1.36/1.48.
- koe-2 35.2/30.9/30.3/18.5° with n₂ sin α₂ = 0.766; virhe 0.651 → 40.6°.
- mittaus: own least-squares fit of the seven points A = 1.4895, ΔA = 0.0162, B = −0.0041; mistakes 0.671 (1/A) and 1.79 (70:39); v = 2.013·10⁸ m/s (mistake 4.47).
- siirto 41.68° (glass 25.94°, mistakes 22.08 and 39.9); tarkistus-2 1.470 (mistakes 0.680, 1.592); normal-incidence R 2.0 % (water) and 4.3 % (glass).
- Conditions kept: angles from the normal, n > 1 for visible light in transparent materials, the same angle of incidence, no absorption in the energy split, oblique view for the straw, frequency set by the source.
- Each choice item has exactly one correct option; distractor feedback is right; the sim model box states its limits and calls readings model values.
- check_layout.py fy7-10 --width 340: fi-easy OK, no formula overflow.
