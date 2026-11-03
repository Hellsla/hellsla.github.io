VERDICT: FAIL
CONTENT-HASH: 7ab0f27db0946968

## Blocking
- inquiry.json:109 (simulaatio.model) — A: "painovoima ... on mallin kentissä vähintään noin kymmenen miljardia kertaa pienempi" holds for the proton only. The alpha particle (q = 2e, m = 6,645·10⁻²⁷ kg) in the weakest field (100 V over 10 cm = 1000 V/m) has 2eE : (m g) = 4,9·10⁹, about five billion. lesson-answers.py checks only the proton (`sim-weight-ratio-min`). — fix: write "vähintään noin viisi miljardia kertaa pienempi" or "miljardeja kertoja pienempi", and add the alpha case to lesson-answers.py.

## Polish
- lessons/FY6/fy6-12/lesson-answers.py:5 — the docstring says gravity is "about 10^-12 of the electric force"; it is about 2·10⁻¹¹ in 5000 V/m, and at least 10⁻¹⁰ in the sim. — fix: correct the comment.
- lessons/FY6/fy6-12/lesson-answers.py:54 — the "retrieval" block computes E = 5000 V/m with wrong options 50 and 8 V/m. The real kertaus item is a qualitative force question, so this block is stale. — fix: drop it or match it to the item.
- inquiry.json:305 (siirto.solution, Järkevyys) — "samalla energialla paljon hitaampi kuin esimerkin revontulielektroni": the example electron has 3,0 keV and the ion 1,2 keV, so they do not have the same energy. — fix: "vaikka energiat ovat samaa suuruusluokkaa".

## Checked
- Every number in the lesson, inquiry and exit ticket recomputed in one script: example 4,806·10⁻¹⁶ J and 3,248·10⁷ m/s (0,108 c); 5 keV electron 4,19·10⁴ km/s ("noin 40 000"); 500 eV proton 309 km/s, electron 13 262 km/s, ratio 42,9; ion 42,0 km/s and its three mistakes; tarkistus-2 300 eV; virhe −4,8·10⁻¹⁷ J.
- Electron at 1000 V reaches 0,0625 c, so "alle 7 %" and classical E_k are fine. Proton weight ratio in the figure's field is 4,9·10¹⁰ ("kymmeniä miljardeja").
- Signs: E_p = qV with q = −e, the field points from higher to lower potential, and both charges start toward lower E_p. Consistent throughout.
- Predictions: exactly one correct option each; every distractor feedback is right. The koe-1 and koe-2 setups isolate d and the particle, and simState gives E, tns, EkeV, EpeV and vkms.
- sim.js integrates F = |q|U/d with an exact arrival step and never uses |q|U, so the energy result emerges. E_p and E_k are consistent with xneg.
- Figures: the tasapotentiaali and vx-graph numbers (50 V/cm, 5000 V/m) match. Field lines are green, equipotentials dashed grey and forces red.
- Aurora physics (acceleration over thousands of km, green light from oxygen) is right.
