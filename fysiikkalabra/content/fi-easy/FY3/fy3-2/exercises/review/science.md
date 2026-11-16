VERDICT: PASS
CONTENT-HASH: 241f39cba1ade0b1

## Blocking
(none)

## Polish
- solutions.md:122 (L3-03) — "Tämä sopii arkikokemukseen aurinkosähköstä" is not a check. The comparison of 648 kJ per hour with 490 kJ before it already is one, so this sentence could go.
- solutions.md:171 (L2-07) — the Mallivastaus stands before Annettu/Kysytty. Place it after Periaate, as in L2-06 and L3-04.

## Checked
- Recomputed all 18 numeric answers in one script. They agree with answers.py and exercises.json: L1-09 18,36 kJ (ρ = 7,8·10³; 7850 gives 18,48, inside 4 %); L2-05 trapezoids 55,3 J; L2-06 1861 J / 8,1 s = 229,8 W, with the range 222–239 W from the extreme times; L3-03 2725 s = 45,4 min.
- L3-04: a least-squares slope through the origin gives 1,00 N/cm, so W = ½·10,0 N·0,100 m = 0,50 J and h = 25,5 cm. The trapezoid check from the data, 0,020 m · 25,0 N = 0,50 J, is right.
- L3-05: the least-squares slope through the origin is 0,815 m/s, so P = 3598 W. In d), Pt = 28,78 kJ and mgh = 28,69 kJ. The constant-velocity argument stays FY3 level, as in the lesson's mgh derivation.
- L1-05 changed check: 3,0 m/s = 10,8 km/h ≈ 11 km/h, a plausible skier's pace for 60 W. Correct.
- L2-08: W₁ = 1,0 J, W₂ = 4,0 J and the second part 3,0 J. One correct option and one correct reason. The "true but incomplete" reasons are rightly marked wrong, and their feedback says why.
- L1-06 and L1-08: exactly one correct option each. The distractor feedback is right (a perpendicular force does no work; power = W/t).
- L3-02: the assumption of no losses into kinetic energy is stated in the task, and the solution uses ΔU, not "heat in the water".
- Figure pull-steps: 25 N over 0–6 m and 10 N over 6–10 m, on grid lines. The description gives the same data without the work.
- Scope: W = Fs, the area under (s,F), mgh with the lift force equal to the weight, and P = W/t = Fv. No E_k, no cos α. Units and significant figures are right.
- Hash the same at the start and the end.
