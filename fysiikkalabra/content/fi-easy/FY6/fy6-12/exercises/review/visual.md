VERDICT: FAIL
CONTENT-HASH: 02eaa1018019e06f

## Blocking
- [Major] fy6-12-L2-09 solutions.md, Kaava and Sijoitus — the fractions are written `\frac`, not `\dfrac`, so the build sets them in script size. In the capture (fy6-12-open-exercises-L2-1280-12.png) the key substitution $\sqrt{\frac{2 \cdot 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 200\,\text{V}}{9{,}109 \cdot 10^{-31}\,\text{kg}}}$ has a numerator and denominator of about half the text size inside the root, and the Kaava $v = \sqrt{\frac{2eU}{m}}$ is equally small; the `\;\Rightarrow\;` also breaks the chain into two rows. At 360 px it is harder still. Every other solution of the set uses `\dfrac` (21 times against these 2 `\frac`) and reads well. Why it matters: the substitution is the line the student checks their own work against. Fix: `**Kaava:** $\dfrac{1}{2}mv^2 = eU$, josta $v = \sqrt{\dfrac{2eU}{m}}$` and `\dfrac` in Sijoitus; use "josta" instead of `\Rightarrow`.

## Polish
- [Minor] fy6-12-L2-09 text — "Kuinka nopea elektroni on" is correct but "Kuinka suuri on elektronin nopeus" matches the other tasks' phrasing.

## Checked
- fy6-12-open-exercises-L2-1280-11.png (task 12-17: text, figure ex-vgraph with $50\,\text{V}$ and $1\,\text{cm}$ gridlines, labelled axes with units, straight line; answer not given away) and -12 (solution rows, Vastaus, Järkevyys); -8 and -9 for the neighbouring tasks.
- The figure and its description agree and give every value the task needs.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
