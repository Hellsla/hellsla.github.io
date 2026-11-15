VERDICT: PASS
CONTENT-HASH: 8da6f300bc0c21fc
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A `sovella/tasks.json` s7 d and e overlap slightly: d's conclusion (cars not driven in the same conditions) returns as e's improvement (same conditions for all cars). e's second criterion could ask only for repeats and several temperatures.
- A `inquiry.json`, `unit.md`: "sisäenergia" now carries the correct option and three feedbacks, but the fi-easy unit never glosses it. Add once at first use: "sisäenergia eli aineen hiukkasten energia".
- C `sovella/solutions.md` s7 b Järkevyys: "Se sopii silti oletuksen rajoitukseen." is opaque; e.g. "Tulos sopii siihen, että malli antaa liian suuren kulutuksen."

## Checked
- Every hunk of item 18 (figures.json, inquiry.json, unit.md, solutions s1/s3/s6, tasks s3 criterion): each carries P1 correctly and still reads as clear Finnish; no feedback or option gives its answer away; quoted misconceptions stay wrong.
- Recomputed: refrigerator share 1,08/1,54 = 70 %; s7 a −28,9 / −42,9 / −45,8 %, mean 39,2 %; b 16,67 and 26,88 kWh, factor 1,6, 600 N; c 27 K / 52 K, 15 kWh, density +16 %.
- s7 in full: source needed in a, d, e; parts progress read → model with a judged assumption → three-field explanation → confounding → limits; criteria observable, sums 3+4+4+2+2 = 15; nothing beyond FY1–FY8; no repeat of s1–s6.
- fi-easy against fi: same parts, points, criteria, headings and every number (script comparison); no step dropped.
- Rendered s7 from the preview at 360 px, all boxes open: no clipped maths or table; stem and table capture read.
