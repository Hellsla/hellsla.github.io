VERDICT: PASS
CONTENT-HASH: ce7528c836feb20f

## Blocking
(none) This is a re-review after commit c6532e4f. The earlier Polish is resolved:
- The sentence starter uses `<em>`, so no asterisks show.
- The table *ITER then and now* is shorter at 390.
- The writing-task title uses the colon.
- The temperatures are in LaTeX.

## Polish
1. [Minor] The two predictions now ask almost the same question (`inquiry.json` `pred-ages` and `pred-change`):
   - pred-ages: "Which kind of **statement** in a careful 2018 article … is most likely to be out of date by 2026?"
   - pred-change: "Which kind of **information** in a 2018 article … is most likely to be out of date in 2026?"

   A reader sees the same question twice. Fix: make the difference explicit. For example, pred-ages asks about the type of claim (result, plan or opinion), and pred-change asks about the topic: "Which **topic** of a 2018 article — physics, goal, site, or dates and costs — has changed most by 2026?" Alternatively, drop one. For pedagogy.
2. [Minor] The then-and-now table at 390: the right column still hyphenates "op-eration" and "bil-lion". Acceptable.

## Checked
- Fresh build and captures for this hash: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets.
- In the built HTML: `<li><em>Update, November 2026:</em>`, and no literal `*Update`.
- The table, the claims sorting with LaTeX −269 °C, and the predictions with their wording.
- Playwright: no `.katex-error`, no raw `$` and no overflow.

## Shared issues
(none new)

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
