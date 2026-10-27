VERDICT: PASS
CONTENT-HASH: 55398c2af3d0f060
## Blocking
## Polish
- content/fi/FY1/fy1-7/lesson.md:216 — "erotuksessa on voi olla" has a stray "on" — write "erotuksessa voi olla".
- content/fi/FY1/fy1-7/solutions.md:L3-01 Vastaus — Annettu uses 2700 kg/m³ but the figure count cites 2,70 g/cm³ — cite the same form as Annettu (2,70·10³ kg/m³ or 2,70 g/cm³) so the three figures are visible.
## Checked
- Round-1 blocking 1 fixed: answers.py now has `fy1-7-inq-tarkistus-2` = 4.00 kg and `fy1-7-inq-virhe` = 675 g; all 16 keys recomputed independently and match the stated answers within tolerance.
- Round-1 blocking 2 fixed: both alumiini feedbacks now say each ratio is within 1 % of the mean 2,70 (deviations -0,66…+0,83 %): true.
- Polish fixes: "kuusitoista" (7870/500 = 15,7) right; L3-01 now 3,32 with three figures and a genuine bracket check (8100 < 8960 < 10 800); displacement sentence now "voi olla … koska kummankin lukeman virhe tulee mukaan" (correct); table sorted by density.
- metalli prompt now lists the table densities: values match lesson table; 8,96 → copper consistent.
- johtopäätös: new question and model answer (copper line steeper because its slope = density is larger) correct; new criterion matches the model.
- Worked example reasonableness rephrased ("7,9 kertaa vettä tiheämpää"): 7870/1000 = 7,87, estimate 15 kg correct.
- Unchanged parts (exercises, figures, predictions, neste, exit ticket) as verified in round 1; nothing in the diff touches them.
