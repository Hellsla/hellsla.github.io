VERDICT: PASS
CONTENT-HASH: 4e821e3ca31d2886
ROUND: 2

## Blocking

## Polish
- solutions.md:190 (L3-05 Vastaus) — the new rounding reason, which is my round-1 wording, says "kahden lähes yhtä suuren resistanssin erotus". That is inaccurate, because 2,76 Ω and 2,00 Ω differ by 38 %. The real reason is that the subtraction keeps two decimals of the three-figure values: $R_{80} - R_{20} = 2{,}76\,\Omega - 2{,}00\,\Omega = 0{,}76\,\Omega$, which has two significant figures. Write "kaksi merkitsevää numeroa, koska erotuksessa $2{,}76\,\Omega - 2{,}00\,\Omega = 0{,}76\,\Omega$ jää kaksi merkitsevää numeroa".
- exercises.json L3-04 (C at 1,0 V: 0,1 mA) — a visible power LED hardly conducts at 1,0 V. The data are labelled as example data, so this is acceptable. A value of 0,0 mA at 1,0 V would be more realistic, and a) and the solution would then start C from 1,5 V.

## Checked
- Hash 4e821e3ca31d2886 at start and end. Counts 8/7/5.
- Round-1 Blocking resolved. L3-04 now includes C at 1,0 V : 0,1 mA = 10 kΩ, and the Vastaus says "10 kΩ:sta 31 Ω:iin". L3-05 no longer cites 0,362 A as two significant figures.
- Round-1 Polish resolved: L2-05 justifies 150 Ω by ΔR ≈ 2 Ω and uses the words "pisteiden hajonnasta saatu arvio"; the L2-06 "Resistanssien suhteen" typo is fixed; the self-contradiction in the last sentence of L1-06 is fixed; L3-04 now says "teholedi", so 98 mA at 3,0 V is realistic.
- I recomputed every answer from answers.py in one script, with my own formulas for the new tasks: L1-08 0,30 A; L2-05 slope of the least-squares fit through the origin 149,97 → 150 Ω; L2-06 1,976 → 2,0; L2-07 4,934 → 4,9 Ω, and the new claim "fit through the origin gives 4,9 Ω" holds (4,926 Ω); L3-04 600 Ω and the ratio 600 : 26,3 = 23; L3-05 38,1 %.
- L1-06 and L1-07, with reworded distractors: there is still exactly one correct option, and resistivity and resistance are kept apart.
- L1-08: the added rule "R ∝ l, joten I ∝ 1 : l" holds at constant voltage and temperature, and the task states both.
