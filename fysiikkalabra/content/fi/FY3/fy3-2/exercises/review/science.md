VERDICT: PASS
CONTENT-HASH: 84f17883f8223bc3
SCOPE: delta added-exercise from f348009c527c1f49 base 89bcb63b7431

## Blocking

## Polish
- exercises/exercises.json (fy3-2-L2-09) — uses the same figure `fy3-2/pull-steps` as L1-04, whose answer (190 J) is the first step here; physically right, but a student who did L1-04 has half of it done. Optional: a different step graph, or accept as a deliberate follow-up.
- exercises/exercises.json (fy3-2-L1-09) — stored answer 18,4 kJ while the data (0,020 m³, 12 m, 7,8·10³ kg/m³) carry two figures and the solution answers 18 kJ; tolerance 0,04 accepts 18 kJ (2 % off) and a 7,85·10³ table value (18,5 kJ), so not blocking.

## Checked
- MAFY value verified on mafytaulukot.fi (*Tiheyksiä*, 20 °C): teräs $7{,}8 \cdot 10^3\,\text{kg/m}^3$, as the solution uses.
- L1-09 recomputed: $m = \rho V = 156\,\text{kg}$, $W = \rho V g h = 18\,364\,\text{J} \approx 18\,\text{kJ}$; answers.py agrees.
- L1-09 model: "hitaasti" stated, so lifting force = weight (the chapter's own condition for $W = mgh$); $m = \rho V$ is defined in the task, so nothing beyond the brief is needed; steel density realistic.
- L1-09 solution solved symbolically ($W = \rho V g h$) before substitution; kJ conversion shown; check (~1,5 kN · 12 m) is a real check.
- L2-09 recomputed from the figure code: 25 N over 0–6 m, 10 N over 6–10 m, $W = 190\,\text{J}$, $F_\text{ka} = W/s = 19\,\text{N}$; answers.py agrees.
- L2-09 figure gives every value on grid lines (1 m, 5 N); description lists the levels, not the work or the mean force; force along the motion stated in the task.
- L2-09 solution complete: graph reading, area principle, symbolic $F_\text{ka} = W/s$, check that 19 N lies between 10 N and 25 N nearer the longer level.
- Units and tolerances fit; both in FY3 scope (W = Fs, area under (s,F)).
- Rest of the set unchanged since PASS; hash same at start and end.
