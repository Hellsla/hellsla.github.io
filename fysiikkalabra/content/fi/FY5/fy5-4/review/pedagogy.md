VERDICT: FAIL
CONTENT-HASH: 29869917bd624813

## Blocking
- inquiry.json exp-1 (`min` 4, pred-2 `reveal.min` 4) — Prediction 2 asks how the car moves after grip fails (trajectory). The measurement table (an, F needed, F max, grip) at 5, 10, 15 and 20 m/s shows grip failing at 20 m/s but never shows the path. The intro asks the student to run 25 and 30 m/s only as an extra, not recorded, so pred-2 is revealed after min 4 without any observation of the motion. The experiment cannot refute "auto liukuu suoraan ulos" or "pysyy radalla". Fix: make the 25 and 30 m/s runs recorded rows (`min` 6, pred-2 `reveal.min` 6), or add a recorded observation measure for the path (e.g. "rata: kaartaa loivemmin / ulkoreunan yli").

## Polish
- lesson.md "Yleinen virhekäsitys" — one paragraph of about 150 words, over the 120-word limit. Split it at "Auto mukana kääntyvässä…", and the two-error ending ("Toinen virhe…") into its own paragraph.
- inquiry.json exp-1 intro — five instructions in one paragraph (set, record four values, then run two more and compare). Put the 25 and 30 m/s step as its own sentence/line, with what to look at in the picture.
- inquiry.json pred-1 correct feedback — it gives model values (3,0 kN, 12 kN) already inside the prediction box; fine after commitment, but the "11,8 kN" comparison previews exp-1's conclusion. Trim to the principle and leave the numbers to the experiment.
- Nyppylä/notko (own section, figure, Etsi virhe, Valitse, siirto, exit ticket) is a second topic beside the slot's core (kaarre, keskeisvoima). Workload is still about one lesson because the sim covers only the car on a flat curve; keep but do not add more.
- inquiry.json check-2 solution — computed 148,0 N, then answer "150 N" at two figures; say that the checker accepts 148 N so a student who rounds to three figures is not told they are wrong.

## Checked
- Path from fy5-3 (v = 2πr/T, direction of v) to a_n and ΣF = mv²/r is followable; the hook question (real or not ulospäin painava voima) is answered only after commitment.
- Goals covered: direction and size of a_n, Newton's 2nd law with force diagram; keskipakoisvoima handled as misconception, with the reference-frame caveat.
- Worked example has seven stages, one step each, symbolic before numeric, with a reasonableness check; not repeated by the exercises in the packet.
- Force-diagram skills: Etsi virhe, Valitse oikea voimakuvio (one error per distractor, feedback names it), draw-it-yourself check-3 with a model figure and criteria.
- Distractor feedback in pred-1/2/3, check-1 and the transfer task repairs the misconception, with mistakes values that are real slips.
- Exit ticket tests the core idea (real force direction, v² scaling, feeling light on a hill).
- Finnish and number+unit LaTeX read correctly; glossary terms (normaalikiihtyvyys, keskeisvoima, lähtökitka) used.
- The model section names its simplifications (no air drag, sliding grip simplified).
- Not examined: captures (none supplied in the packet), so figure legibility and the phone layout are left to the visual review and the 360 px tests.
