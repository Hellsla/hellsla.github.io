VERDICT: PASS
CONTENT-HASH: 3c71dfde0dd50970
Mode: delta (new graph tasks fy8-12-L2-09 and L3-07 on fy8-12/tuntematon, unit 1/min -> min⁻¹, paragraph splits)

## Blocking
(none)

## Polish
- exercises/solutions.md:500, 502, 521–527: the new English solutions use decimal commas ($2{,}5$, $0{,}17678$, $141{,}42$, $5{,}6439$, $67{,}73$), but every other English solution uses a decimal point. Use decimal points in the en text. The numbers are right.
- exercises/solutions.md:502–504: Substitution, Answer and Reasonableness in L2-09 have no blank lines between them, unlike every other solution. Add the blank lines so each stage is its own block.
- figure fy8-12/tuntematon (shown on the en page): the axis label `\text{pulssia}\ /\ \text{min}` and the description are Finnish. For the visual and editorial reviewer: give the English page an English label.
- exercises/exercises.json:319 (carried over): the source URL still has "anti%2D5g". Use a plain hyphen.

## Checked
- Hash 3c71dfde0dd50970 (`--exercises --lang en`) at the start and the end.
- Figure data: lesson-answers.py has CHK_R0 = 800 and CHK_D = 12.0. The curve is 800·(1/2)^(d/12) on 0–48 mm with a 2 mm and 50/min grid, so 400 at 12 mm and 200 at 24 mm can be read off. The figure does not give either answer away.
- L2-09 recomputed: 800·0.5^2.5 = 141.42/min. answers.py gives 141.421 and the JSON answer is 141.4. The stated 140 lies within 0.99 % (tolerance 2 %). Two figures, limited by the read-off 12 mm, is justified.
- L3-07 recomputed: d = 12 mm·ln 50/ln 2 = 67.73 mm. answers.py gives 67.726 and the answer is 68 (tolerance 2 %, so 67.7 is also accepted). Rounding up is right: the shield must be at least this thick for an "at most" rate.
- L3-07 conclusion: at 48 mm the rate is 800/2⁴ = 50/min, above the allowed 16/min, so 48 mm is not enough. That is correct. The bracket check 1/32 < 1/50 < 1/64, giving 60–72 mm, is a real check. The rendered page (L3 shot 13) shows correct aligned rows.
- Physics of both tasks: the graph shows the net rate, so no background subtraction is needed, and the solutions say so. The attenuation law and the symbolic solving before substitution match the lesson's notation. d½ = 12 mm is a realistic value (like iron at 662 keV). Both tasks are inside FY8 scope.
- L1-07: only the unit changed (min⁻¹). Recomputed 1215/0.75 min − 90/min = 1530/min, which matches.
- L3-02, L2-01 and the other edits only change unit notation or split paragraphs. No number, sign or formula changed.
- L2-08 is unchanged: 14.48 µeV recomputed again.
