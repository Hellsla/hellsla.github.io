VERDICT: FAIL
CONTENT-HASH: 71f841a0fe71562f

## Blocking
- [Major] exercises.json L1-01, L1-03, L1-04, L2-01, L2-02, L2-04, L3-01, L3-02 — numbers with units in the task texts are plain text ("720 N", "0,30 m²", "98,5 kPa", "0,0025 m²", "350 kPa", "0,85 bar", "380 cm²") while other values in the same sentence are KaTeX ("1000 kg/m³", "4,0 m"); mixed typefaces in one sentence (L2-02: "ylipaineen 350 kPa ... 1000 kg/m³"); breaks the 2026-10-28 rule — inconsistent notation within the set — set every value with unit as inline maths ($720\,\text{N}$, $0{,}30\,\text{m}^2$, $350\,\text{kPa}$, $0{,}85\,\text{bar}$).

## Polish
- [Minor] L2-04 text "(1 bar = 100 kPa)" plain; same fix as above.
- [Minor] two-liquids graph — sound: axes, units, 1 m / 25 kPa grid, points at x=5 distinct from lines; the A and B colours are blue and orange, distinguishable also by the end labels.
- [Minor] Solutions — "Vastaus" rows consistent; L3-03 "19,0 kPa" vs task answer 19: fine.

## Checked
- open-exercises-1280 L1-1, L2-2, L2-3 (two-liquids figure), L3-3 and the solution cards (Annettu to Järkevyys), solutions.md and exercises.json text read in full; the two-liquids description matches the figure and does not give the answer.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
