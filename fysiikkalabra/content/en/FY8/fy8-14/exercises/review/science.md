VERDICT: PASS
CONTENT-HASH: b4b13e41518dddf9

## Blocking

## Polish
- exercises/review/packet-science.md — the packet's exercise brief and exercise list are empty for en (the generator seems to look for the Finnish section names and task layout). I judged exercises.json and the en lesson's Formula, Worked example, misconception and Summary directly. Fix scripts/review_packet.py for translated packets.
- exercises.json L3-02 — the task says the mean energy is about 20 keV and then assumes 30 keV without a reason. Add "so that the chapter's table values can be used". Carried over from the Finnish review.
- solutions.md L1-05 Reasonableness — "decreases to clearly more than 50 %" is clear in English (the Finnish wording was not). L3-03: the half-value thickness is a narrow-beam value; buildup means a real shield needs somewhat more lead. Carried over.

## Checked
- One script recomputed every answer from the English task text: 25 %, 37.67 → 38 MBq, 5.7 mSv, 0.10 J, 31.52 → 32 kBq, 17 029 → 17 000 a, 0.303 mm, 572.5 → 570 d, 10 µSv, 15.6 → 16 Gy, 8.87 → 8.9, 16.86 → 17 mm. All are within tolerance, and lessons/FY8/fy8-14/answers.py prints the same values.
- Every number in exercises.json and solutions.md matches the passed Finnish version.
- Task conditions survive translation: L1-02 "if nothing left the body", L2-02 background subtracted, L2-04 point source and constant dose rate, L3-01 other beams not through the entry point.
- Solutions solve symbolically first (log form for L2-01, L2-02, L3-03); conversions (g → kg, min → h, a → d) and rounding by the limiting datum are right.
- L3-02 reasoning reads "halved about three more times", which is correct (3.15 extra halvings).
- Data agree with the en lesson: Tc-99m 6.01 h, Am-241 432 a, C-14 5700 a, 5.1 mSv/a, Pb 3.9 / 0.26 mm, d½ 1.8 / 0.27 cm at 30 keV.
