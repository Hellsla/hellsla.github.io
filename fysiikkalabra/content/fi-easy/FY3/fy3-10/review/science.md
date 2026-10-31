VERDICT: FAIL
CONTENT-HASH: 8eeb15b65d9bab34

## Blocking
- inquiry.json:326 (laske-r, solution, Periaate). Class B (the condition is stated so that it reads as a false claim). "Harvat todelliset kaasut noudattavat niitä hyvin" reads first as "few real gases obey them well". That contradicts the lesson ("Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa"), and in fi-easy the reading "few" is the likely one. Fix: "Todelliset kaasut noudattavat niitä hyvin, kun kaasu on harvaa eli paine ei ole suuri eikä lämpötila matala."

## Polish
- inquiry.json:511 (check-2, solution, Periaate). "Joka hetkellä pätee $pV = NkT$" uses $k$, a symbol the lesson never defines. Also, the simulation's pressure only follows the law as an average. Fix: "Tilanyhtälön mukaan $p \propto NT/V$ (hiukkasmäärä $N \propto n$)."
- inquiry.json:62, 75 (pred-n feedback). "Mittauksissa" presents the simulation's numbers as measurements. Fix: "Simulaation mittauksissa".
- inquiry.json:169 (kokeile.calc). The text says that at $N \approx 20$ the variation is "noin ±10 %". In my runs of the sim, ten successive 2 s averages at N = 20 ranged from 0.83 to 1.17 times the model value. Fix: "noin ±15 %".
- lesson.md:257–261. The three "paine kaksinkertaistuu" cases do not say "kun muut suureet pysyvät samoina". Add that clause once.

## Checked
- Recomputed with my own formulas in one script: m/M for all four gases (0.2075 / 0.2064 / 0.2076 / 0.2068 mol, spread 0.56 %), R from the mean (8.32) and from helium (8.302), and the three unit mistakes (121.7, 8302, 0.008302). These agree with lesson-answers.py.
- Worked example: n = 0.2073 mol, m = 0.829 g, molar volume 24.0 l, air 6.0 g. The answer is solved symbolically first, the rounding is justified by the 2-digit data, and the reasonableness check is a real one.
- virhe (1.2 → 0.083 mol), siirto (91 200 mol, 2645 kg; mistakes 9870 and 2.64; ρ(20 °C) = 1.20 kg/m³, 2640 kg), check-c2 (1.068, about 7 %), check-2 (3.0; mistakes 2.25 and 1.69), exit ticket (0.601 mol), Koe 2 (N = 50; mistakes 71, 4.00 and 0.50).
- In every choice item exactly one option is correct, and each distractor's feedback gives the correct reason. The pred-1 helium feedback (more hits, each with less impulse, since mv ∝ √m) is correct.
- sim.js: 2D impulse per unit perimeter gives p = NkT/A, P_REF agrees with kT/m = v_rms²/2, the thermalisation is exact, and V changes keep the gas isothermal as the "model" box states. Run in Chromium: mean/prediction is about 1.00 at every state tried.
- The taulukko model values reproduce as 1.05, 0.98 and 5.11 (rows 2–3 vary within the ±2 % scatter). exp-1 and exp-2 lock T and V, vary only N, and simState has pMeasured and hitRate.
- Figures: the mole-masses bars are 3.5 px/g, so to scale. The helium/air arrow ratio is 2.7 (√(29/4) = 2.69). The paine-ja-tekijat panels show 6/12/6/6 particles, a half-height cylinder for V/2, and 2T arrows longer by about √2.
- Scope: everything is inside FY3 "kaasujen tilanmuutokset ja ideaalikaasun tilanyhtälö". The model's limits (high pressure, low temperature) are stated.
- The content hash is the same at the start and the end.
