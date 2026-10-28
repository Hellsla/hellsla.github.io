VERDICT: DONE

Round 1 fix; `check_lesson.py fy2-3` ok on every line.

- lesson.md: price cited as Tilastokeskus 2025, about 18 snt/kWh total price, with 20 snt/kWh kept as a labelled round example price; 80 W conversion by substitution (80 · 10^-3 kW); every number with a unit in LaTeX; standby "alle wattista muutamaan wattiin"; Olkiluoto 3 (1600 MW, TVO) line for power-plant scale; both figures now show the television as 80 W.
- figures.py: television 80 W (bars, graph line, aria-labels).
- inquiry.json: mittari headers shortened (keitin, tosteri, televisio; kJ said in the text; television 1,6 / 3,2 / 4,8 kJ); ennuste-1 now asks for the time in orders of magnitude (no giveaway); aika drops the 15 h row, student computes t = E : P then checks the table; siirto solution converted by substitution; "mittarin lukema kasvaa"; contribution says energy in kWh is power times time; units in LaTeX throughout.
- exit-ticket.json: units in LaTeX, "jouleina", answer 3 rounded to 44 and 37 kWh.
- lesson-answers.py: television 80 W, Olkiluoto line.
