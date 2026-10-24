VERDICT: FAIL

Reviewer: physics-expert. Lesson fy3-2 (Työ ja energia). All 12 exercise numbers and all units are correct; sim.js implements W = F s exactly. FAIL is for scope errors (items 1-3) and one missing-condition error in the lesson text (item 4). The rest are minor.

## Python recomputation (python3 -I, g = 9.81, from problem text only, done before reading solutions.md)
```
fy3-2-L1-01 mine=2.0000 ans= 2.0 kJ rel=0.0000 tol 0.05 OK
fy3-2-L1-02 mine=176.5800 ans= 177 J rel=0.0024 tol 0.02 OK
fy3-2-L1-03 mine=1530.0000 ans= 1530 J rel=0.0000 tol 0.02 OK
fy3-2-L1-04 mine=3.0000 ans= 3.0 kW rel=0.0000 tol 0.05 OK
fy3-2-L1-05 mine=360.0000 ans= 360 kJ rel=0.0000 tol 0.02 OK
fy3-2-L2-01 mine=375.0000 ans= 375 kJ rel=0.0000 tol 0.02 OK
fy3-2-L2-02 mine=16.2000 ans= 16.2 MJ rel=0.0000 tol 0.02 OK
fy3-2-L2-03 mine=43.1732 ans= 43.2 m rel=0.0006 tol 0.02 OK
fy3-2-L2-04 mine=760.2750 ans= 760 W rel=0.0004 tol 0.02 OK
fy3-2-L3-01 mine=14.4300 ans= 14.4 kJ rel=0.0021 tol 0.02 OK
fy3-2-L3-02 mine=100.0000 ans= 100 kW rel=0.0000 tol 0.02 OK
fy3-2-L3-03 mine=45.4167 ans= 45.4 min rel=0.0004 tol 0.02 OK
```
Formulas used: W=Fs; ΔE_p=mgh; E_k=½mv²; P=W/t; W=Pt; W=ΔE_k with 90 km/h = 25 m/s; h=Pt/(mg); E_loss=mgh-½mv²; P=Fv with v=80/3.6; t=mgh/P. No answer is out of tolerance. Units (kJ, J, kW, MJ, m, W, min) match the quantity asked in every case.

## Findings

1. lesson.md:21-25 (and exercises.json:5, 10, 16; solutions.md:21, 44-47, 77-79) — SCOPE ERROR. The lesson says E_k = ½mv² and E_p = mgh "tulivat tutuiksi FY2-moduulissa". The MAOL guide says the opposite. FY2 (maol txt, ~lines 197-230) introduces energy forms "ilman kullekin energialajille kuuluvia lausekkeita, kuten Ek = ½mv², Ep = mgh". The expressions, mechanical energy and the work principle (net-force work = ΔE_k) are FY4 content (maol txt ~lines 388-407). FY3 central content is force as a measure of interaction, mechanical work W=Fs, and energy conservation/transfer. Three exercises rest on E_k (L1-03, L2-01, L3-01). Fix: (a) delete the false "FY2" sentence; (b) drop E_k = ½mv² from the formula section and from the exercises, or get the human's decision to widen the scope; (c) keep the gravitational case by deriving it from W = Fs with F = G = mg (weight G=mg is explicitly in FY3 content), i.e. lifting work W = G h, with E_p change as the work done; (d) rewrite L1-03 as a W=Fs or P=W/t problem; rewrite L3-01 so the energy lost is found from lifting-type quantities only, e.g. "a skier's friction work/heat equals F·s" or an energy-accounting task with given energies (E_in 29.4 kJ, E_out 15 kJ given in J); (e) rewrite L2-01 (see item 2).

2. exercises.json:10 / solutions.md:44 — SCOPE ERROR. L2-01 asks for the work of the "kiihdyttävä voima" and the solution uses W = ΔE_k. MAOL FY3 says: "Voiman tarkastelussa ei ole tarkoitus käsitellä voiman merkitystä liiketilan muutoksen aiheuttajana". The work-energy theorem is FY4. It also silently assumes that resistances are zero and that the force is the net force. Fix: replace with a problem that uses W=Fs and a unit conversion or rearrangement (e.g. "A 2,4 kN force moves a car 18 m... work in kJ" or "work 45 kJ, force 1,5 kN: distance?"), or reword as an energy-transfer question with stated energies.

3. solutions.md:4-5 — SCOPE ERROR. Formula is given as W = F s cos α with α = 0°. The angle between force and displacement (projection) is vector content (FY4) and never appears in the lesson. L1-01 is a plain W = Fs problem. Fix: use "W = F s" and say "voima on liikkeen suuntainen".

4. lesson.md:8 and lesson.md:63 — MISSING CONDITION / WRONG AS STATED. "Kun teet kappaleeseen työtä, sen energia kasvaa täsmälleen tehdyn työn verran" and "tehty työ kasvattaa kappaleen liike- tai potentiaalienergiaa" are false in general. When you pull a box at constant speed along a floor (exactly what sim.js shows), the work does not raise E_k or E_p. It becomes heat through friction. The spring example stores elastic energy, which is not "liike- tai potentiaalienergia" as defined by E_p = mgh. Fix: "Työ siirtää energiaa kappaleelle tai kappaleesta: se voi kasvattaa potentiaalienergiaa (nosto), liike-energiaa tai sisäenergiaa (kitka, lämpeneminen)." This also connects to the FY3 Joule experiment (item 8).

5. lesson.md:7, 62 — wording. "Voima tekee työtä vain, kun se siirtää kappaletta omaan suuntaansa" is OK as a W=Fs-level simplification, but it should state the condition explicitly: W = Fs holds for a constant force along the displacement. A force at an angle does some work without moving the body "in its own direction", so the summary line "Voima, joka ei siirrä kappaletta omaan suuntaansa, ei tee työtä" over-claims. Fix: "Voima, joka on kohtisuorassa liikettä vastaan (kuten reppua kantava voima vaakasuoralla), ei tee työtä." Also line 6: add "vakionopeudella" to the carrying example (it matches exit-ticket Q1).

6. lesson.md:8 — "Energia on kappaleen kyky tehdä työtä" is a textbook shorthand but is wrong for thermal/internal energy (heat cannot be fully converted to work). Given that the module goes on to thermodynamics, prefer "Energia on suure, jonka avulla kuvataan, mitä tapahtuu; työ siirtää sitä." Low priority.

7. lesson.md:27-31 — P = Fv. Condition ("Tasaisessa liikkeessä", force along motion) is stated adequately; but with constant speed, P = Fv is the (constant) power, with varying speed it is instantaneous power. Optional: add "voima liikkeen suuntainen". Check of derivation: P = W/t = Fs/t = Fv. Correct. Worked example (lines 51-53): 0,5·40·0,20 = 4,0 J; 20·0,20 = 4,0 J; 4,0/0,50 = 8,0 W; SVG geometry (triangle (80,250)-(480,250)-(480,50), 40 N at top, 0,20 m at x=480) is correct; the "kaksinkertainen virhe" 8,0 J is correct. 1 J = 1 N·m, 1 W = 1 J/s and the 6 kW = 6000 J/s statement are correct. No findings here beyond the optional wording.

8. lesson.md (whole) — omission against curriculum goal. meta.json/curriculum.json give "Täsmennys: työn laki W = Fs määritellään kokeeseen perustuen (Joulen koe)". The lesson never mentions the Joule experiment (mechanical work → measured heat). Not a physics error, but the goal is unmet; one or two sentences (falling weight turns a paddle in water, temperature rises, W = mgh ≈ heat) would also repair item 4.

9. exercises.json:12 / solutions.md:58-63 — L2-03: the 12 kW power is not said to be the power delivered to the load. A real crane has losses; "Oleta, ettei energiaa häviä" or "nostoteho 12 kW" is needed (L3-03 states the assumption, L2-03 does not). Numbers are correct (43,2 m; v = 1,44 m/s).

10. solutions.md:71 — L2-04: sanity check calls 760 W "hetkellinen teho", but the problem asks for and the solution computes the average power over 12 s. Fix: "keskimääräinen teho" (also the comparison with 1 hp = 746 W is correct). 15 m in 12 s (~5 storeys) is hard but plausible for a fit runner.

11. solutions.md:85 / exercises.json:17 — L3-02: substitution "4500 N · 22,2 m/s = 100 000 W" is inconsistent with the rounded 22,2 (gives 99 900 W). Fix: use v = 80/3,6 m/s = 22,22 m/s or write "≈ 100 000 W (80 km/h = 22,22 m/s)". The answer 100 kW is correct. The level is only borderline "L3": it is P = Fv with a conversion; the "Perustele kaava" part carries the reasoning. Also solutions.md:87 "Kuorma-auton moottorin teho..." is hand-waving; a 4,5 kN drag for a trailer at 80 km/h is large but plausible for a heavy full trailer, so the sanity check should say the 4,5 kN is the resisting force the pull balances. Do not invoke Newton's laws (FY4).

12. exercises.json:18 / solutions.md:93-95 — L3-03: "keskimäärin 180 W" for a cabin solar panel is unrealistic as an average (180 W is a typical peak rating; in Finland the yearly average is a few tens of W). Fix: "tuottaa auringonpaisteessa 180 W" or change to a 'nimellisteho' phrasing. Computation (490 500 J / 180 W = 2725 s = 45,4 min) is correct.

13. solutions.md:7, 23, 39, 47, 55, 63, 79 — sanity-check commentary quality. L1-01 "200 kg:n nostaminen metrin verran" is numerically right (1,96 kJ) but irrelevant to the pushing; L2-01 "tuttu luku kolaritarkasteluista" is not a check (use 90 km/h = 25 m/s and compare to lifting the car ~31 m); L3-01 "pehmeällä lumella" is speculation (the check √(2gh) = 28,0 m/s is correct, and 14,43/29,43 = 49 % is correct). All other sanity numbers verified: 147 N shelf weight, 1,53 kJ = 1,8 m of lifting for the cyclist, 36,7 m for 360 kJ, 16,2 MJ = 4,5 kWh, 1,44 m/s crane, 490 kJ = 0,136 kWh.

14. exercises.json:3, 6 — tolerance 0.05 on L1-01 and L1-04 versus 0.02 elsewhere. Not wrong (exact answers), only inconsistent. Fix: 0.02 for uniformity.

## sim.js check
- sim.js:32 `W = F * s` — exact W = F s; sim.js:33 `P = W / t`; sim.js:35 `Wdone = W * u` (linear in covered fraction, correct for constant force); sim.js:64 shaded rectangle width ∝ u, height ∝ F, so the filled area equals F·(s·u) = Wdone. Units in the readout are J and W. Force arrow scale (F·1,2 px) is consistent with the comment.
- No angle, no cos, no vector arithmetic: in scope (force arrow only illustrates the interaction).
- Minor: sim.js:43 `fi(W, 0)` rounds W when F is odd and s ends in .5 (e.g. 61 N × 10,5 m = 640,5 J shows as 641 J or 640 J). Fix: `fi(W, 1)` when W is non-integer. Cosmetic.
- Minor: the box moves at constant speed s/t under a constant "pulling force" with no friction shown, so a student may ask where the energy goes (see item 4). Suggest a caption "kitka pitää nopeuden vakiona; työ muuttuu lämmöksi" or the box on a lifting setup. Not a physics error because the sim reports only W and P.
- Minor: sim.js:6/56 at s = 20 m the box (x = 320 + 20) overshoots the floor line that ends at x = 330. Cosmetic.

## Summary
Numbers and units: all correct. Sim: correct. Required before PASS: items 1, 2, 3 (scope: E_k/E_p expressions and the work-energy theorem are FY4 per MAOL; cos α is vector content) and item 4 (unconditional "work increases kinetic or potential energy" is false with friction). Items 5-14 are recommended.
