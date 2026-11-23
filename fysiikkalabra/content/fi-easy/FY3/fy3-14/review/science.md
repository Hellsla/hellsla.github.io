VERDICT: PASS
CONTENT-HASH: b6aa82ddc71bc9de

## Blocking

## Polish
- lesson.md Tiivistelmä, third bullet — the formula for m_s is stated under "Jos Q_v < Q_j" but gives a negative value in case 3 (Q_v < Q_j,läm, water freezes); the bullet's "Poikkeus" covers only case 4. C: maybe add "kun vesi riittää lämmittämään jään 0 °C:seen", optional.
- inquiry.json koe-1 numeric — the answer is 26.6 but the solution's stated answer is 27 °C (two figures). It is inside the 5 % tolerance, so it is consistent; it could be worth saying which value the box expects.

## Checked
- Figures (the reason for this review): before-after numbers (75.3 g melts, 0.375 kg water, 0.025 kg ice left) recomputed; the cube sides halve, which fits area ∝ mass (1/4).
- Energy-balance bitmap measured against its gridlines: water bar ≈25 kJ, warming ≈2 kJ, total ≈36 kJ (25.1 / 2.1 / 35.5); to scale as claimed; the pale part is the unmelted ice.
- T(T_v) graph: threshold 26.57 °C at x=252.8, 40.07 °C at 80 °C at y=69.6, dot at 20 °C; all correct.
- Recomputed in one script: worked example (25 140 J, 17 540 J, 6.05 °C, ≈19 °C without fusion, 2/3, 18.8 kJ balance), misconception (15 °C, 24.7 g), predictions 1–2 (24.7 g; 5.9 / 18.5 g, Δ 12.6 g, 1/8), koe-1 (62.4 g, 10.1 °C, 0.3 g left at 26.5 °C), Etsi virhe (−26 °C, 0.225 kg), siirto (39.9 g; mistakes 43.9, 438), tea (40 °C; 56), exit ticket (66.8 kJ, 12.5 g), 80 K. All agree.
- The four end cases and the boundary (≥, exactly 0 °C) match the guardrail in the theory, summary, sim howto, sim code and feedback.
- sim.js solve(): case-4 temperature balance verified numerically; Q_end per case and the sequential stateAt keep liquid ≥ 0 °C and ice ≤ 0 °C; the chart scale choice matches the calc box.
- Experiments: koe-1 varies only TW0 and koe-2 only TI0, with the others locked; simState gives Tf and iceLeftG.
- Every choice item has exactly one correct option; the distractor feedback is right. Melting is described as an increase in interaction energy (guardrail wording), and the constant temperature is tied to normal pressure in the summary.
- Hash checked at the start and at the end: b6aa82ddc71bc9de.
