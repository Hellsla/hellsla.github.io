VERDICT: PASS
CONTENT-HASH: d664f2efd876fc3d

## Blocking
(none)

## Polish
- solutions.md:95–100 (L3-01) uses $F_\text{avg}$, while solutions.md:233–238 (L2-09) uses $F_\text{av}$ for the same quantity. Use one symbol.
- solutions.md:122 (L3-03) — "This matches everyday experience of solar electricity" is not a check. The 648 kJ per hour comparison before it already is one.

## Checked
- The packet's lesson brief is empty (an empty markdown fence). I judged the physics from the exercises themselves; notation follows the Finnish set (W = Fs, G = mg, P = W/t = Fv).
- Recomputed all 18 numeric answers in one script. Every answer, unit and tolerance is identical to the fi-easy set, and all agree with answers.py: L1-09 18,36 kJ; L2-05 55,3 J; L2-06 229,8 W; L3-03 45,4 min; L3-04 25,5 cm (least-squares slope 1,00 N/cm); L3-05 3,598 kW (slope 0,815 m/s).
- The changed L1-05 check is right: 3.0 m/s ≈ 11 km/h, a skier's pace. The work in one second, 60 J, gives 60 W.
- L1-06, L1-08 and L2-08 (option and reason): exactly one correct option each. The distractor feedback is physically right, and the true-but-incomplete reasons in L2-08 are explained.
- L2-07 error analysis: mass used as force, so the factor g is missing. 588,6 J becomes 590 J.
- L3-02: the energy assumption is stated, and the result is called an increase in internal energy, not heat.
- L3-05 b) and L2-06: lift force equals weight at constant velocity, the lesson's FY3-level statement, with no Newton's laws.
- Scope: no E_k, no cos α. Units and significant figures are right, and so are the rounding reasons.
- Hash the same at the start and the end.
