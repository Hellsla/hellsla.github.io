VERDICT: PASS
CONTENT-HASH: 42a85f8ae42cb80b

## Blocking
(none)

## Polish
- exercises.json fy8-6-L2-08, options — the correct one is the only hedged, quantified one ("sopusoinnussa ... koska ero on epävarmuutta pienempi"); the others are categorical ("epäonnistunut", "liian pieni", "määrää"). Fix: give the distractors the same "koska ero ..." form, e.g. "Ryhmän Planckin vakio poikkeaa hyväksytystä arvosta, koska ero ei ole nolla" and "... on liian pieni, koska ryhmän arvo on hyväksyttyä pienempi".
- exercises.json option 4 ("jännite määrää fotonin energian") — it is off the data question (conclusion from the table) and so weak. Replace it with a conclusion about the intercept or about 5 points being too few.
- stem — the rule "ero pienempi kuin epävarmuus = sopusoinnussa" and dh = e dk are not in the brief (it speaks only of uncertainty qualitatively). The stem gives dk, so the arithmetic is fair; add one sentence in the stem, "Tulos on sopusoinnussa, jos hyväksytty arvo on välillä h ± dh", or confirm it from an earlier course.

## Checked
- New task fy8-6-L2-08 (measurement data, type 10): recomputed the fit of the five points: k = 3,98e-15 V s, intercept -0,07 V, residuals within about 0,05 V. Consistent with the stem's values.
- h = 6,376e-34, dh = 0,336e-34, difference 0,25e-34: the correct option holds. The distractors catch the lesson's warned errors (the line not through the origin; reading a difference inside the uncertainty as an error).
- The correct feedback does not give a reason stage ahead of time.
- Data caption short; table columns have units.
Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders were opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
