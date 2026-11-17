VERDICT: PASS
CONTENT-HASH: d47b4a3baee11581

## Blocking

## Polish
- exercises/solutions.md:275 (L2-09) — the solution says the curve passes "ruudukon viivan 8,7 kohdalla" at A = 100, but the drawn curve (semf) is at 8,684 MeV there, just under the line. The curve's own values give Q = 153,6 MeV, not 160. This is inside the 15 % tolerance and inside the ±20 MeV the solution states, so it is not an error — to be exact, say "noin 8,7".
- exercises/solutions.md:280 (L2-09) — the model splits 200 nucleons into exactly 2 × 100 with no free neutrons. That is a fair idealisation (C) because the task says "Oletetaan". You could add half a sentence saying that a real fission also releases 2–3 neutrons, so the student does not take the 2 × 100 split as a real reaction.

## Checked
- L2-09: own script with the figure generator's semf. ε(200) = 7,916 MeV and ε(100) = 8,684 MeV. Q from the curve is 153,6 MeV, Q from the grid readings 7,9 and 8,7 is 160 MeV, and readings ±0,05 MeV give 140–180 MeV. The stored 160 MeV with tolerance 0,15 (136–184 MeV) accepts every honest reading. answers.py gives 160,0.
- L2-09 physics: Q = A(ε_100 − ε_200) from the rise in binding energy is right (nucleon number conserved; prerequisite chapter). The check is right: U-236 → 2 × 118 on the same curve gives 218 MeV and a rise of 0,92 vs 0,77 MeV per nucleon, so the lighter nucleus releases less, as stated. The figure marks no values, so it does not give the answer away. The description gives the axes and the grid.
- L3-06: the figure's data are A0 = 720 kBq and T½ = 5,0 h (fy8-9 CHK_A0, CHK_T). t = T½·log2(1000) = 49,83 h, stored 50 h, tolerance 5 %. Readings of 4,9–5,1 h give 48,8–50,8 h, all inside the tolerance. The check values (180 kBq at 10 h, 45 kBq at 20 h) are right.
- L3-06: the extrapolation beyond 20 h is named and justified by the task's stated assumption. The safe level of 0,1 % is an assumption given in the task, not presented as a fact. The Pu-239 figure (24 100 a, about 2,40·10^5 a) agrees with L3-03 in answers.py.
- Rounding: 50 h has two significant figures, the same as the read 5,0 h. For 160 MeV the two figures are justified by the grid uncertainty.
- Both solutions are complete: symbolic first, conversions stated, reasonableness checks real.
- The captions of L2-05 and L3-04 lost "esimerkkiaineisto", but both task texts still say "taulukko, esimerkkiaineisto", so the data are still labelled. L3-06 says "Arvot ovat esimerkkiarvoja".
- Scope: binding energy and the decay law are both FY8 central contents. The notation (E_B/A, T_1/2, A0) matches the brief.
- The hash was identical at the start and the end.
