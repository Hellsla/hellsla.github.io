VERDICT: PASS
CONTENT-HASH: 01607ed274d08372

## Blocking
- none

## Polish
- [Minor] Teoria, "Suhteellinen epävarmuus…" example sentence — "vähintään 4 s" has the unit in plain text, while the neighbouring numbers are LaTeX (untouched text) — set as $4\,\text{s}$.

## Checked
- delta: opened fy1-8-stage-selita-390-1 and -3, fy1-8-theory-1280-1, -2 and -3 (the three new "Pysähdy ja mieti" blocks, the surrounding text, the setup and uncertainty figures, the table).
- The three blocks show a left bar, a label, the question, and an answer collapsed under "Vastaus". The question is last and is its own paragraph. No clipping or overflow at 390 or 1280 px. KaTeX in the third block ($0{,}2\,\text{s}$, $2{,}0\,\%$) renders cleanly. The solution (not opened) is plain LaTeX in the source: $t = \Delta t/\varepsilon_\text{max}$.
- The blocks sit after the paragraph or figure they refer to, and the layout around them survived.
- Finnish: simple, clear and consistent with the glossary terms (hypoteesi, muuttuja).

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
