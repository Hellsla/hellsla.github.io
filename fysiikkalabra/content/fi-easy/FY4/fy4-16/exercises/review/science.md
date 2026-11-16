VERDICT: PASS
CONTENT-HASH: 92fbde3992f971c6

## Blocking
None.

## Polish
1. solutions.md:310 (L3-04 Periaate) — "pulkka pysähtyy aidan viereen juuri suurimmalla sallitulla pituudella" contradicts the task and the solution's own d = 20,0 m: at the greatest length the sled stops 5,0 m before the fence (reported last round, still there). — "pysähtyy $5{,}0\,\text{m}$ ennen aitaa".
2. solutions.md:141 (L2-03 Vastaus) — the reason for three significant figures names 80,0 kg and 52,0 m/s, but $v_2 = 6{,}0\,\text{m/s}$ has two; three hold because the $v_2$ term is only 1,4 kJ of 221 kJ. — Add that reason in one clause.

## Checked
- Every answer recomputed in one script from the task text with my own formulas; all agree with exercises.json and answers.py: L1-01 742,7 N; L1-02 1,217 kN; L1-03 7,924 m/s; L1-04 22,94 m; L1-05 8,531°; L1-08 33,98 N (student's 39,24 N); L2-01 1,063 m/s²; L2-02 0,1373; L2-03 220,5 kJ; L2-04 6,671 kW; L2-05 0,400 m/s², 633,0 N; L2-06 0,0805; L2-07 0,3211 (0,306–0,335); L2-09 0,643 m/s²; L3-01 37,5 m; L3-02 2,287 m/s (slowing 0,857 m/s², 2,67 s, matches the ex-hissi graph); L3-03 2,124 kN; L3-04 16,33 m, 7,67 m/s; L3-05 h = 55,63 m, 2,205 kN.
- Rounding: L3-04's "at most" length rounded down to 16 m (P7); L3-05 c (speed still falling 3–4 s → drag > weight) and its distance-average vs time-average reasoning (1,76 kN) right.
- Conditions stated where used: tan α = μ only for steady sliding after a push (L2-07); slopes steep enough to slide (L3-01, L3-04); constant mean drag (L3-03, L3-05); P = Tv with T = mg at constant speed (L2-04).
- L1-06, L1-07, L2-08: exactly one correct option, distractor feedback right; L2-08's uncertainty reasoning (2Δx, overlap does not prove equality, extrapolation) follows the guardrails.
- Force-diagram blocks in the solutions (L2-03 F_v = 1520,8 N average, L3-02, L3-04 both parts) have the right forces and directions; liukukitka everywhere (P8).
