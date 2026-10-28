VERDICT: PASS
CONTENT-HASH: a74dfb2e59b19197

## Blocking
(none)

## Polish
- lesson.md:159 — "Kilometreiksi tunnissa muunnetaan miettimällä…" is odd Finnish; write "Yksikköön $\text{km/h}$ muunnetaan miettimällä…". "Tämä sijoitetaan yksikön paikalle." is vague: "Sijoitetaan $1\,\text{m/s}$:n paikalle $3{,}6\,\text{km/h}$." tells the student what to do.
- lesson.md:170 — the second aligned block restarts "v &=" after the m/s lines; label the line ("km/h-yksikössä") or keep it, since the \\[4pt] gap already separates it.
- Round-2 polish on the t = 0 readout and the pred-1 hint still stands.

## Checked
- Round-2 blocker class fixed: m/s → km/h is now by meaning. 1 m/s gives 3600 m in 3600 s, which is 3,6 km in an hour, so 1 m/s = 3,6 km/h; the example then substitutes 14,715·1 m/s = 14,715·3,6 km/h = 52,97 km/h (right). The summary bullet carries the reasoning, not a bare factor.
- km/h → m/s in the transfer task (inquiry.json hints 2-3, solution Muunnokset) uses 1 km = 1000 m and 1 h = 3600 s: 108·1000 m : 3600 s = 30,0 m/s, t = 3,06 s, correct; no "jakamalla luvulla 3,6" remains.
- Unrounded value converted, not 15 m/s: kept in the Tulos stage.
- Notation: \cdot for products, colon in the sim readout; no ×.
- Rest of the lesson unchanged since the passed version; the diff touches nothing else.
