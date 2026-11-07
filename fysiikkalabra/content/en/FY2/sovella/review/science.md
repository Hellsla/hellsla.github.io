VERDICT: PASS
CONTENT-HASH: 31d260a2d9963b78
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- Diff `git diff origin/main...HEAD` of sovella/tasks.json, sovella/solutions.md, lessons/FY2/sovella/answers.py (en); content hash recomputed and equal to the brief's.
- Ran `python3 lessons/FY2/sovella/answers.py` and `python3 scripts/practice.py check FY2` (OK, 2 tasks, 32 points, all three languages).
- fy2-s1 b five answers recomputed: coal $820\cdot380\cdot10^{6}\,\text{g} = 311\,600\,\text{t}$, gas $490 \to 186\,200\,\text{t}$, wind $11 \to 4180\,\text{t}$, cuts $1-490/820 = 40{,}2\,\%$ and $1-11/820 = 98{,}7\,\%$; match answers.py and the task text asks for exactly these.
- fy2-s1 c: $P_\text{tuuli} < 0{,}05\cdot28\cdot5{,}0\,\text{MW} = 7\,\text{MW}$ so $P_\text{muualta} > 80 - 7 = 73\,\text{MW}$: inequality direction correct in solution and rubric.
- Biomass $230\,\text{g/kWh}$ now a stated calculation assumption from IPCC AR5 WGIII Annex III (certain biomass chains, median; forest chips may differ considerably): matches the source; counterargument and alternative solution consistent.
- English changes match the fi source in substance (CO2 equivalent, internal energy vs heat, accounting assumption).
