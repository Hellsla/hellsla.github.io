VERDICT: DONE

Stage 4 round 1 fixes.

- Visual [Major] figure `geometry` (`lessons/FY7/fy7-13/figures.py`): the rays are shortened (Lr 300 -> 200), so the lower ray ends at (372, 292), above and left of the label "kohti varjostinta" (x 380-588, y 316-345); no overlap. Figures regenerated into lesson.md.
- Pedagogy polish, `lesson.md` "Kuinka monta maksimia syntyy": condition now $k\lambda < d$, and the edge case reads "Tasarajalla $k\lambda = d$ ...", consistent with the sim and inquiry.
- Science polish, `lesson.md` hila paragraph: "... kaksoisraon kirkkaat juovat, kun rakojen väli on sama, eli ...".
- Visual polish, `inquiry.json` Alkutila: unit of N "1/mm" -> "viivaa/mm" in all three experiments; the builder only typesets units without digits, so the line is now $N = 300\,\text{viivaa/mm}$ in KaTeX.
- Science polish, `lesson-answers.py`: stale keys setup-x1/x2 (300 lines/mm, 650 nm, duplicates of koe1-x-300 and koe3-x-1.00) removed, comment points to koe2-*-532; comments 11,245° and 15,664° corrected.

Not done (not requested): figure `white` and `pattern` label sizes, sim slider label wrap, alt-text "korkeita", hook "tasavälisiä", optional pedagogy suggestions.

`check_lesson.py fy7-13`: all ok.
