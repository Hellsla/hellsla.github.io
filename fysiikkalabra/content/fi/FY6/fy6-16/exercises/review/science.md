VERDICT: PASS
CONTENT-HASH: 74e9de790a996e86

## Blocking

## Polish
- solutions.md L2-05 Vastaus a) — the question asks for the peak power and its time, but a) gives only the time. The value 6,8 kW appears only in the reading step. — Write "Huipputeho on $6{,}8\,\text{kW}$ kello 19–20". The step heading "Kuvaajan lukeminen" introduces a table, so "Taulukon lukeminen" would fit better.
- solutions.md L2-07 Vastaus — "kaksi merkitsevää numeroa kuten tehoissa" is not the real reason, because most of the powers have three figures. The real limit is the trapezoid approximation. — Name that as the reason.
- solutions.md L3-04 Kaava — the symbol $v$ for 6,50 l per 100 km clashes with velocity. — Use $V$.
- exercises.json L2-05, L3-03, L3-05 — the shared ±2 % check also accepts a value just past the limit: 10,5 kW, 7,1 A and 7,7 A. This is known and outside this set; the one-sided limit check is pending with the coordinator.

## Checked
- The hash was 74e9de790a996e86 at the start and at the end.
- I recomputed all 20 answers in one script from the task data with my own formulas. Every one agrees with answers.py and exercises.json. The fi, en and fi-easy answers, tolerances and units are identical.
- L3-02, last round's blocking item: (16 : 10)² − 1 = 1,56. Under P7b both currents have two figures, so the answer $1{,}6 \cdot 10^{2}\,\%$ is right, and the reason given names both currents. With data-step 10 the page accepts 151–161, so both 156 and 160 pass. Resolved.
- L3-03: the minimum is 40 000 Wh : (3 · 0,90 · 230 V · 9,0 h) = 7,157 A. It is rounded up to 7,2 A, and the solution now says so (P7c).
- L3-05: 12,0 kW : 690 V = 17,39 A, which leaves 7,609 A. It is rounded down to 7,6 A, and the solution now says so. The cable dissipates 23,6 W at that current and 104 W at 16 A, a factor of about 4,4, and the 33,4 A overload is right.
- L2-03: the limit 11,96 A is rounded down to 11 A. Answer 11,478 with tolerance 0,043 accepts 10,98–11,97 A, so 11 A and 11,96 A pass and 12 A fails.
- L2-05: 17,25 − 6,8 = 10,45 kW, rounded down to 10,4 kW. In c) only 19–20 h exceeds 6,25 kW.
- L2-08: the four options recompute to 15,3, 11,1, 13,0 and 5,1 h. Exactly one is correct, and each distractor's feedback names its own error. L1-06 has exactly one correct option, and every feedback is right.
- Physics and scope: power factor ≈ 1 is stated, 3UI is used only with equal phase currents, R = ρ·2l/A, and the fuse protects the cable. Everything stays within FY6.
- Figures lataus-ex and talo-ex give every value their tasks need, on grid lines, without the answer.
