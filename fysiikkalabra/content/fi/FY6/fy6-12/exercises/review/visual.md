VERDICT: FAIL
CONTENT-HASH: 9f84f4124a537fa5

## Blocking
- [Major] fy6-12-L2-09 solution, Kaava and Sijoitus (12-17) — the fractions inside the root are written with `\frac` in inline maths, so KaTeX sets them in script size: $\sqrt{\tfrac{2eU}{m}}$ and the substitution with  \cdot 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 200\,\text{V}$ over $9{,}109 \cdot 10^{-31}\,\text{kg}$ are tiny, the exponents and units barely legible at 1280 px and worse on a phone (cramped fractions, the worst in the set) — the student must read the key formula and the numbers from here — write `\dfrac` inside the root in both lines (as the other solutions of the set, e.g. fy6-10 L2-09, do) so the root and fraction take the size of the line.
- [Major] fy6-12-L2-09 Kaava — "$\frac{1}{2}mv^2 = eU \;\Rightarrow\; v = \ldots$" is broken by the page after `⇒ v`, leaving "v" alone on one row and `= √…` below — a chain split at a meaningful boundary should end at the arrow — write the two steps as a chain "$\tfrac{1}{2}mv^2 = eU$, josta $v = \sqrt{\dfrac{2eU}{m}}$" (words, not ⇒, as in the other Kaava lines).

## Polish
- [Minor] fy6-12/ex-vgraph — the y axis has no tick at 0 while the x axis shows 0 once; fine, but note both axes use whole numbers only, which suits the 50 V steps.

## Checked
- review/shots/fy6-12-open-exercises-L2-1280-11.png and -12.png (stamp hash 9f84f4124a537fa5): task 12-17 (L2-09) with figure fy6-12/ex-vgraph (axes with quantity and unit, ticks at 50 V and 1 cm, straight line, nothing marked, description matches and gives no answer), answer row and the whole open solution.
- Finnish and structure of the task and solution are good (situation, then question; Järkevyys with energy and speed estimates). Only the two typographic findings above block.

## Scores
illustrations 5 · typography 2 · Finnish 5 · accessibility 4
