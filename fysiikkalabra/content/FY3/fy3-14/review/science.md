VERDICT: FAIL
CONTENT-HASH: e97cf2119c84570f

## Blocking
- exit-ticket.json:4,12 — the calculations in the model answers are plain text ("Q = sm = 334 kJ/kg · 0,20 kg = 66,8 kJ", "Q = cmΔT = 4190 J/(kg·K) · …"). This breaks the teacher's standing rule that calculations in solutions are LaTeX. The page's KaTeX auto-render covers the exit ticket. — Write each calculation as `$Q = sm = 334\,\tfrac{\text{kJ}}{\text{kg}} \cdot 0{,}20\,\text{kg} = 66{,}8\,\text{kJ}$`, and the same for item 3.

## Polish
- inquiry.json:157 — koe-1 asks for the temperature "jolla jäätä ei ole enää jäljellä mutta T ei ylitä 0 °C". The slider step is 0,5 °C, so no slider value meets that: 26,5 °C leaves 0,3 g of ice and 27,0 °C gives 0,3 °C. The 26,6 °C answer is still accepted, but the prompt should say "rajaa liukusäätimellä ja laske tarkka arvo".
- lesson.md:180 — Q_j goes from the formula straight to "840 J + 16 700 J" with no substitution line with units. Add `2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}050\,\text{kg} \cdot 8{,}0\,\text{K} + 334\,000\,\tfrac{\text{J}}{\text{kg}} \cdot 0{,}050\,\text{kg}`.
- sim.js:139 — in case 1 after all the ice has melted, "vesi" shows the original water's temperature (for example 30,2 °C with 60 °C water) while the melt water sits apart at 4,6 °C. A stirred thermometer would already read T_f = 23,8 °C. Name the label "alkuperäinen vesi", or show the mixed temperature once the ice is gone.
- sim.js (case 4) — after all the water freezes, the four cubes still float on top of a solid ice block. Hiding the cubes would read better.

## Checked
- All 12 answers recomputed in one script. They equal answers.py, and every json answer is within tolerance. L3-02 and L3-03 take the right branch.
- Every inquiry, exit-ticket and lesson number matches its value: 24,7 g, 75,3 g, 26,6 °C, 12,6 g, −26 °C, 39,9/43,9/438 g, 40/56 °C, 6,05 °C, about 19 °C, 12,5 g.
- All five round-1 fixes are in. The 6,05 °C unit is right, "below the midpoint" is true, the all-water-freezes exception is in the misconception and the summary, figure 2 shows "−10 °C" in LaTeX, and the howto's pale-segment sentence is fixed.
- I ran the sim in Chromium (real clicks, sim on screen) for cases 1–4 and the worked example. The end states equal my solver: 23,8 °C; 24,7 g; 498,1 g; −3,5 °C; 6,05 °C. At the end q/Q_end = 1.
- I checked each of about 490 frames per run. No liquid water was ever below 0 °C, and no ice above 0 °C. q, T_w and T_i are monotonic. Mass is conserved. The ice mass changes only while the side changing phase is at 0 °C.
- The sim's Q_end in each branch satisfies the energy balance. The axis (≤ 209 kJ) fits within 0–250 kJ.
- The "nopea" speed changes only the pace, and the end state is the same.
- Figures 1–3 have their numbers to scale (26,6 °C break, 40,1 °C at 80 °C, bar heights). All labels are LaTeX, and they are print-clean.
- Formulas, their conditions and the four cases are correct and within FY3 scope. koe-1 and koe-2 lock everything except their varied parameter.
- No lesson ids appear in student text. Only the template's exercise aria-labels contain them.
