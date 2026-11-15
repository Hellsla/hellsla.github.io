VERDICT: PASS
CONTENT-HASH: 1042d3c37f4db574
SCOPE: delta added-exercise from cbbbb7286332c468 base 6792c2c543a7

## Blocking

## Polish
- solutions.md fy8-2-L3-06 Vastaus — "lukuvirhe näkyy jo kolmannessa numerossa" is ambiguous. A reading error of ±2 nm in each line moves ΔE by about ±0,02 eV (0,767–0,814), so it already reaches the second significant figure of 0,79, which is the third digit of 3,06 and 2,27 — say "energioiden toisessa desimaalissa" so that it is clear which numbers are meant.
- solutions.md fy8-2-L2-09 Kuvaajan lukeminen — "Sininen viiva on viiva, joka on lähimpänä arvoa 436 nm" still assumes the value it is meant to read. Describe the line first (between 430 and 440 nm, a little to the right of 430) and then give the reading 436 nm.

## Checked
- I recomputed in my own script with h = 6,626e-34, c = 2,998e8, e = 1,602e-19: hc = 1,9865e-25 J m; L2-09: 4,5561e-19 J = 2,8440 eV, so 2,84 eV. L3-06: 3,0617 − 2,2711 = 0,7907 eV, so 0,79 eV. These match answers.py (2.844029; 0.790664), the JSON and every intermediate value in solutions.md ✓.
- The split chains are correct. L2-09 gives hc as its own step, then J, then eV, and every unit carries through. In L3-06 a), hc/(λ·e) with e in J/eV gives eV directly ✓.
- Renamed indices: E_viol and E_vihr, and E_a,viol and E_a,vihr, are used consistently. ΔE = E_a,vihr − E_a,viol = E_viol − E_vihr has the right sign: the green line ends at the higher lower level (6³P₂, 5,461 eV) ✓.
- c) model answer: the two lines are alternative transitions, not a cascade. A sum (5,33 eV) would count E_y twice. This is correct ✓.
- Järkevyys: 5,461 − 4,667 = 0,794 eV agrees with NIST. The 1570 nm remark stays conditional (hc/0,7907 eV = 1568 nm) ✓.
- Tolerances are unchanged and still fair. L2-09: ±0,03 covers readings from 434 to 441 nm. L3-06: ±0,05 covers ±2 nm in both readings ✓.
- The figure is unchanged: it is to scale with lines at 405, 436 and 546 nm, and it does not give the answers away ✓.
- Hash 1042d3c37f4db574 at the start and the end.
