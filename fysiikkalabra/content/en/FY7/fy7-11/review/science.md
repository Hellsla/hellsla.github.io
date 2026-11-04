VERDICT: PASS
CONTENT-HASH: dd48ae14e2916f2f

## Blocking

## Polish
- lesson.md:290 (theta-graph aria-label) — says "n = 1.332", but the text uses $n = 1.3315$; the peak is 42.3° either way. Carried from round 1.

## Checked
- Red subscript fix: lesson.md, inquiry.json, solutions.md and lang/en.json sims.fy7-11 now use \text{r}/\text{v} throughout (no \text{p} left in en). r never clashes with another symbol here: the lesson names the critical angle in words only, with no α_r.
- Shortened sim legend ("Dashed lines: the surface normals and the extended incident ray.") matches what the canvas draws.
- One script (scratchpad sci/recompute_r2.py): crown speeds 198 111 / 196 053 km/s; worked example 34.88° / 34.47°, Δα = 0.41°; virhe 39.2° vs 34.5°.
- koe-1 (α1 = 50°, crown, Cauchy coefficients from sim.js): Δδ 0.527/0.702/0.942/1.395/4.446° for A = 30…70°; 38.44°/39.83° at 60°; flint 3.92°, water 0.85°.
- koe-2: 40.0° at 40°, minimum 38.43° near 49–50°, 50.25° at 80°; exactly one correct option.
- Rainbow: 42.30° (α ≈ 59.5°), 40.63° (α ≈ 58.8°); secondary 50.5°/53.5°; θ(90°) = 14.7°; siirto 25.40 mm; tarkistus-2 1945.9 km/s; exit ticket 42.3° − 50° < 0.
- Physics statements: colour fixed by frequency; the electron response growing towards UV absorption; prism equations hold only when the ray can leave; antisolar-point geometry and the sun-height limit.
- check_layout.py fy7-11 --width 340: en OK, no formula overflow.
