VERDICT: PASS
CONTENT-HASH: 5376a4178071797a
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography from af0ac97658e02be2 base b5600a6

## Blocking

## Polish
- content/fi/FY6/fy6-6/exercises/solutions.md:96 (fy6-6-L3-01) — the chain uses $U$ both for the general $P = U^2 : R$ (lamp at its rated voltage) and for the series sum $U = U_{40} + U_{100}$; the values coincide (both 230 V), so nothing is wrong, but $U_\text{n}$ in the rating rows would keep the two meanings apart.

## Checked
- Hash 5376a4178071797a at start and end; delta judged: the Kaava steps of 17 solutions rewritten to start from $P = UI$, $U = RI$, $E = Pt$, $Q = cm\Delta T$, the loop sum $U = U_1 + U_2$ or $P = P_1 + P_2$; paragraph splits; captions without "(esimerkkiaineisto)".
- Every new chain is a correct derivation and ends in the form the unchanged Sijoitus substitutes into (L1-03, L1-05, L2-01…07, L2-09, L3-01…05, L1-08).
- Conditions kept: L2-04 $E = Q$ rests on the Periaate's "koko energia lämmittää vettä eikä olomuoto muutu"; L3-04 $P' = U'^2 : R$ on constant resistance, stated in the Periaate.
- Series chains (L2-02, L3-01, L3-05) apply the voltage law with the same current; parallel L3-03 uses energy conservation $P = P_1 + P_2$; all as the brief teaches.
- One script recomputed every number on the touched solutions: 1996 W, 5,0 Ω, 7,83 A, 3,2 W, 15,8 V, 17,9 K, 20,4 W, 287,5 Ω, 12 Ω, 7,2 W, 12,1 K/W, 172 %, 3,0 W, 822 W, 152,5 W / 50,9 W, 780 kJ: all agree; answers.py unchanged.
- Split paragraphs (L2-06, L3-04, L3-05): same sentences, numbers and order.
- Caption change: removing the data-origin marker follows the teacher's rule (no provenance badge on example data) and leaves no data presented as measured that the tasks' texts contradict.
