VERDICT: PASS
CONTENT-HASH: 6a20ede240385bd9

## Blocking

## Polish
- inquiry.json:16 (hook) — "Viimeiset kymmenen prosenttia vievät lähes yhtä kauan kuin koko alkuosa": in the lesson's own constant-voltage model 90 → 100 % takes about 18 min against 30 min for 10 → 52 %. As a description of a real phone (CC/CV) it is fair (C), but "melkein yhtä kauan" may make a student expect the sim to reproduce it; "pitkään" would avoid that.

## Checked
- Round-1 Blocking fixed: sim `model` now says a too-low charger discharges the cell until its source voltage has fallen to the charger's voltage, and only a charger below 3,40 V empties it. This matches sim.js `cell()` (x → 0 asymptotically; stop at q = 0 only when x0 < 0 reaches empty) and my own run: 3,6 V from 80 % settles at 25 %, 3,3 V empties it.
- Round-1 Polish taken: virhe feedback "noin 15 %" (4,57 A vs 4,0 A, +14 %); siirto "lähes kolmannes" (30 %); koe-2 intro wording.
- Hook "noin puoleen": model gives 10 % → 52 % in 0,5 h at 4,5 V, 0,40 Ω.
- Every number recomputed in one script: start 2,2 A; drops 0,88/0,22/3,40 V; terminal 3,62 V; koe-1 1,47/0,99/0,66 A; koe-2 −0,88/−0,08/0,32/1,12 A; koe-3 2,01/1,37/0,87 h, 86/83/76 %; full charge 9,0/7,6 Wh, η 84 %.
- Worked example 2,0 A, 3,90 V and the 16,8 A check; virhe 35 A vs 4,0 A; siirto 1,68 with mistakes 2,5/2,40/1,75; check 2 6,0 A (48 A, 7,2 A), 12,9 V both ways; exit ticket 9000 C.
- Energy wording "sisäenergiaksi, joka siirtyy lämpönä"; no "lämmöksi"; efficiency sentence follows the guardrail.
- The cell neutral, stores chemical energy; capacity is charge, energy UQ with nominal voltage.
- Predictions: exactly one correct option each; distractor feedback right with model values.
- Experiments vary one parameter and lock the rest; simState keys I, E, soc, tFull, Wlat, eta exist.
- Voltage law and conditions ($U_\text{lat} > E$, diode) stated.
