VERDICT: FAIL
CONTENT-HASH: 04842bd55c702318

## Blocking
- lesson.md:326 (Tiivistelmä, first bullet) — "Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$" leaves out the condition the guardrails require wherever the law is used. The summary is a closed box that students read on its own, and the next chapter is about changes of state. **B, Minor.** — Fix: add "kun olomuoto ei muutu" (the Kaava section, line 164, already says it).

## Polish
- lesson.md:177 — "Eristetyssä astiassa energia säilyy, kun astian omaa lämpökapasiteettia ei oteta huomioon" makes energy conservation sound conditional. The condition only decides that the two bodies exchange heat with each other alone. Use the worked example's wording instead ("Energia säilyy. Kun astia ja ilma eivät ota lämpöä, …"). Minor.
- lesson.md:175 — "Kappale, jonka lämpökapasiteetti on suuri, lämpenee ja jäähtyy hitaasti" holds only at the same heating power. Add "samalla lämpöteholla". C/B borderline, Minor.
- inquiry.json:275 — the `siirto` answer is 29.1, but its solution's Vastaus says $29\,\text{kg}$ to two significant figures (correctly, because $8{,}0\,\text{K}$ has two). The tolerance accepts both. Make the stored answer 29 for consistency. Minor.
- inquiry.json:379 — the criterion "noin viisinkertainen hiekkaan tai maahan verrattuna" asks for a ratio for "maa" that the task does not give. Soil's $c$ varies with its moisture. Write "moninkertainen" or "hiekkaan verrattuna". Minor.

## Checked
- One script recomputed every number from the task data: worked example (5656,5 J; 374,6 → 3,7·10² J/(kg·K); 383 at 24,6 °C; Cu → 24,6 °C; 1257 and 75 J/K), misconception (35 °C, iron ×9,3), ennuste-1 (26,8 / 44,0 °C, 30 / 8,5 kJ), ennuste-2 (40,0 / 55,0 / 63,1 °C), virhe (6,6 → 30,0 °C, the kelvin shift gives 6,6 again), siirto (29,09; mistakes 220 and 21,3), checks (4500 / 838 J/K; 35 and 65 °C; 890,6; mistakes 768 and 501; 134 J/K), exit ticket (419 kJ, ×9). All agree.
- Significant figures: each answer is limited by the right datum (4,5 K; 8,0 K; 11,0 K; 2,0 kg).
- Exactly one correct option in each choice item. Every distractor's feedback is correct.
- Experiments: koe-1 varies only cB, koe-2 only mB. The initial values are valid select/slider values, and simState gives Teq and CB.
- sim.js implements the weighted-mean equilibrium. Because both temperatures relax with the same τ, energy is conserved at every instant (checked numerically). The model box states its limits: insulated vessel, no phase change, τ for illustration only.
- Figures: the c-bars are to scale (≤0,4 px). The water-sand ΔT ratio is 5,25 against 5,24 from the c values. The calorimeter figure's numbers match the example and say "ei mittakaavassa".
- Causality: the sand–water explanation names c and also the thin heated surface layer. The kettle caption is right (condensed droplets).
- Kertaus and the guardrails: heat is energy in transfer, ΔU = Q when no work is done, no "lämmöksi".
- Scope: within the FY3 central content "aineen lämpeneminen ja jäähtyminen". Calorimetric measurement is covered.
- There is no lesson-answers.py in lessons/FY3/fy3-6/. Its numbers were checked here instead.

## Scores
- 1 Physics and mathematical correctness: **3**. Every number, figure and the sim are right; one unstated condition (B) in the summary.
- 6 Experimental reasoning, physics part: **4**. Model values are labelled and assumptions stated, real losses are discussed in the right direction and controlled variables are isolated. No uncertainty is quantified beyond the ±0,1 K sensitivity in the example.
