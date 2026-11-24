VERDICT: PASS
CONTENT-HASH: e86447c15ad2370f

## Blocking

## Polish
- assets/sims/fy1/fy1-6/sim.js:1052 — `tx()` always writes a decimal comma, so the English readout shows "27,5 m/s" and "6,88 m/s²" while the English text uses decimal points (exp-3 capture). Not a physics error. Fix: take the separator from the page language (shared with the other FY1 sims).
- lesson.md:130 — the heading "Mass does not affect falling" has no condition. The first sentence below it states one ("When there is no air resistance"), so this is C. "…in a vacuum" in the heading would match exp-3, where mass does matter in air.
- inquiry.json exp-1 solution — it uses $v_1 = 9.81\,\text{m/s}$, but the readout shows one decimal ($9.8$). The result and tolerance are unaffected.

## Checked
- Diff since the last PASS: the canvas note `huomautus` was removed from sim.js. Its content (dashed line = $v=gt$, arrow length = speed, dots = whole seconds) is still in the sim's `howto` box, so no model limit was lost. The physics, `simState` keys and adapter are unchanged.
- Sim model: vacuum $v=gt$, fall $\tfrac12 gt^2$; air $dv/dt=g-(K/m)v^2$ with the exact tanh / ln cosh solution, $K=\tfrac12\cdot1.2\cdot0.47\cdot\pi\cdot0.1^2$. These match sim-spec and the `model`/`calc` boxes. In vacuum, 4 s gives 78.5 m, which fits the 0–80 m scale.
- Recomputed with my own formulas in one script; every value matches lesson-answers.py: exp-1 9.81, data slope 9.8 (least squares through the origin 9.78), siirto 11.1 → 11, check-2 3.058 → 3.06 s, worked example 14.7 m/s / 52.97 km/h → 15 / 53, exit ticket 4.9, 29, 6.06, retrieval 1.08 → 1.1.
- All mistake values recomputed (1.82, 0.93, 2.7; 19.6, 29.4; 0.1; 29.4, 22.2, 3.7; 11.0, 30, 0.327).
- Air values at $t=4.0$ s: 0.1 kg 10.5, 1 kg 27.5 (the capture shows the same), 10 kg 37.5 m/s, all below $gt=39.2$ m/s. The exp-3 correct option and the conclusion's model answer agree.
- Experiments: exp-1 varies $t$ with environment and masses locked; exp-2 and exp-3 vary $m_B$ with environment, $t$ and $m_A$ locked. The slider steps (0.5 s, 0.1 kg) reach every suggested value, and `simState` gives vA and vB.
- Predictions, find-the-error and checks: exactly one correct option each. Every distractor's feedback says correctly why it is wrong. pred-1's "90" matches $v\propto t^2$.
- Figures: free-fall distances 0/4.9/19.6/44.1 m with gaps 4.9/14.7/24.5 m; $(t,v)$ graph points and slope 9.81 match their pixel scale; the data-graph points and fitted line (slope 9.81, 4.9 m/s at 0.5 s) are plotted correctly.
- Scope: $v=gt$ as a linear model, with no forces and no $s=\tfrac12gt^2$ formula. The air explanation names the mechanism (drag relative to the mass), and the condition "no air resistance" is stated in the theory, the summary and the formula.
- Retrieval context is realistic: a 1.4 m drop on the Moon takes 1.31 s.
