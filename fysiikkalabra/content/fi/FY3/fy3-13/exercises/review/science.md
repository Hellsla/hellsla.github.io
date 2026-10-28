VERDICT: PASS
CONTENT-HASH: 0af6ca31258def39

## Blocking

## Polish
- lessons/FY3/fy3-13/answers.py:22 — the extra key "L2-03-gauge-zero" (5,45 °C) is printed among the exercise answers — keep it as a comment so that the printed JSON holds only exercise ids.
- exercises/solutions.md (L2-01 Järkevyys) — "ero johtuu kahden pisteen mittausvirheestä" is stated as fact. A difference of 17 °C could also come from a systematic error — write "voi johtua".

## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff (there were none). The only change, "järjestelmällinen virhe" → "systemaattinen virhe" in L3-03 Periaate and Järkevyys, matches the guardrail term and the lesson. It is grammatical, and the physics and the answer are unchanged.
- All 12 answers recomputed in one script from the task text with my own formulas. All agree with answers.py and exercises.json, and the tolerances fit the rounded answers.
- θ₀ = −p₀/k and θ₀ = θ₁ − p₁/k are used correctly; ΔT in °C equals ΔT in K; bar units cancel (L2-01).
- L2-03: the gauge pressure is correctly converted to absolute pressure before the fit, and the reasonableness check (a gauge-pressure zero at 5,5 °C) is a real check.
- L3-01: the two-point extreme lines give −234,55 and −275,17 °C, so Δθ₀ = 20,3 °C. The reason it is wider than for seven points (the intermediate bars constrain the slope) is correct.
- L3-02: p ∝ T in kelvin gives 28,2 kPa at 77 K. The stated condensation temperature of about 67 K at about 25 kPa is consistent with nitrogen's vapour pressure, and the reason the line cannot reach 0 K (the amount of gas changes) is correct.
- L3-03: n = 11,15/6,00 = 1,86. The solution says the uncertainty is not a strict limit and names systematic error or an underestimated uncertainty, in line with the guardrails.
- L1-03 uses the accepted value as the reference for the signed error and the absolute deviation, which is correct use of the term mittausvirhe.
- The symbols (p₀, k, θ₀, Δθ₀) and the significant-figure reasons match the lesson.
