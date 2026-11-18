VERDICT: PASS
CONTENT-HASH: b61fa0a2e8442d35
SCOPE: delta: en tasks fy9-kaasut-s8 (fy3-10/pt-suorat) and s9 (fy3-11/pv-isobaari) in sovella/tasks.json and solutions.md, and the changed intro (git diff 49ba8f9 HEAD); fidelity to fi; s1-s7 not re-judged. Language: en.

## Blocking
(none)

## Polish
- s9: heating air to about 1170 K (about 900 °C) is implausible for a school cylinder; a smaller volume ratio or "the gas is idealised" would help. The task is labelled an invented example.

## Checked
- Recomputed in one script (R = 8.31, 273.15): s8 a n = 1e5*2.0e-3/(8.31*400) = 0.0602 mol (200 K / 50 kPa gives the same); b 60/100 = 0.60, 40 % smaller, n_B = 0.036 mol; c 100*253.15/400 = 63.3 kPa; s9 a 250 kPa*3.0 l = 750 J; b 250/(8.31*293.15) = 0.1026 mol; c T2 = 4*293.15 = 1172.6 K (899 °C). All answers inside tolerances; 1.2e3 K is inside 3 %. Order-of-magnitude checks (0.083 mol in 2 l, 0.042 mol in 1 l of room air) right.
- Figure source (lessons/FY3/fy3-10, fy3-11 figures.py): A (200 K; 50 kPa), (400 K; 100 kPa), B (200; 30), (400; 60); isobar 250 kPa from 1.0 l to 4.0 l. Readings in the solutions match.
- Physics: rigid sealed vessel, n and V constant, p proportional to T; comparison at equal T and V; W = p dV at constant pressure as the area; s9 d dU > 0, Q = dU + W, so Q > W, sign convention consistent. Scope FY3. Kelvin conversions explicit.
- Assessment: criteria sum to part points; criteria ask only what each part asks; alternative methods (slope, V/T constant, Celsius answer) accepted.
- Fidelity to fi: ids, figures, points, criteria, answer values and tolerances identical; every number in s8/s9 text, criteria and solutions matches fi.
- Intro: "Nine problems", "one of the problems is source-based", consistent with the set.
- Hash b61fa0a2e8442d35 (units.py hash --lang en) at start and end.
