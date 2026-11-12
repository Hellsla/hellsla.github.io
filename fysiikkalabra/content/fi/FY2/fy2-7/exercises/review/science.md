VERDICT: PASS
CONTENT-HASH: d142b1dc9f41c8e8
SCOPE: delta added-exercise from d3675d9165793190 base 611fb7d5c174
Mode: delta
Round: 2

## Blocking

## Polish
- solutions.md fy2-7-L1-09 Järkevyys: "20 · 4 = 80 MJ hieman pienennettynä" is still a weak check. Checking back in kWh would be a real one: 72 MJ : 3,6 MJ/kWh = 20 kWh, which is 4 % of 500 kWh.
- solutions.md fy2-7-L2-09 Vastaus: three significant figures hold only if the figure's 4 % and 9 % are exact labels. One clause saying so would help: a student who reads them as one-figure data and answers 13 MWh falls outside the 3 % tolerance.

## Checked
- Hash d142b1dc9f41c8e8 at the start and the end. I judged only the added L1-09 and L2-09.
- L1-09 recomputed in my own script: 0,040 · 500 kWh = 20 kWh, and 20 · 3,6 MJ = 72 MJ. This matches answers.py and exercises.json (MJ, 0,04).
- L1-09 Vastaus now says the conversion 1 kWh = 3,6 MJ is exact, as it is by definition. This answers my round-1 point.
- L1-09 physics: the loss share is taken of the energy sent, as the lesson's rule says. Two significant figures follow 4,0 %. The MAFY hint is in `hints`.
- L2-09 recomputed: (0,09 − 0,04) · 250 MWh = 12,5 MWh. This matches answers.py and exercises.json (MWh, 0,03).
- L2-09 figure: the shares 96/4 % and 91/9 % are drawn to scale with the same input width, and the description agrees. No energies are printed, so the answer is not given away.
- L2-09 solution: E_häviö = p E_lähtö and ΔE are written in symbols before substitution. The check 5 % · 250 MWh is right, and it stays inside FY2 (simple loss percentages).
