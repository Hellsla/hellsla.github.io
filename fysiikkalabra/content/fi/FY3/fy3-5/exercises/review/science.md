VERDICT: PASS
CONTENT-HASH: 37e15a3d153f0c4c

Delta review over the audit's PASS (a3a64a7608c7dd0a): L2-01 now reads a varying piston force from figure piston-force (area of a trapezoid).

## Blocking
- none
## Polish
- solutions.md:59 says −14,5…−15,5 J is accepted, but tolerance 0,03 on −15 accepts −14,55…−15,45 J. Both end points are exact grid crossings, so no reasonable reading falls in the gap. Narrow the stated range, or set tolerance 0.034.
## Checked
- Recomputed: W = (200 N + 400 N)/2 · 0,20 m = 60 J on the air (positive), Q = ΔU − W = 45 − 60 = −15 J; answers.py −15.
- Sign of work right (the surroundings do work on the gas, W > 0); Q < 0 means heat leaves the air, as the task defines.
- Figure piston-force: (0; 200 N) and (0,20 m; 400 N) on the 0,05 m × 50 N grid crossings; no area shaded; the description lists the end points only.
- Wrong methods rejected: F_max·s gives −35, F_min·s gives +5, the wrong sign of W gives +105.
