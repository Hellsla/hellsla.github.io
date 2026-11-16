VERDICT: FAIL
CONTENT-HASH: 660e1899027dc8bc

## Blocking
- [Critical] inquiry.json `virhe` (Etsi virhe, the solution to examine; 352 and 1280 px) — three separate equations are merged into one chain: "qU = mv²v = √(qU/m) = 4,38 · 10⁵ m/sr = mv/qB = 4,57 cm"; the left sides $v$ and $r$ of rows 2 and 3 now trail the previous row as factors — broken notation: the block states things that are not equations, and the student cannot find the intended error — restore one equation per row, each with its own left side: `\begin{aligned} qU &= mv^2 \\ v &= \sqrt{\frac{qU}{m}} = 4{,}38 \cdot 10^{5}\,\text{m/s} \\ r &= \frac{mv}{qB} = 4{,}57\,\text{cm} \end{aligned}` (the earlier form fitted 352 px).

## Polish
- [Minor] `siirto` Sijoitus — the stacked numerator's second row reads "·20 000 V" with no space after the dot — `{} \cdot 20\,000\,\text{V}`.

## Checked
- batch delta review: content changed during the review (commit 7e4ba8466f), so the lesson was redone from a fresh preview/fy7-2.html: every re-broken chain rendered with all boxes open and inspected as crops at 352, 390 and 1280 px (own captures; the repository's captures predate this hash and keep hints and solutions closed at 390 px); nothing clipped; the other chains read well.
