VERDICT: PASS
CONTENT-HASH: 7fda86c22f2d15e3
SCOPE: delta numbers,typography,wording,md-paragraphs from df6cf372cf645c1d base 5b3ca4f

## Blocking
- none

## Polish
- none

## Checked
- Full diff `git diff 5b3ca4f -- content/en/FY6/fy6-7/exercises lessons/FY6/fy6-7` judged.
- Formula blocks now start from the basic equations: E_i = P_i t_i, E = ΣE_i (washer, three-phase cost task); P = UI, E = Pt, E = UIt; E = Pt, K = aE, K = aPt; ΔE = E_1 − E_2 = (P_1 − P_2)t; E_2 = E_1 so t_2 = P_1t_1/P_2; K = K_base + aE solved for E; U = RI, I = U/R, P = UI, E = UIt (resistor); E_day,i = P_i t_i, ΣE_day,i, E_year = 365·E_day,tot. Every row is a correct step and the last row is the one substituted into.
- L3-04: K = ΣaE, a_avg = K/E_tot, E_heater = Pt, K_high = a_high E_heater, K_low = a_low E_heater, S = K_high − K_low = E_heater(a_high − a_low). Correct; no false row remains.
- Recomputed touched numbers: washer 2.0·0.25 + 0.2·1.0 + 0.4·0.25 = 0.80 kWh; first period 1.2·3.9 = 4.68 c; a_avg = 267.44/19.0 = 14.08 c/kWh; E_heater = 6.0 kWh, S = 6.0·15.5 = 93.0 c; refrigerator 344 kWh/8760 h = 39.27 W, k ≈ 0.39; 0.0393 kW·8760 h ≈ 344 kWh; average power 2.01 kWh/24 h ≈ 84 W. All agree.
- lesson-answers.py kertaus rows: 230·0.43 = 98.9 W ≈ 99 W, 230/0.43 = 535 ≈ 530 (2 s.f.); both agree with inquiry.json (en and fi) option and feedback values.
- Paragraph splits change no physics and no order of reasoning.
- Content hash checked at the start and at the end.
