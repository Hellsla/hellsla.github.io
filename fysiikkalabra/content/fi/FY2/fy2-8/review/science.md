VERDICT: PASS
CONTENT-HASH: e7519d68054da63a

## Blocking

## Polish
- assets/sims/fy2/fy2-8/sim.js:8–9 — the header comment still breaks off mid-sentence: line 9 begins "towards the level's value gradually…" with no subject. Fix: start line 9 with "The ground temperature moves".
- content/fi/FY2/fy2-8/inquiry.json koe-1 `measure` — the recorded key `Teq` is the level's constant. Recording `T` once `tila` is "asettunut" would make each row something the student actually observed.

## Checked
- The delta changes two ennuste-2 feedbacks (the correct option's, and the one for "suurimmat maakaasulla"). "lähes kokonaan" became "suurimmaksi osaksi", about how much of coal's energy comes from burning its carbon.
- The new wording is physically more accurate. Coal is roughly 70–85 % carbon and about 4–5 % hydrogen by mass, and the hydrogen supplies a noticeable share of the heating value (about 15–20 %). So "suurimmaksi osaksi" is right, where "lähes kokonaan" overstated it.
- The surrounding reasoning still holds: natural gas's hydrogen burns to water, so gas gives less CO₂ per kWh than coal (490 vs 820 g/kWh).
- No numbers, symbols, correct-option flags or experiment setups changed. Everything else is as I passed it in round 2 (hash 1a0dc50dd6998ead).
