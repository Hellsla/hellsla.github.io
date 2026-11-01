VERDICT: FAIL
CONTENT-HASH: 7d7b29efa3098499

## Blocking
- lesson.md:653 — B (missing condition): "Kiihtyvyys on koko lennon ajan $g = 9{,}81\,\text{m/s}^2$ alaspäin" is stated for a thrown ball with no condition; with air resistance the acceleration during the flight is not $g$ (only at the top point, where $v = 0$). The same paragraph adds the condition only for the third misconception. — Fix: "Kun ilmanvastus on pieni, kiihtyvyys on koko lennon ajan …" (as check-1 already states in its prompt).

## Polish
- inquiry.json:280 (exp-3 prompt) — the right tangent end is given as $(4{,}2\,\text{s};\,16\,\text{m})$, but hint 3 and the solution use $16{,}2\,\text{m}$; with 16 m the slope is 5,92 m/s (accepted by the 5 % tolerance, but the solution then disagrees with the given data). — Give $16{,}2\,\text{m}$ in the prompt too. The (t,x) graph's 20 m gridlines do not allow reading these points; the prompt giving them is right, so "Piirrä kuvaajasta lukemillasi pisteillä" should say the points are given.
- inquiry.json:345 (putoaminen solution) — "kolme merkitsevää numeroa kuten matkoissa, jotka on luettu millimetrin tarkkuudella": the small early distances have one or two significant figures; justify three by the large distances (0,477…0,832 m) that dominate $A$.
- lesson.md:595 — the fit uses $s$ while the position equation uses $x$; one sentence saying $s$ is the position measured downward from the first frame would make $A = \tfrac12 a$, $B = v_0$, $C = x_0$ explicit.

## Checked
- One script recomputed every number from the task data: hook 1,23 m / 4,91 m; retrieval 3,0 m/s; exp-1 1,0/4,0/9,0 m, third second 5,0 m; exp-2 v = 2/0/−2 m/s, x(3 s) = 9,0 m, back at 0 at 6,0 s; tangent ends 1,8 m and 16,2 m, v = 6,0 m/s; worked example 76 m²/s², 8,72 m/s, 9,44 s, rejected −25,4 s, check 60 m, 31 km/h; error-spot 24 m vs 48 m; transfer 1,875 m/s², 40 s, 0,19 g; check-2 32 m (16 + 16); check-3 4,9 m and 14,7 m.
- Free-fall data: own least-squares fit A = 4,884 m/s², B = 0,126 m/s, C = 0,0013 m, g = 9,77 m/s² (residuals ≤ 2,4 mm, plausible noise); one-point mistake 10,4 m/s².
- Every prediction, experiment question, error-spot and check: exactly one correct option, each distractor wrong with correct feedback; mistakes' values match their feedback.
- Sim: implements v = v0 + at, x = v0 t + ½at², x0 = 0; tangent ±1,2 s gives the 1,8 s / 4,2 s ends; signed area shading; limits stated in the model box; exp setups lock v0, a and vary t, simState gives x and v.
- Figures: strobe gaps 50/150/250 (1:3:5) and reverse, v arrows linear, a arrows constant; hero gaps 25/75/125/175 (1:3:5:7) and v arrows 19/38/57/76; fall-points and check-tv plots match their data.
- Definitions (a, sign of a vs speed change, tangent vs secant, area = signed displacement) consistent across theory, summary, glossary, exit ticket and model answers; scope inside FY4 central contents.
