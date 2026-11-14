VERDICT: PASS
CONTENT-HASH: 5ba40612c9cadfb9

## Blocking
(none)

## Polish
- sim.js:1050-1053 — the English page shows decimal commas in the sim readout and canvas (20,0 °C, 0,30 kg, 5,80 kJ; seen in fy3-6-sim-1280.png), because `tx`/`fi` always write a comma. The numbers are correct, but this is not English notation — let the locale choose the separator (this is a shared formatting fix, not a physics error).
- lesson.md:416 (scene aria-label) — "steam rises from the stones": what you see is condensed droplets, as the kettle caption on lesson.md:158 says. Saying "a cloud of vapour droplets" would match that caption.

## Checked
- Recomputed everything in one script with my own formulas. Worked example: Q_w = 5656.5 J, c_m = 374.6 → 3.7·10² J/(kg·K). The 24.6 °C variant gives 383. A lossless copper object would give T = 24.62 °C. C_w = 1257 J/K, C_m ≈ 75 J/K. Misconception box: 35 °C; water/iron ratio 9.3, which matches "almost ten times" and the exit ticket's "about nine times". Exit ticket: 419 kJ.
- inquiry numbers all agree. ennuste-1 / koe-1: 26.8 °C (+6.8 K) and 44.0 °C, Q 8.5 kJ and 30.2 kJ, C 160 J/K and 838 J/K. ennuste-2 / koe-2: 40.0, 55.0 and 63.1 °C. virhe: 6.6 °C (wrong form) and 30.0 °C (right); adding 273.15 to every temperature does not change the wrong result. siirto: 29.09 kg, with mistakes 220 and 21.3. tarkistus-2: 890.6, with mistakes 768 and 501.0; 838/134 = 6.25. tarkistus-1: 4500 vs 838 J/K. check-c2: 35 °C, and the 65 °C distractor is correctly explained.
- Choice items: exactly one correct option in each, and every distractor's feedback names the right mechanism (heat as energy in transfer, net transfer, no "cold", equal temperatures not equal internal energies).
- Conditions are stated where the law is used: no phase change for Q = cmΔT, the container's heat capacity and losses ignored, ΔT the same in K and °C, and the signs of Q and ΔT.
- Figures: c-bars are to scale at 93.5 px per 1000 J/(kg·K); all six bar lengths match the table. In water-sand the rises are drawn to scale (105/20 = 5.25 vs 4190/800 = 5.24). Calorimeter figure numbers = worked example.
- Simulation: Teq, Q and QW implement the lesson's equation. Both curves relax with the same τ, so CwΔTw + CbΔTb = 0 at every instant: energy is conserved during the animation too. The model box states τ is only an illustration. The phase range is kept (body 0–100 °C, water 5–60 °C).
- Experiments: koe-1 locks mW, TW0, mB and TB0 and varies only cB. Its initial "800" is a select option value. koe-2 locks everything but mB. Teq and CB are in simState, and every initial value is inside its slider range.
- Explain model answers (johtopaatos, tarkistus-3) match the theory and call the numbers model values. "Slightly lower in a real calorimeter" holds because the object is the hotter body.
- Sig-fig reasons are correct: 4.5 K in the worked example and 8.0 K in siirto each limit the answer to two figures.
- Scope: within FY3 central contents (aineen lämpeneminen ja jäähtyminen, kalorimetria).
