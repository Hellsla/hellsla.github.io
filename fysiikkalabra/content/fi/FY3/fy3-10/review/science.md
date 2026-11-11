VERDICT: PASS
CONTENT-HASH: 42bda478c0fafe59

## Blocking

## Polish
- lesson.md:230: "Siksi ... kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan" ties T ∝ E_k to the negligible interaction energy. For air the guardrail wording is translational energy. Fix: drop "Siksi" and write "etenemisliikkeen keskimääräiseen liike-energiaan".
- lesson.md:489: "aina yhtä monta moolia". Add "(ideaalikaasu)" or "tavallisissa oloissa".
- inquiry.json:272 (taulukko, 100/600/50): the sim gives 3,99–4,04 there (six 2 s averages in Playwright), so 3,91 lies outside its real scatter. Use about 3,98.
- inquiry.json:102 (punnitus, Järkevyys): "5,00 · 0,041" has no unit. Write 5,00 l / 24,1 l/mol ≈ 0,21 mol.

## Checked
- One Python recomputation (all match): example 0,2073 mol, 0,83 g, air 6,0 g, 24,1 l/mol. m/M 0,2075 / 0,2064 / 0,2076 / 0,2068 mol, R 8,32 and 8,302 with its mistakes. virhe 1,2 → 0,083 mol. siirto 2645 kg, mistakes 9870 / 2,64. check-c2 1,068. check-2 3,0, mistakes 2,25 / 1,69. Exit ticket 0,601 mol. Taulukko pV/(NT) column. Koe 2: N = 50, mistakes 71 / 25 / 200.
- Round 2 (e9228a0e, only the exp-2 tolerance 0,02 → 0,1): the accepted range is 45–55. It holds 50 and keeps every listed mistake out.
- sim.js: the impulse 2|v⊥| summed over the walls and divided by the perimeter is the 2D pressure, with P_REF = NkT/A. ⟨vx²⟩ = ⟨vy²⟩ = kT/m is exact, v ∝ √T, and a V change is isothermal, as the model box states.
- Playwright run of the sim at the taulukko, exp and check-2 states: pMeasured matches (N/100)(T/300)(100/V) to within about 3 %. At N = 20 the scatter is about ±10 %, as the calc box says.
- exp-1 and exp-2 vary only N, with T and V locked. The measured keys are in simState, and the initial values can be set on the sliders.
- Every choice item has exactly one correct option, and the distractor feedback is right.
- Figures: the bars are 4 : 29 : 44 and the arrow ratio is √(29/4) ≈ 2,7, both to scale.
- Scope is within FY3. The kinetic picture stays qualitative.
- Conditions stated: absolute pressure, kelvins, the model's limits, R for a dilute gas.
- Model answers agree with the theory. The sim's values are called model values and the weighing data example values.
