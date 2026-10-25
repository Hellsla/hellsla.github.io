VERDICT: DONE
Round 1 fixes for fy3-5 (no simulation, so test_sims.py is not run).

## Findings
1. editor + educator, Blocking, exercises.json:98 (L3-03 repeats L2-03). Replaced with the educator's two-route task: the same gas goes from the same initial to the same final temperature in two ways. In A, Q = +400 J and the gas does 150 J of work. In B, the gas does 60 J of work. The student finds Q in B and explains why ΔU is the same. Answer 310 J (ΔU_A = 250 J, Q_B = 250 J + 60 J). answers.py was changed first, then exercises.json and solutions.md.
2. editor + educator (+ mathematician, physics-expert 4), Blocking, exit-ticket.json:11–12 (system boundary). The isolated system is now "termospullo ja sen sisältö". In the answer, the system's U stays constant while heat moves from the coffee to the colder inner wall and air, so the coffee's U falls and theirs rises by the same amount.
3. physics-expert 1, mathematician 3, exercises.json:82 (L3-01). Now reads "mäntä työntää ilmaa 0,15 m:n matkan keskimääräisellä 120 N:n voimalla", so W = Fs = 18 J is exact.
4. physics-expert 2, solutions.md:77. Narrowed to a gas: "Kaasun sisäenergia riippuu käytännössä vain sen lämpötilasta ja määrästä." The new L3-03 solution uses the same wording.
5. physics-expert 3 / mathematician 2, lesson.md:43. Now reads "Jos sama 150 J:n työ tehtäisiin niin hitaasti, että …".
6. physics-expert 5, lesson.md:10 and :52. The isolated system now keeps its "kokonaisenergia" constant. Line 10 also defines it against "suljettu" (educator).
7. editor + educator, lesson.md:17 and :6, "edellisellä oppitunnilla". Both now say "oppitunnilla fy3-2". Line 17 also says the piston's work is found as in fy3-2, as force times distance (educator, in words, so no new undisplayed formula).
8. editor + educator, glossary. Added "eristetty systeemi" to glossary.json (two sentences that contrast it with "suljettu") and to meta.json `glossary`.
9. mathematician 1, lesson.md:31. The SVG label "Q < 0 tai W < 0" is now at `x="414" text-anchor="start"`, so it clears the box.
10. educator, exercises.json:72, L2-04 had the same steps as L2-02. It now gives P, Q and ΔU and asks for the time: W = ΔU − Q = 10 kJ, t = W/P = 40 s. answers.py, exercises.json and solutions.md were updated to match.
11. educator, lesson.md:6 and :8, micro-model. On line 6, fy3-2's everyday wording "työ muuttuu lämmöksi" is acknowledged and made precise. On line 8, one clause was added: the moving piston hits the particles like a bat hits a ball, and they bounce back faster.

## Not applied
- editor, polish on lesson.md:43: shortening the example's remark to a hint. Skipped because physics-expert 3 (applied) keeps the remark and only states its assumption. The new L3-01 wording asks for more than the remark gives.
- proofreader polish ("+ 0 kJ", "koskettavat toisiaan"): the proofreader marked these as not applied, and its diff is empty.
- web-designer, true minus in answer rendering, and the site.css line length: these concern the template or CSS, so they cannot be fixed here.
- web-designer, no-break spaces in solutions: this is a site-wide rendering choice, so it is left to the human or the template.
- web-designer, larger SVG font: at 24 px or more, the "Q < 0 tai W < 0" label would overflow the 600 px viewBox from x = 414, so the size stays at 22 px.

## Files changed
content/FY3/fy3-5/lesson.md, exercises.json, solutions.md, answers.py, exit-ticket.json, meta.json; glossary.json.

Checks: lint 0 errors / 0 warnings; check_latex ok; build --all ok (skipped fy3-7). Stale reviewers to re-run: physics-expert, mathematician, educator, proofreader, editor, web-designer (all six).
