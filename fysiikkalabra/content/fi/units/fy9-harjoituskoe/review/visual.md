VERDICT: PASS
CONTENT-HASH: 8fe07a88b6155df4

Delta (goal wording, previous PASS hash 34569735919c8d54): inquiry.json learn[1] now reads "valitsemaan omaan osaamiseesi parhaiten sopivat tehtävät." Correct, idiomatic Finnish, same length class and form as the other goals (3rd infinitive + object, full stop). No layout impact. objectives.py and units.py check pass. Verdict unchanged.

Round 2 (delta review of round 1 fixes; round 1 hash 1e35148179fc1f8f).

## Verified in the built preview (python3 scripts/build.py fy9-harjoituskoe; Playwright at 390 and 1280, all done-boxes ticked, all details open)
- Polish 2, plan figure: the Osa II/III dividers now stop short of the labels, and no line crosses "Osa II" or "Osa III". This holds at 390 and 1280.
- Polish 3, s10 graph: the intercept label "(0; 0,032 s²)" is offset with a leader to the circled intercept. All six data points are visible (m = 0,100 kg included), and the slope label 1,58 s²/kg is legible.
- No horizontal overflow (scrollWidth = 390 and 1280), 0 .katex-error, no raw $…$ in the rendered text, no console errors.
- The changed texts render correctly: s5 c), s8 d), s9 b) Järkevyys, s10 e) and teacher notes. The Finnish is natural, with decimal commas and units in LaTeX.

## Remaining (shared, not this unit's)
- Model figures inside opened answers render at about 0,5 scale at 390 px (ticks under 14 px). This is a template issue (details padding / figure width).
- Fold-chip wrapping of "OSA I" at 390, and the stage chip "Sovella" for exam sections, are shared CSS/template issues.

## Blocking
(none)

## Polish
(none new)
