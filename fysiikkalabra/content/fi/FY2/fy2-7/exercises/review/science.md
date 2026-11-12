VERDICT: PASS
CONTENT-HASH: 39e27a745e4dd913
SCOPE: delta added-exercise from d3675d9165793190 base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- solutions.md fy2-7-L1-09 Vastaus — "eri taulukoiden arvot poikkeavat hieman" does not fit here: 1 kWh = 3,6 MJ is exact by definition, as the lesson itself says (1000 W · 3600 s). Drop the clause; the tolerance can stay.
- solutions.md L1-09 Järkevyys — "20 · 4 = 80 MJ hieman pienennettynä" is a weak check. "20 kWh · 3,6 MJ/kWh: kymmenen kilowattituntia on 36 MJ, joten kaksikymmentä on 72 MJ" or a check back in kWh (72 MJ : 3,6 = 20 kWh) would be a real one.
- solutions.md fy2-7-L2-09 Vastaus — "kolme merkitsevää numeroa kuten … 250 MWh" holds only if the figure's 4 % and 9 % are read as exact labels. Say so ("kuvan prosentit ovat tarkkoja merkintöjä"), since a student who treats them as one-figure data and answers 13 MWh falls outside the 3 % tolerance.

## Checked
- Hash 39e27a745e4dd913 at the start and the end. I judged only the added L1-09 and L2-09.
- L1-09 recomputed: E_häviö = 0,040 · 500 kWh = 20 kWh, and 20 · 3,6 MJ = 72 MJ, the same as answers.py. The MAFY value 1 kWh = 3,6·10^6 J is VERIFIED in docs/mafy-arvot.tsv. The hint is in `hints`.
- L1-09 physics: the loss share is taken of the energy sent, as the lesson's rule says. 4 % is the lesson's Finnish grid loss, and two significant figures follow 4,0 %.
- L2-09 recomputed: 0,09 · 250 = 22,5 MWh and 0,04 · 250 = 10,0 MWh, so ΔE = 12,5 MWh, the same as answers.py. The check 5 % · 250 MWh agrees.
- L2-09 figure: the labels 96/4 % and 91/9 % and the widths (H = 80 in both, loss widths 3,2 and 7,2) are to scale and match the description. No energies are printed, so the answer is not given away. The wider district-heating loss arrow agrees with the Järkevyys.
- L2-09 solution: E_häviö = p E_lähtö and ΔE are written in symbols before substitution, the same input is stated for both networks, and the conversions are shown. It stays inside FY2 (simple loss percentages).
