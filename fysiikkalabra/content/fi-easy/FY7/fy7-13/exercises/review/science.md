VERDICT: PASS
CONTENT-HASH: 1bd412beb5abc8e6

## Blocking

## Polish
- solutions.md:155 (L2-05): "sama mittausvirhe $x_k$:ssa" should be "sama lukeman epävarmuus".
- solutions.md:78 (L2-03): "Ero johtuu mittausepävarmuudesta" should be "Ero johtuu mittausvirheistä ja on mittausepävarmuuden rajoissa".
- solutions.md:123 and exercises.json:66 (L1-06): "mitä lähempänä raon leveys on aallonpituutta" suggests that a slit narrower than λ spreads light less (C at this level). "mitä kapeampi rako on" is safer.
- lessons/FY7/fy7-13/answers.py:60: the comment says 629,6 nm, but the line computes 629,84 nm.

## Checked
- Round 2: the round-1 blocking item is fixed. solutions.md:170 (L2-07) now says "ja suhteellinen epävarmuus kasvaa", in line with the stem, the correct option and the rest of the answer. `git diff HEAD~1` shows no other change to exercises.json, solutions.md or answers.py.
- I reran my one recomputation script on the current exercises.json and answers.py. All 21 numeric answers agree: d = 1 mm/N, d sin θ = kλ, tan θ = x/L, the k < d/λ count, and least squares through the origin.
- L2-05 (red laser): slope 0,06337 gives 633,7 nm, and single points give 625–638 nm. tan is taken before sin, and the through-origin fit is justified.
- L2-07: Δλ/λ = cos²θ · Δx/x falls as x grows, so the correct option holds. Exactly one option is correct, and the distractor feedback is right.
- L3-04 (6,3·10² nm): the table fits I = cos²(πx/5,0 mm) within ±0,02. Two significant figures are justified by x₁ = 5,0 mm. In b) 10,0 mm is right, and so is the grating comparison in c).
- L2-08: the factor is 1,53, so only "noin 1,5" is correct. Each distractor's feedback names its mistake.
- L3-05 (DVD): mean d = 0,7374 µm. Second order would need sin θ = 1,44, which is impossible, and the zero order goes back through the hole.
- L3-01 overlap (3·400 < 2·700 nm), L3-02 CD 1,60 µm, L3-03 532,6 nm, L1-09 MAFY He 587,56 nm gives 20,64°.
- Figures are to scale: setup-q puts k = 2 at 69,98 cm, and spectrum-q's edges are at 17,77 and 10,05 cm. Neither gives N or λ away.
- Scope (grating, diffraction, reflection grating) and the laser safety sentences are in place.
