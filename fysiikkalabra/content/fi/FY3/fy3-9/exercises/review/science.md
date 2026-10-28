VERDICT: PASS
CONTENT-HASH: 3d0ab462b0888669

Delta review over the audit's PASS (ba0823c1b322100e): L1-03 (water rocket) replaced by a figure task reading Boyle's law points off fy3-9/boyle-points.

## Blocking
- none
## Polish
- none
## Checked
- Figure code: points V = 10, 15, 20, 30, 40 ml at p = 2000/V kPa; (10; 200), (20; 100), (40; 50) lie on 5 ml / 25 kPa grid crossings; screenshot at 360 px matches the description.
- Answer: p2 = 100 kPa · 20 ml / 25 ml = 80 kPa (also from (10; 200) or (40; 50)); (15; 133) gives 79,8 kPa.
- Tolerance 0,03 -> 77,6–82,4 kPa: accepts every grid-point reading and 79,8; rejects the linear interpolation between (20; 100) and (30; 66,7), 83,3 kPa, which the solution names as the wrong method.
- Task text gives no values that the figure supplies; isothermal condition (slow piston, closed tip) stated.
- answers.py = 80; solution symbolic first, units cancel, 2 s.f. justified; Järkevyys numbers (67 kPa, ≈83 kPa) correct.
- Figure is a safe variant (no curve, no pV value).
