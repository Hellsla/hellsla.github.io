VERDICT: PASS
CONTENT-HASH: c94e399e0c9db48d
SCOPE: delta added-exercise from 0d804621ffb859e2 base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- solutions.md fy2-8-L1-09 Järkevyys — "noin 2,6-kertainen massa … tyypillistä hiilivedyille" names the cause but checks nothing. A real check fits in one clause: for methane CH₄ → CO₂ the mass ratio is 44 : 16 ≈ 2,8, close to 2,6.
- solutions.md fy2-8-L2-09 Vastaus — "luettu kahden luvun erotuksena" is an unclear reason for the figures. Say instead that the factors 820 and 490 are rounded medians with two significant figures, so the difference is known to about two figures.
- Earlier item outside this delta (L2-08, the 2020–2021 interval wording) is still open.

## Checked
- Hash c94e399e0c9db48d at the start and the end. I judged only the added L1-09 and L2-09. As the teacher decided, the unnamed source of the 55 g/MJ factor is not reported.
- L1-09 recomputed: E = Hm = 47 MJ/kg · 2,0 kg = 94 MJ and m_CO2 = eE = 55 g/MJ · 94 MJ = 5170 g = 5,17 kg, the same as answers.py; the stated 5,2 kg is 0,6 % away. H = 47 MJ/kg is the MAFY value (docs/mafy-arvot.tsv, VERIFIED). The other chapter's 48 MJ/kg gives 5,28 kg (+2,1 %), also inside the 4 % tolerance.
- L1-09 physics: 55 g/MJ is a realistic combustion factor for natural gas (IPCC default about 56). Both formulas are written in symbols, and m_CO2 is kept apart from the fuel mass m. The task says "palamisen päästökerroin", which is right for combustion CO₂ only. The hint is in `hints`.
- L2-09 recomputed: Δm = (e_kivihiili − e_kaasu)E = 330 g/kWh · 20 000 kWh = 6,6 · 10^6 g = 6,6 t, the same as answers.py. The tolerance of 3 % fits.
- L2-09 check: 16,4 t − 9,8 t = 6,6 t, which is 40,2 % of coal's emission; both statements are right.
- L2-09 figure: the bars print 820 and 490 at their ends, the unit heading is g CO₂-ekv./kWh, and the description agrees. No difference is shown, so the answer is not given away. "Elinkaaren" factors are used for electricity, as the lesson does.
- Both tasks use the lesson's m = e · E. Scope is inside FY2 (emissions, comparing production methods).
