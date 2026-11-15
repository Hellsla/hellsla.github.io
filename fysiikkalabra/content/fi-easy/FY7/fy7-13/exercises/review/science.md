VERDICT: FAIL
CONTENT-HASH: 9b434954715398f2

## Blocking
- solutions.md:170 (L2-07 Mallivastaus) — **A, definition (guardrail "Keep the terms apart").** The stem, the correct option and this answer's first sentences all speak of *suhteellinen epävarmuus*. The sentence on moving the screen then ends "…on suurempi osa, ja virhe kasvaa". The signed, unknown error does not grow; the relative uncertainty does. This task is the set's lesson on that distinction. — Write "…ja suhteellinen epävarmuus kasvaa."

## Polish
- solutions.md:155 (L2-05) — "sama mittausvirhe $x_k$:ssa" → "sama lukeman epävarmuus".
- solutions.md:78 (L2-03) — "Ero johtuu mittausepävarmuudesta" → "Ero johtuu mittausvirheistä ja on mittausepävarmuuden rajoissa".
- solutions.md:123, exercises.json:66 (L1-06) — "mitä lähempänä raon leveys on aallonpituutta" suggests a slit narrower than λ spreads light less (C at this level). "mitä kapeampi rako on" is safer.
- lessons/FY7/fy7-13/answers.py:60 — the comment says 629,6 nm, but the line computes 629,84 nm.

## Checked
- One script recomputed all 21 numeric answers with my own formulas: d = 1 mm/N, d sin θ = kλ, tan θ = x/L, the k < d/λ count, and least squares through the origin. All agree with answers.py and exercises.json.
- L2-05 (punainen laser): slope 0,06337 gives 633,7 nm; single points give 625–638 nm; tan is taken before sin; the through-origin fit is justified.
- L2-07: Δλ/λ = cos²θ · Δx/x falls as x grows, so the correct option holds. There is exactly one correct option, and the distractors' feedback is right.
- L3-04 (6,3·10² nm): the table fits I = cos²(πx/5,0 mm) within ±0,02. The two figures are justified by x₁ = 5,0 mm. b) gives 10,0 mm, and the grating comparison in c) is right.
- L2-08: the distance goes from 13,03 to 19,88 cm, a factor of 1,53. Only "noin 1,5" is correct, and each distractor's feedback names its mistake.
- L3-05 (DVD): d = 0,7389–0,7363 µm, mean 0,7374. Second order would need sin θ = 1,44, so it does not occur; the zero order goes back through the hole.
- L3-01 overlap (3·400 < 2·700 nm), L3-02 CD 1,60 µm, L3-03 532,6 nm, L1-09 MAFY He 587,56 nm → 20,64°.
- Figures to scale: setup-q puts k = 2 at 69,98 cm, and spectrum-q's edges are at 17,77 and 10,05 cm. Neither gives N or λ away.
- Scope (grating, diffraction, reflection grating) and the laser safety sentences are in place.
