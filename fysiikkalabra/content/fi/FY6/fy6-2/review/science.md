VERDICT: PASS
CONTENT-HASH: 823ba4ab829f413c

## Blocking

## Polish
- lessons/FY6/fy6-2/lesson-answers.py:53 — the comment still says "= 0,050 V". The inquiry item now gives 0,05 V. Fix: change the comment to 0,05 V (comment only; the value is right).
- lesson.md (Esimerkki) and the error-bands figure — 0,0095 → 0,01 → 0,010 V applies "first digit 1" to the already rounded value. The value is defensible, but add one clause as in exercise L1-05 (carried over).
- inquiry.json (koe-1 intro) — "mitä mittarille tapahtuu?" for the ammeter across the lamp: the model shows 136,4 mA and no fuse blows (carried over).

## Checked
- Round-1 blocker fixed: "Miksi pienin sopiva alue" now has the condition "Jos alueilla on sama p ja sama n, kuten tämän mittarin jännitealueilla". The table supports it: 2 V and 20 V are both ±(0,5 % + 2), with r = 0,001 V and 0,01 V. The decade claim (n·r drops tenfold) holds under that condition: 0,002 V against 0,02 V. The 0,02 A example on the 10 A range does not depend on the condition and stays correct.
- The condition now agrees with the table's current ranges (1,0 % + 2 and 2,0 % + 3), which the text no longer contradicts, and with the Esimerkki's Järkevyys.
- Etsi virhe: 0,005 · 6,00 V + 2 · 0,01 V = 0,05 V. The first digit is 5, so one figure is right. The last distractor's feedback gives 0,05 V : 6,00 V = 0,83 % ≈ 0,8 %, which is correct. No other 0,050 is left in lesson.md, inquiry.json or exit-ticket.json.
- The diff (commit 7d247616) touches only these two places in the lesson. All other numbers, the sim and the figures are as recomputed and passed in round 1.
- The content hash is the same at the start and the end.
