VERDICT: FAIL
CONTENT-HASH: 389f38cde0cd5ca2

## Blocking
- exercises.json fy6-16-L2-05 (answer 10.4, tolerance 0.005) — A, assessment: the narrower tolerance does nothing. templates/lesson.js accepts max(2 % · answer, tolerance · answer, half a step), which is ±0,208 kW here, so 10,19–10,61 kW counts as correct. The page therefore marks the rounded-up $10{,}5\,\text{kW}$ correct (and $10{,}6$, which is over the limit), while solutions.md:155–157 says the limit must be rounded down. No symmetric band can accept both 10,4 and 10,45 and still reject 10,5. — Fix: needs a one-sided limit check in the shared answer check (a shared change, to go through the coordinator first). Or ask for a quantity whose rounded-down and rounded-up values are more than 4 % apart. Until then, do not claim that the check enforces the rounding direction.
- exercises.json fy6-16-L2-03 (answer 11, tolerance 0.09) — A, assessment: the band 10,01–11,99 A marks clearly wrong maxima such as $10{,}2\,\text{A}$ correct. It also accepts 11,97–11,99 A, which is above the true limit of 11,957 A. — Fix: centre the answer between the rounded and the exact limit, answer 11.48 (in answers.py, e.g. (floor + exact) / 2) with tolerance 0.02. The half-step rule then accepts 10,98–11,98 A: 11 and 11,96 pass, 12 is only "Lähellä". The shown answer stays $11\,\text{A}$.

## Polish
- solutions.md L3-04 Vastaus — "$1370\,\text{€}$ … pyöristettynä kymmeneen euroon" reads as four figures under P7b. $1{,}37 \cdot 10^{3}\,\text{€}$ says the same thing in one form.

## Checked
- Hash 389f38cde0cd5ca2 at start and end. The changes are L2-03 and L2-05 (answer, tolerance, answers.py and solutions; git c40cc4fbb); I still reviewed the whole set.
- Recomputed every answer in one script. L2-03: exact limit 11,957 A, rounded down to 11 A. L2-05: 17,25 − 6,8 = 10,45 kW, rounded down to 10,4 kW. L3-05: 7,609 A, rounded down to 7,6 A. L3-03 is a minimum: 7,157 A, rounded up to 7,2 A. All four follow P7c, and every other answer agrees with answers.py.
- The new reasonableness checks are right: 13,0 + 11 = 24 A; 3·230·11 W ≈ 7,6 kW; 10 400 W : 690 V = 15,1 A, which with the house's 9,9 A gives 24,9 A.
- P7a: 230 V is treated as three figures everywhere, and the limiting data are named correctly.
- L2-08: 15,3 h; the distractors are 11,1 h (times η), 13,0 h (no η) and 5,1 h (3UI). Exactly one is correct.
- Physics: P = UI and 3UI with the power factor ≈ 1 stated, t = W_akku/(ηP), the cost from grid energy, and the cable R = ρ·2l/A. The fuse protects the cable, not the device.
- Figures lataus-ex (11 kW, then 5,5 kW) and talo-ex (2/5/7/3 kW) match their alt texts and give no answer away.
