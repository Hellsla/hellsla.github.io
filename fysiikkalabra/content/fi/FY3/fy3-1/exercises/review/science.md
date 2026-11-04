VERDICT: PASS
CONTENT-HASH: aee75e10fdf5cfc4

Round 2. Delta review of the round-1 fixes (HEAD~2..HEAD~1) on the 20-task set; focus on the 8 new tasks.

## Blocking
- none

## Polish
- exercises/exercises.json:105 (L1-08) — the mass is now given as $0{,}18\,\text{t}$, so the task needs a t → kg conversion; this set's answers.py header puts "one conversion" at level 2. — Acceptable at level 1; or give $180\,\text{kg}$ again (two significant figures can be said in the answer line).
- exercises/exercises.json:188 (L2-06) — the Kuu row (1,2 N) is still unused; the solution now says so, but the plan line asks "g-arvot ja vertailu". — Ask also $g_\text{Kuu}$ (1,59 m/s²) and a comparison, or drop the row.

## Checked
- Round-1 Blocking (L2-07 a, "viidesosa") resolved: solutions.md:167 now says the mass is about a tenth of the reading 4,9, i.e. ≈ 0,49 kg; correct and consistent with b) 0,4995 → 0,50 kg.
- Round-1 Polish resolved: L2-05 slope read from the fitted line (origin, 0,50 kg; 4,90 N) → 9,8 m/s², least squares through origin 9,800; answers.py line updated to match.
- L3-05 Järkevyys now 2,64 · 612 kg ≈ 1616 ≈ 1620 kg; aligned Sijoitus block recomputed: 935 kg, 9172 N, 3469 N, 1617 kg, 682 kg.
- L3-04: "graph" dropped from kind, step renamed "Taulukon lukeminen"; task now says where b) is checked; g_X = 3,59 → 3,6 m/s² unchanged.
- L1-08: 0,18 t = 180 kg, G = 667,8 → 670 N, two significant figures from 0,18 t; answers.py `0.18 * 1000 * g["Mars"]` right.
- L1-06, L1-07: options reordered only; `answer` still equals the single correct option; feedback unchanged in physics.
- Plan docs/exercise-bank/FY3.md:11 now names the spring-calibration and lander tasks and gives the reason for leaving out the lift scale (Newton's laws, FY4).
- Hash checked at start and end: unchanged.
