VERDICT: FAIL
CONTENT-HASH: 2c1c2a557074f30d

## Blocking
- inquiry.json:530 — (A) the siirto mistake value 1,65 does not match its own feedback: 5,2 V · 0,30 A = 1,56 W, so a student who multiplies the differences gets 1,56 and never sees this feedback — set `"value": 1.56`.
- inquiry.json:534 — (A) siirto "Vastaus": the rounding reason is wrong. Every datum used (18,0 V; 5,50 A; 12,8 V; 5,80 A) has three significant figures and the difference 99,0 W − 74,2 W is good to 0,1 W, so the result is 24,8 W. The nominal "12 V" is not used — answer $24{,}8\,\text{W}$ (tolerance already accepts it) or give ≈ 25 W a correct reason.

## Polish
- lesson.md:269, 624 (and glossary *estosuunta*) — (B, mild) "koko lähteen jännite on diodin yli, virtaa ei kulje" holds only below the diode's reverse breakdown voltage. The sim's model box states this (an LED is often rated for only about 5 V in reverse), but the theory does not — add "kunhan jännite ei ylitä diodin suurinta estojännitettä".
- lesson.md:380 and inquiry.json:602 — the lamp is said to follow Ohm's law approximately and, in the same breath, to have a resistance that grows as it heats. The main reason it survives is that its filament has a sizeable resistance, so I = U : R (for a lamp rated for that battery); the rise with temperature only adds to this. Make the two places say the same.
- lesson.md:565 — the efficiency is computed with the maximum power. Say "maksimitehopisteessä".
- inquiry.json:121 — the example voltages in koe-1 (2, 3, 5, 7, 9 V) leave out 6,0 V, which ennuste-1 and its feedback compare (1,91 V and 12,4 mA). Add 6,0 V.
- assets/sims/fy6/fy6-14/sim.js (ledPicture) — the canvas literals `$\text{virta yli } 20\,\text{mA}$` and `$\text{estosuunta: ei virtaa}$` break the FY6 thread rule (word labels via `__('key')`). Not physics.

## Checked
- Recomputed in one script (own solver): koe-1, ennuste-1 (3,5→12,4 mA), koe-4, panel MPP 4,96 V / 185 mA / 0,918 W / 26,8 Ω, P(300 Ω) 0,12 W, U_t(500) 5,72 V, η 15 %; example, kertaus, Etsi virhe, tarkistus-3, exit ticket all right.
- Every choice item has exactly one correct option; distractor feedback correct.
- sim.js implements the stated models; simState keys and locks isolate each varied parameter.
- Figures match the models and captions; current violet #7048e8; "sisäenergiaksi", no "lämmöksi"; sim numbers called model values; no error limits; scope as in the täsmennys.
