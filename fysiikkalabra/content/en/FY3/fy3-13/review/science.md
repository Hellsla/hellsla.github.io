VERDICT: PASS
CONTENT-HASH: b1e6f4325c6b5b7c

## Blocking

## Polish
- inquiry.json suora, solution "Answer" — the rounding reason cites "the subtraction 20.0 − 296", but the substitution shown goes through p0 = 101.26 kPa and θ0 = −p0/k, not θA − pA/k — give the reason for the route actually shown (θ0 = −275.8 °C rounded to whole degrees).
- lesson.md, liquid-nitrogen caption — "water droplets condensed around the cold nitrogen vapour": more exact is "water droplets condensed from the air's water vapour, cooled by the cold nitrogen vapour".
- lesson.md Key idea and Summary — "Measurement uncertainty describes the uncertainty attached to a measurement result" is circular; the guardrail wording "an estimate of how large the error may be" says more.

## Checked
- One script recomputed everything from the data: least-squares line k = 0.3667 kPa/°C, p0 = 101.26 kPa, θ0 = −276.2 °C (matches the drawn line and A, B); worked example −276.02 °C, limit zeros −258.66 and −294.81 °C, Δθ0 = 18.08 °C → −276 ± 18 °C; lesson-answers.py output agrees.
- Limit lines: a brute-force search over bar-end pairs confirms that (10; 104)–(85; 133) and (25; 111)–(100; 137) are the steepest and shallowest lines through all ±1 kPa bars; s2 = 98.9 + 0.42θ misses exactly 10, 70, 85 and 100 °C, as the feedback says.
- Numeric tasks and their mistakes: suora −275.8 (mistake −295.8 → −296), epavarmuus 18.1 (mistake 36.2), siirto −276.9 (p0 120.0, mistake −306.9), tarkistus-2 −282.9 (mistake −297.9), virhe −316 wrong vs −276 right; exit ticket k = 0.36 kPa/°C and interval −282…−258 °C.
- Formula-section figure checked against its pixels: all seven points, the best line (θ0 −276 °C) and both limit lines (−259 and −295 °C, p at 10 °C 104.0 and 105.8 kPa) are to scale, as stated; inquiry figures 3, 4 and 6 agree with the given equations.
- Models and conditions: constant V and n, dilute gas, linear only within the measurement range, liquefaction before 0 K, the extrapolated value only an estimate, the true value "probably" in the interval, the manufacturer's error limit kept apart from uncertainty (guardrails).
- Predictions: exactly one correct option each (kertaus 313/293 ≈ 1.07; ennuste-1 linear, below 0 °C; ennuste-2 tens of degrees); every distractor's feedback is right.
- tarkistus-1, check-c2, the explain model answers and criteria agree with the theory and the guardrails on fits and outliers.
- Hash same at start and end.
