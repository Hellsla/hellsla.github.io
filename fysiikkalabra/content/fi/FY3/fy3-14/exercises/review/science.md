VERDICT: PASS
CONTENT-HASH: d5ba7c6f9fd90049

Round 2. Full review of the 20-task set (8/7/5) after the round-1 fixes (`git diff HEAD~1`); focus on new L1-06..08, L2-05..07, L3-04..05.

## Blocking

## Polish
- exercises.json L2-07, fourth option feedback — "Virhe syntyy siitä, että jään massa tai lämpötila poikkeaa oletetusta": in this task only the mass explains a too-small s (colder ice makes it too large, as the first option's feedback says). Write "jään massa poikkeaa oletetusta".
- exercises.json L1-06 / solutions.md L1-06 — "Täsmälleen 0 °C" holds at normal pressure; the lesson's Tiivistelmä says "normaalipaineessa". Optional to add (level-1 simplification, C).
- docs/exercise-bank/FY3.md fy3-14 Taso 2 — the planned "lämpötila-aikakuvaaja, jossa kaikki jää ei sula (figure)" has no task; L2-06 (error analysis, table-free) covers "kaikki jää ei sula". Update the plan line or note the substitution.

## Checked
- Round-1 Blocking (L2-07 third option) resolved: the cup distractor is replaced by "Lopputilan lämpötila luettiin liian matalaksi"; lower T raises both T_v − T and lowers c_v m_i T, so s comes out too large: really wrong, feedback and solutions.md Mallivastaus right. Exactly one correct option remains.
- Round-1 Polish resolved: L2-05 b now names room heat as the opposite effect; L3-05 a states the exact boundary case and refers to c); L3-04 run 1 now T = 8,2 °C (no longer identical to L2-04).
- All numeric answers recomputed in one script (c_v 4190, c_j 2100, s 334 kJ/kg): agree with answers.py and exercises.json (L1-07 20,95 → 21 kJ; L2-05 338; L2-06 61,1 g; L3-04 331/373/335,1; L3-05 Q_j 36 704 J, T_j −15,7 °C, T_v,min 29,2 °C).
- L3-04 data plausible against the model with s = 334 kJ/kg (8,06 and 6,25 °C predicted vs 8,2 and 6,2 measured); answers.py comment updated to 8,2 °C.
- L2-05: least-squares slope (free 338,3, through origin 337,7 kJ/kg) agrees with the read line.
- L3-05: rows 10 and 20 °C give negative "all melted" T (−14,4; −6,9 °C) and Q_v exceeds the ice-warming 3304 J, so T = 0 °C with ice left is consistent; rows 30/40/60 reproduce 0,6/8,1/23,1 °C.
- L1-06 reworded options (0 °C stated explicitly) and L1-08: one correct option each, feedback correct.
- Scope inside FY3 (Q = cmΔT, Q = sm, energy conservation, Pt = Q); levels and kinds fit; every new task has a complete solution, symbolic before substitution.
- Hash unchanged at start and end.
