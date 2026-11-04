VERDICT: PASS
CONTENT-HASH: 71907f335cfdbc4e

## Blocking

## Polish
- solutions.md:307–308 (L3-05 c, Järkevyys) — "Pisaran paino on vain noin 1,4·10⁻⁴ N, joten pieni ilmanvastus riittää … pienellä nopeudella" is true only for a small, light drop relative to its cross-section (B); and "kokee putoamisen vain noin 190 s ajan" says "vain" although the fall lasts ten times longer than without drag (17,5 s) — write "pisara on kevyt kokoonsa nähden, joten …" and drop "vain".
- solutions.md:252 and 291 (L2-05, L3-04) — three significant figures are justified by the mass, but the limiting datum is the time step read from the table (Δt = 0,40 s and 1,0 s, two figures) and the secant only approximates the slope at the midpoint — answer 0,11 N and 2,2 kN, or justify the third figure.
- solutions.md:253 (L2-05 Järkevyys) — "kiihtyvyys … noin puolet putoamiskiihtyvyydestä, kuten pitää" repeats the result instead of checking it — compare instead with the table's end: F_v approaches the weight 0,196 N as v levels off.
- exercises.json:215 (L2-06) — the comparison of drag at different speeds needs cones of the same size and shape; "samanmuotoisia" alone leaves size open — write "samankokoisia ja samanmuotoisia (sisäkkäin)".
- Set vs plan (docs/exercise-bank/FY4.md) — L2-05 (falling ball, slope → F_v = m(g − a)) repeats the method of L3-03 one level lower; the plan's level-3 linearisation (v_raja², m) is not there, and the plan's (t, v) parachute figure is a table in L2-07 — update the plan or change one task.

## Checked
- All 17 numeric answers recomputed independently (one script): json, answers.py and own model agree within tolerance; L3-04 F_v/mg = 2,78, ΣF = −1435 N; L3-05 v = 171,6 m/s = 618 km/h, 21× the 8,0 m/s.
- Data realism: foam-ball table follows v_t·tanh(gt/v_t) with v_t ≈ 5,8 m/s; cone speeds scale as √m (F ∝ v², plan's test); 0,0140 g drop ≈ 3 mm, 8 m/s terminal realistic; parachute decelerations 2,8 g, consistent with the lesson's "lähes kolminkertainen".
- MC L1-06, L1-07, L2-07: exactly one correct option, every distractor's feedback right; "samankokoinen ja samanmuotoinen" condition stated in L1-07.
- L1-08: student's 2089 N reproduces mg + F_v; correct 911 N up.
- Voimakuvio specs of new solutions: forces, a and v agree with the motion (L3-05 render checked).
- Scope: G + F_v = ma, terminal velocity, v² = 2gh; drag never computed from speed; F ∝ v² only inferred from data, as planned.
- Levels 8/7/5 fit; solutions complete.
