VERDICT: PASS
CONTENT-HASH: 64560c496d3a4f35

## Blocking

## Polish
- solutions.md L2-05 — the step heading "Reading the graph" introduces a table. Part a) of the Answer gives only the time, while the task also asks for the peak power. — Use "Reading the table", and write "The peak power is $6.8\,\text{kW}$ at 19–20".
- solutions.md L2-04 Reasonableness — "about $3.5\,\text{W}$ per metre" means per metre of cable, counting both conductors. — Say so.
- solutions.md L2-07 Answer — "two significant figures like the powers" is not the real reason, because most of the powers have three figures. The real limit is the trapezoid approximation. — Name that as the reason.
- exercises.json L2-05, L3-03, L3-05 — the shared ±2 % check also accepts a value just past the limit. This is known and outside this set; the one-sided check is pending with the coordinator.

## Checked
- The hash was 64560c496d3a4f35 at the start and at the end.
- I recomputed all 20 answers in one script with my own formulas. Every one agrees with answers.py and exercises.json. The answers, tolerances, units and numbers match the Finnish set, apart from the decimal separator.
- L3-02 now answers $1.6 \cdot 10^{2}\,\%$ (calculated 156 %), with two figures from $10\,\text{A}$ and $16\,\text{A}$ (P7b). The "exact settings" reason is gone. With data-step 10 the page accepts 151–161.
- L3-03: the minimum 7.157 A is rounded up to 7.2 A, and the direction is stated. L3-05: the maximum 7.609 A is rounded down to 7.6 A, and the direction is stated. The cable dissipates 23.6 W and 104 W.
- L2-03: the limit 11.96 A is rounded down to 11 A. The page accepts 10.98–11.97 A, so 12 A fails. L2-05: 10.45 kW is rounded down to 10.4 kW, and in c) only 19–20 h exceeds 6.25 kW.
- L2-08: the options recompute to 15.3, 11.1, 13.0 and 5.1 h, with exactly one correct and every feedback right. L1-06 has exactly one correct option.
- Physics and scope: power factor ≈ 1, 3UI only with equal phase currents, R = ρ·2l/A, and 230 V with three figures (P7a). Everything stays within FY6.
- The figures give every value their tasks need, without the answer.
