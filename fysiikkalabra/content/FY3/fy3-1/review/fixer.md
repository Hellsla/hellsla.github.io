VERDICT: DONE

Round 1 fixes for fy3-1. Build, check_latex and test_sims (now 17 assertions) all pass.

1. tester 1 / physics-expert 1 / editor 1 (BLOCKING, sim.js): the stretch cancelled the mass. Fixed: stretch = maxLen * G / (100 * G_MAX), a fixed full scale of 100 kg on Jupiter (2480 N). Bar heights use the same scale (h = G / 2480 * 220 px), and the weight arrow length grows with G (20 + 50 * G / 2480 px). The sliders now visibly change the spring, the arrow and the bars. simState.stretch stays purely proportional to G (so the tester's stretch/G assertion passes without being loosened). The visibility of small weights is handled only in the drawing: a fixed spring rest length (40 px, with a dashed marker at the unloaded end), a 2 px minimum bar height, a minimum arrow length, and a label "asteikko 0 – 2480 N" in the chart. The sim.js header comment and sim-spec.md describe exactly this.
2. tester assertions: the existing stretch assertions (3) pass unchanged. I added 2 assertions to tests/sims/fy3-1.json: bar heights are proportional to G (10x mass gives 10x height for every body) and the full scale fits the chart. For this I expose simState.bars (heights in px). The tester listed no other missing assertion.
3. physics-expert 2, educator 4, editor 2 (g convention, lesson.md): stated once under the formula: g = 9,81 N/kg means the weight of one kilogram of mass is 9,81 N; same number as FY1's 9,81 m/s², and N/kg and m/s² are the same unit. No causal wording, "mittaamasi" removed. Not applied: the editor's remark to add prerequisites to meta.json (decision for the human; the FY1 remark is now neutral).
4. physics-expert 3: the table header is "g pinnalla (N/kg)" and the text says the values are for the body's surface (Jupiter: cloud-top level). The sim labels were not changed.
5. physics-expert 4: "kun jousta ei venytetä liikaa" added to the proportionality sentence.
6. educator 1, editor 3 (spring paragraph): split into single-idea paragraphs: stretch is proportional to force; the (force, stretch) line passes through the origin (FY1 linear model with zero constant term); a worked proportion (5,0 N / 2,0 cm gives 4,0 cm and 1,0 cm); calibration by marking known weights. A separate worked calibration example or graph was not added (it would widen the lesson beyond the gold length; the proportion line covers the method used in L1-04, L2-04 and exit-ticket Q2).
7. educator 2: applied in small form (Maa pulls an apple, "paino" is now introduced after the apple), the magnet example was left out.
8. educator 3: bridge added as the first line under Kaava: two similar bodies stretch the spring twice as much as one, so weight is directly proportional to mass.
9. educator 5, editor 3 (meta sentence): the "Tässä oppitunnissa paino ymmärretään ... vain suuruus" sentence was removed from Kaava and replaced with one short sentence in Ydinajatus ("Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa."). The arrow in the figure stays.
10. mathematician 1/4, educator 6, editor 4 (example numbers): 120 kg on Earth is now 1180 N (1,18 kN); Mars 445 N; units use "\,". Summary formulas also use "\,". The SVG was not moved (educator's optional move, no need).
11. educator 7: one sentence on why a bathroom scale shows kilograms (measures a force, scale made on Earth by dividing by 9,81 N/kg).
12. editor 4 (repetition): "mass is the same, only weight changes" is now in exactly three places: Ydinajatus (paragraph on weight), the misconception section, and the summary bullet. Removed from the example and the duplicate fourth summary bullet; the astronaut sentence no longer repeats it.
13. proofreader 1: Finnish quotation marks ”painan 70 kiloa” in lesson.md and exit-ticket.json.
14. educator 8, editor 5 (L1-03): replaced by a Moon task, 30 kg object on the Moon with g read from the lesson table; answer 49 N (exact 48,6 N, relative error 0,8 % < tolerance 0,02). Solution rewritten (Earth comparison 294,3 N). Counts stay 5/4/3 with a solution for each id. Not applied: editor's suggestion to swap L1-05 or add a short-text reasoning task (opinion; the level counts and the types of task are fine).
15. educator 9: L2-04 says "kappale"; L3-03 reworded and the term unified (the "vaaka" is now voimamittari whose scale is made on Earth).
16. educator 10, editor 5 (L3-01 hint): the hint "Vihje: mikä pysyy samana?" was removed from the text; the solution's Kaava line already carries the idea.
17. mathematician 2/3: L3-01 intermediate is now "18/9,81 kg ≈ 1,8349 kg"; G_Mars ≈ 6,807 N. L1-05 shows "62 N" instead of "62,0 N". All changed numbers recomputed with python3 -I: 30*1,62 = 48,6; 30*9,81 = 294,3; 18/9,81 = 1,83486; 6,80734; 6*1,62/9,81 = 0,99083; 120*9,81 = 1177,2; 120*3,71 = 445,2; 3*9,81 = 29,43; 3*1,62 = 4,86.
18. educator 11: exit-ticket Q1 gives g = 1,62 N/kg for the Moon. Editor's suggestion to replace Q3 with a mass-from-weight check was not applied (opinion).
19. proofreader 2 and 3 (glossary): comma added in "massa"; new term voimamittari added to glossary.json (and to meta.json glossary list, plus "voima" see_also); the word jousivaaka is no longer used in lesson.md, exercises or solutions.
20. web-designer 2 and 4 (sim.js): the block width is at least 2,8 times the label size (Math.max(..., ts(13) * 2.8)); non-selected bars have alpha 150 (was 90) and darker colours (Kuu 110,110,110; Jupiter 176,120,50). The weight/arrow figure was checked visually at 1280 and 390 px.
21. web-designer 1, 5, 6 (select height, SVG font size, table box): CSS/template, "not fixable here". The SVG font size was also left alone (optional).
22. proofreader nits (kankaan, "Tässä oppitunnissa", "Massa on aineen määrä"): not applied, wording opinions that are acceptable as they are. mathematician 3 (62,0 N) is covered in item 17.

Files changed: lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js, sim-spec.md, meta.json (glossary list only), ../../glossary.json, ../../../tests/sims/fy3-1.json. No status field, template or CSS was touched.

NEW HASH: python scripts/gate.py --hash fy3-1 = fc5375c46d696bd5

Every edit changes the content hash, so all reviewers must run again (physics-expert, editor, tester must re-verify their FAILs; the PASS reviewers too, since the hash changed).
