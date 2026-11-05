VERDICT: PASS
CONTENT-HASH: 1e3facb8514637c6
Round 2.

## Blocking

## Polish
- exercises.json:124 (L2-05 tolerance 0.015) — the page accepts at least 2 % (lesson.js), so 0,015 has no effect. The box accepts 307,7–320,3 lx, not the 309–319 lx the solution states. 322 lx is still only "Lähellä", so the intent holds. Either write "noin 308–320 lx" or leave the tolerance at the default.
- solutions.md L3-05 c (new sentence) — "polaroidut lasit puolittavat" holds for an ideal polariser. Add "ihanteelliset" (real lenses pass about 40 %).

## Checked
- Round-1 Blocking L3-04 Järkevyys resolved: the readings now differ from the calculated values in both directions (60°: 93 against 90 W/m²), and this is called measurement uncertainty. The model 120 sin²2θ gives 0/30/90/120/90/30/0.
- Round-1 Polish resolved: L3-04 c (the transmitted light is polarised along the transmission axis and part of it is absorbed); 12,5 % is called exact (1/8); L3-05 7,1 W/m² is limited by I₀ = 40 W/m²; L2-07 adds that 36,3° is the Brewster angle from inside the ethanol.
- One script recomputed every new answer: 98,70 W/m²; 55,59°; LSQ slope 313,9 lx with intercept 6,9 lx; 50,77°; 53,67°; 12,5 %; α_B 53,06°, Sun altitude 36,94°, 7,144 W/m², tinted glass 12 W/m², crossover 56,8°/33,2°. All agree with exercises.json and answers.py.
- L3-05 c addition: unpolarised light is halved against 30 %, so plain tint darkens the rest of the view more. Correct.
- L1-06 reordered: one correct option, it matches `answer`, and the feedback on each distractor is right.
- Hash the same at start and end.
