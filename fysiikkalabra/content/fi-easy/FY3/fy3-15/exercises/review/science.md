VERDICT: FAIL
CONTENT-HASH: b7d7e4725f7e9cf3
Round: 2
Mode: delta

## Blocking
- exercises/solutions.md:271–276 (fy3-15-L3-04, Kaava) — the asked quantity is the difference P_o,A − P_o,B, but the new block stops at P_o,B; the old Kaava ended with "Erotus on P_o,A − P_o,B …", so the change removed the symbolic solution of what is asked (rule 7 step 3) — add the final row `\Delta P_\text{o} &= P_{\text{o},\text{A}} - P_{\text{o},\text{B}}` (numbers and Sijoitus unchanged).

## Polish
- exercises/solutions.md:47 (L1-04) — the Kaava's P_o means the stage's input power (P_o = P_1, defined after the block), while the task's figure gives P_o = 400 MW for the fuel power; the row P_o − P_a = P_1 − P_2 reads as 400 − … — write the stage balance directly as P_1 = P_2 + P_h, P_h = P_1 − P_2.
- exercises/solutions.md:268 (L3-04 Annettu) — "kaukolämpöteho 0,560 P_o,B" names the CHP plant's fuel power P_o,B, but the Kaava uses P_o,CHP for it and P_o,B for the plant plus boiler — use P_o,CHP in Annettu (preexisting).

## Checked
- Every other changed Kaava starts from P_1 = η_1 P_o … or η = P_s/P_o, P_o = P_a + P_h, Q = cmΔT, and solves symbolically; every row algebraically right.
- Chain efficiency η = P_3/P_o = η_1η_2η_3 (L1-01, L2-01, L2-07) right; recomputed 90.16 %, 108.66 MW, 36.6 %.
- L2-03: m = P_s t/(ηH) = 166.7 t; L3-02: m = E/(ηH) = 13.64 kt right.
- L2-04, L3-05, L1-09: P = c q_m ΔT from Q = cmΔT and P = Q/t right.
- L3-03: E = Q_1/(η_siirto η_voimala ε) = 87.7 kWh right.
- L3-04 recomputed: 472.22 − 340.28 = 131.9 MW, matches answers.py.
- Hash identical at start and end.
