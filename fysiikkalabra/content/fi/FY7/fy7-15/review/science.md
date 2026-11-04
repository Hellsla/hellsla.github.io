VERDICT: FAIL
CONTENT-HASH: ce684c7f1daaa50d

## Blocking
- content/fi/FY7/fy7-15/lesson.md:594 (Yleinen virhekäsitys) — A: "Kolmas virhe on kuvitella, että polarisaattori vain poistaa valoa eikä voi lisätä sitä." The statement called a misconception is true: a polariser only absorbs, it never adds light. What the three-sheet case refutes is the idea that *adding a sheet between crossed polarisers* can only reduce the transmitted light. As written it contradicts the theory ("absorboi") and ennuste-kolme's feedback. — Fix: "Kolmas virhe on kuvitella, että lisäkalvo voi vain vähentää läpi tulevaa valoa. Kun ristiin asetettujen …", and keep the rest of the paragraph.

## Polish
- Scope: LOPS asks for "valon polarisaatio kvalitatiivisesti", and the scope note names Brewster's law only. Malus's law with numeric tasks (koe-1, Etsi virhe, tarkistus-2, the worked example) goes beyond that. The glossary carries Malusin laki, so this is the teacher's call, not a finding.
- inquiry.json ennuste-kolme, distractor "lisäkalvo voi vain absorboida lisää valoa": its feedback is right. It could add that the sheet absorbs but changes the polarisation direction.

## Checked
- One script recomputed every number and all agree: Malus points, the worked example 282 W/m², koe-1 37,5 % and its mistakes, the ennuste values, koe-2 12,5 %, virhe 25 W/m², siirto 2,128 m and its mistakes, tarkistus-2 2,066 mW and its mistakes, Brewster 53,1°/56,3°/36,9°, the exit ticket.
- mittaus fit recomputed by least squares: A = 360,72 lx, B = 14,64 lx, ΔA = 2,37 lx, residuals within ±3 lx. These match the given 360,7 / 14,6 / 2,4.
- Brewster figure geometry: incidence 53,0°, refraction 36,9° and the right-angle mark agree with "kulmat mittakaavassa". The graph's marked points are correct.
- Brewster derivation, its conditions (n₁ = the medium of incidence and reflection, angle from the normal) and the s-polarised reflected light (pinnan suuntainen, ⊥ tulotaso) are correct.
- Mechanisms are correct: absorption by the film's chains, the ½ for unpolarised light, intensity ∝ amplitude², sunglasses, LCD and 3D.
- sim.js implements I₁ = 50 %, then Malus stage by stage; d and cos² are given for two sheets. simState exposes i1, i2, i3 for koe-1 (n = 2, θ₁ locked) and koe-2 (n = 3, θ₁ and θ₃ locked). The limits are stated in `model`.
- Each prediction and check has exactly one correct option, and every distractor's feedback is right. The explain model answers and their criteria match the theory.
