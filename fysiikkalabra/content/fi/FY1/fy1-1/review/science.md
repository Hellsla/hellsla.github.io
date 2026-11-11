VERDICT: PASS
CONTENT-HASH: c82a3b21eb6adbee
Mode: full, round 1 (reason: sim.js changed; the diff is label layout only, no change to the model, OBJ data or simState)

## Blocking

## Polish
- inquiry.json:117 (`calc`) — the threshold "noin 1/1000–3 kertaa näkymän leveys" does not match the code exactly: an object counts as visible from about 1/1200 of the view (fadeIn reaches 0,5 at about 0,47 px). sim-spec.md also gives 1/2000. — Use one value (for example "noin 1/1000") in both texts.
- lesson.md:270 — Sgr A* is "noin neljä miljoonaa Auringon massaa" here and "noin 4,3 miljoonaa" in the sim's Mallin oletukset. The two agree as rounded values; writing 4,3 in both would remove the gap. (The horizon diameter 2,5·10¹⁰ m follows from 4,3·10⁶ M☉; with 4,0·10⁶ M☉ it would be 2,4·10¹⁰ m.)

## Checked
- Recomputed in one script against lesson-answers.py: all 12 numbers agree. These are the example k = 6,47·10⁴ and Δn = 5, exp-1 5, exp-2 8, exp-3 −4, the Eratosthenes task d = 12 732 km (C 40 000, r 6366, 1° = 111 km), and check-2 5,79·10⁴ and its inverse.
- Simulation (recomputed mainObj and kohdeExp = round(log₁₀ m)): initial states L = −9 / 7,7 / 27,5 give water / Earth / universe as stated in the intros. Each jump target is the nearest object at its own jump: atom −10, proton −15, quark −18, Sun 9, Neptune 13, Milky Way 21, Planck −35 (clamped at L = −34), hair −4. So exp-1, exp-2 and exp-3 answer as their solutions say. Rounding log₁₀ matches the √10 rule in the lesson.
- OBJ sizes checked against reference values (nuclei, atoms, water, RBC, Everest, Moon, Jupiter, Sun, 120 AU = 1,8·10¹³ m, Oort 10⁵ AU, Proxima 4,0·10¹⁶ m, Orion, LMC, MW, Andromeda, Local Group, Virgo, Laniakea, 93 Gly = 8,8·10²⁶ m).
- Sgr A* horizon diameter 2,54·10¹⁰ m; neutron star 1,4 M☉, 20–25 km; Coulomb/gravity for two protons 1,2·10³⁶. All correct.
- Figures: the scale-axis and object-types positions are to scale (11,8 and 26 px per decade, every point within 0,1 decade). The ladder and matter figures are marked "ei mittakaavassa". The stadium/pea ratio of 4·10⁴ fits "kymmeniätuhansia". In the force arrows, gravity points toward the Sun and the EM pair is attractive.
- The four interactions are right: β⁻ is weak, the residual strong force binds the nucleus, and the weak force takes part in the Sun's energy production. The text explains why gravity dominates at large scales (charge neutrality). It stays within the FY1 scope note: qualitative, no QM or cosmology equations.
- Predictions: exactly one correct option in each, and every distractor's feedback is right (pred-2 "neljä" ≈ Neptune–Proxima, 10¹³ → 10¹⁷).
- tunnista, vuorovaikutukset, virhe, menetelmat, exp-2 question, check-1 (4,0·10¹⁶ → 10¹⁷, log 16,60), check-c2: one correct option in each, and the feedback physics is right.
- Model answer of check-3 (31 decades) and the exit ticket (residual strong force, short range) agree with the theory.
- Simulation limits are stated: the Mallin oletukset box covers rounded values, nucleus drawn too large, orbits labelled with their radius but drawn as diameter, Planck grid symbolic, horizon not a solid sphere.
