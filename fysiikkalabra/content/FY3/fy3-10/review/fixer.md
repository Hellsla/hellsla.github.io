VERDICT: DONE

fy3-10, after review round 1. Files changed: lesson.md, exercises.json, solutions.md, answers.py, exit-ticket.json. Not touched: sim.js and tests/sims/fy3-10.json (the graphics agent is reworking them in parallel), meta.json, glossary.json.

## Blocking
1. physics-expert 1 / mathematician 1 (lesson.md, misconception): the false claim that kPa with litres is "tuhat- tai miljoonakertaisesti väärä" is gone. The misconception section is now a three-item list. The units item says that kPa with m³, or Pa with litres, gives a result 1000 times wrong, and tells the student to convert pressure to Pa, volume to m³ and temperature to K.
2. mathematician 2 (solutions.md L2-03): changed to "= 828,4 K. θ₂ = 828,4 − 273,15 = 555,3 °C ≈ 555 °C". Changed the answers.py comments the same way (828,4 K, 555,3 °C).
3. educator 1 / physics polish 1 / editor polish 3 (lesson.md): Ydinajatus now says "Avogadron vakio N_A = 6,022 · 10²³ 1/mol". Kaava now has the display formula `N = n N_\text{A}`, which names N (hiukkasten lukumäärä) and N_A.
4. editor / educator (L2-01 repeated the worked example): reversed the task. A 10,0 l cylinder holds 2,40 kg of O₂ (M = 32,0 g/mol) at 15 °C, and the task asks for the pressure in bar. Answer 180 bar (179,6), tolerance 0,02. Updated answers.py, exercises.json and solutions.md.
5. educator (L3-02 repeated the example's last paragraph): made the task backward. The argon fill makes a 1,20 m × 1,00 m glazing unit 6,0 g heavier than an air fill (101 kPa, 20 °C), and the task asks for the gas layer thickness. The chain is n = Δm/(M_Ar − M_ilma), then V = nRT/p, then d = V/A. Answer 11 mm (10,96), tolerance 0,02. Dropped the "perustele" question that lesson.md answered verbatim. Updated answers.py, exercises.json and solutions.md.

## Polish applied
- solutions.md L1-03: "patruunassa hiilidioksidi on nesteenä suuressa paineessa".
- exit-ticket.json: Q2 uses "ainemääränä" and "Ainemäärä on sama". Q1 uses 300,15 K, which gives 0,601 mol.
- solutions.md L3-03: "V = 200 l = 0,200 m³". L1-04: "324 − 273,15 ≈ 51 °C".
- lesson.md Kaava names θ: a temperature in degrees Celsius is converted to kelvins by adding 273,15.
- Hook changed to "**Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?"
- lesson.md Kaava now says that p ∝ NT/V (doubling N or T, or halving V, doubles p). A paragraph points to the sim and says that particle–particle collisions do not change the pressure and are left out. The summary has a new bullet on p ∝ NT/V.
- 1 Pa · m³ = 1 N/m² · m³ = 1 N · m = 1 J is written out. The mole paragraph says why particles are counted in moles (with a link to chemistry), and M has its own paragraph.
- The worked example's sanity check now uses the molar volume of about 24 l/mol and no longer argues in a circle. "Pyöristämätön" is gone; the example uses 0,2073 mol for the mass.

## Polish skipped
- tester 1–3 (clearAvg in sync(), a test at N = 20), web-designer (ts(11) for "ref"), physics polish 4 (the collision text in sim.js): skipped because sim.js and tests/sims are being reworked by the graphics agent. The lesson text now covers the collision point.
- editor (replace exit Q1 with a ratio question): the brief kept Q1 and asked only for the 300,15 K fix. The p ∝ NT/V reasoning is now in the Kaava text, figure 2 and the summary.

## Lesson form (CLAUDE.md, NOTES.md section 4)
- Ydinajatus has an SVG: two equal balloons with the same 12 particles. One holds helium (0,21 mol · 0,83 g) and the other air (0,21 mol · 6,0 g). The aria-label says the figure is schematic.
- Kaava has an SVG: four gas containers, alku p, 2N 2p, 2T 2p (longer speed strokes) and V/2 2p.
- Both SVGs use viewBox 0 0 600 300, currentColor, 24 px text (15 px rendered at 360 px) and an aria-label. At 360 px no text box overlaps another text box or a shape.
- Paragraphs are all under 120 words. The misconceptions are bullets.
- The Esimerkki has 5 `<!-- vaihe -->` stages: Tunnetut ja kysytty (list), Kaava ratkaistuna (n = pV/(RT), m = nM), Sijoitus, Tulos, Järkevyys. Every display starts with a symbolic row.
- solutions.md: every **Kaava:** line ends with the asked quantity solved in symbols. L2-02 (M = mRT/(pV)), L3-01 (N = pVN_A/(RT)), L3-02 and L3-03 (Δm = ΔpVM/(RT)) were rewritten that way. Numbers appear only in **Sijoitus:**.

## Checks
answers.py runs and matches exercises.json. lint_lesson.py fy3-10 gives 0 errors and 0 warnings. check_latex.py is OK (21 fragments). build.py --all is OK. check_layout.py fy3-10 is OK at 360 and 390 px. test_sims.py fy3-10 passes. Screenshots at 360 px of both figures and the fully revealed example were checked. Counts are still 5/4/3.

Stale reviewers (gate.py fy3-10): tester, physics-expert, mathematician, educator, proofreader, editor, web-designer, i.e. all seven.
