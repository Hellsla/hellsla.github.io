VERDICT: PASS
CONTENT-HASH: fe2164fcd01f7717

## Blocking

## Polish
- lesson.md:174 — case 3 says "part of the water *may* freeze"; when $Q_\text{w} < Q_\text{i,warm}$ some water necessarily freezes (only how much depends on case 3 vs 4) — "part of the water freezes".
- lesson.md:317 (Summary) — the $m_\text{melt}$ formula is given under "If $Q_\text{w} < Q_\text{i}$" without its condition $Q_\text{w} \ge Q_\text{i,warm}$ (in case 3 it turns negative) — add "when the water can warm the ice to 0 °C", as in lesson.md:199.
- inquiry.json siirto solution, Answer step — the sig-fig reason "affects only the thousands place of the third figure" is unclear; say the 8.0 K term changes the denominator by under 0.1 %, so the three-figure data (0.250 kg, 14.0 K) limit the answer.
- inquiry.json koe-1 solution — the answer is rounded to $27\,{}^\circ\text{C}$ but the numeric key is 26.6; both are accepted by the tolerance, but the stated answer and the key could agree (e.g. state 26.6 °C as the threshold with three figures from the slider bracket).

## Checked
- One script recomputed every number: 25.1/33.4/35.5 kJ, 75.3 g melts, 24.7 g left, limit 26.57 °C, 40.07 °C at 80 °C, 10 °C→62.4 g, 40 °C→10.1 °C, worked example 6.05 °C (balance 18.80/18.81 kJ, 19 °C without latent heat), prediction 2 5.9/18.5 g, Δ12.6 g, 31.4 kJ, find-the-error −25.6 °C / 0.075 / 0.225 kg, transfer 39.9 g (mistakes 43.9, 437.5), tea 40.06 °C (mistakes 56, 35), exit 66.8 kJ and 12.5 g, "almost 80 K" (79.7).
- Four end states and boundaries (≥ for all melts, exactly 0 °C at equality, all-water-freezes case) agree across theory, summary, misconception, sim boxes, feedback (guardrails).
- sim.js `solve`: all four cases and the case-4 temperature derived from the energy balance; `Qend` per case and `stateAt` sequence (water never below 0 °C liquid, ice never above 0 °C) are correct.
- Experiments isolate the varied parameter (TW0, then TI0) with the others locked; slider steps reach the asked values; `simState` carries Tf and iceLeftG.
- Exactly one correct option in every choice item; every distractor's feedback names the right physics.
- Figures: energy bars to scale (25.1 vs 35.5 kJ), before-after masses (0.375/0.025 kg), T(Tv) graph coordinates (26.6 → x 252.8, 40.07 → y 69.6) verified.
- Melting described as increasing interaction energy, freezing releasing energy; pressure condition stated in the summary; within FY3 scope.
- Model values labelled as model values; animation time scale said to be illustrative.
