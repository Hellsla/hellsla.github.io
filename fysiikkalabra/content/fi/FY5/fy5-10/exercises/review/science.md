VERDICT: PASS
CONTENT-HASH: 16626c2582880ebf

## Blocking

## Polish
- solutions.md:126 (L1-06 Mallivastaus) — the options changed but the model answer still discusses only the old ones; it does not address the new distractor "kohdat pysyvät paikallaan, vain pää värähtelee" — add one sentence (every point oscillates in turn as the disturbance passes), as in its feedback.

## Checked
- L2-07: answer 340 (3,4·10² m/s) recomputed (1,50 m / 4,4 ms = 340,9 m/s); two figures justified by Δt = 4,4 ms; tolerance 0,02 still accepts 341. New argument correct: a constant timer offset cancels in Δt, and 0,1 ms is about 2 % of the 4,4 ms difference.
- answers.py updated consistently (round(…, −1) = 340); all 18 numeric answers equal exercises.json.
- L3-04: k renamed C = v²/F throughout task-free solution, Kaava, Sijoitus and answers.py comment; values unchanged (C = 22,0, v = 25,7 m/s, λ = 5,1 m, recomputed 5,13 m). Removing the hint leaves the task at a fair level 3 ("suoraan verrannollisesti vai jollakin muulla tavalla" still steers the test).
- L1-06: exactly one correct option (longitudinal: oscillation along the direction, compressions and rarefactions); each distractor wrong (transverse, matter transport, points stay still) with correct feedback.
- L2-06 quotation mark and L2-07 "välin" typo fixes: no physics impact.
- No new errors in the diff; scope and notation unchanged.
- Hash identical at start and end.
