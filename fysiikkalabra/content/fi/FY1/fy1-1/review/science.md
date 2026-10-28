VERDICT: FAIL
CONTENT-HASH: ca26f894b74a6477

## Blocking
- lang/fi.json:739 (sims.fy1-1 "o_proxima"; shown by assets/sims/fy1/fy1-1/sim.js:796 and readout line 936) — A: the object of size {,}0\cdot10^{16}\,\text{m}$ is named just "Proxima Centauri", so the readout says "Kooltaan lähin kohde: Proxima Centauri, koko {,}0\cdot10^{16}\,\text{m}$". That is the distance to the star, not its size (the star is about \cdot10^{8}\,\text{m}$ across). The siblings already say what is measured ("heliopaussin etäisyys", "Oort-pilven säde"), and the lesson itself says "Proxima Centaurin etäisyys" (check-1) and "Lähin tähti" (menetelmat). Fix: rename it "etäisyys Proxima Centauriin" (or "Proxima Centaurin etäisyys").

## Polish
- assets/sims/fy1/fy1-1/sim.js:790-795 — the orbit objects (1 AU, Saturnus, Neptunus, heliopaussi, Oort) are drawn at their diameter but labelled with their radius. Mallin oletukset says so, but a student comparing the Sun with 1 AU by eye gets a factor of 2 wrong. Still open from the last round.
- lessons/FY1/fy1-1/sim-spec.md:1 and the sim.js header — say objects show from about 1/2000 of the view. Laskennan selitys says 1/1000, and the code (a ≥ 0,5) gives about 1/1200. Use "noin 1/1000" in all three.
- lesson.md:46 — "nykyiset teoriat eivät enää toimi" is an expectation, not a tested fact. "teorioiden odotetaan lakkaavan toimimasta" is safer.

## Checked
- The changes since the last pass (the definition of suuruusluokka "kymmenpotenssien akselilla lähinnä" in Ydinajatus, Tiivistelmä and check-1) are correct: on a log axis the halfway point is √10 ≈ 3,16, and that matches the "a about 3" rule and kohdeExp = round(log₁₀ d).
- Recomputed in one script: example  = 6{,}47\cdot10^{4}$, Δn = 5; exp-1 5 (mistake 65 000); exp-3 −4 (31, 4,4·10²⁶); siirto 12 732 km (40 000, 6366, 111); check-2 {,}79\cdot10^{4}$ (inverse {,}73\cdot10^{-5}$); Sun:Earth 109 (about 1,3·10⁶ Earths); e/g ratio for two protons 1,2·10³⁶; Sgr A* horizon diameter {,}5\cdot10^{10}\,\text{m}$ for 4,3·10⁶ M☉.
- The experiments' start states give the stated nearest objects (water at L = −9, Earth at 7,7, universe at 27,5). The rows are −10/−15/−18, then 7/9/13/21, then hair −4.
- All 43 sim sizes are realistic. Neptune's orbit gives 10¹³ m whether you take its radius or its diameter. Milky Way 10²¹ m, observable universe 8,8·10²⁶ m = 93 Gly.
- Physics is right: β-decay and the weak interaction in the Sun, the residual strong force, the two kinds of Solar System edge (heliopause 120 AU, Oort cloud 2000–100 000 AU), neutron star 20–25 km at more than 1 M☉, black holes from stars at 3 M☉ or more, "not sucking everything in", and the observable universe being bigger than 2·13,8 Gly because of expansion.
- Assessment: exactly one correct option in every choice item (pred-1/2, exp-2, menetelmat, tunnista, vuorovaikutukset, virhe, check-1), and every distractor's feedback is right.
- Scope: qualitative structure and interactions only, as the brief of 2026-10-28 asks; no cosmology equations.
- Hash identical at start and end.
