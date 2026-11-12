VERDICT: PASS
CONTENT-HASH: b8187c70d80f7adc
SCOPE: delta added-exercise from 648be0e8512e7cf8 base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- solutions.md fy2-5-L2-09 Kuvaajan lukeminen — "Vaaka-akselin yksikkö on MJ/kg" is right, but in the figure the unit is written as the heading "H (MJ/kg)" above the bars. "Kuvan otsikon mukaan yksikkö on MJ/kg" would match what the student sees (C).
- Earlier items outside this delta (L2-08 "lähes 40 MJ", L2-08 104 MJ significant figures, L1-06 distractor wording, L3-04/L3-05 same chain) are still open.

## Checked
- Hash b8187c70d80f7adc at the start and the end. I judged only the added L1-09 and L2-09.
- L1-09 recomputed: E = Hm = 26,7 MJ/kg · 0,50 kg = 13,35 MJ, the same as answers.py. H = 26,7 MJ/kg is the MAFY LHV value (docs/mafy-arvot.tsv, VERIFIED). The rounded 13 MJ is 2,6 % away, inside the 4 % tolerance. Other table values (26,8–27,0 MJ/kg) give 13,4–13,5 MJ, also accepted.
- L1-09: two significant figures follow m = 0,50 kg. The estimate 25 · 0,5 ≈ 12 MJ and "about two thirds of petrol's 43" (0,62) are real checks. The solution rightly says that ethanol is not in the lesson's table, and the hint sits in `hints`.
- L1-09 physics: an LHV for a heating value agrees with the lesson's "teholliset lämpöarvot". E = Hm is used with the mass in kg, as the lesson requires.
- L2-09 recomputed: E = 43 · 12 = 516 MJ and m_p = H_b m_b / H_p = 516 : 15 = 34,4 kg, the same as answers.py. The stated 34 kg is 1,2 % away, inside the 2 % tolerance.
- L2-09 figure: the bars print 43 (bensiini) and 15 (polttopuu), and the description says "polttopuu (ilmakuiva) 15". The lengths are to scale (6,8 units per MJ/kg, 48 : 10 ≈ 5 as said). The figure does not give the answer.
- L2-09 solution: m_p is solved symbolically from H_p m_p = H_b m_b before substitution. No conversions are needed (as it says), two significant figures follow from 12 kg, and the ratio check 43 : 15 ≈ 2,9 → about 36 kg is a real check.
- Both tasks stay inside FY2 (E = Hm, comparing fuels) and use the lesson's symbols H, m, E.
