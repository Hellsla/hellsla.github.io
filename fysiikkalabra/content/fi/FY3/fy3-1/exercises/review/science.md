VERDICT: FAIL
CONTENT-HASH: 7f00ff02dc7b5fbb

## Blocking
- exercises/solutions.md:167 (fy3-1-L2-07, Mallivastaus a) — A: "Luku $4{,}9$ on lähellä viidesosaa luvusta $9{,}81$" is wrong arithmetic: 4,9 is about half of 9,81 (ratio 0,50), which is exactly why the answer is 0,50 kg. — Replace with "Luku $4{,}9$ on noin puolet luvusta $9{,}81$, joten massa on noin $0{,}5\,\text{kg}$, paljon pienempi kuin $4{,}9\,\text{kg}$."

## Polish
- exercises/solutions.md:146 (L2-05, Kuvaajan lukeminen) — the slope is taken from the two raw end points (0,10; 0,99) and (0,50; 4,89), whose line misses the origin (intercept 0,015 N), while the text says the fitted line goes through the origin; guardrail: read the slope from points on the fitted line. — Read it from the drawn line, e.g. origin and (0,50 kg; 4,90 N) → 9,8 m/s² (least squares through origin also gives 9,80).
- exercises/solutions.md:193 (L3-05, Järkevyys) — "$2{,}6 \cdot 612\,\text{kg} \approx 1620\,\text{kg}$" is 1591 kg; the ratio is 2,644. — Write $2{,}64$.
- exercises/exercises.json:258 (L3-04) — `kind` has "graph" and solutions.md:174 has a "Kuvaajan lukeminen" step, but the task asks no graph; the step is a ratio from the table. — Drop "graph" or ask for the (m, x) graph in a).
- exercises/exercises.json:188 (L2-06) — the Kuu row (1,2 N) is never used; plan asks "g-arvot ja vertailu". — Ask also g_Kuu or drop the row.
- docs/exercise-bank/FY3.md:11 — level-3 plan (lift scale, why Earth does not "feel" the apple) is not what L3-04/L3-05 do; the lift reading needs Newton's laws (FY4), so the new tasks are the better choice. — Update the plan line to the spring-calibration and lander tasks.

## Checked
- All six new numeric answers recomputed independently (one script, own models, least-squares fits through origin): L1-08 667,8 → 670 N; L2-05 9,80; L2-06 3,71; L2-07 0,4995; L3-04 3,61 (sum ratio 3,59); L3-05 682 kg. All inside tolerance, answers.py lines right.
- L3-04 b): Mars is the only table value within ~3 %; Kuu check in L2-06 data consistent (1,59 m/s²).
- L3-05: 935 kg, 9,17 kN > 6,00 kN on Earth, 3,47 kN on Mars, Earth max 612 kg; force-limited model stated in task.
- L1-06, L1-07: exactly one correct option, every distractor wrong with correct feedback; mass/weight and interaction pair per glossary.
- Units, significant figures and rounding reasons in all new solutions; unknown solved symbolically before substitution; all within FY3 scope (G = mg, spring proportionality).
- No duplicate of an existing task; L2-07 follows plan's "voimamittari näyttää massan" error task.
