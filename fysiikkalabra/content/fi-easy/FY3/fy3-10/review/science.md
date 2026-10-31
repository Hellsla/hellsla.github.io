VERDICT: PASS
CONTENT-HASH: 1aed3e4e759cc3a2

## Blocking

## Polish
- inquiry.json:62, 71, 75 (pred-n feedback) — "Mittauksissa" presents the simulation's model values as measurements (carried over from round 1) — "Simulaation mittauksissa".
- lesson.md:257–261 — the three "paine kaksinkertaistuu" cases do not say that the other quantities stay the same (carried over; the figure shows it, the text does not) — add "kun muut suureet pysyvät samoina" once.
- inquiry.json:169 (kokeile.calc) — "±10 % at N ≈ 20": my port of the sim gives a relative standard deviation of 4.8 % for 2 s averages at N = 20, so ±10 % is about 2σ. Round 1 saw 0.83–1.17 in Chromium. Either value is defensible — consider "noin ±10–15 %".
- inquiry.json:426 (siirto, Järkevyys) — "noin 700 kg kevyempää kuin syrjäyttämä ulkoilma" assumes the outside air is at 20 °C, which the task does not give — write "jos ulkoilma on 20 °C".

## Checked
- Round-1 blocker fixed: laske-r Periaate now reads "Todelliset kaasut noudattavat niitä hyvin, kun kaasu on harvaa", consistent with lesson.md "Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa". The check-2 Periaate no longer uses an undefined k ("keskimääräiselle paineelle p ∝ NT/V"). The diff since round 1 is only these two strings.
- One script, my own formulas: m/M 0.2075/0.2064/0.2076/0.2068 mol (spread 0.56 %); R from the mean 8.32 and from helium 8.302; mistakes 121.7, 8302, 0.008302, 4.82, 3.32. All agree with lesson-answers.py.
- Worked example: n = 0.2073 mol, m = 0.829 g, molar volume 24.1 l, air 6.01 g. Solved symbolically first, the rounding justified by the 2-digit data.
- virhe 1.22 → 0.0829 mol; siirto 91 200 mol, 2645 kg (mistakes 9869, 2.64; ρ₂₀ = 1.20 kg/m³); check-c2 1.068 (6.8 %); check-2 3.0 (mistakes 2.25, 1.69); exit ticket 0.601 mol; Koe 2 N = 50 (mistakes 70.7, 4.00, 0.50).
- taulukko: pV/(NT) recomputed from the rows (1.05, 1.00, 0.98, 0.98, 0.99). The deviations from the model (≤5 %) fit the simulated scatter (σ ≈ 3 % at N = 100).
- sim.js: the 2D impulse per unit perimeter gives p = NkT/A, and P_REF agrees with kT/m = v_rms²/2. Thermalisation is exact and v ∝ √T. A Python port gives mean/prediction 1.00 at six states. The volume change is isothermal, as the "model" box says. sim.js is unchanged since the round-1 Chromium run.
- Every choice item has exactly one correct option, and each distractor's feedback gives the right mechanism. That includes pred-1 (more frequent but weaker hits for He) and check-1 (hit frequency, not speed).
- Experiments: exp-1 and exp-2 lock T and V and vary only N, and simState has pMeasured and hitRate. The slider ranges and steps allow every value the lesson asks for.
- Figures: the mole-masses bars are 3.5 px/g, to scale. The arrow ratio is 2.67 against √(29/4) = 2.69. The paine-ja-tekijat panels have 6/12/6/6 particles, the 2T arrows are about √2 longer, and the V/2 cylinder is half height.
- Scope: within FY3 "ideaalikaasun tilanyhtälö". The model's limits (high pressure, low temperature) and the conditions on R are stated. The content hash is the same at the start and the end.
