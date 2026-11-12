VERDICT: PASS
CONTENT-HASH: 45f15bceac913270
SCOPE: delta added-exercise from 2c9fdf155f72e6a3 base 141dc47a8c70

## Blocking
(none)

## Polish
- exercises.json fy2-1-L1-10 — the task still does not say the heating value is read in MJ/kg. Fix (optional): add "Yksikkö on MJ/kg." after "bensiini-rivillä".

## Checked
- Key 86,8 MJ = 43,4 MJ/kg * 2,0 kg; answers.py (43.4 * 2.0) agrees with exercises.json and solutions.md.
- The 4 % tolerance covers 83,3 to 90,3 MJ/kg-based answers, so other tables' values (about 43 to 44) are still accepted.
- Solution still staged (given, asked, principle, formula, units, substitution, sense check); the rounded answer 87 MJ matches the two significant figures of m.
- Sense check follows the new value: 87 MJ is about 24 kWh (86,8 / 3,6 = 24,1); the 80 MJ estimate still holds.
- Level, scope and Finnish unchanged from the earlier pass; no new phone-layout risk (same text length).
- Hash is the same at the start and the end (45f15bceac913270).
