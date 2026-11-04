VERDICT: PASS
CONTENT-HASH: 9b7783e5537063cc

## Blocking

## Polish

## Checked
- One script recomputed all 12 answers from the task text with my own formulas. All agree with exercises.json and answers.py to within 3·10⁻⁵ relative: 1,3636; 1,2397; 38; 34,733; 58,750; 36,602; 2,0019; 34,667 ps; 1,5321; 60,0; 52,940; 34,249.
- Round-1 polish done. L3-03 now shows 34,249° before answering 34,2°. L3-01 says "samaan periaatteeseen perustuvat" (a bicycle reflector is a corner cube), and the task restricts the ray to the plane of the normals.
- L1-05 (40,0°) and L3-02 (36,87°) go from water to air below the critical angle of 48,75°, so a refracted ray exists, and the solutions check sin α₂ < 1.
- L2-01 converts the 25,0° measured from the surface to 65,0° from the normal. The quoted wrong result of 16,1° is right.
- L2-03: Δt = (n − 1)d : c is derived symbolically, cm → m is right, and the answer has two significant figures (35 ps). The check of ≈67 ps in air against ≈100 ps in glass is right.
- L2-04 figure (figures.py): α₁ = 50° in the air quadrant and α₂ = 30° in the glass quadrant are drawn from the normal and can be read on the 10° ticks between the labelled 40/60 and 20/40. The half-cylinder geometry (no refraction at the curved surface) is stated. The alt text does not give the angles away.
- L3-03: sin α₁ : v₁ = sin α₂ : v₂ follows from n = c : v and is derived symbolically. The independent check with n = 1,33 and 1,52 gives the same 0,563.
- Every solution has all seven steps and solves for the unknown before substituting. Rounding follows the limiting datum. The units (blank, °, · 10⁸ m/s, ps) and the tolerances fit. The materials and indices match the lesson's table.
