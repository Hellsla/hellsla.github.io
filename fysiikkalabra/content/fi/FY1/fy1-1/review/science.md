VERDICT: PASS
CONTENT-HASH: 58fc8d7de6ebacca

## Blocking

## Polish
- lesson.md:376 (object-types figure, aria-label) — the label says "jokainen askel on kymmenkertainen koko", but the axis ticks are two decades apart (10⁴, 10⁶, 10⁸ …), so each tick step is a factor of 100. The drawing is right; only the description is off. Fix: "jokainen merkitty askel on satakertainen koko", or leave the step out.
- sim-spec.md vs inquiry.json simulaatio.calc — the spec says objects show from about 1/2000 of the view width, and Laskennan selitys says 1/1000. In sim.js an object reaches half opacity at S ≈ 0,48 px (≈ 1/1200 of 560 px), so the student-facing 1/1000 is the better figure. Fix: align the spec.

## Checked
- Changed paragraph lesson.md:198: "alle noin 3 → 10ⁿ, yli noin 3 → 10ⁿ⁺¹" is a fair level-C wording of the log-midpoint (√10 ≈ 3,16) rule. It matches the glossary, check-1's feedback (4,0·10¹⁶ → 10¹⁷), the examples (1,7 m → 10⁰, 8,8·10³ m → 10⁴) and sim.js `kohdeExp = Math.round(log10 m)`.
- Recomputed in one script: the example k = 6,47·10⁴ ≈ 6,5·10⁴ and Δn = 5; exp-1 5; exp-2 8; exp-3 −4 (the hair in the sim has n = −4); siirto d = 12 732 km (40 000, 6 366 and 111 are the right mistakes); check-2 57 917 (inverse 1,73·10⁻⁵); virhe 109 and about 1,3·10⁶ Earths; reflection 42 and 62. lesson-answers.py agrees.
- Magnitudes: proton 1,7 fm, H atom 1,1·10⁻¹⁰ m, nucleus/atom 10⁴–10⁵, stadium/pea 4·10⁴, nucleus >99,9 % of the mass (H 99,95 %), Sgr A* horizon 2·2GM/c² = 2,5·10¹⁰ m at 4,3·10⁶ M☉, heliopause 120 AU = 1,8·10¹³ m, observable universe 93 Gly = 8,8·10²⁶ m, Milky Way 10⁵ ly = 9,5·10²⁰ m, Coulomb/gravity for two protons 1,2·10³⁶.
- The scale-axis and object-types figures are to scale as they say (measured against the tick spacing to within 0,05 decade). The cosmic-address and matter-ladder values are right, and both figures are marked "ei mittakaavassa".
- The sim OBJ table agrees with the lesson and the glossary. Initial states L = −9, 7,7 and 27,5 give the nearest objects the intros name (water, Earth, universe). The calc example of 62 px is right. Orbits use the radius for n and the diameter for drawing, as Mallin oletukset says.
- Each choice item (kertaus, pred-1, pred-2, exp-2, menetelmat, tunnista, vuorovaikutukset, virhe, check-1, check-c2) has exactly one correct option, and the distractor feedback is right.
- The four interactions, the residual strong force, β⁻ decay, the role of the weak force in the Sun, neutron star and black hole facts, and the observable versus whole universe are all right and inside the teacher's qualitative scope.
- The exit ticket and the check-3 model answer (31 orders of magnitude) agree with the theory.
- The hash was the same at the start and at the end.
