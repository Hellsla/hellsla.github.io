VERDICT: PASS
CONTENT-HASH: 58fc8d7de6ebacca

## Blocking

## Polish
- lesson.md:376 (object-types aria-label) — the label says "jokainen askel on kymmenkertainen koko", but the ticks are two decades apart (10⁴, 10⁶, 10⁸ …), so each step is a factor of 100. The drawing is right. Fix: "satakertainen", or leave the step out.
- sim-spec.md vs inquiry.json simulaatio.calc — the spec says objects show from 1/2000 of the view width, and calc says 1/1000. In sim.js an object reaches half opacity at about 1/1200, so calc's figure is the better one. Fix: align the spec.

## Checked
- Changed lesson.md:198: "alle/yli noin 3" is a fair level-C wording of the √10 ≈ 3,16 boundary. It matches the glossary, check-1 (4,0·10¹⁶ → 10¹⁷), the examples (1,7 m → 10⁰, 8,8·10³ m → 10⁴) and sim.js `kohdeExp = Math.round(log10 m)`.
- Recomputed in one script: example k = 6,5·10⁴ and Δn = 5; exp-1 5; exp-2 8; exp-3 −4 (the hair in the sim has n = −4); siirto 12 732 km (mistakes 40 000, 6 366, 111); check-2 57 917; virhe 109; reflection 42 and 62. lesson-answers.py agrees.
- Magnitudes: proton 1,7 fm, nucleus/atom 10⁴–10⁵, stadium/pea 4·10⁴, nucleus over 99,9 % of the mass, Sgr A* horizon 2,5·10¹⁰ m, heliopause 120 AU, 93 Gly = 8,8·10²⁶ m, Coulomb/gravity 1,2·10³⁶.
- The scale-axis and object-types figures are to scale, to within 0,05 decade. The not-to-scale figures carry the right values.
- The sim's OBJ table agrees with the lesson. The initial states L = −9, 7,7 and 27,5 give the objects the intros name. The calc's 62 px is right. Orbits use the radius for n, as Mallin oletukset says.
- Every choice item has exactly one correct option, and the distractor feedback is right.
- The interactions, β⁻ decay, the neutron star and black hole facts and the observable universe are right and inside the qualitative scope. The exit ticket and check-3 agree with the theory.
- The hash was the same at the start and at the end.
