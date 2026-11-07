VERDICT: PASS
CONTENT-HASH: 75644e4be115aed6
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- k3-b list: I = 2,98/220 = 0,013545 A; ΔU = 0,005·2,98 + 0,02 = 0,0349 V (1,17 %), + 5 % → 6,17 %, ΔI = 0,000836 A ≈ 0,00084 A (tol 0,1). Matches answers.py.
- k5: control electronics keeps drawn power 15 mW constant down to 2,0 V (statement, b solution, common error). W = ½·0,47·(4,5² − 2,0²) = 3,819 J, t = 3,819/0,015 = 254,6 s ≈ 255 s; list values 3,82 J and 255 s match.
- k6-e: Coulomb exact for point charges, spherically symmetric sphere acts as a point charge at its centre, nearby conducting spheres redistribute charge: correct in solution and rubric.
- k7-d: I_k = 51,2 V / 8,0 mΩ = 6400 A (51 × the 125 A fuse; ≈ 330 kW), with cable 4,3 kA; stored 16 · 3,20 · 200 = 10,24 kWh ≈ 10 kWh; full 58,4 V. Touching terminals no longer declared safe; below 120 V alone does not make it safe; arc, molten metal, fire; handle only with protection, competence, manufacturer instructions. Task, solution, rubric and common error agree. k7-e rubric wording on 120 V correct.
- practice.py check FY6/koe: OK, 120 points.
