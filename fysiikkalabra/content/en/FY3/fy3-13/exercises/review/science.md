VERDICT: PASS
CONTENT-HASH: 00a825e2f438db3a

## Blocking

## Polish
- solutions.md fy3-13-L3-05 Formula — the last row $\Delta\theta = \Delta p/k$ is stated, not derived from the row above it. — Optional fix: insert $\Delta\theta = \dfrac{(p + \Delta p) - p}{k}$ before it, or one word: "a change $\Delta p$ shifts $\theta$ by".

## Checked
- Diff: only Formula steps changed. Each extrapolation now starts from the line equation $p = p_1 + k(\theta - \theta_1)$ (or $p = p_0 + k\theta$), then sets $p = 0$ and solves symbolically to $\theta_0 = \theta_1 - p_1/k$. This is the form each unchanged Substitution uses (L1-01, L2-01, L2-03, L2-05, L2-06, L2-07, L2-09, L3-01, L3-04).
- L2-03: absolute pressure $p = p_\text{g} + p_\text{air}$ comes before the fit. The correct reason is stated (only the absolute pressure's zero means a vacuum), and θ0 = −270 °C.
- L2-02, L3-01, L3-04: the limit-line zeros and $\Delta\theta_0$ = half of the interval agree with the guardrail ("estimated" interval, "probably"). Δθ0 = 14.1 °C, and the A and B intervals contain −273.15 °C.
- L3-02: $p/T = p_0/T_0$ holds in kelvins only, and the condition "the gas stays a gas" is in the Principle (guardrail: thin gas far from condensing). p = 28.2 kPa.
- L3-05: inverting the calibration line gives θ = −17.5 °C and Δθ = 2.73 °C. The extrapolation length is stated.
- L2-10: the conversion $\theta = T - 273.15$ K comes first, then the line, giving p = 54.9 kPa.
- L1-09: $T = \theta + T_0$ with $T = 0$ gives $\theta_0 = -T_0$. This is correct.
- I recomputed every changed solution in one script, and all match. The hash is identical at start and end.
