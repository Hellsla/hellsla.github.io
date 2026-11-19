VERDICT: PASS
CONTENT-HASH: 6147fa631487e5da

## Blocking
(none)

## Polish
- inquiry.json koe-1 / ennuste-2 — both predictions are pure proportional arithmetic (given 33 s per 10^7 km, or 8 min per AU, scale up), and koe-1 only reads off  = s : c$ that the sim computes; it confirms arithmetic, not something that emerges (inquiry spec). Acceptable here (teacher's scale-sim brief, unit topic), but the prefix conversions and significant figures, which are the slot's goals, have no student action in the core path besides the pysahdy items and check 1. Fix: make koe-1 or the optional items ask the student to convert a read value (km to m, mm) and round it.
- inquiry.json voyager-malli — the table shows $ = 16,5–21,9 h before koe-2, so koe-2 (read $ and $ for two dates) repeats what the table already gives and ennuste-1's answer is visible before its reveal. Fix: put voyager-malli after koe-2, or drop one of the two.
- inquiry.json simulaatio/koe-1 — AU is used as a readout and in the measure column before it is defined anywhere visible (the definition is only in the closed *Laskennan selitys* and in Teoria). Fix: one clause in the hook or the sim lead, "yksi AU on Maan ja Auringon etäisyys".
- lesson.md "Merkitsevät numerot" vs "Kaava" and exit-ticket.json q2 — the lesson warns that trailing zeros of an integer are ambiguous, then writes {,}2\,\text{km} = 4200\,\text{m}$, {,}5\,\text{m} = 2500\,\text{mm}$ and the exit answer /bin/bash{,}50\,\text{mm} = 500\,\mu\text{m}$ (two figures). Fix: write {,}2\cdot10^{3}\,\text{m}$, {,}5\cdot10^{3}\,\text{mm}$, {,}0\cdot10^{2}\,\mu\text{m}$.
- inquiry.json merkitsevat and tarkistus-2 — both repeat the worked example's numbers or method (0{,}1\,\text{AU}$ to {,}50\cdot10^{9}\,\text{km}$; AU to light time). Fix: fresh data (e.g. Jupiter {,}20\,\text{AU}$). Also hook/hero say the signal comes "tänne" (to Earth) while the sim and predictions compute from the Sun; one clause saying so would remove the mismatch.

## Checked
- Opening question is answered only in the explain model answer and the sim; the hook does not disclose it; retrieval item (optional) matches the prerequisite.
- Predictions: wrong options' feedback repairs the specific slip (exponent added/divided, constant speed means constant time); reveal gated after the matching experiment, min 2; numbers verified (42{,}2\,\text{AU}$, 9{,}7\,\text{h}$, 340\,\text{s}$, \,\text{AU/h}$, 3\,000\,\text{AU/ly}$).
- Core path is one lesson's work: optional items are marked; 3 checks with check 1 concept, 2 reasoning, 3 calculation.
- Worked example: seven stages, one step each, symbolic first; arithmetic checked ({,}503\cdot10^{9}\,\text{km}$, {,}17\,\text{h}$, reasonableness).
- Error-spotting item targets the real misconception (km² = 10^6 m²) and every option's feedback repairs it.
- Finnish: case after number+unit correct throughout (42{,}2\,\text{AU}$:n, /bin/bash{,}387\,\text{AU}$:n); glossary terms match.
- Siirto task and solution follow the 7-point form; hints progressive; mistakes cover unit slips ({,}236$ vs 236$).
- Captures: sim at 390 px readable, controls and readout not clipped, model values labelled; Pohdinta capture fine.
