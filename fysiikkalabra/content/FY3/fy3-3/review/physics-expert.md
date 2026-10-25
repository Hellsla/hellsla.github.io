VERDICT: PASS
CONTENT-HASH: 9c6ecf76a631b766

Reviewer: physics-expert. Lesson fy3-3. Hash checked before and after the review: identical (9c6ecf76a631b766).
Scope check against MAOL FY3 (lines 309-345 of the guide): system and state variables, T/p/V linkage ("jos yhtä muutetaan, vähintään toinen muista muuttuu myös"), micro model, absolute zero by extrapolation. No ideal gas law, no E_k formula, no first law in the lesson. In scope.

No FAIL-level errors found. Findings below are minor (all non-blocking).

1. sim.js:52-53 — the pressure readout is systematically 4-11 % above the "teoria" value, because particles bounce at distance R=4 px from the walls (effective box (W-2R)×(h-2R)) while pMeas and pRef divide by the nominal W and BOX.h. My replica of the model gives about 104 at 300 K / 1,0 dm³ (theory 100), 211 at 0,5 dm³ (theory 200), 51 at 2,0 dm³ (theory 50), 207 at 600 K (200). Header comment (sim.js:5-6, "p is proportional to T/V") holds, with this offset. The reference state "100" therefore reads about 104. The tester's 30 % tolerance hides it. — fix (optional): use effective lengths (BOX.h-2R, W-2R) in both pMeas and pRef, or soften the comment to "approximately proportional".

2. sim.js:33 — "Kun hiukkaset liikkuvat nopeammin tai astia on pienempi, ne osuvat seinään useammin ja kovempaa." In a smaller box the hits are more frequent but each hit is not harder (same speed, same impulse). "kovempaa" applies only to faster particles. — fix: "Kun hiukkaset liikkuvat nopeammin, ne osuvat seinään useammin ja kovempaa. Kun astia on pienempi, ne osuvat seinään useammin."

3. lesson.md:61 — "Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu." The inference depends on mean kinetic energy being proportional to kelvin temperature. The lesson only says that temperature "kertoo" the mean kinetic energy (line 8) and never states the proportionality. Exercise L3-03 and the exit ticket do state or assume it. Physically correct for an ideal gas, but not explicit. — fix: add one qualitative sentence in the micro-model paragraph, e.g. "Keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan." Do not add the E_k formula, which is FY4.

4. lesson.md:10 — "100 °C kiehumispiste" holds only at normal pressure; the lesson itself tells the student that pressure is a state variable. — fix (optional): "veden kiehumispiste normaalipaineessa".

5. solutions.md:23 and :39 — "77 astetta absoluuttisen nollapisteen yläpuolella" and "muutaman asteen" use "aste" for kelvins. This contradicts lesson.md:17 ("Kelvineissä ei käytetä sanaa aste"). The file is unpublished. — fix: "77 kelviniä" and "muutaman kelvinin".

6. lesson.md:58 and :10 — the extrapolation result is presented as "lähellä absoluuttista nollapistettä" without noting that real gases condense before reaching it, so the straight line is only a model extrapolation. Fine at FY3 level; optional one-clause caveat.

Checked and correct (no finding):
- Definitions of system, surroundings, closed system, state variables; T = θ + 273,15; 0 K = −273,15 °C; "lämpötilaero sama K ja °C"; "kelvin, ei kelvinastetta"; negative Celsius allowed, negative kelvin not.
- Micro model: T as mean kinetic energy of the particles, pressure from wall collisions, "useammin ja kovempaa" at higher T and constant V (correct).
- The misconception: 283 K to 293 K is 3,53 % (checked). Fine.
- Worked example: k = 37/100 = 0,37 kPa/°C, θ0 = −100/0,37 = −270,27 °C, about −270 °C. A least-squares fit of the six points gives −271,1 °C. The data are consistent with an ideal gas (136,6 kPa at 100 °C against 137 in the table). SVG geometry: 1,25 px/°C and 1,5 px/kPa; the points and the −270 intersection (x=107) are consistent with the table.
- Units and magnitudes in exercises are plausible (liquid N2 77 K, CMB 2,7 K, Moon −173/127 °C, tyre pressure).
- solutions.md and exit-ticket.json: no wrong reasoning. The "relative temperature" sanity checks (about 7 %, halve in kelvins not Celsius) are correct.
- Sim physics: speed = V_REF·sqrt(T/300), so E_k is proportional to T (correct). Wall momentum 2|v_n| per collision, force per wall length, averaged over both axes and divided by 2 walls per axis: the 2D formula p = N m v²/(2A) is reproduced by pRef (m=1). Readout "keskinopeus sqrt(T/300) × ..." is correct. 300 K = 27 °C (26,85 rounded).

Python output (python3 -I, from problem text alone, before reading solutions.md):
L1-01 21+273.15 = 294.15 (answer 294)
L1-02 350-273.15 = 76.85 (answer 77)
L1-03 77-273.15 = -196.15 (answer -196)
L1-04 45-20 = 25 (answer 25)
L1-05 2.7-273.15 = -270.45 (answer -270)
L2-01 303-273.15 = 29.85 (answer 30)
L2-02 100+0.37*50 = 118.5 (answer 119; rel. dev. 0.0042 against tolerance 0.02; 118 also passes at 0.0084)
L2-03 k=0.275, theta0 = 20-80/0.275 = -270.91 (answer -270; rel. dev. 0.0034)
L2-04 127-(-173) = 300 (answer 300)
L3-01 300*308.15/288.15 = 320.82 (answer 321); with 273: 320.83
L3-02 least-squares slope 0.95, intercept 259.5, theta0 = -273.16 (answer -273)
L3-03 293.15/2-273.15 = -126.575 (answer -127; with 273: -126.5)
All 12 answers correct within the 0,02 relative tolerance, including rounding with 273 instead of 273,15.
Example: fit of 6 points theta0 = -271.06; endpoints -270.27; ideal-gas p(100 C) = 136.61 (table 137); 283->293 K = +3.53 %.
Sim replica (Python port of draw loop, 80 particles, 30 s):
 T=300 V=1: measured 103.7 theory 100.0
 T=600 V=1: 207.1 / 200.0
 T=100 V=1: 34.6 / 33.3
 T=300 V=0.5: 211.0 / 200.0
 T=300 V=2: 51.2 / 50.0
 T=600 V=0.5: 422.2 / 400.0
 T=100 V=2: 17.0 / 16.7
