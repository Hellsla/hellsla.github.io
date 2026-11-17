VERDICT: PASS
CONTENT-HASH: cc5d56c6b2fe7c00

## Blocking
(none)

## Polish
- [Minor] solutions.md, "Hyväksytään myös" (en), part d bullet — the paragraph split leaves "The point for the result requires…" outside the bullet list, so it reads as a free paragraph, not a continuation of the bullet — indent the continuation by two spaces, or rejoin it to the bullet.
- [Minor] solutions.md, Graph a (Io) — the display `$$…$$` still sits mid-sentence before ", so $v^2 = …$"; it renders fine (fi capture), but the sentence is now the start of a new paragraph and reads better if the example is its own line — optional.
- [Minor] tasks.json — the English page is not captured by screenshot.py; the fi captures were the visual reference, so the English wording of the split steps is judged from the source.

## Checked
- Diff 2dc38e00^ of en solutions.md and tasks.json (all split points read as one idea per paragraph, the question last in the three tasks).
- fi captures (the reference): contact-2.png; FY5-sovella-page-390-16.png (Jupiter a, the Io display chain and the table) and FY5-sovella-page-390-8.png (crane d, operator's explanation split, \overline{a}_\text{n}).
- The split paragraphs are intact at 390 px; no display maths is cut, clipped or overflowing, and the spacing between the new paragraphs is even.
- Not opened: the 1280 px captures and the other stages (the diff does not touch them).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
