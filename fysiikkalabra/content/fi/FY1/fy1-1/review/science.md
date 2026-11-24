VERDICT: PASS
CONTENT-HASH: 8c2027f14e94df82

## Blocking

## Polish
- inquiry.json:117 (simulaatio `calc`) — says an object shows from about 1/1000 of the view width; the code (`fadeIn` a ≥ 0,5 at S ≈ 0,48 px) gives about 1/1200, and sim-spec.md:1 says 1/2000 — use one figure in both, e.g. "noin $\dfrac{1}{1000}$" in both.
- assets/sims/fy1/fy1-1/sim.js:189 — `kohdeExp` rounds the orbit's radius (`logM`), while "kooltaan lähin" picks by the drawn diameter (`logExt`); for the heliosphere this gives n = 13 for a 3,6·10¹³ m circle. The model box says so and no experiment uses it; consider noting "rata: säde" in the readout.
- lesson.md:207 — Sgr A* "noin neljä miljoonaa" vs the sim's model box "noin 4,3 miljoonaa"; the same value in both reads better (2,5·10¹⁰ m fits 4,3·10⁶ M☉).
- inquiry.json pred-1 correct feedback — "viisi suuruusluokkaa" followed by "kymmeniätuhansia kertoja" is right (6,5·10⁴) but could say why five orders gives tens of thousands, not exactly 10⁵.

## Checked
- One script recomputed every lesson-answers.py number with my own formulas: Δn = 5, 8, midpoint −4, k = 6,47·10⁴, Earth d = 12 732 km (C 40 000, r 6366, 111 km/°), 5,79·10⁴ and its inverse. All agree, and so do the mistake values.
- The sim's nearest object and `kohdeExp` at the experiments' initial L: −9 → water (n −10), 7,7 → Earth (7), 27,5 → universe (27); hair n = −4 at the exp-3 midpoint; H atom −10, proton −15, Neptune radius 13, Milky Way 21.
- Figure positions on the to-scale axes (scale-axis 11,8 px per decade; object-types 26 px per decade): every marker is within 0,1 decade of its stated size.
- Magnitudes: Sgr A* d = 4GM/c² ≈ 2,5·10¹⁰ m; proton–proton Coulomb/gravity ≈ 1,2·10³⁶; 4 ly ≈ 3,8·10¹⁶ m; 93 Gly ≈ 8,8·10²⁶ m; stadium/pea 4·10⁴; Sun/Earth 109 and about 1,3·10⁶ in volume.
- The OBJ table sizes (nuclei by 1,2 fm·A^⅓, atoms, Oort cloud 10⁵ AU, heliopause 120 AU, LMC, Andromeda, Local Group, Laniakea) are plausible rounded values; the model box states rounding, the orbit radius and the illustrative drawings.
- The order-of-magnitude rule (about 3) is the same in the glossary, the theory, the pysähdy box, check-1 and pred-2's distractor feedback.
- The four interactions and their mechanisms are correct: residual strong force, β⁻ by the weak force, the weak force in the Sun's fusion, neutral bulk matter for gravity's dominance. The exit ticket matches the theory.
- Exactly one correct option in each choice, and every distractor's feedback is correct (tunnista: the black-hole mass limit, Jupiter about 10⁻³ M☉, the 26 000 ly distance to the galactic centre).
- Worked example: symbolic first, two significant figures justified, a real reasonableness check.
- In scope for FY1: qualitative structure and interactions, no cosmology equations; Eratosthenes geometry only.
