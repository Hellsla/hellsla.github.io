VERDICT: PASS
CONTENT-HASH: 3a034727967b1659

## Blocking

## Polish
- inquiry.json exp-1 (pred-2 `reveal.min` 4) — the table rows 5–20 m/s do not show pred-2's refutation: at 20 m/s the radius is v²/(μ₀g) = 51 m against 50 m, so the car looks almost on the track. The clear cases (25 and 30 m/s) are only asked for in the intro, not recorded, so pred-2 can be revealed without them. Fix: raise `min` to 6 for pred-2 (record 25 and 30 m/s too), or name the two runs in the question.
- lesson.md "Yleinen virhekäsitys" — one paragraph of about 190 words, over the 120-word rule, with S2-hard terms ("maahan sidotussa koordinaatistossa", "näennäisvoima") unexplained. Fix: split into three paragraphs (the feeling, what really acts, the fictitious force in a rotating frame) and give each term one plain-language gloss.
- inquiry.json "virhe" and "valitse" — both are required next to "siirto", the exercises, three checks and the exit ticket. That is a full hour, and the core path makes Etsi virhe optional. Fix: mark "virhe" `optional` (the "valitse" task already covers the same misconception).
- lesson.md apollo8-centrifuge photo — it sits between two theory paragraphs and its caption (the centrifuge's acceleration equals the launch's) teaches nothing the text uses; "sentrifugi" is unexplained. Fix: move it under Tiivistelmä or add one sentence, such as "pyörii ympyrää ja antaa normaalikiihtyvyyden".
- lesson.md Kaava — "Miksi juuri nopeuden neliö?" is qualitative only. That is fine for FY5, but one line with v = 2πr/T would let a student see v²/r, for example Δv ≈ v·(vΔt/r) per time Δt, giving a = v²/r.

## Checked
- Path: fy5-3 prerequisites suffice. The hook question (what force holds the car, is the outward force real) is answered only after the commitment in pred-1, pred-2 and the reflect task.
- Predictions: committed, each wrong option's feedback repairs its own misconception, and the correct one names the evidence in model values. Pred-1 and pred-3 are refutable by the table (3,0 → 12 kN; ratio 0,92 for every mass).
- Variable control: exp-1 locks r, m and surface and varies only v. Exp-2 locks v at 19 m/s, near the limit, and varies m. The numeric question follows from the table (19,81 m/s).
- The simulation shows the motion and the friction limit, not just a formula. `model` honestly says the slide is simplified (friction taken as constant).
- The worked example has seven stages, one step each. It opens from the force diagram, converts units, solves in symbols first and ends with a reasonableness check. It does not repeat the exercises.
- Force-diagram plan: "check-3" has the student draw alone (`draw: true`). Each "valitse" distractor has one error (N = G, N < G, an added F_kp) and its feedback names it. "Etsi virhe" names F_kp as the error.
- Solutions: complete and in the order given, hints in three steps, mistake values correct (18,79 and 10,85 m/s; 47,12 and 294,3 N). check-2's rounding (150 N against the 148 N answer) is inside the tolerance.
- Exit ticket and checks: concept, calculation and drawing. Misconception-based distractors and observable criteria. The exit ticket tests the centripetal force direction, v² scaling and weight at the hill top.
- Finnish and S2 level are good (tangentti and normaali explained). Not opened: captures, because the packet had none ("Screenshots: none yet").
