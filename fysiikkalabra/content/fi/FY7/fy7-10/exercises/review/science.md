VERDICT: PASS
CONTENT-HASH: 6bf94060b87b3ff4

## Blocking

## Polish
- exercises/solutions.md:118 (L3-03) — it shows "α₂ = 34,25°" and then answers 34,2°, which looks like a rounding slip (the exact value is 34,249°). Show 34,249° or 34,2°.
- exercises/solutions.md (L3-01 Järkevyys) — "palaa tulosuuntaansa vastakkaiseen suuntaan" holds in the plane of the normals, which the task states. A bicycle reflector uses three mirrors (a corner cube); "periaatteeseen perustuvat" would be safer.

## Checked
- One script recomputed all 12 answers from the task text and all agree: 1,3636; 1,2397; 38; 34,733; 58,7495; 36,6022; 2,0019; 34,667 ps; 1,5321; 60,0; 52,9395; 34,2494.
- L1-05 and L3-02 (water → air) are below the critical angle of 48,8°, so a refracted ray exists, and the solutions say so.
- L2-01 converts the angle from the surface to 65,0° from the normal. L1-03 and L3-01 handle the normal geometry correctly.
- L2-03 Δt = (n − 1)d : c, derived symbolically. The cm → m conversion and the 2 significant figures are correct.
- L2-04 figure (figures.py): α₁ = 50° and α₂ = 30° can be read off the ticks every 10°. The numbers are measured from the normal in the right quadrants. The alt text does not give the answer away. The half-cylinder geometry is stated correctly (no refraction at the curved surface).
- L3-03 sin α₁ : v₁ = sin α₂ : v₂ follows from n = c : v and is derived symbolically. The check with n = 1,33 and 1,52 is an independent check.
- Every solution has all the steps and solves for the unknown before substituting. Rounding follows the limiting datum. Units are "", "°", "· 10⁸ m/s", "ps". The materials and indices match the lesson's table.
