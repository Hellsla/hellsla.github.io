VERDICT: PASS
CONTENT-HASH: 1286237925d4cb6c
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography from d41d82457f2f3aac base b5600a6

## Blocking
- none

## Polish
- solutions.md fy6-6-L3-01 Kaava — $U$ stands first for the rated voltage ($R = U^2 : P$) and then for the mains voltage ($U = U_{40} + U_{100}$); both are $230\,\text{V}$ here, so correct, but $U_\text{n}$ for the rated one (as in L3-05) would keep them apart.

## Checked
- Every rewritten Kaava block (L1-03, L1-05, L2-01…04, L2-05, L2-06, L2-07, L3-01…05, L2-09) starts from $P = UI$, $U = RI$, $E = Pt$, $Q = cm\Delta T$ or the series sum $U = U_1 + U_2$ and derives the formula the Sijoitus uses; every row is algebraically right and the last row is the one substituted into.
- Physics of the derivations: series ($U = (R_1 + R_2)I$, same current), parallel (same voltage, $P = P_1 + P_2$ by energy conservation), the heater's $E = Q$ with no change of state, $\Delta T = kP$ through the origin; all match the brief's Kaava.
- Recomputed in one script (my formulas vs answers.py vs exercises.json): 1,996 kW; 5,0 Ω; 7,83 A; 3,2 W; 15,8 V; 17,9 K; 20,4 W; 287,5 Ω; 12 Ω; 780 kJ; and from the Sijoitus lines 822 W and 152,5 W. All agree within tolerance.
- Paragraph splits in L2-06, L3-04, L3-05 change no number, sign or claim.
- exercises.json: only the esimerkkiaineisto marker removed from captions (teacher-approved); no data or answer changed.
- Content hash checked at start and end: unchanged.
