VERDICT: FAIL
CONTENT-HASH: 14f290f6e62807dd

## Blocking
- [Major] L2-08 (5-16), choice with figures, after a wrong answer (open-exercises-L2-1280-9; reproduced live at 390 and 1280 px) — the feedback `div.feedback` sits below a `label` that has `height:100%` in the `fieldset.choice.figures` grid, so it overflows the list item: at 1280 px it hides under the next card and the Vastaa button (only "paluumatkalla." peeks out) and its KaTeX ("6,0 m") is drawn large over graph C/A; at 390 px it is drawn over the next figure. The student cannot read why the choice is wrong, and the card shows a tall empty green box. Fix in the template (templates css, `fieldset.choice.figures`): make `li` a flex column as `.models` already does (`li{display:flex;flex-direction:column}`, `.feedback{margin-left:0}`) and drop `height:100%` on the label, so the feedback follows its card in the same cell. This is the only chapter whose task uses figure choices.

## Polish
- [Minor] Graphs A–D — the y ticks 2…12 are shown but the option graphs have no marked point at 6 m, 4 s, 10 s; acceptable, optional.

## Checked
- Hash at start and end 14f290f6e62807dd. Opened open-exercises-L2-1280-8, -9, -10 (the new task, its solution card, "Kuvaajan lukeminen"), plus own live renders of L2-08 at 390 and 1280 px, unanswered and after a wrong answer.
- The four new figures (pick-away, -back, -distance, -vt): consistent axes and strokes, units on axes, A–D readable at 390 px; B is clearly a (t, v) graph. Solution text: maths, decimal comma, units correct. Paragraph splits in other tasks render cleanly.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 3
