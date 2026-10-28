VERDICT: PASS
CONTENT-HASH: a5fd473fe9aaac0d

## Blocking

## Polish
- lesson.md:258 — "sulaminen vie kaksi kolmasosaa veden luovuttamasta lämmöstä (16,7 kJ lämmöstä 25,1 kJ)" and, two sentences later, "vesi luovuttaa yhteensä ≈ 18,8 kJ": the same paragraph says the water gives off two different amounts — write "veden 0 °C:seen jäähtyessä luovutettavissa olevasta lämmöstä $Q_\text{v}$".
- lesson.md:274 (Tiivistelmä) — the m_s formula is given for every Q_v < Q_j, but the theory (line 264) states it only when the water can warm the ice to 0 °C; add "kun vesi riittää lämmittämään jään 0 °C:seen" (B-type, minor: a negative m_s would mean freezing, and the next sentence names that case).
- inquiry.json:337 (tarkistus-1) — "Eristetyssä astiassa … Astiaan siirtyy lämpöä" reads as a contradiction; say how the heat enters (e.g. a heater) or drop "Eristetyssä".
- lesson.md:113 — aria-label uses decimal points (25.1, 2.1, 33.4, 35.5 kJ); Finnish text uses commas.

## Checked
- Recomputed in one script: figure 1 (24,7 g ice left, 0,375 kg water), bar chart (25,1 / 2,1 / 33,4 / 35,5 kJ, bar heights to scale), T(T_v) graph (kink 26,57 °C, 40,1 °C at 80 °C), worked example (25 140 J, 17 540 J, 6,05 → 6,0 °C, balance 18,8 = 18,8 kJ), misconception 15 °C / 24,7 g.
- Inquiry numbers: ennuste-1/-2 feedback (75,3 g, 5,9 / 18,5 / 12,6 g, 4,2 kJ, 31,4 kJ, 81,5 g), koe-1 26,6 °C and slider bracket 26,5–27,0 °C, johtopäätös 62,4 g and 10,1 °C, virhe −25,6 °C and 0,075 kg, siirto 39,9 g with mistakes 43,9 g and 437,5 g, tarkistus-2 40,06 °C with mistakes 56 and 35, exit ticket 66,8 kJ and 12,5 g.
- Exactly one correct option in kertaus, ennuste-1, ennuste-2, virhe, tarkistus-1; every distractor's feedback right.
- Boundary cases follow the guardrail: ≥ for "all melts", exactly 0 °C at equality, ice left at 0 °C, partial and total freezing kept (theory, summary, sim boxes, feedback).
- Melting described with the guardrail wording (vuorovaikutusenergia); "normaalipaineessa" stated in the summary.
- Experiments isolate the varied parameter (koe-1 TW0, koe-2 TI0, others locked); simState gives Tf and iceLeftG.
- sim.js: all four cases of solve() and the end states of stateAt() agree with the energy balance (case-4 T and Qend verified symbolically); chart scales cover the slider ranges (max 209 kJ < 250 kJ); pace stated as illustration only.
- Scope inside FY3 (Q = cmΔT, Q = sm, energy conservation).
