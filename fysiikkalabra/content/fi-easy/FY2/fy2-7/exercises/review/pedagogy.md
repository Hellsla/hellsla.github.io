VERDICT: PASS
CONTENT-HASH: a023cb337412f5f0
SCOPE: delta added-exercise from fe05eb0dfc9bafde base 611fb7d5c174

## Blocking
(none)

## Polish
- exercises.json fy2-7-L1-09: "Muuta häviö jouleiksi" and "Anna vastaus megajouleina" pull in two directions; the instruction to use joules is not needed. Fix: drop the sentence "Muuta häviö jouleiksi." and keep "Etsi kilowattitunnin ja joulen muunnos ... Anna vastaus megajouleina."
- solutions.md fy2-7-L1-09, Järkevyys: "noin 20 * 4 = 80 MJ, hieman vähemmän" is a loose check; better "20 * 3,6 = 72 MJ, joka vastaa vastausta" or "20 * 4 = 80 on hieman liikaa, koska 3,6 < 4".

## Checked
- L1-09: situation, lookup instruction and question last; MAFY hint names only the table (teacher's decision); key 0,040 * 500 kWh * 3,6 MJ/kWh = 72 MJ; tolerance 4 % covers 3,6 and 3,60.
- L1-09 solution is staged (percentage to decimal, loss in kWh, conversion to MJ); level 1 fits; it practises loss percentages and units, as FY2-7 should.
- L2-09: the figure is needed (loss shares); its description gives 4 % and 9 % to a reader who cannot see it and does not state the difference.
- L2-09 key: 0,09 * 250 - 0,04 * 250 = 12,5 MWh; the solution checks with 5 % of 250 MWh.
- Level 2 fits (read two shares, two products, one difference); the question differs from the other tasks on the same figure, per the teacher's decision.
- Finnish clear in short sentences; case forms after numbers and units correct.
- Hash is the same at the start and the end (a023cb337412f5f0).
