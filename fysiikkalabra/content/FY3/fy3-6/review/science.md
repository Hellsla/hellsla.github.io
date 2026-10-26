VERDICT: PASS
CONTENT-HASH: 37088270afb1e8f6

## Blocking

## Polish
- sim.js:886 — the animated sim has no speed control (hidas · normaali · nopea), which CLAUDE.md form rule 3 asks for. This is not a physics fault, because the 1,5 s time constant is labelled as illustration — fix: add the three-way speed control, or leave it if illustration-only timing is accepted.
- lesson.md:146 — "Kappale, jonka lämpökapasiteetti on suuri, lämpenee ja jäähtyy hitaasti" holds only for the same heat flow — fix: add "samalla lämmönsiirtonopeudella" or "saman lämpömäärän vaikutuksesta" (the depth paragraph at line 106 already sets the right tone).
- exercises.json fy3-6-L3-03 — the stored answer 3,3 m³ is 0,8 % above the computed 3,27 m³. This is inside the tolerance and is a correct two-figure rounding, so nothing needs to change.

## Checked
- I recomputed all 12 exercise answers from the task data with my own formulas. Each is within 0,9 % of the stored value, and answers.py matches line by line (the c values come from the lesson's table, and ΔT read in °C is the same as in K).
- The worked example is right: Q_v = 5656,5 J, c_m = 374,6 J/(kg·K), and a reading of 24,6 °C gives 383 J/(kg·K). A 0,200 kg copper body in a lossless calorimeter gives 24,6 °C, which matches the sim's default reset state. The unknown is solved symbolically before the numbers go in.
- Misconception section: T = 35 °C by both routes. Iron against water is about 9,3×, so "lähes kymmenkertainen" is fair.
- Predictions in inquiry.json:
  - ennuste-1: sand gives 26,8 °C and 8,5 kJ; hot water gives 44,0 °C and 30,2 kJ; heat capacities 160 and 838 J/K.
  - ennuste-2: 40,0 / 55,0 / 63,1 °C.
  - In both, the correct options and every feedback's numbers are right.
- virhe: the wrong algebra gives 6,6 °C, and the Kelvin version also gives 6,6 °C, so the first option's feedback is correct. The correct result is 30,0 °C.
- siirto 29,1 kg; its mistakes 220 and 21,3 are exactly the errors described. tarkistus-2 gives 891, with mistakes 768 and 501; tarkistus-1 compares 4500 J/K with 838 J/K. The exit ticket gives 419 kJ, about 9×, and 65 °C.
- Experiments:
  - koe-1 changes only cB, and koe-2 changes only mB (0,50 kg falls in the slider's 0,05–1,00 range and gives the average).
  - Every initial value fits the slider limits and steps. The simState carries Teq and CB.
  - The screenshot shows the koe-1 initial state applied: 26,8 °C, 160 J/K, 8,52 kJ.
- sim.js physics:
  - The Teq formula is correct. Q and QW are equal, and the sign is handled when the body is colder than the water.
  - Both temperatures relax with the same τ, so energy is conserved at every moment of the animation (this is also the true two-body behaviour). The illustrative timing and the assumptions (insulation, no phase change) are stated in `model`.
- Figure 1: the rise bars are 105 px against 20 px, a ratio of 5,25 (c ratio 5,24). Figure 2: the bar lengths are to scale at 0,0933 px per J/(kg·K).
- Scope: Q = cmΔT, C = cm, calorimetry and the balance equation all fall within the FY3 content "aineen lämpeneminen ja jäähtyminen" and "lämpömäärä". The c values in the table are realistic.
- The content hash was 37088270afb1e8f6 at both start and end.
