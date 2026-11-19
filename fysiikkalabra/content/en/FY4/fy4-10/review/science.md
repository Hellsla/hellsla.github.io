VERDICT: PASS
CONTENT-HASH: 620a6676a436e439

## Blocking

## Polish
- inquiry.json:132 (sim `model` box): "then the bumper stays compressed, and its energy becomes internal energy". An elastically compressed spring held by velcro would keep its elastic energy. The model really treats the soft bumper as crushed (permanently deformed), so its energy goes to internal energy. Say "the soft bumper stays crushed (permanently deformed), so its energy becomes internal energy". The readings do not change.
- lesson.md "Worked example", Result: the two-figure rounding cites only the velocities. The masses 32 000 kg and 18 000 kg are ambiguous. Could add "the masses are given at least as precisely".

## Checked
- One script ran model.js in node, compared the results with lesson-answers.py and with my own closed-form formulas for 12 runs (tarra, kimmoisa, rajahdys, kimmoton × m2 = 0.20/0.40/0.60 kg). They agree: tarra 0.40/0.30/0.24 m/s; elastic (0.20, 0.80), (0, 0.60), (−0.12, 0.48); explosion 0.632/1.265 m/s with 0.24 J. In every run the momentum drift is ≤ 7e-16 and the energy drift is ≤ 1e-6 J. Conservation comes out of the equal and opposite bumper forces; it is not written into the model.
- Every number in the lesson and the inquiry matches my own recomputation: kertaus 0.30, pred-1 distractor 0.424, worked example 1.14 m/s and 38.3 → 32.5 kJ (15 %), virhe 0.025/0.475, siirto 1.0 (mistakes 2.4, 0.706, 5.76), check-2 0.15 (mistakes 0.60, 0.20), Kaava example 0.30 m/s and 0.072 → 0.036 J, exp-1 E_k′ range 0.029–0.048 J.
- The feedback for mistake 0.706 (the boy's velocity taken relative to the boat) is the right physics.
- Conservation is derived from the third law plus impulse, and the condition (zero external net force or negligible impulse) is stated in the theory, formula section, summary, exit ticket and every solution. The section is named after the right law.
- Billiard argument: v₁′v₂′ = 0, so the cue ball stops. The equal-mass and elastic conditions are stated, and real-world deviations (spin, not perfectly elastic) are named.
- Every prediction, experiment question, find-the-error item and check has exactly one correct option. Every distractor's feedback is correct.
- Experiments: each sets tyyppi, m1, v1 and v2, locks them and varies only m2. `simState` provides u1, u2, pJ and EkJ. In the explosion case the velocities are zeroed and the sliders are disabled.
- Figures: in "tarra" the momentum arrows are equal and the velocity arrow is halved; in "tyypit" the momenta are to scale and the animation speeds are consistent (exchange, half-speed, equal and opposite); "vuorovaikutus" shows equal and opposite F and Δp.
- Energy language follows the guardrails (internal energy, never "heat"). The only "heat" is in a wrong option, as the guardrails allow.
- Scope is one-dimensional only, within FY4's central contents.
