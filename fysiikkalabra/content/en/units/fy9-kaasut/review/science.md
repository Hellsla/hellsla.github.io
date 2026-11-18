VERDICT: FAIL
CONTENT-HASH: a2b51d07ea6aadea
SCOPE: delta: new tasks fy9-kaasut-s8 (fy3-10/pt-suorat) and s9 (fy3-11/pv-isobaari) and the changed intro; s1–s7 not re-judged (hash at start and end identical).

## Blocking
- **s9 text vs figure (B, model condition).** "whose other end is closed by a light movable piston" while the figure holds the gas at a constant 250 kPa. A light piston with outside air on its other side keeps the gas at about 101 kPa, not 250 kPa. State what holds 250 kPa (a load on the piston) and drop "light".
- **s9 c rounding and tolerance (A, assessment).** The solution gives three significant figures "like the initial temperature 293 K", but 293 gets its third figure from adding 273.15. The data are 20 °C, 1.0 l and 4.0 l (two figures), and part b rounds to two figures "like the volume 1.0 l". By the same reasoning c should be 1.2·10³ K, and that is 2.3 % from 1172.6 K, outside the 2 % tolerance. Make b and c consistent (two figures, tolerance at least 3 %).
- **Intro (A, internal consistency).** "The last problem is an applied source-based problem…": since s8 and s9 were added after it, the last task is s9 (a graph task), and the source-based task is s7.

## Polish
- s9: heating air to about 1170 K (900 °C) is not plausible for a student in a school cylinder. A smaller volume ratio or a note would help.

## Checked
- Own recomputation (R = 8,31, 273,15) from the figure sources (`pt_lines`: p = 0,25 T and 0,15 T kPa, points 200/400 K; `pv_isobar`: 250 kPa, 1,0→4,0 l): s8 0,0602 mol (both points), 0,0361 mol, 40,0 %, 63,29 kPa; s9 750 J, 0,1026 mol, 1172,6 K, 899,5 °C, ΔT 879,5 K. All match answers.py and tasks.json. Magnitude checks (0,083 and 0,042 mol of air) right.
- The figures show every value read. V and 20 °C come from the text.
- s9 d: ΔU > 0, Q = ΔU + W, Q > W; the physics, sign convention and energy wording are correct.
- Points add up, criteria match the parts, alternatives accepted; scope FY3; other tolerances admit two figures.
- Numbers, criteria and physics match the fi version.
