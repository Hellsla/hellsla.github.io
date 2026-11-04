VERDICT: PASS
CONTENT-HASH: c24ba5ae8d1c151a

## Blocking

## Polish
- exercises.json L1-06 — "Kahden auton nopeuksia kuvaavat (t,v)-kuvaajat on piirretty samaan koordinaatistoon" refers to a graph the student cannot see (no figure, and the solution's "Kuvaajan lukeminen" reads one). Either attach a figure (two lines crossing at 4,0 s) or write "Kuvittele kahden auton (t,v)-kuvaajat samassa koordinaatistossa: ne leikkaavat hetkellä t = 4,0 s."
- exercises.json L2-05 — kind says graph but the task asks only for a calculation from the first and last row; the solution tells the student to use end rows although FY4-1 teaches fitting a line to all points. Add "Piirrä pisteet ja sovita suorat" and let the solution read the speeds from the fitted lines (3,5 and −2,5 m/s), or drop "graph" from kind.
- exercises.json L2-07 — the question (the gap is greatest when the speeds are equal) is the lesson's own worked idea with new numbers (12 m/s and 2 m/s²); acceptable at level 2, but asking additionally "Milloin kärryt ovat taas samassa paikassa?" (12 s) would need the student to act on the result, not only recall it.
- exercises.json L1-07 — a start delay requires the substitution t − t0 and a rearranged equation, which is more than one step; it matches the plan ("lähtöviive") and the solution is clear, but it sits at the top of level 1.
- solutions.md L3-05 Mallivastaus — the effect of the limit is described only in words; one numeric line would close it: with the cap 11,1 m/s the car reaches it at 5,6 s and passes at about 9,3 s and 56 m, i.e. later and farther, as the text says.

## Checked
- Recomputed: L2-05 t = 7,0 s (3,48 and −2,52 m/s), L2-06 6,0 s (and the student's 2,0 s is the instant of the largest gap, 16 m, as the solution says), L2-07 36 m at 6,0 s (32 m at 4 s and 8 s), L3-04 t = 6,0 s, s = 147 m, d = 267 m, 29 m/s = 104 km/h, L3-05 x = 52 m at 8,74 s with 14,5 m/s = 52 km/h > 40 km/h; all match the answers in exercises.json.
- Plan (+3/+3/+2) met: v-intersection MC (misconception: same speed = meeting), meeting condition MC, start delay; two-runner table, error analysis (the plan's "nopeudet yhtä suuriksi"), (t,v) table of two carts; overtaking with oncoming car and a car-vs-cyclist model with data.
- Levels fit; the new L3 tasks are multi-step, in YO style (model, data, reasoning, limit check, plausibility), and neither repeats the worked example.
- Scope: only uniform and uniformly accelerated motion in one dimension and the meeting condition; no new theory (speed limit and road lengths are context only).
- Solutions are complete: principle, formula, units (km/h to m/s shown), substitution, significant figures, sanity check; L3-04 gives both the number and the argued decision.
- MC distractors are misconception-based and each feedback repairs rather than restates (L1-06, L1-08).
- Finnish and decimal commas read correctly; situation first, question last; multi-part a/b/c tasks name the part that goes into the answer box.
- Capture L3 1280 px (part 6): the long L3-04 calculation renders in separate blocks without clipping.
