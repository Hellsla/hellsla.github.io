VERDICT: PASS
CONTENT-HASH: 036ee53fbe5f7239
Mode: full. Round 1 (English set after the extension labels and the added tasks L1-10, L1-11, L2-08)

## Blocking

## Polish
- solutions.md:168 — L1-09 says the middle polariser "turns the polarisation direction". That can suggest a lossless rotation, which L3-04 (c) explicitly rules out. — Say "lets through the component along its own axis, so the light after it is polarised along that axis".
- solutions.md:255 — L2-08 calls "43–46°" a good answer. 46° is 4.1 % above 44.2° and outside the 3 % tolerance, so the page marks it "close", not right. — Write "43–45°".
- solutions.md:234 — L1-10 calls "260–280 W/m²" a good answer. 280 is 4.3 % above 268.4, outside the 4 % tolerance. — Write "260–279" or widen the tolerance slightly.
- exercises.json:58 — In the L1-06 distractor feedback, "Light reflected from a surface is polarised along the surface" drops the "partially" that the correct option and the solution keep. — Add "partially".
- exercises.json — Only L2-04…L2-08 and L3-05 carry "Extension task." Most other Malus and Brewster tasks (L1-02…L1-05, L1-07, L1-08, L1-10, L1-11, L2-01…L2-03, L3-01…L3-04) are unlabelled. The Finnish set labels the same six, and the core path (L1-01, L1-06) stays qualitative, so this is not blocking. If the label is meant to mark every quantitative polarisation task, extend it there.

## Checked
- One script recomputed all 22 numeric answers with my own formulas (halving, Malus, Brewster, a least-squares fit on L2-05 and L2-08, the maximum of (1/8)sin²2θ). All 22 agree with exercises.json and answers.py within 0.03 %.
- L1-09 ordering: D 100 < E 125 < A 150 < B 200 < C 240 W/m². Correct, and the model answer's distractor reasoning is correct.
- Brewster direction: n₂ is the medium the light refracts into (L2-07, L3-02). L3-02's angle of 36.9° is below the 48.8° critical angle, as the solution states.
- L2-07: the student's 36.3° is both the refraction angle and the ethanol→air Brewster angle (both 36.33°).
- L3-05: the Sun's height is 36.9°, θ = 65°, 7.14 W/m². The tilt at which the two lenses break even is 33.2°. The comparison for unpolarised light (50 % against 30 %) is right.
- L3-04: the model gives 0/30/90/120/90/30/0 W/m² and the example data scatter ±6 W/m² around it. Plausible.
- L2-05 fit: slope 313.9 lx, intercept 6.9 lx (the background). L2-08 fit: 360.7 lx and 14.6 lx, matching the figure's line (15 to 375 lx).
- L1-11: crown glass n = 1.520. Plausible, but I did not check it against the MAFY table.
- Scope: Malus and Brewster are extension, and the core path is qualitative, as in the scope notes.
- The exercise brief in the packet was empty, so notation was judged against the glossary.
