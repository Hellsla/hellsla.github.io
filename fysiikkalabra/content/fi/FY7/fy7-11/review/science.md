VERDICT: PASS
CONTENT-HASH: 5df30b79ce516816

## Blocking

## Polish
- lesson.md:179 (theta-graph aria-label): it says "n = 1,332", but the text and lesson-answers.py use 1,3315. The plotted peak (42,28° at α ≈ 59,4°) fits either value to the nearest pixel. Fix: write 1,3315 in the label.
- lesson.md:84 (Sivukaari): "violetti … noin 54°". The model gives 53,50° for violet and 50,50° for red (lesson-answers.py bow2-v and bow2-p). Fix: write "noin 53,5°" or "noin 53°".
- inquiry.json siirto solution: the reason given for two significant figures ("a difference loses figures") is weak. The data (2,00 m, 60,0°, n to 5 figures) fixes the tan difference 0,01270 to three figures, so 25,4 mm is justified too. Fix: give 25,4 mm, or state why 2 figures is the deliberate choice. The tolerance accepts both, so nothing breaks.
- lesson.md Tiivistelmä, 4th bullet: "alle 42°:n korkeudella" leaves out "tasaisella maalla", which the theory states. Fix: add "tasaisella maalla" so the bullet matches the theory.
- inquiry.json:80: the pending text says "Teoriatiivistelmän", but the stage is now called Teoria. This is wording only, not physics.

## Checked
- One script recomputed every number from the task data with my own formulas and compared it with lesson-answers.py. All agree: speeds in crown glass (198 111 / 196 053 km/s); the worked example (34,88°, 34,47°, Δ 0,41°); rainbow extrema by brute force (red 42,30° at α 59,50°, violet 40,63°; secondary bow 50,5° / 53,5°); θ(90°) = 14,7°; koe-1 differences 0,53 / 0,70 / 0,94 / 1,40 / 4,45°; koe-2 minimum 38,43° at α₁ ≈ 49°, with δ = 40,0° at 40° and 50,3° at 80°; flint 3,92°, water 0,85°; virhe 39,2° and 91,8°; siirto 25,40 mm with mistakes 11,23 mm and 3464 mm; tarkistus-2 1945,9 km/s; exit ticket −8°; pysähdy 12°.
- The sim's Cauchy coefficients give 1,5143 / 1,5302 for crown glass and 1,3315 / 1,3431 for water at 656,3 / 404,7 nm, as the model box claims. They also reproduce the other N-BK7 and F2 table values to within about 10⁻⁴. The sim's Δδ matches the table-based values (4,446° at A = 70°).
- Sim: the incident direction, refraction in vector form, the total-internal-reflection branch, the sign of the deviation (turning towards the base is positive) and the δ readout are right. Koe-1 and koe-2 lock α₁ and aine (or A and aine) and vary only one parameter. simState holds dP, dV and dd, and every colour leaves the prism at every listed setting.
- Derivations are right: α₂ + α₃ = A from the normals meeting at 180° − A; δ = α₁ + α₄ − A; total turn 180° + 2α − 4β, so θ = 4β − 2α.
- n-graph: the six plotted points and the axes match the N-BK7 values exactly.
- Observer and drop figures: violet leaves at the shallower angle; the upper drop's violet passes above the eye and the lower drop's red hits the ground. Both are right.
- Causality is right: the electron response grows towards the UV absorption, frequency and colour are kept at the boundary, Alexander's dark band is explained, and a parallel-sided pane gives no visible spectrum.
- Every choice item has exactly one correct option, and each distractor's feedback is correct. The johtopäätös model answer's critical-angle mechanism is right.
- Scope: refraction and dispersion within FY7 "valon heijastuminen, taittuminen".
