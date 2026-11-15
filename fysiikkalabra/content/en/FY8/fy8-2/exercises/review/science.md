VERDICT: PASS
CONTENT-HASH: aee274b8dfc29f65
SCOPE: delta added-exercise from d4cac7da6f13b625 base f6ae5d507c79

## Blocking

## Polish
- solutions.md fy8-2-L3-06 Answer — "a reading error of a few nanometres already affects the third figure" is ambiguous. ±2 nm in each line moves ΔE by about ±0.02 eV (0.767–0.814), so it reaches the second significant figure of 0.79, which is the second decimal of 3.06 and 2.27 — name which numbers are meant.
- solutions.md fy8-2-L2-09 Reading the graph — "The blue line is the one closest to 436 nm" assumes the value it is meant to read. Describe the line's position first (between 430 and 440 nm) and then give 436 nm.

## Checked
- I recomputed in my own script (h = 6.626e-34, c = 2.998e8, e = 1.602e-19): hc = 1.9865e-25 J m. L2-09: 4.5561e-19 J = 2.8440 eV, so 2.84 eV. L3-06: 3.0617 − 2.2711 = 0.7907 eV, so 0.79 eV. These match answers.py (2.844029; 0.790664), the JSON and every intermediate value ✓.
- The split chains are correct. L2-09 computes hc as its own step, then J, then eV. In L3-06 a), hc/(λ·e) with e in J/eV gives eV directly, and the units carry through ✓.
- Renamed indices: E_viol and E_green, E_u, and E_l,viol and E_l,green are consistent. ΔE = E_l,green − E_l,viol = E_viol − E_green has the right sign (the green line ends at 6³P₂, 5.461 eV, which is above 6³P₀) ✓.
- c) model answer: the two lines are alternative transitions, not a cascade. A sum (5.33 eV) would count E_u twice. This is correct ✓.
- Reasonableness: 5.461 − 4.667 = 0.794 eV agrees with NIST. The 1570 nm remark is conditional (hc/0.7907 eV = 1568 nm) ✓.
- Tolerances are unchanged and fair. L2-09: ±0.03 covers readings from 434 to 441 nm. L3-06: ±0.05 covers ±2 nm in both readings ✓.
- The figure is unchanged: it is to scale (lines at 405, 436 and 546 nm) and does not give the answers away ✓.
- The numbers and physics are the same as in the Finnish version ✓.
- Hash aee274b8dfc29f65 at the start and the end.
