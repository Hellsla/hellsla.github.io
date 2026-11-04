VERDICT: FAIL
CONTENT-HASH: dca4421249ccc177
Round 2: full review of the exercise set after the round-1 fixes (commit c18c6114).

## Blocking
- solutions.md:167 (L2-07) — A, internal consistency: the Annettu still calls $t_1 = 0{,}320\,\text{s}$ and $t_2 = 0{,}575\,\text{s}$ "saapumishetki", which is the round-1 error; the task (exercises.json:243) and the Periaate (:168) now say they are the mid-times of the light interruption — write "katkoksen puolivälin hetki $t_1 = 0{,}320\,\text{s}$" (and the same for $t_2$).
## Polish
- exercises.json:243 (L2-07) — "valon katkos on puolivälissä, eli kappaleen keskikohta on portin kohdalla": the two are not the same moment for an accelerating body (the centre passes 0,38 ms after the mid-time at gate 1, 0,03 ms at gate 2; effect on g 0,14 %) — drop the "eli …" clause or write "suunnilleen silloin, kun keskikohta on portin kohdalla".
- exercises.json:359 (L3-05) — v = 24,5 m/s after 2,5 s means a 31 m drop with no air resistance; the task does not say air resistance is negligible — add "ilmanvastus jätetään huomiotta" (or use smaller times).
- exercises.json:359 vs :197 (L3-05 vs L2-06) — both now grade a clock offset found from a straight $(t, v)$ line (t₀ = 0,20 s and 0,15 s) — consider grading $g$ or the ratios' trend in L3-05 instead, so the level-3 task is not a copy of L2-06 with the sign reversed.
- exercises.json:44 (L1-06) — carried from round 1: same idea as L3-01; one distractor set in air (feather vs hammer on Earth) would separate them.
## Checked
- Hash dca4421249ccc177 at start and end.
- One independent script (python3 -I): all 16 numeric answers recomputed, all within tolerance; answers.py agrees.
- Round-1 Blocking 1 (L2-07 timing): task and Periaate now define t as the mid-time, where L/Δt equals the instantaneous speed; Δt_true 0,2553 s vs 0,255 s; only the Annettu label is left.
- Round-1 Blocking 2 (L2-05): "9,8 m/s²", 9,75 is 0,6 % below 9,81 — correct.
- Round-1 Blocking 3 (L1-08): 35,3 km/h with three digits — correct.
- Round-1 Polish: L2-07 sig figs and L1-08 kind fixed.
- L3-05 rewritten: ratios 7,54, 8,91, 9,25 → 7,5/8,9/9,2 as stated; slope 9,80 m/s² from every pair; t₀ = 0,65 − 4,9/9,8 = 0,15 s (0,1505 with 9,81; tolerance 0,05 OK), offset cancels in Δt.
- L3-04 text edits: 5 % criterion (0,98 − 0,93)/0,98 = 5,1 %; 62,0 % unchanged.
- Scope stays at v = g t, Δv = g Δt.
