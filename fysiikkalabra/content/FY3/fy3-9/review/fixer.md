VERDICT: DONE

Round 1 fixes for fy3-9. All checks pass: answers.py, lint (0 errors, 0 warnings), check_latex (5 fragments), build --all, test_sims (62 assertions, no console errors) and check_layout (OK at 360 px).

## Blocking
1. physics-expert 1 (gas weight misconception): lesson.md misconception now says "suljetun astian kaasun paine johtuu kaasun painosta. Pienessä astiassa kaasun paino on mitätön, ja paine syntyy hiukkasten törmäyksistä…". This agrees with fy3-4 (air pressure as the weight of the air column).
2. physics-expert 2 (L2-04): exercises.json now reads "Alun perin kuoressa ollut ilma lämpenee kokonaan 100 °C:seen. Kuinka monta kuutiometriä tästä 100 °C:n ilmasta ei mahdu kuoreen vaan on työntynyt ulos aukosta?" The answer stays 890 m³. Updated solutions.md (Kysytty, Sijoitus, and Järkevyys without "ympäröivä ilma nostaa", physics polish 5) and the answers.py comment.
3. mathematician 1 (SVG points): added circles (417.2, 170) and (504.4, 90). Both panels now show 8 points. Polish: replaced the Bézier with a 22-point polyline sampled from y = 250 − 8360/(x − 50) that passes through every point; the example now says "noin 30 %" and no longer gives "1,04 l"; solutions.md L2-01 and answers.py now say "≈ 2020 l".
4. educator 1 (why 1/V gives a line): Kaava now reads: display p₁V₁ = p₂V₂, then "Yhtälö on sama kuin pV = vakio. Kun se jaetaan V:llä, saadaan", then display `p = \text{vakio} \cdot \frac{1}{V}`, then the sentence that with x = 1/V and y = p the equation has the form y = kx, as in the FY1 line equation, so the graph is a line through the origin with slope k = pV. pV = vakio appears only inline, so no formula is displayed twice. This also covers mathematician polish 4.
5. editor + educator 2 (joules in L2-03): added to Kaava: "Tulon pV yksikkö on Pa · m³ = N/m² · m³ = N · m = J, ja 1 kPa · 1 l = 1 J." L2-03 still asks for joules (2,0 J).

## Polish applied
- physics 1: L2-03 now says "ruiskun mäntää liikutettiin hitaasti, jotta ilman lämpötila pysyi samana".
- physics 2: the Boyle paragraph adds the conditions "kunhan kaasun määrä pysyy samana ja paineena käytetään kaasun koko painetta eikä mittarin näyttämää ylipainetta".
- physics 4: one realism sentence in each of the L1-03 solution (fast expansion cools the air, so the pressure is a little lower) and the L2-01 solution (air is about 10 % stiffer at 300 bar, so the volume is about 1,8 m³).
- educator 1 / editor 1: the chip-bag answer moved to the end of the Boyle paragraph.
- educator 2: the temperature paragraph names "(isobaarinen tilanmuutos)" and "(isokoorinen tilanmuutos)".
- editor 3: the °C misconception now shows one worked step: "V₂ = V₁T₂/T₁ = 1,00 l · 293 K / 283 K ≈ 1,04 l", about 3,5 %.
- editor 4: the experiment paragraph ends with "Kokeile simulaatiossa: tallenna mittauksia eri tilavuuksilla ja valitse ”Piirrä p 1/V:n funktiona”."
- web-designer 1: SVG font-size changed from 20px to 26px. Checked visually at 360 and 1280 px: labels are clear of the curves and the edges.
- web-designer 3: sim.js now creates the legend note right after the readout and before the table. The DOM order is canvas, controls, readout, note, table.
- tester 1: sim.js exposes `pistonY` (piston bottom, canvas px) and `needleKPa` (the value that sets the needle angle; the needle now draws from it). tests/sims/fy3-9.json gained 9 assertions: piston and needle in all three modes, at the slider extremes, plus the note's DOM position. No existing test was changed.

## Skipped
- physics 3: duplicate of mathematician 1 (done).
- web-designer 4 (tab bar clips "Lähtölippu" at 360 px): this is the template, so it is not fixable here.
- tester 2: no action was requested.
- The proofreader's diff was empty.

## Files changed
lesson.md, exercises.json, solutions.md, answers.py, sim.js, tests/sims/fy3-9.json. meta.json, exit-ticket.json and sim-spec.md are unchanged.

Stale reviewers (must run again): tester, physics-expert, mathematician, educator, proofreader, editor, web-designer (all seven).
