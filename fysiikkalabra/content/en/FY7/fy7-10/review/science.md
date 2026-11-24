VERDICT: FAIL
CONTENT-HASH: 51d65af69607e8c4

## Blocking
- inquiry.json:445 (tarkistus-3), B: the prompt says the glass is looked at "from the side, obliquely from above". The model answer and criteria 1 and 4 then require refraction at the water surface. That only holds when the eye looks through the water surface, as lesson.md:59 says. Looked at from the side, the light leaves through the glass wall, which is the mechanism the pencil photo caption gives (lesson.md:69). So a student who explains the effect with the caption's mechanism fails two criteria, and the lesson gives two mechanisms for one task without saying which view each belongs to. Fix: make the prompt say "looked at obliquely from above through the water surface", the same condition as lesson.md:59. Leave the model answer as it is.

## Polish
- lessons/FY7/fy7-10/lesson-answers.py:54: the comment says 0,674. The computed value is 0,671, which matches the 0.671 in the mistake data.
- lesson.md, "Towards the normal": "the greater the difference between the refractive indices, the more the ray is refracted" fits the level (C). "The greater the ratio n₂ : n₁" would be more exact.
- lesson.md, Partial reflection: "about 4 % from each surface of the glass" is correct for normal incidence (4.3 %). The sentence already says "perpendicular".

## Checked
- My own numpy script recomputed every number. All agree to the stated precision: worked example (sin α₂ = 0.6159, α₂ = 38.0°, v = 2.26·10⁸ m/s), the speed in diamond, the glass at 40° (25.0°), predictions (28.9°; 22.1° → 40.6°, factor 1.84), maxima 48.8° and 24.4°, experiment 2 (35.2, 30.9, 30.3, 18.5°; n₂ sin α₂ = 0.766), angle ratios 1.36 and 1.48, virhe (0.651, 40.6°), siirto (25.9°, 41.7°; mistakes 22.08 and 39.9), tarkistus-2 (1.470; mistakes 0.680 and 1.59), exit ticket (25°, 50°, 1.33).
- mittaus: an independent least-squares fit gives A = 1.4895, B = −0.0041 and ΔA = 0.0162. The graph reading (0.60; 0.89), the per-row ratios 1.42 and 1.49, and the mistakes 0.671 and 1.79 are right. The half-cylinder reasoning (no refraction along a radius) is correct.
- Sim: Snell's law, β = α₁, the TIR condition, and Fresnel R averaged over s and p (the sign of r_p is irrelevant once squared) are right. R at 0° (2.0 %) matches the text. Unpolarised R rises monotonically with angle for all the material pairs, so the claim "a greater angle reflects more" holds. The model box states the limits (flat, non-absorbing, 589 nm, computed values).
- koe-1 and koe-2 hold the right parameters constant and vary only the intended one. simState gives beta, alpha2, sin1, sin2 and n2. At α₁ = 0 the sim gives sin2 = 0 with no error.
- Figures, from figures.py and the screenshots: interface 50° → 35.2°; wavefronts with λ₂ = λ₁/1.33 and fronts matched at the surface; the depth image point is from back-extended rays; the graph curves end at 48.8° and 24.4°; the fit points match the data.
- Each choice item has exactly one correct option, and every distractor's feedback states the physics correctly. The explanation of refraction is the wavefront mechanism with the frequency fixed by the source. The formula section is named after its law.
- Scope: reflection and refraction are in FY7. Brewster and TIR are only pointed to in later chapters.
- Hash at the start and at the end: 51d65af69607e8c4.
