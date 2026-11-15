VERDICT: PASS
CONTENT-HASH: 7438c4b5df51d729
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: `sovella/solutions.md`, s5 common mistakes: "ainemäärä lasketaan kokonaispaineella 311 kPa ..., jolloin tulos on noin kaksi kolmasosaa oikeasta" is right for the molar mass (17,2 against 25,4 g/mol, 0,68) but the amount of substance itself becomes 1,5-fold; write "jolloin moolimassaksi tulee noin kaksi kolmasosaa oikeasta".
- C: s2 c check row: 485 - 175 - 233 = 77 kW is right for the rounded terms shown; the unrounded value is 77,6 kW (16 %, = 25 % of 310,5 kW), which the text around it still matches.
- A: s7 e says the cooling water is "noin 20 °C"; c's own check gives about 21 °C. Either is fine at two figures.

## Checked
- Both item 18 hunks against their tasks (s2 c numbers, s5 a with p0 + 210 kPa = 311 kPa).
- s7 recomputed in one script: eta = 0,3721; P2 = 2700 MW; Q2 = 64,8 GWh = 2,333e14 J; 62,8 % + 37,2 %; 38,4 + 64,8 = 103,2 GWh; 14,0 TWh a year; c·rho·V/t = 2,388e8 W/K; dT = 11,31 K; 47,4 kJ/kg; wrong 18,0 K; 563 K, 283 K, 280/563 = 0,50. All agree with tasks.json answers, solutions.md and answers.py; `practice.py check` OK (7 tasks, 110 points; s7 2+3+4+3+3).
- Physics of s7: steady state gives P1 = Ps + P2; the heat-engine argument in d is the right mechanism (Q2 is a condition of operation, not a loss; temperature ratio used qualitatively, within the unit's scope); c's upper-bound judgement and the salt remark are correct; e's low-temperature argument is correct. Rubric criteria match the parts and the solution.
