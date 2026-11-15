VERDICT: PASS
CONTENT-HASH: d3400f5728b0c96a
Mode: full (round 1)

## Blocking
- none

## Polish
- exercises.json fy8-6-L1-06 (correct option, also solutions.md model answer) — "only when the energy $eU$ ... is approximately equal to $hf$" reads as if no photon were produced above the threshold — "at least approximately equal", as the L2-01 solution says.
- solutions.md fy8-6-L2-06 (part b) — "the electrons need extra voltage ... to make the current larger" names no mechanism — say that above the threshold the voltage across the LED grows with the current, so the reading depends on the chosen current.
- solutions.md fy8-6-L2-05 (Reasonableness) — the check uses the raw point $(2.30\,\text{V};\ 27.3\,\text{mA})$, not a point of the fitted line ($27.2\,\text{mA}$) — take the point from the line.
- solutions.md fy8-6-L2-08 — the yellow LED's residual is $-0.052\,\text{V}$, just over $\pm 0.05\,\text{V}$; "the points also fit the line" could say "about within the uncertainty".

## Checked
- All 19 numeric answers recomputed in one script from the task texts with own formulas and fits: each agrees with exercises.json and answers.py to under 0.2 %; rounding to the data's figures stays inside every tolerance.
- Fits: L2-05 slope 61.5 mA/V, U_k 1.857 V; L3-01 k 4.212e-15 V s, b -0.164 V; L3-04 k 4.208e-15 V s, b -0.062 V -> -0.112 V, slope unchanged; L2-08 table gives k 3.98e-15 V s, b -0.07 V, standard error 0.21e-15 V s.
- L2-06: 5.858, 6.329, 6.868 e-34 J s; -11.6 %, -4.5 %, +3.65 %.
- L2-08: exactly one justified option (6.626 inside 6.04–6.71); each distractor wrong for the reason its feedback gives.
- L3-05: 486.0 nm, direct formula 504.1 nm, interval 476.7–495.7 nm.
- L2-03, L3-03: one photon per electron stated in the task; share under 100 %.
- L2-04, L2-07: fluorescence energy balance, "internal energy" wording per guardrails.
- e U_k ≈ hf kept approximate; the 0.1 V offset and the slope method consistent across solutions; L3-02 interval called estimated.
- Scope inside FY8; units and dimensions right; symbolic form before substitution.
