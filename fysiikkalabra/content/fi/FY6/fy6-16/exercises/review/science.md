VERDICT: FAIL
CONTENT-HASH: 7fd5eddc31d0e0b4

## Blocking
- exercises.json fy6-16-L3-02 (answer 156, tolerance 0.02) and solutions.md L3-02 Vastaus — B, assessment. Under P7b, $10\,\text{A}$ and $16\,\text{A}$ have two significant figures, so the data-precision answer is $1{,}6 \cdot 10^{2}\,\%$ = 160. The page accepts only 152,9–159,1, so a student who rounds correctly to the data gets "Lähellä". The solution keeps three figures because the currents are "latauslaitteen tarkat asetukset", but the task text never says this. — Fix: either add to the task that 10 A and 16 A are the charger's exact set currents (then 156 % stands), or set tolerance 0.03 so that 160 passes.

## Polish
- solutions.md L3-05 Vastaus — 7,609 → 7,6 A is a maximum but, unlike L2-03, L2-05 and P7c, the rounding direction is not stated. Add "raja-arvo pyöristetään alaspäin". The same applies to L3-03, a minimum: 7,157 → 7,2 A, rounded up. Part a) gives "17 A" but c) uses 17,4 A, and 12,0 kW supports 17,4 A.
- solutions.md L2-07 Vastaus — "kaksi merkitsevää numeroa kuten tehoissa": most powers (11,0, 10,8) have three figures. The real limit is the trapezoid approximation, so name that as the reason, or give 22,9 kWh.
- solutions.md L2-05 — the heading "Kuvaajan lukeminen" introduces a table: "Taulukon lukeminen".
- solutions.md L3-04 Kaava — the symbol $v$ for $6{,}50\,\textsf{l}$ per 100 km clashes with velocity. Use $V$.

## Checked
- Hash 7fd5eddc31d0e0b4 at start and end.
- All 20 answers recomputed independently in one script, and every one agrees with answers.py. Spot values: L3-04 gives 14 640 km, 390,4 €, 1760,5 € and 1370,1 €; public charging costs 1171,2 €, so the saving is 589,3 €. L2-07 trapezoids give 22,85 kWh. L3-05 gives 7,609 A and cable losses of 23,6 W and 104,4 W.
- L2-03 now has answer 11,478 with tolerance 0.043. By the half-unit rule it accepts 10,98–11,98 A: 11 and 11,96 pass, and 12 is rejected. This is right under P7c. The band's top, 11,96–11,98, is only 0,02 A above the exact limit, which is negligible.
- L2-05 10,4 kW, L3-05 7,6 A and L3-03 7,2 A: the shared 2 % floor also accepts 10,5 kW, 7,7 A and 7,1 A. No per-task setting can fix this, and the solutions no longer claim the check enforces the direction. This is not blocking for the set; the shared one-sided check is pending.
- L2-05 c): only 19–20 h (6,8 kW) exceeds 6,25 kW. The within-hour caveat is stated.
- L2-08: 15,3 h. The distractors are 11,1 h (times η), 13,0 h (no η) and 5,1 h (3UI), each with feedback that is correct. Exactly one option is correct.
- L1-06: one option is correct, and every distractor's feedback is right.
- Physics: the power factor ≈ 1 is stated. P = UI and 3UI use the 230 V phase voltage (three figures, P7a). The fuse protects the cable. Cable resistance uses 2l. The Tukes 8 A socket limit is stated correctly. All within FY6 scope.
- Figures lataus-ex (11 kW, then 5,5 kW, on gridlines) and talo-ex (2/5/7/3 kW) give every value the tasks need and give no answer away.
- Every remaining answer rounded to its data stays within tolerance (L1-02 is at 2,2 % with tolerance 0.03). Every solution is symbolic first.
