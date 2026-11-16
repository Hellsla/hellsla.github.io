VERDICT: PASS
CONTENT-HASH: ce62540bde4a3a8a

## Blocking
None.

## Polish
1. solutions.md:68 (L1-04 Reasonableness) — "$6\,\text{s} : 0.8$" should be "$6\,\text{m/s} : 0.8\,\text{m/s}^2$" (wrong unit on the speed).
2. solutions.md:310 (L3-04 Principle) — "the sled stops next to the fence exactly at the maximum allowed length" contradicts the task: it stops 5.0 m before the fence (20.0 m from the foot). Write "stops exactly 5.0 m before the fence". This was already noted in the previous review.

## Checked
- One script recomputed all 19 numeric answers from the task text with its own formulas, and they agree with exercises.json and answers.py (for example L2-03 220.5 kJ, L3-02 2.287 m/s, L3-04 16.33 m and 7.67 m/s, L3-05 h = 55.625 m and 2.205 kN, c) 851 N).
- ex-hissi (figures.py) is consistent: 650 N for 1.0–3.0 s, then 800 N for 6.0–8.67 s, stops the lift exactly. The 0.2 s ramps are centred on the phase limits, so Δt = 2.0 s holds.
- L3-01: the sled reaches the flat at any split of the 4.5 m height (slope horizontal 9.6–25.5 m < 37.5 m), and both parts have tan α > 0.120.
- The data sets fit their models: L2-06 has nearly constant deceleration and the sled stops after 5.0 s; L2-08 has h/x ≈ 0.10 in every row; L2-05 has a ≈ 0.40 m/s².
- L2-08 follows the guardrails: 2Δx overlap, "cannot be shown" is not "equal", and the extrapolation is flagged. L2-07 calls the half-range a scatter estimate, not the uncertainty of the mean.
- L1-06 and L1-07 each have exactly one correct option, and the distractor feedback is right.
- The rounding is right: L3-04 is an "at most" value, 16.33 m rounded down to 16 m; L2-06 has two significant figures, limited by 0.46 m.
- The force diagrams are right: the drag is drawn longer than the weight while slowing, the friction points up the slope or backwards, N = mg cos α, and velocity is not drawn as a force.
