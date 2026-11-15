VERDICT: PASS
CONTENT-HASH: 320ca3bdcb7fd032
SCOPE: delta added-exercise from cbbbb7286332c468 base 6792c2c543a7

## Blocking

## Polish
- solutions.md fy8-2-L2-09 Kuvaajan lukeminen — "Sininen viiva on viiva, joka on lähimpänä arvoa 436 nm" is circular: the reading should come before the value. Also, "toinen desimaali on varma" overstates it, because ±3 nm gives ±0,02 eV — write "the blue line lies between 430 and 440 nm, about 4 nm before 440 nm" and "toinen desimaali voi muuttua yhdellä tai kahdella".
- solutions.md fy8-2-L3-06 Vastaus — the reason for two significant figures ("erotus on lähes yhtä suuri kuin lukuvirheen vaikutus kolmannessa numerossa") is hard to follow — say that subtracting two nearly equal energies loses the leading digits, and that ±2 nm in each reading moves ΔE by about ±0,02 eV.
- solutions.md fy8-2-L3-06 — the index $\text{g}$ for vihreä (green) is an English letter. It is fine because $\text{v}$ is taken by violetti, but a word index ($E_\text{vihreä}$, $E_\text{violetti}$) would read better.

## Checked
- I recomputed both answers in my own script with E = hc/λ (h = 6,626e-34, c = 2,998e8, e = 1,602e-19). L2-09: 436 nm gives 2,8440 eV, so 2,84 eV. L3-06: 3,0617 − 2,2711 = 0,7907 eV, so 0,79 eV. Both match answers.py (2.844029; 0.790664) and solutions.md ✓.
- The L3-06 physics is correct. In Hg, 404,7 nm (7³S₁→6³P₀) and 546,1 nm (7³S₁→6³P₂) share the upper level. With NIST levels, 5,4606 − 4,6668 = 0,794 eV, which agrees with the Järkevyys value 5,461 − 4,667 eV. E_v − E_g = E_a,g − E_a,v, and E_y cancels ✓.
- c) model answer: the two lines are alternative transitions, not a cascade. A sum would be 2E_y − E_a,v − E_a,g (5,33 eV), with E_y counted twice. This is correct and matches the task ✓.
- The 1570 nm remark is now conditional ("Jos atomi voisi siirtyä…"). hc/0,7907 eV = 1568 nm, which is infrared, so there is no visible line. There is no false claim that a 1570 nm line is emitted ✓.
- Tolerances: L2-09 ±0,03 eV covers readings from 434 to 441 nm (433 → 2,864 is just outside, which is fair at 10 nm ticks). L3-06 ±0,05 covers ±2–3 nm in both readings (403/548 → 0,814; 407/544 → 0,767) ✓.
- Figure lamp-spectrum: the scale is linear from 380 to 720 nm, with ticks every 10 nm and numbers every 50 nm. The lines are at 405, 436, 546, 577 and 579 nm, so the figure is to scale as it says. It gives every value both tasks need and does not show the answers. Its description gives the same values ✓.
- Scope: both tasks use only hf = E_y − E_a and λ = hc/ΔE from the brief, with its symbols E_y and E_a. Level 2 is a reading plus a conversion. Level 3 has two ideas: shared upper level and difference, not sum ✓.
- Hash 320ca3bdcb7fd032 at the start and the end.
