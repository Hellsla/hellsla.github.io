VERDICT: PASS
CONTENT-HASH: 80c94865e7e05d45

Round 2: the round-1 Blocking item and the changed tasks (L1-07, L1-08, L3-04, L3-05, the L2-05/L2-06 solutions) are checked against the whole set.

## Blocking
(none)

## Polish
- exercises.json:273 (L3-04): "lyijyisen kappaleen" gives away the metal that the task asks the student to infer, and the checked answer 11,3 is the lead value from the table. Write "metallikappaleen".
- exercises.json:104 (L1-08): with m = ρV it is now the same task type as L1-02 (g/cm³ · cm³ → g). Consider adding a unit change, for example asking for the answer in kg.
- solutions.md:185 (L3-04): "massa ja lukemat kolmella numerolla" leaves out the bubble's 2,0 ml. Better: "V = 10,0 cm³ is exact to 0,1 ml, like the readings".
- solutions.md:185 (L3-04): the only way given to detect the bubble is "lasin sivusta katsomalla". Also mention repeating the measurement.

## Checked
- Round-1 Blocking (L1-07, layering is not the same as mixing): resolved. The stem says "Öljy ei sekoitu veteen", and the C and D feedback and solutions.md:133 tie the order of the layers to liquids that do not mix. The round-1 Polish on L2-05, painaa → massa and L3-05 significant figures is fixed.
- One script recomputed the changed answers: L1-08 56,5 g. L3-04 V = 12,0 − 2,0 = 10,0 cm³ and ρ = 11,3 g/cm³; the student gets 9,42 g/cm³ (−16,7 %), nearest to copper. L3-05 V_Cu = 39,94 cm³ and V_Al = 60,06 cm³; the masses are 357,8 g and 162,2 g, so there is more Al by volume and more Cu by mass. All match answers.py and are within tolerance.
- L3-04 physics: the bubble adds to the displaced volume, the mass is unaffected and the error has the right sign. The task is now level 3 (data, error, a false identification).
- The L2-06 line reading and the check at 60 cm³ are correct. Notation follows the lesson.
