VERDICT: PASS
CONTENT-HASH: 7a62f7e3fe7ca103

The lesson does what its goals promise and tells one story. The pump question opens it. The theory separates temperature, internal energy and heat, and ΔU = Q + W appears once with a sign diagram. The example, the misconception section and L3-01 all return to the pump. The isolated system now has a definition (contrasted with fy3-3's "suljettu"), a glossary entry and an exit-ticket check whose system boundary holds. The new L3-03 is a real level-3 task: two paths with the same initial and final state, so ΔU is the same and Q and W depend on the path. It does not reach into cmΔT, which stays in fy3-6. Both blocking items from round 1 are fixed.

## Blocking

## Polish
- lesson.md:6 — L3-01, L3-03 and the example's closing remark (lesson.md:43) all rely on the converse: a gas whose temperature and amount stay the same keeps the same U. The lesson only says that U rises with temperature and depends on the amount. The converse appears in solutions.md:77 and :93, but with `solutions: first`, the L3-03 solution is not published. — After "…sen sisäenergia kasvaa.", add one sentence: "Kaasun sisäenergia riippuu käytännössä vain sen lämpötilasta ja määrästä, joten jos ne eivät muutu, ei muutu sisäenergiakaan."

## Checked
- lint_lesson.py: 0 errors, 0 warnings. The hash was the same at the start and the end.
- All 12 answers recomputed from answers.py and matching exercises.json.
- New L3-03 (exercises.json:98): ΔU_A = 250 J, Q_B = 310 J. It is level 3 and differs from L2-03.
- Exit ticket 3: the system is "termospullo ja sen sisältö", U stays constant, and the coffee-to-wall transfer is inside the system.
- "eristetty systeemi" is in glossary.json and meta.glossary, and is defined at lesson.md:10.
- lesson.md:6 and :17 say "oppitunnilla fy3-2", which is correct.
- The example's closing remark is kept with "niin hitaasti" made explicit. L3-01 still has to compute W = Fs and justify ΔU = 0, so it does not repeat the remark.
- P = W/t and W = mgh come from fy3-2; there is no cmΔT (that is fy3-6).
- Levels 5/4/3, and the signs are consistent in the lesson, SVG, solutions and exit ticket.
- lesson.md has 722 words (fy3-2: 703, fy3-3: 829), with the same sections.
