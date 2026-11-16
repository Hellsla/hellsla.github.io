VERDICT: PASS
CONTENT-HASH: a2e76a1a16d904ec

## Blocking

## Polish
- content/fi/FY3/fy3-10/inquiry.json:151 — pred-1, feedback on the "heliumpallossa" option: "Punnitus näyttää, että lopputulos on sama paine samalla hiukkasmäärällä" says the weighing measured pressure. The pressure was set equal; the weighing showed the same n at equal p, V, T — rephrase, e.g. "Punnitus näyttää, että samassa paineessa hiukkasia on yhtä monta."
- content/fi/FY3/fy3-10/lesson.md:231 — "keskimääräiseen liike-energiaan": the guardrail wording is the kinetic energy of motion from place to place (etenemisliike). Air is diatomic, and its rotation also carries kinetic energy. This is a C-level simplification; "keskimääräiseen etenemisliikkeen liike-energiaan" would fit the guardrail word for word.

## Checked
- All lesson and inquiry numbers recomputed in one script with my own formulas: m/M of the four gases (0,2075/0,2064/0,2076/0,2068 mol, spread < 1 %), R = 8,32 from the mean and 8,302 from helium, laske-r mistakes 121,7/8302/0,008302, the worked example (n = 0,2073 mol, m = 0,829 g, air 6,01 g), virhe (1,2 → 0,083 mol), siirto 2645 kg and its mistakes 9869 kg and 2,64 kg, check-c2 1,068, check-2 3,0 with mistakes 2,25 and 1,69, exp-2 N = 50 with mistakes 200 → 4,00 and 25 → 0,50, exit ticket 0,601 mol. All agree; lesson-answers.py uses the same model.
- The "Mikä pysyy samana?" table: pV/(NT) is 1,05/1,00/0,98/0,98/0,99 against my NT/V. Every state can be set on the sliders' steps.
- sim.js: 2D point particles that hit only the walls; the impulse per perimeter equals NkT/A on every wall; v ∝ √T; thermalize gives exactly ⟨vx²⟩ = ⟨vy²⟩ = kT/m. The volume change is isothermal, and the model box says so. pMeasured and hitRate are in simState; the adapter exposes N, T and V.
- exp-1 and exp-2 lock T and V and vary only N; the initial states match the questions.
- Figures: helium-ilma arrow ratio 32 : 12 = 2,67 ≈ √(29/4); mole-masses bars 14 : 101,5 : 154 = 4 : 29 : 44; paine-ja-tekijat has 2N = 12 particles, arrows ×1,41 at 2T and half the height at V/2.
- Every prediction and check has exactly one correct option, and each distractor's feedback names the right mechanism (hit rate × impulse, kelvin scale, no mutual collisions).
- The model's limits are stated: point particles, high pressure / low temperature, R valid "kun paine ei ole kovin suuri". The combined gas law is said to need a fixed amount of gas.
- Scope: within FY3 (state equation, separate gas laws, particle-level pressure simulation).
