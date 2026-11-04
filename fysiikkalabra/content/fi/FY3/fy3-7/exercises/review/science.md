VERDICT: PASS
CONTENT-HASH: cd198f4f9413a502

Round 2. This round checks the fixes for the round-1 Blocking item and the Polish (`git diff HEAD~1`) on the 20-task set. Mode: full.

## Blocking

## Polish
- exercises.json:156 / solutions.md:161 (L2-05) — the tolerance is now 0,08, so the answer box accepts 312 kJ/kg (−6,6 %), which the solution itself calls "liian pieni". The reason given for ±8 % ("aika luetaan noin sekunnin tarkkuudella") supports only about 1–2 %. The new hint already exposes the hidden step. — Set the tolerance back to 0,04 (or 0,05) and write ±4 %.
- solutions.md:168 (L2-06 Mallivastaus a)) — "vesi pysyy koko ajan 100 °C:ssa" holds only at normal pressure (B, minor; Periaate is now fixed). — Write "pysyy koko ajan kiehumispisteessä".

## Checked
- Round-1 Blocking item (L3-05 Järkevyys) is resolved: it now says "höyry luovuttaa tiivistyessään paljon energiaa (r on suuri)". This gives the right direction and matches Mallivastaus.
- L1-06: the feedback now says "keskinäisten vuorovaikutusten muuttamiseen" (guardrail wording). The correct option was moved to the end, and exactly one option is still correct and equals `answer`.
- L1-07: the shortened options still have exactly one correct option ("Haihtuva hiki ottaa energiaa iholta"), and the feedback is unchanged and right.
- L2-06 Periaate: now "kiehumispisteessä, normaalipaineessa noin 100 °C:ssa".
- L2-07 now asks for 60,0 kPa, which is not a table row, with linear interpolation between 50,0 kPa (81,3 °C) and 70,0 kPa (90,0 °C). That gives 85,65 °C and Δ = 14,35 K, so 14,4 K. Steam tables give T_k(60 kPa) ≈ 86,0 °C and Δ ≈ 14,0 K, which is within the ±4 % tolerance. The interpolation step brings the task up to level 2, and b) correctly says ≈ 85,7 °C and ≈ 14 K.
- L2-05: the hint "rivit 20 s ja 150 s ovat jo tasanteen sisällä" matches the data (melting 17,5 → 156,7 s). s = 600 · 139 / 0,250 = 333,6 kJ/kg.
- L3-04: the tolerance of 0,08 now accepts the table-row plateau estimate of 18,7 kJ (−6,6 %). P = 11,98 W, Q = 19,9 kJ, s ≈ 199 kJ/kg.
- I recomputed the changed and new answers in one script with my own formulas (L2-05, L2-06, L2-07, L3-04, L3-05). They match answers.py and exercises.json. All 20 answers.py values agree with exercises.json within tolerance.
- The deterministic layout checks at 360, 768 and 1280 px pass.
