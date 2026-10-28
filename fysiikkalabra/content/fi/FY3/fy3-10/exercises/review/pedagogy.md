VERDICT: FAIL
CONTENT-HASH: d343b548cba8c730

Delta review over the audit's PASS (1148bc79f3cd67b1): L2-04 (cold morning volume) replaced by a figure task fy3-10/pt-suorat (two p(T) lines); LaTeX conversion of units.

## Blocking
- solutions.md:89 — a tab character in "$0{,}0233$–$0{,}0247\,	ext{mol}$" (the "\t" of "\text" was eaten); the unit renders garbled. Fix: `\,\text{mol}`.
## Polish
- many quantities are still plain (0,250 m³, 0,460 mol, 0,400 mol, 101 kPa, 4,60 MPa, 10,0 bar, 7,0 bar, 1 bar = 100 kPa); the LaTeX conversion is incomplete.
- the task asks for the difference of two amounts; the solution's first line could say that n is found from each line separately first.
## Checked
- Figure needed: the text gives only V = 2,00 l; both lines' values come from the grid. Description lists the points, not n. At 400 K: pA = 100 kPa, pB = 60 kPa.
- n difference = 40 000 Pa · 0,00200 m³ / (8,31 · 400 K) = 0,02407 mol; answer 0,024 with 3 % (0,0233-0,0247) accepts rounded readings.
- 360 px capture: two coloured lines labelled A and B (letters, not colour alone), axes legible, grid 100 K and 10 kPa.
- Level L2 fits (read two series, two uses of the equation of state). Kuvaajan lukeminen present; Finnish clear.
