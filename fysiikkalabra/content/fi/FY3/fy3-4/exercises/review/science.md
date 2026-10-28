VERDICT: FAIL
CONTENT-HASH: 7bc076f5030b1364

Delta review over the audit's PASS (e421ffd346e680cb): L2-03 (oil density) replaced by figure task two-liquids, LaTeX units elsewhere.

## Blocking
- exercises.json:68 (fy3-4-L2-03) — solutions.md:79 says a value read by eye from 5,8 to 6,2 m is accepted, but tolerance 0,03 on 6,0 accepts only 5,82–6,18 m. A horizontal from B at 160 kPa (between the 150 and 175 kPa gridlines) to line A read on a 1 m grid easily gives 5,8 or 6,2, and the checker rejects them. Fix: tolerance 0.04 (5,76–6,24 m). The swapped ratio (2,7 m) stays rejected.
## Polish
- none
## Checked
- Recomputed: k_A = 100 kPa/10 m = 10 kPa/m, k_B = 150 kPa/10 m = 15 kPa/m, p_B(4,0 m) = 160 kPa, h_A = 60/10 = 6,0 m; answers.py 6,0.
- Figure two-liquids: both lines start at (0; 100 kPa) and end on grid crossings (10; 200) and (10; 250); mid points (5; 150) and (5; 175) agree; implied densities 1019 and 1529 kg/m³ are plausible.
- Solution's physics (same p0, slope ρg, the less dense liquid needs more depth) correct; Kuvaajan lukeminen present.
