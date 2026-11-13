VERDICT: PASS
CONTENT-HASH: 52e40c11931c671e

## Blocking

(none)

## Polish

- lesson.md:94 — the lesson no longer says when a number rounds up, yet the example "8,8·10^3 m → 10^4 m" and Tarkista check-1 (4,0·10^16 m → 10^17) need it. The student meets the rule only in check-1's wrong-answer feedback ("yli noin 3"). Fix: add one plain sentence after the examples, e.g. "Jos kerroinosa on yli noin 3, suuruusluokka on seuraava kymmenpotenssi, esimerkiksi $8{,}8\cdot10^{3}$ → $10^{4}$." No sqrt needed.

## Checked

- Diff only: the sqrt(10) sentences are gone; the "Toinen esimerkki" sentence reads cleanly and the paragraph is shorter (easier for S2).
- Nothing else in lesson.md or inquiry.json refers to sqrt(10) or 3,16 (grep); no dangling reference, the exercises/solutions are not judged here.
- The remaining definition ("lähimpänä lukua" on the power-of-ten axis) is still correct and matches the axis figure.
- Content hash unchanged at start and end; no other part of the lesson touched.
