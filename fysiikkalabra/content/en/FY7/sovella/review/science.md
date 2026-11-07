VERDICT: PASS
CONTENT-HASH: baab2c940725a6d9
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the FY7 editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- fy7-s3: 6.0 MW now the power fed into the line, simplified two-wire model stated. Recomputed: R = 2.82e-8 * 5.0e4 : 150e-6 = 9.40 ohm, I = 6.0 MW : 20 kV = 300 A, P_h = 9.40 * 300^2 = 846 kW = 14.1 % of fed power, mine receives 6.0 - 0.85 = 5.15, about 5.2 MW (solution right). Answer split into Ph 846 kW / rel 14.1 % matches answers.py keys fy7-s3-a-Ph and fy7-s3-a-rel. mu0 approx 4 pi 10^-7 in s3 e text and solution (2019 SI) correct. Language checked: en.
- Round 2: s3 a task text, criterion detail and answer now say "johtoon syötetystä tehosta" / "power fed into the line", consistent with the given data (previous polish resolved); numbers unchanged (846 kW, 14.1 %).
