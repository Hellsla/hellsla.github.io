VERDICT: PASS
CONTENT-HASH: cd9b243866124293

## Blocking
None.

## Polish
- content/fi-easy/FY3/fy3-8/lesson.md (Yleinen virhekäsitys) — "Vesi kutistuu 0 °C:n ja 4 °C:n välillä" still does not say the direction — "Vesi kutistuu lämmetessään 0 °C:sta 4 °C:seen", as in the theory.
- content/fi-easy/FY3/fy3-8/inquiry.json `simulaatio.howto` — "Kuvaajan ohuet suorat ovat muiden aineiden suorat. Jyrkin on alumiini" is wrong when aluminium is the chosen (thick) line — "Jyrkin suora on alumiinin".
- content/fi-easy/FY3/fy3-8/lesson.md (Eri aineiden lämpölaajeneminen) and inquiry.json `olomuodot` — the gas's large expansion at constant pressure comes from p staying constant (V ∝ T, γ ≈ 1/T), not mainly from weak interactions; "lähes vapaita" is a fair level simplification (C).
- content/fi-easy/FY3/fy3-8/inquiry.json `johtopaatos.model` — "Δl = 6,0 mm" next to "12,0 mm" and the predictions' 6,00 mm: write 6,00 mm.
- content/fi-easy/FY3/fy3-8/lesson.md particles figure — each particle vibrates symmetrically about a shifted equilibrium. Closest approach is 58 → 54 px and farthest 82 → 126 px, so the figure does show the asymmetry the text describes. This is a fair simplification (C) and is noted only for awareness.

## Checked
- One script recomputes every number with my own formulas, and all agree. Worked example: Δl = αl₀ΔT = 86,4 mm. The new Tulos rounds it up to "vähintään 87 mm" with the reason given (safe-side rule). αΔT = 0,072 %, and the estimate of 60 mm holds.
- Predictions: 6,00 and 12,0 mm and 0,0600 % are right. Each has exactly one correct option, and every distractor's feedback is right. In pred-3, Bea is right and Cem's feedback names the missing asymmetry correctly.
- Volume table: 0,36 / 2,1 / 11 / 34 cm³ are right. Air γ = 3,4·10⁻³ 1/K ≈ 1/293 K.
- Etsi virhe: 27,9 mm vs 1,84 mm, a factor of about 15 and 0,70 %, are right.
- Siirto: h = γV₀ΔT/A = 44 mm. The mistakes 0,044 and 110 are right. Glass γ is about 40× smaller, giving 42,9 mm with glass. The solution is symbolic first.
- check-2: α = 23·10⁻⁶ 1/K from both columns, and the mistakes 46 and 15,3 are right. check-3: air/steel γ ≈ 94 ("noin sata"). Exit ticket: 21 mm.
- Changed particles figure: neighbours are in opposite phase, with d₀ = 70 px and d = 90 px. It is labelled as exaggerated, the particles keep the same size, and the still shows the equilibrium positions. It agrees with the anharmonic explanation in the theory, pred-3, the conclusion and check-3.
- Conditions: the linear formula is limited to about 100 K or less, and liquids' γ is used only near 20 °C (guardrail). Gas is said to be at constant pressure.
- sim.js: ΔL = αL₀(T − 20 °C), rel = αΔT, with the ×100 exaggeration labelled and amplitude ∝ √T. The maximum is 0,23 % (under 0,3 %, as stated). The Mallin oletukset box says the spacing comes from the formula and that the asymmetry is not shown.
- Experiments: exp-1 locks material and L₀, varies T, and simState has dT and dL. exp-2 locks material and T, varies L₀, and simState has dL and rel.
