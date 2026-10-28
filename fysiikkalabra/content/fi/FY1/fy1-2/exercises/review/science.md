VERDICT: PASS
CONTENT-HASH: e66a67c219672d7e

Delta review over the audit's PASS (4157a622aabadf49): L1-04 (km/s → m/s) replaced by a ruler-reading figure task (fy1-2/ruler-read); numbers with units elsewhere turned into LaTeX.

## Blocking
(none)
## Polish
- solutions.md:39 — "kolme merkitsevää numeroa kuten lukemat": 2,0 cm has two figures; the real reason is that both readings are to 0,1 cm, so the difference 11,6 cm keeps the tenths. Say "kuten erotus 11,6 cm, koska lukemat ovat millimetrin tarkkuudella".
- Figure at 360 px: millimetre ticks are about 1,7 px apart; the dashed guides help, and the tolerance (±2,3 mm) forgives a 1–2 mm misreading, so not blocking.
## Checked
- Figure code: rod from X(2,0) to X(13,6) at 36 units/cm, mm/5 mm/cm ticks, numbers 0–15; description matches.
- Recomputed (13,6 − 2,0) cm = 11,6 cm = 116 mm; answers.py 116; tolerance 0,02 → 113,7…118,3 mm accepts any reasonable reading, rejects the wrong method "right end only" (136 mm).
- LaTeX conversions (384 400 km, 1,85 m, 0,92 m, 3474 km, 15,341 km/s) leave values unchanged; answers unchanged.
