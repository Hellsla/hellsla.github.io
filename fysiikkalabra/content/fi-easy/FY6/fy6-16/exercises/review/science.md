VERDICT: PASS
CONTENT-HASH: 18ab4765994d3ada

## Blocking

## Polish
- solutions.md L2-05 — the step heading "Kuvaajan lukeminen" introduces a table. Part a) of the Vastaus gives only the time, while the task also asks for the peak power. — Use "Taulukon lukeminen", and write "Huipputeho on $6{,}8\,\text{kW}$ kello 19–20".
- solutions.md L2-07 Vastaus — the reason given is two figures "kuten tehoissa", but most of the powers have three figures. The real limit is the trapezoid approximation. — Name that as the reason.
- exercises.json L2-05, L3-03, L3-05 — the shared ±2 % check also accepts a value just past the limit. This is known and outside this set; the one-sided check is pending with the coordinator.

## Checked
- The hash was 18ab4765994d3ada at the start and at the end.
- I recomputed all 20 answers in one script with my own formulas. Every one agrees with answers.py and exercises.json. The answers, tolerances, units and the numbers in the tasks and solutions are the same as in the Finnish set.
- L3-02, last round's blocking item: the answer is now $1{,}6 \cdot 10^{2}\,\%$ (laskimen arvo 156 %), with two figures from 10 A and 16 A (P7b). The page accepts 151–161 via data-step 10, so a student who rounds to the data passes. Resolved.
- L3-03: the minimum 7,157 A is rounded up to 7,2 A, and the solution now says so. L3-05: the maximum 7,609 A is rounded down to 7,6 A, and the solution now says so. The cable dissipates 23,6 W and 104 W.
- L2-03: the limit 11,96 A is rounded down to 11 A. The page accepts 10,98–11,97 A, and 12 A fails. L2-05: 10,45 kW is rounded down to 10,4 kW, and in c) only 19–20 exceeds 6,25 kW.
- L2-08: the options recompute to 15,3, 11,1, 13,0 and 5,1 h, with exactly one correct and every distractor's feedback right. L1-06 has exactly one correct option.
- Physics and scope: power factor ≈ 1, 3UI only with equal phase currents, R = ρ·2l/A, 230 V with three figures (P7a), and the fuse protects the cable. Everything stays within FY6.
- Figures lataus-ex and talo-ex give every value their tasks need, without the answer.
