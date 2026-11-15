VERDICT: FAIL
CONTENT-HASH: 88e654d5526de26f

## Blocking
- solutions.md:109 (L3-02, exercises.json:280) — B: the answer keeps three figures, "156 %", because the currents are "latauslaitteen tarkat asetukset", but the task text never says so. Under P7(b), 10 A and 16 A each have two significant figures, so a student who rounds to the data writes 1,6·10² %. The shown step of "156 %" is 1, so the page accepts only about 153–159, and 160 gets "Lähellä". CLAUDE.md requires that a student rounding to the data stays inside the tolerance. Fix: either state the exactness in the task ("laturin asetukset ovat tarkalleen 10 A ja 16 A"), or give the answer as $1{,}6 \cdot 10^{2}\,\%$ (step 10, so 151–161 is accepted), with two figures as the reason.

## Polish
- exercises.json:128 (L2-05) and exercises.json:355 (L3-05) — the maximum is rounded down (10,4 kW; 7,6 A, P7c), but the site-wide ±2 % check still accepts 10,5 kW and 7,7 A, which break the limit. This cannot be fixed in this set (templates/lesson.js); the one-sided limit check proposed to the coordinator would fix both tasks.

## Checked
- All 22 numeric answers recomputed in one script (P = UI, P = 3UI, I = P/(3U), t = W_akku/(ηP), K = aW_verkko, R = ρ·2l/A, P = RI², trapezoids in L2-07, 14 640 km and 1370,1 € in L3-04); all agree with answers.py and exercises.json.
- L2-03 (P7c): exact limit 11,96 A, shown 11 A; answer 11,478 with tolerance 0,043 and a half step of 0,5 gives 10,98–11,98 A, so 11 A and 11,96 A pass and 12 A does not; answers_shown picks "11 A".
- L2-05: limit 17,25 − 6,8 = 10,45 kW, rounded down; c) only 19–20 exceeds 6,25 kW; the one-hour-constant assumption is stated in the task.
- L3-05: 17,39 A per phase, 7,61 A left on the charger's phase, rounded down to 7,6 A; cable 0,408 Ω gives 23,6 W and 104 W; the explanation of the factor of about 4,4 is right.
- L3-03: the minimum current 7,157 A is rounded up to 7,2 A (safe direction); 9,0 h is right.
- L2-08: options 15,3 / 13,0 / 11,1 / 5,1 h recomputed; exactly one is correct, and each distractor's feedback names its error.
- 230 V is treated as three figures (P7a); the limiting data are named correctly elsewhere.
- Three-phase P = 3UI is used only with equal phase currents, as the tasks state; a single-phase charger loads one phase.
- Figures lataus-ex (11 kW for 2,0 h, then 5,5 kW for 1,0 h) and talo-ex (2, 5, 7, 3 kW) and their descriptions give every value the tasks need, without the answer.
- Safety: a socket charger limited to 8 A, a fuse that protects the cable, and current limited in the evening; all are consistent with the brief.
