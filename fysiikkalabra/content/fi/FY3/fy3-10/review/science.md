VERDICT: PASS
CONTENT-HASH: 42bda478c0fafe59

## Blocking

## Polish
- lesson.md:230: "Siksi ... kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan". The "Siksi" makes T ∝ E_k sound like a result of the negligible interaction energy, and for air (diatomic) only the translational energy matches the guardrail wording. Fix: drop "Siksi" from that clause and write "etenemisliikkeen keskimääräiseen liike-energiaan".
- lesson.md:489 (Tiivistelmä): "on aina yhtä monta moolia kaasua". The next bullet states the model's limits, so this is C, but "(ideaalikaasu)" or "tavallisissa oloissa" would close the gap.
- inquiry.json:272 (taulukko, row 100/600/50): 3,91 is 2–2,5 % below what the sim gives in that state. Six 2 s averages in Playwright gave 3,99–4,04, so 3,91 is outside the scatter the sim really shows. A value near 3,98 (column ≈ 0,99–1,00) would be more representative. The other rows match the sim's ranges.
- inquiry.json:102 (punnitus solution, Järkevyys): "5,00 · 0,041" has no unit (mol/l) and leans on the result being checked. Better: 5,00 l / 24,1 l/mol ≈ 0,21 mol.

## Checked
- One Python recomputation of every number with my own formulas (all match): worked example n = 0,2073 mol, m = 0,83 g, air 6,0 g, V_m = 24,1 l/mol. m/M for the four gases: 0,2075 / 0,2064 / 0,2076 / 0,2068 mol. R from the mean = 8,32 ≈ 8,3. laske-r 8,302, with its mistakes 121,7 / 8302 / 0,008302. virhe 1,2 → 0,083 mol. siirto 91 200 mol, 2645 kg, with mistakes 9870 / 2,64, and the buoyancy check (3360 → 2639 kg) holds. check-c2 1,068. check-2 3,0, with mistakes 2,25 / 1,69. exit ticket 0,601 mol. Taulukko pV/(NT) column right. Koe 2: N = 50, with mistakes 71 / 25 (p = 0,50) / 200 (p = 4,00).
- Round-2 change (commit e9228a0e, only exp-2 tolerance 0,02 → 0,1): the accepted range is 45–55. It holds the right answer, keeps all three listed mistakes outside, and suits a noisy reading. On the slider (step 10) only 50 falls inside it.
- sim.js physics: the impulse 2|v⊥| summed over the walls and divided by the perimeter is the 2D pressure. P_REF = NkT/A. Thermalize makes ⟨vx²⟩ = ⟨vy²⟩ = kT/m exact. T is set by rescaling speeds by √T, so v_rms ∝ √T. Changing V moves only positions, which is isothermal, and the Mallin oletukset box says so.
- Sim in Playwright at the taulukko, exp-1, exp-2 and check-2 states: pMeasured agrees with (N/100)(T/300)(100/V) to within about 3 %. At N = 20 the scatter is about ±10 %, as the calc box states. hitRate ∝ N√T/V.
- exp-1 and exp-2 lock T and V and vary only N. simState gives pMeasured and hitRate, and all the initial values can be set on the sliders.
- Every choice item (kertaus, pred-n, punnitus-vertailu, pred-1, taulukko, virhe, check-1, check-c2) has exactly one correct option, and each distractor's feedback gives the right reason.
- Figures: the bar lengths 14 / 101,5 / 154 match 4 : 29 : 44. The helium/air arrow ratio is about 2,7 = √(29/4). The labels of the 2N / 2T / V/2 figure are right.
- Scope: within FY3's "kaasujen tilanmuutokset ja ideaalikaasun tilanyhtälö". The kinetic picture stays qualitative, with no FY4 mechanics.
- Model conditions are stated: absolute pressure, kelvins, failure at high pressure and low temperature, and R valid for a dilute gas.
- The johtopaatos and check-3 model answers agree with the theory. The sim's numbers are called model values and the weighing data invented example values.
