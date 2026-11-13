VERDICT: FAIL
CONTENT-HASH: 8edcd16166667112
Round 1
Mode: delta (added exercise fy6-12-L2-09, shown as 12-17)

## Blocking
- [Major] fy6-12-L2-09 solutions.md, Formula and Substitution — both fractions are written with a bare `\frac` in an inline chain, so KaTeX sets them in script size: in the Substitution row `\frac{2 \cdot 1.602 \cdot 10^{-19}\,\text{C} \cdot 200\,\text{V}}{9.109 \cdot 10^{-31}\,\text{kg}}` under the root is about 9 px with the exponents and units barely legible (capture L2-1280-12), and the Formula row is set small too — clearly poor mathematical readability of the central step — the other solutions of the set use `\dfrac` for such fractions — write `\dfrac` in both places, so `v = \sqrt{\dfrac{2eU}{m}}` and the root's content is full size.
- [Major] fy6-12-L2-09 Formula — `\frac{1}{2}mv^2 = eU \;\Rightarrow\; v = \sqrt{\ldots}` in one chain is broken by the layout into "½mv² = eU ⇒ v" and then "= √…", so a row ends in a bare "v" and the next begins with "=" — the reader sees an unfinished equation — write the principle `\tfrac{1}{2}mv^2 = eU` and then, as a second item, "so `v = \sqrt{\dfrac{2eU}{m}}`" (as in the Formula line of 12-16 style), with no `\Rightarrow` inside the chain.

## Polish
- [Minor] fy6-12/ex-vgraph — the starting point x = 1.0 cm has a tick but no marker, and the "0" origin label sits below-left of the axis crossing; fine to read, no change required.

## Checked
- fy6-12-open-exercises-L2-1280-11.png (task 12-17 statement, graph with V (V) and x (cm) axes, ticks every 50 V and 1 cm, straight line, description consistent, answer chip) and -12.png (full solution).
- Graph is clear and does not give the potential difference away; statement reads well, units in LaTeX, decimal point in en. Faults are only in the solution's maths set-up above.

## Scores
illustrations 4 · typography 2 · English 4 · accessibility 4
