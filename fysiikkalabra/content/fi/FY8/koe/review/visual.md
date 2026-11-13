VERDICT: FAIL
CONTENT-HASH: 54f883462cec865c

## Blocking
- [Major] solutions.md k2 a, figure fy8-k2-graph (fig-3) — the text and the figure say each point has a vertical error bar ±0,05 V, but the bars are 9 px long inside markers of r 5,5 (11 px) and are completely hidden. k2 c reads the bars off the figure (points (4,80; 1,96), (6,97; 2,89)), so the student cannot check it. — Fix: draw the bars longer than the marker with caps (enlarge the y-scale or widen the markers' gap), or state under the figure that the bars are smaller than the markers.

## Polish
- [Minor] k5 b Muunnokset (capture 390-36/37) — the chain E_2−E_1 = −3,4 eV+13,6 eV = 10,2 eV = 1,634·10^-18 J is split: the first two rows are in a white box, the last row is outside it and aligned differently. The same happens in k5 c and k7 d (a boxed fraction and loose rows). Fix in mathlayout so one chain is one block.
- [Minor] k2 b Järkevyys (390-14) — "yksikkö V s" and "J s" read as plain-weight text next to the maths; check they are `\text` with a thin space. "2-3 %" uses a hyphen: write "2–3 %" in maths.
- [Minor] k4 a Vastaus/Järkevyys — "28,30 MeV − 2,22 MeV / −8,48 MeV" breaks the line before the minus sign, which reads as a sign; keep the chain together or write it as a subtraction in parentheses.
- [Minor] k7 c Sijoitus (390-55/56) — a mixture of words and chain ("Ensin c² = …; Sitten E = … ; Aallonpituudelle hc = …") is hard to follow; setting each step on its own line would help. The E in "λ = hc/E" gets cut at the end of a capture (a screenshot seam, not a page defect).
- [Minor] k1 b (390-7) — "Sijoitus (omalla rivillään):" is a stray label and reads as an instruction to the writer; replace it with "Sijoitus:".

## Checked
- Contact sheets 1–5. Page captures 390-7, 13, 14, 15, 22, 28, 29, 30, 35, 36, 37, 38, 55, 56, 57 (every Sijoitus chain of k1 b, k2 b, k3 c, k4 a–c, k5 a–c, k7 c at 390 px). Sample at 1280 px: page-1280-30. Figures fig-1, 3, 6 and 18 (the four graphs, enlarged). The other fig-N captures are inline icons of 28–100 px (no figures). Stamp hash matches the packet hash.
- The graphs have quantities and units, honest scales, data markers apart from the lines, and the extrapolation dashed (k2). No chain is clipped or shrunk, and the decimal commas, \cdot and units are consistent. Not rechecked: the other tasks' text and k6.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
