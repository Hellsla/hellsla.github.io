VERDICT: PASS
CONTENT-HASH: af4a4cef49e4f774

## Blocking

## Polish
- content/en/FY3/fy3-5/exercises/solutions.md:105 — L3-02 gets the rope force $F = G = mg$ from "constant speed", which is Newton's first law (FY4 by the scope note). This is fair at the level (C) and matches FY3's $G = mg$, $W = Fs$, but it could say "the rope holds the weight up with a force equal to its weight $G = mg$" without the dynamics — optional.
- lessons/FY3/fy3-5/answers.py — the comments use Finnish decimal commas and Finnish names (Q_ulos) in an English set. Cosmetic only.

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas, without using answers.py. They match answers.py and exercises.json, and every one is inside its tolerance.
- The sign convention $\Delta U = Q + W$ (W > 0 when work is done on the system) is the same in every task, solution, statement feedback and the L2-06 error analysis.
- L1-06 and L1-07: exactly one option is correct in each. Every distractor is really wrong, and its feedback gives the right reason (heat ≠ internal energy; temperature ≠ internal energy).
- L1-09: the true/false judgements are right. Q = 0 and W = 60 J give ΔU = 60 J, and the temperature rises because the air stays a gas.
- L2-01 and L2-08: the trapezoid read from `fy3-5/piston-force` at grid points (0; 200 N) and (0.20 m; 400 N) gives 60 J. The figure description gives the same points, and the figure does not give the answer away.
- L2-05: in a cycle ΔU = 0 because U is a function of state. W₄ = −90 J, and the check ΔU₄ = −90 J is consistent.
- L3-01 and L3-03: the condition "same T ⇒ same U" is stated as ideal gas (plus, in L3-03, negligible interaction energy), as the guardrail requires.
- L3-04: trapezoid rule 0.04 m · 468 N = 18.72 J. The slow isothermal work of 14.0 J < 18.7 J is physically consistent: an isothermal estimate from the table data gives about 14.7 J.
- L3-05: P = 2.00 kW, Q_out = 34.8 kJ (14.5 %), and the losses 8.1/16.3/26.1/34.8 kJ grow on every row. The assumptions (heater and kettle body not warming, W = 0) are stated in the task.
- L1-10: 1 cal = 4.1868 J (MAFY). The rounded 11 kJ is 3.3 % from 11.37 kJ, so it is inside the 4 % tolerance. Significant figures and reasonableness checks are real checks throughout.
