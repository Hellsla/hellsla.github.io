VERDICT: PASS
CONTENT-HASH: 1f1a6b1c38646d0c

## Blocking

## Polish
- sim.js:945,994 — when the T-axis span is 70 °C (e.g. 20–90 °C, step 20) the top value `hi` gets neither a grid line nor a label, so the axis ends unlabelled — choose a step that divides `hi − lo`, or always label `hi`.
- exercises.json fy3-6-L2-02 — uses power P = E/t (P t = Q) (not in FY3's listed contents) — say in the solution that P is energy per second.

## Checked
- One script recomputed all 12 exercise answers. My values, answers.py and exercises.json agree within 0.8 % (tolerance 2 %). The solutions.md reasoning and sanity ratios are right, and each solution solves symbolically first.
- Worked example: 5656,5 J; c = 374,6 → 3,7·10² J/(kg·K); 24,6 °C gives 383; a lossless copper body gives 24,6 °C (the sim default reproduces it); C values 1257 and 75 J/K.
- Formulas: Q = cmΔT and its sign convention, C = cm, the balance equation and its rearrangement to a weighted mean. All are within FY3 scope.
- Misconception section: 35 °C; water/iron ratio 9,3 ("lähes kymmenkertainen"). Exit ticket: 419 kJ, about 9×, 50 °C and 65 °C.
- Figures: fig 1 thermometer rises 20 px vs 105 px = 5,25 (4190/800 = 5,24), so "mittakaavassa" holds. Fig 2 bar lengths 391,1·c/4190 all match. Material c values are realistic.
- Ennuste 1: sand 26,8 °C / 8,5 kJ, water 44,0 °C / 30,2 kJ, C 160 and 838 J/K. Ennuste 2: 40,0, 55,0 and 63,1 °C. The correct options and all feedback numbers are right.
- Virhe: 6,6 °C (wrong) and 30,0 °C (right). The kelvin-shift argument is right. Siirto: 29,1 kg, and the mistakes 220 and 21,3 kg match their stated errors. Tarkistus-1: 4500 vs 838 J/K, 50×. Tarkistus-2: 891, and the mistakes 768 and 501 match their stated errors.
- Experiments: koe-1 varies only cB and koe-2 varies only mB, with all other inputs locked. The measured keys Teq and CB are in simState. Initial values are inside the slider ranges.
- sim.js implements the lesson's model (weighted mean, Q_body = Q_water, readout 5,80 kJ = 5,80 kJ at the defaults). The exponential approach is declared illustrative in the code and in "model", and the 0–100 °C / no phase change limit is stated. `test_sims.py fy3-6` passes now (47 assertions).
- Hash unchanged start to end.
