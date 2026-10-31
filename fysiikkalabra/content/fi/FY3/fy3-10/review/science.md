VERDICT: PASS
CONTENT-HASH: 5e3d91121ea79e92

## Blocking

## Polish
- inquiry.json:507 (check-2 solution): "Jokaisella hetkellä pätee $pV = NkT$". $k$ is not defined anywhere in the lesson, and the sim's pressure fluctuates, so the law holds for the averaged pressure, not at every instant. Fix: derive $p \propto NT/V$ from $pV = nRT$ with $n = N/N_\text{A}$, and drop "jokaisella hetkellä".
- inquiry.json:322 (laske-r Periaate): "harvat todelliset kaasut noudattavat niitä hyvin" reads as "few real gases". Fix: "todelliset kaasut noudattavat niitä hyvin, kun kaasu on harvaa".
- inquiry.json:422 (siirto Järkevyys): "700 kg kevyempää kuin syrjäyttämä ulkoilma" assumes 20 °C outside air, which the task never gives. Fix: add "jos ulkoilma on 20 °C".
- lesson.md:230: the "Siksi" makes $T \propto \langle E_k\rangle$ follow from neglecting interactions, which is not the reason. For the molecular gases used here (N₂, air, CO₂), the energy proportional to $T$ is the kinetic energy of the motion from place to place (guardrail). Fix: drop "Siksi … ja" and say "etenemisliikkeen liike-energiaan".
- lesson-answers.py: it does not compute the worked example, virhe, siirto, check-2 or the exit ticket. I recomputed them myself (all correct), but they belong in the file.

## Checked
- One script recomputed every number from the task data: the weighing masses against $n = pV/(RT)$ with ±0,02 g scatter, every $m/M$, the mean 0,2071 mol, $R$ ≈ 8,3 (8,319 and 8,302), all the mistake values (121,7; 8302; 0,008302; 4,82; 3,32; 70,7; 9870; 2,64; 2,25; 1,69), the worked example 0,2073 mol and 0,83 g, virhe 1,2 → 0,083 mol, siirto 91 200 mol and 2645 kg, check-c2 1,068, check-2 3,0, the exit ticket 0,601 mol, and $V_m$ ≈ 24 l. All agree.
- Sig-fig reasoning in each solution names the datum that really limits it.
- Figures: the speed-arrow ratio 2,7 = √(29/4); the mass bars are 4 : 29 : 44 to scale; the 2T arrows are ≈ √2 longer; 2N has 12 particles; V/2 has 6 particles in half the volume.
- sim.js physics: $p = NkT/A$ in 2D (impulse per unit perimeter), $kT/m = \langle v^2\rangle/2$, Box–Muller thermal speeds, exact rethermalisation on an N change, $v \propto \sqrt{T}$, and V changes at constant speed (stated in the model box).
- Sim in Playwright, 20 s runs: every state including the taulukko rows, exp-2 (600 K → 2,00, N = 50 → 1,00) and check-2 (3,00) matches $(N/100)(T/300)(100/V)$. Noise is 3–5 % SD at N ≥ 50 and −8…+11 % at N = 20, which agrees with the stated "±10 %". The taulukko values are plausible draws.
- exp-1 and exp-2: T and V are locked, only N varies, and hitRate and pMeasured exist in simState.
- Exactly one option is correct in every choice item, and each distractor's feedback names the right mechanism (impulse $mv$ against hit rate in pred-1).
- Ideal-gas limits (high p, low T) are stated in the theory, the R paragraph and the summary. Celsius against kelvin and the Pa·m³ = J argument are correct.
- Scope: the lesson stays inside FY3 (state variables, the ideal gas law, gas laws as special cases).
- The johtopäätös and check-3 model answers agree with the theory and label model values against example data.
