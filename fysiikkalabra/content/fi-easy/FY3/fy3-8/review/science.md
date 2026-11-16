VERDICT: PASS
CONTENT-HASH: 55d454ed07d07adc

## Blocking
None.

## Polish
- content/fi-easy/FY3/fy3-8/lesson.md:308 — "Vesi kutistuu 0 °C:n ja 4 °C:n välillä" does not say in which direction the temperature changes — write "Vesi kutistuu lämmetessään 0 °C:sta 4 °C:seen" as at line 261.
- content/fi-easy/FY3/fy3-8/inquiry.json:144 — "Kuvaajan ohuet suorat ovat muiden aineiden suorat. Jyrkin on alumiini" is wrong when aluminium itself is the chosen material, because it is then the thick line — "Jyrkin suora on alumiinin".
- content/fi-easy/FY3/fy3-8/lesson.md:259 and inquiry.json `olomuodot` — for a gas at constant pressure the reason is that the pressure stays the same, so V ∝ T (γ ≈ 1/T); it is not mainly the weak interactions. The level-appropriate wording "lähes vapaita" is fine (C).

## Checked
- I recomputed every number in one script with my own formulas, and all agree. Worked example: Δl = αl₀ΔT = 12·10⁻⁶·120·60 = 86,4 mm, given as 86 mm with 2 significant figures (α and ΔT limit it). αΔT = 0,072 %, and the 60 mm estimate holds.
- Predictions: 6,00 and 12,0 mm and 0,0600 % are right. In each prediction exactly one option is correct, and every distractor's feedback is right.
- Volume table: 0,36 / 2,1 / 11 / 34 cm³ are right, and air γ = 3,4·10⁻³ ≈ 1/293 K.
- Etsi virhe: 27,9 mm vs 1,84 mm (about 15×, 0,7 %) are right.
- Siirto: h = γV₀ΔT/A = 44 mm. The mistakes 0,044 and 110 are right, glass γ ≈ 40× smaller (42,9 mm with it), and the solution is symbolic first.
- check-2: α = 23·10⁻⁶ 1/K from both columns, and the mistakes 46 and 15,3 are right. check-3: air/steel γ ≈ 94 ("noin sata"). Exit ticket: 21 mm.
- Model and conditions: the anharmonic mechanism (repulsion close up, attraction weakening further out) is stated in the theory, pred-3, the conclusion and check-3. Particles do not grow. The linear formula holds for about 100 K or less, and liquids' γ only near 20 °C (guardrail).
- sim.js: ΔL = αL₀(T − 20 °C), rel = αΔT, ×100 exaggeration labelled. Vibration amplitude ∝ √T. The real change is at most 0,23 % (under 0,3 %, as stated). The Mallin oletukset box says honestly that the spacing is set from the formula and that the asymmetry is not shown.
- Experiments: exp-1 locks material and L₀, varies T, and simState has dT and dL. exp-2 locks material and T, varies L₀, and has dL and rel.
