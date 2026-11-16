VERDICT: FAIL
CONTENT-HASH: 4a04b9c36c93e1fb

## Blocking
- [Critical] inquiry.json `virhe` (Etsi virhe, the solution to examine; 352 and 1280 px) — the unit conversion and the calculation are merged into one chain: "A = 6,0 cm² = 0,060 m²|e| = NΔB·A/Δt = … = 72 V"; $|e|$ trails the conversion row as a factor and the chain claims A = 72 V — broken notation in the very block whose error the student must find — restore two equations: `\begin{aligned} A &= 6{,}0\,\text{cm}^2 = 0{,}060\,\text{m}^2 \\ |e| &= \frac{N \Delta B \cdot A}{\Delta t} \\ &= \frac{200 \cdot 0{,}30\,\text{T} \cdot 0{,}060\,\text{m}^2}{0{,}050\,\text{s}} \\ &= 72\,\text{V} \end{aligned}`.
- [Critical] inquiry.json `johtopaatos`, model answer (own capture at 352 px, model answer shown) — the chain put back inline by the latest edit, "−NΔΦ = −10 · 2,0 mWb = −20 mWb", does not wrap: the line ends at "2,0 mWb =" and the result "−20 mWb," is cut off at the card edge — the value the sentence is about cannot be read on a phone — let the shared chain layout break it before the second `=` (or keep the two-row form with its comma inside the formula, which fitted).

## Polish

## Checked
- batch delta review: content changed during the review (commit 7e4ba8466f), so the lesson was redone from a fresh preview/fy7-5.html: every re-broken chain rendered with all boxes open and inspected as crops at 352, 390 and 1280 px (own captures; the repository's captures predate this hash and keep hints and solutions closed at 390 px); nothing clipped; the other chains read well.
