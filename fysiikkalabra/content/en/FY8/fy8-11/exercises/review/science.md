VERDICT: PASS
CONTENT-HASH: f8c07e8ba0e19ff7

## Blocking

## Polish
- solutions.md:70 (L2-01) — the solution's answer is "1.5 kg, two significant figures", the stored answer 1.51; same in solutions.md:136 (L2-04): "about 4.1 %" against stored 4.11. Both are inside the tolerance; give one value in both places.
- exercises.json:151 (L2-05) — "five successive generations", but the table has six rows (generations 0–5); say "generations 0–5".
- exercises.json:347 (L3-04 c) — "isolated for thousands of years" understates what the solutions of L3-03 and L3-04 show (a thousandth only after about 240 000 a); write "hundreds of thousands of years".
- The packet says check_lesson.py had not been run: stored answers were compared with answers.py's output by hand (all 17 agree).

## Checked
- All 17 numeric answers recomputed with own formulas; every stored value within its tolerance (largest difference 0.57 %, L3-01).
- Reaction energies: Li-6 + n 4.783 MeV, D + D 3.269 MeV, D–T 17.59 MeV and 3.374e14 J/kg, Xe/Sr fission x = 2 and 184.68 MeV, 4 H to He-4 26.73 MeV; electron bookkeeping with atomic masses right in each.
- L2-08: Q = 12 (7.074 - 7.680) MeV = -7.27 MeV, agrees with the atomic masses (7.27 MeV); exactly one correct option and one correct reason.
- L3-04: own least-squares fit gives lambda = 0.02285 1/a, A0 = 30 060 TBq/t, T = 30.3 a, t = 249.7 a; two-point method 251 a, inside the 5 % tolerance; ln A values right; extrapolation range stated; Pu-239 factor 0.993.
- L3-05: 1536 MW, 1029 MW, 4.457e16 J, 543.0 kg, 1.54e6 t coal, ratio 2.8e6; assumptions stated in the task.
- L2-05: k = 1.01248, 1859.6; k rounded to 1.012 gives 1816, inside the 3 % tolerance.
- L2-06: 4394 MW, 34.64 TWh; L2-01 1.509 kg; L3-01 4.526 kg; L3-02 8.944e37 1/s (assumption on radiated power stated); L3-03 240 175 a.
- Multiple choice L1-06, L1-07, L2-07: one correct option each, distractors wrong, feedback physics right.
- Solutions: symbolic form before substitution, conversions right, reasonableness checks recomputed.
- Scope: inside FY8 central contents and the scope notes (931.5 MeV/c^2, decay law).
