VERDICT: PASS
CONTENT-HASH: fab3dbae3a3ca3ca

## Blocking

## Polish
- lessons/FY7/fy7-10/lesson-answers.py:54: the comment still says 0,674. The computed value is 0,671, which matches the mistake value 0.671 in inquiry.json. Correct the comment.
- lesson.md, "Towards the normal or away from it": "the greater the difference between the refractive indices, the more the ray is refracted" is fine at this level (C). "The greater the ratio n₂ : n₁" would be more exact.

## Checked
- Round 1 blocking item is fixed. tarkistus-3 now says "looked at obliquely from above through the surface of the water". That matches lesson.md "Apparent depth", the model answer and criteria 1 and 4.
- My own script recomputed every number. All agree with the text and with lesson-answers.py: worked example (0.6159, 38.0°, 2.26·10⁸ m/s), diamond 1.24·10⁸ m/s, glass at 40° → 25.0°, predictions (28.9°; 22.1° → 40.6°, factor 1.84), graph limits 48.8° and 24.4°, koe-2 (35.2, 30.9, 30.3, 18.5°), angle ratios 1.36 and 1.48, virhe (0.651, 40.6°), siirto (25.9°, 41.7°; the mistakes 22.08 and 39.9 lie outside the 2 % tolerance), oil (1.470; 0.680 and 1.59), exit ticket (25°, 50°, 1.33).
- mittaus: an independent least-squares fit gives A = 1.4895, B = −0.0041 and ΔA = 0.0162. The reciprocal 0.671, the angle ratio 1.79, the row ratios 1.42 and 1.49 and the graph reading (0.60; 0.89) are right. The half-cylinder geometry is stated correctly. The fit figure matches the data.
- nopeus 2.01 (mistake c·n = 4.47) is right.
- Sim code: Snell's law, β = α₁, the TIR condition and unpolarised Fresnel R are correct. R is 2.0 % at 0°, 2.4 % at 40° and 35 % at 80°, as the text and the readout say. The model box states the limits (589 nm, flat boundary, no absorption, values computed by the model). The 1280 px capture shows 40° → 28.9° and R = 2.4 %.
- koe-1 holds m1 and m2 constant and varies alpha. koe-2 holds m1 and alpha constant and varies m2. simState provides beta, alpha2, sin1, sin2 and n2.
- Each choice item has exactly one correct option, and every distractor's feedback states the physics correctly. Refraction is explained by the wavefronts and the change of speed, with the frequency set by the source.
- Partial reflection values are right (4.3 % for glass and 2.0 % for water at normal incidence). The exceptions (TIR and Brewster) are only pointed to in later chapters, so the lesson stays within FY7 scope.
- The formula section is named after its law, and the formulas carry their MAFY names.
- Hash at the start and at the end: fab3dbae3a3ca3ca.
