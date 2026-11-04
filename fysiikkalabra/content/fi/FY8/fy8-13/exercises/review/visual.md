VERDICT: FAIL
CONTENT-HASH: b81e54ad228f16ca
ROUND: 2

## Blocking
- [Major] fy8-13-L2-05 data table (exercises.json, row "Muu luonnon säteily (maaperä ja rakennusaineet, kosminen säteily, kehon omat radioaktiiviset aineet)") — the 100-character row label makes the table wider than the 664 px exercise column; at 1280 px the label is cut off ("…kehon") and the whole $H_\text{E}$ column with the values 4,0 / 1,1 / 0,8 is pushed out of view, only a scroll shadow hints at it. The data needed to solve the task is not visible without sideways scrolling, and on a phone it is worse (no 360 px capture exists to confirm, but the cell cannot get narrower). New in round 2 (the row replaced three short ones). Fix: shorten the label to "Muu luonnon säteily" and move the explanation into the task text or caption ("muu luonnon säteily = maaperä, rakennusaineet, kosminen säteily ja kehon omat radioaktiiviset aineet"), then rebuild and re-capture.

## Polish
- [Minor] L2-05 and L1-08 are both "share of the 5,9 mSv annual dose" with one division (three-term sum plus percentage); L2-05 sits low for level 2. L3-04 still repeats the radon proportion model of L2-03/L3-02.
- [Minor] L2-06 — the answer chip shows "11 µSv/h" but the Vastaus says "11 (tarkemmin 11,2)" while the Sijoitus carries 11,208; the task asks for the mean method only, so one sentence on rounding is enough.
- [Minor] L3-04 c) — mallivastaus gives the heating-season result as "noin 310–380"; the 310 is not derived from the table (say "enintään 380" or show the mean of the chosen periods).

## Checked
- Round 1 had no Blocking items; its Polish is resolved: L2-06 units now on every k row, list with semicolons, the law as a display line, answer text "keskiarvomenetelmällä". L3-04 kind no longer says graph.
- Captures at 1280 px (every solution open): L2 parts 6-7 (L2-05, L2-06), L3 parts 5-6 (L3-04). No 360 px exercise captures in the packet.
- Recomputed 5,9 mSv / 68 %, 100,875 / 11,2 µSv/h, 270, 9,19, 58,75 Bq/m3: match answers.py and exercises.json. No red KaTeX elsewhere. Hash at start and end the same.

## Scores
illustrations n/a · typography 4 · Finnish 5 · accessibility 3
