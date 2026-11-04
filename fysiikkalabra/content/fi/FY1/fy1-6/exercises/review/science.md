VERDICT: FAIL
CONTENT-HASH: 5de57c6f45f43e68

Full review of the exercise-bank additions (L1-06..08, L2-05..07, L3-04..05); existing tasks unchanged.

## Blocking
- exercises.json:243 (L2-07) — the task says $t$ is the moment the body *arrives* at the gate, but $v = L/\Delta t_\text{valo}$ is the mean speed over the 25,0 ms and 11,1 ms passages, i.e. the speed at the passage's mid-time. With the stated timing the data give $g = 2{,}505 / (0{,}255 - 0{,}00695) = 10{,}1\,\text{m/s}^2$, not 9,8 (data built as if v were the arrival speed) — say that the clock records "hetken, jolloin valon katkos on puolivälissä" (for constant acceleration the mean speed equals the speed at the mid-time, so 9,82 stays exact), and mention it in solutions.md:169 Periaate.
- solutions.md:152 (L2-05) — 9,75 m/s² is rounded to "9,7", and "poikkeaa alle prosentin" is false for 9,7 (1,1 %) — write $g \approx 9{,}8\,\text{m/s}^2$ (9,75; 0,6 % below 9,81); answers.py 9,74 unchanged.
- solutions.md:141 (L1-08) — "35 km/h … kolme merkitsevää numeroa" shows two digits — write $35{,}3\,\text{km/h}$ sekunnissa.
## Polish
- solutions.md:173 (L2-07) — the limiting datum is $L = 5{,}0\,\text{cm}$ (two digits); say that instead of "kolme merkitsevää numeroa nopeuksissa … mutta kahdella".
- exercises.json:108 (L1-08) — kind "concept" on a numeric unit conversion; "model" or none fits better.
- exercises.json:44 (L1-06) — same idea as L3-01 (mass does not matter in vacuum); the plan asked for the question "ilmanvastus huomioiden": one distractor could be set in air (feather vs hammer on Earth) to separate the two.
## Checked
- answers.py run with python3 -I: all 18 numbers match exercises.json; recomputed independently in one call.
- L2-05 least squares k = 9,743 m/s², b = 0,013 m/s (through origin justified: time from release); tolerance 0,05 → 9,26–10,23.
- L2-06 fit k = 9,80 m/s², b = 1,97 m/s, t₀ = 0,201 s; intercept = speed at measurement start, explained right.
- L3-04 ball v/t = 9,80–9,87 m/s²; paper data follow 1,5·tanh(gt/1,5) to within 0,1 m/s (realistic terminal speed); (3,924 − 1,49)/3,924 = 62,0 %.
- L3-05 true times 0,50 s and 1,50 s, clock 0,15 s early, 14,7/1,65 = 8,9 too small, slope 9,8 m/s²; systematic error named correctly.
- L1-06, L1-07 one correct option each; distractor feedback says why each is wrong.
- Scope stays at v = g t and Δv = g Δt; no forces or s = ½gt².
