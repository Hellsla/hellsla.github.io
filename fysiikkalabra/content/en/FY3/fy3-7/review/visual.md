VERDICT: FAIL
CONTENT-HASH: 0db05c39c956e676

## Blocking
- [Major] lesson.md ("Where does the energy go?" para 2; "Common misconception") — plain-text units remain, and they are in the lesson, not only the inquiry prose: "steam at 100 °C burns worse than water at 100 °C" and "ice at 0 °C and water at 0 °C" are plain Latin text, while the same paragraphs set "$0\,{}^\circ\text{C}$ to $80\,{}^\circ\text{C}$" and "$100\,{}^\circ\text{C}$" in KaTeX (selita-390-2, selita-390-4, theory-1280-2). Two typefaces and two degree glyphs in one sentence. The inquiry fix ("zero degrees", "100-degree steam") is fine; these four are not covered by it — NOTES §1 (2026-10-28): a number with its unit in prose is maths — wrap in `$100\,{}^\circ\text{C}$`, `$0\,{}^\circ\text{C}$` (or reword as "at zero degrees", which also works in the Finnish compound form).
- [Major] top-390 and selita-390-4 — inline maths still leaves punctuation orphaned at a line start: "…not rise above 100 °C / , even though the hob…" (the opening question) and "…from 0 °C to 80 °C / . Another mistake…". The "=" gluing works (verified below), but this was the other half of the earlier finding and is unfixed: the trailing punctuation must be bound to the preceding inline formula (no break between `$…$` and `,` `.` `;` `:` `)`), e.g. a nowrap span in the shared template.

## Polish
- [Minor] heating-curve figure — horizontal parts not to scale against the text (boiling flat much shorter than 5.4 x water rise, 6.8 x melting); say so in the description or lengthen the flat.
- [Minor] phase-diagram figure — gas/liquid fills end in a flat edge right of the boiling curve's end, implying an undrawn boundary; stop at the curve or mark the critical point. For science: confirm.
- [Minor] Worked example Reasonableness — the fraction becomes a block mid-sentence ("With the table value, [block] or 133 g, would vaporise"); end the sentence with the calculation. Straight quotes "all the energy goes into the water" should be typographic.
- [Minor] micro-model — description says "arrows" for gas particles, none with heads are drawn; sim canvas text is small at 390 px.

## Checked
- Point 2 (breaks after "="): VERIFIED RESOLVED. selita-390-1..4, example-390-1/2, theory-1280-2/3: "Q = cmΔT", "Q = sm or Q = rm", "s = 334 kJ/kg", "r = 2260 kJ/kg", "1 W · 1 s = 1 J", "r = Pt/Δm" all stay whole at 366 px; long chains wrap at "=" as designed, no overflow.
- Point 1 (plain units): inquiry prose uses words (grep: no "°C" plain left in inquiry.json), but lesson.md lines 145 and 267 still hold plain "°C" (see Blocking).
- Also opened: top-390, top contact sheet, fig 2-4 in context, example-390-1/2, theory-1280-2/3. Exercises not judged.

## Scores
illustrations 4 · typography 3 · Finnish (English) 4 · accessibility 4
