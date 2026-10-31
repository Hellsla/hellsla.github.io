VERDICT: FAIL
CONTENT-HASH: 6e882df51e114bbe

## Blocking
- [Major] exercises.json fy1-2-L1-01, L2-01, L2-02, L3-02, L3-03 (and tarkistus-2 in inquiry.json) — numbers with units are plain text ("82 µm", "3,2 GHz", "5,0 ms", "2,0 µm", "1,0 mm", "1920 px", "30,07 AU", "145 AU:n", "0,387 AU:n"), while the same sentence has maths ("$1\,\text{GHz} = 10^{9}\,\text{Hz}$") — house rule §1 makes a number with its unit maths, and the page shows two typefaces and decimal point/units unstyled side by side (screenshots L1 #1, L2 #1, L3 #2) — write each as `$82\,\mu\text{m}$`, `$3{,}2\,\text{GHz}$`, `$145\,\text{AU}$:n` etc.

## Polish
- [Minor] solutions.md L2-01 Muunnokset — "$3{,}2\cdot10^{9}\,\text{1/s}$" renders as "10^9 1/s", easily read as an exponent "9 1/s" — use `\tfrac{1}{\text{s}}` or write Hz.
- [Minor] fy1-2/ruler-read (L1-04) — the "cm" label sits alone far below the scale right — move it beside the 15 or under the numbers.
- [Minor] solutions.md L1-04 "Kuvaajan lukeminen" — the figure is a ruler, not a graph — use "Lukeminen kuvasta".

## Checked
- open-exercises-1280-1, -3 (L1 tasks 1-4 and ruler figure), L2-1280-1, L3-1280-2
- exercises.json and solutions.md read in full; ruler-read description matches the drawn ends (about 2,0 cm and 13,6 cm) and does not give the answer

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
