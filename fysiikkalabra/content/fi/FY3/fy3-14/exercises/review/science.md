VERDICT: FAIL
CONTENT-HASH: 0683fd0b7fef9f45

Full review (20 tasks, 8/7/5), focus on new L1-06..08, L2-05..07, L3-04..05.

## Blocking
- exercises.json:231-232, solutions.md:178 (L2-07, third option) — A, assessment: "Kalorimetrin astia lämpeni veden mukana, joten vesi luovutti osan lämmöstään astiaan" cannot happen here: the water cools, so the cup cools with it and gives heat to the ice. A neglected cup heat capacity (the usual systematic error) makes s too SMALL, so this option is defensibly a second correct answer, and its feedback ("liian suuren sulamislämmön") teaches the opposite. — Replace with a distractor clearly in the wrong direction, e.g. "Lopputilan lämpötila luettiin liian matalaksi" (T_v − T too large → s too large); update its feedback and the sentence at solutions.md:178.

## Polish
- solutions.md:162 (L2-05 b) — besides heat lost to the funnel, note that room heat melting ice acts the other way; the 1 % difference is within the line reading.
- solutions.md:193/197 (L3-05 a) — T = 0,0 °C also fits the exact boundary (all ice just melted, ≥); add that c) shows rows 10 and 20 °C lie below the limit.
- exercises.json:267 ff. (L3-04) — run 1 repeats L2-04 exactly (0,200 kg, 30,0 °C, 0,0500 kg, 8,1 °C → 333 kJ/kg); vary it or say so.

## Checked
- All 17 numeric answers recomputed in one script (c_v 4190, c_j 2100, s 334 kJ/kg): agree with answers.py and exercises.json (L2-05 338; L2-06 61 g; L3-04 333/373/335; L3-05 Q_j 36 704 J, T_j −15,7 °C, T_v,min 29,2 °C).
- L2-05: through-origin least-squares fit also gives 338 kJ/kg.
- L3-05 data consistent: row-40 Q_j reproduces rows 30 and 60 °C (0,60; 23,1 °C).
- L3-04 data plausible (model with s = 334: 8,06 and 6,25 °C); error direction in b) right.
- L2-06: "kaikki jää ei sula" verified (25 140 J < 54 825 J); matches the plan's virheanalyysi.
- L1-06, L1-08: one correct option, feedback right; boundary cases per guardrails.
- Scope inside FY3 (Q = cmΔT, Q = sm, energy conservation, Pt = Q); levels and kinds fit the plan; every new task has a complete solution.
- Hash unchanged at start and end.
