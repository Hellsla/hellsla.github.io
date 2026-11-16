VERDICT: PASS
CONTENT-HASH: 9a3a2d43c4c1b265

## Blocking
- none

## Polish
- exercises.json L3-01 and L3-04 — "$40,6\,\tfrac{...}$" is written with a plain comma; LaTeX sets a space after it. Write $40{,}6$ (CLAUDE.md decimal comma).
- fy2-5 L3-01, L3-04, L3-05 — the lesson's table lists diesel at 43 MJ/kg while "kevyt polttoöljy" is now 40,6 (MAFY); the task text says "MAFY-taulukko", which suffices, but a short note that the oil is not the lesson's diesel would avoid confusion.

## Checked
- Delta review of the changed values: L3-01 now 120 : 15 − 120 : 40,6 = 8,0 − 2,96 = 5,04 → 5,0 kg (answer, answers.py and solution agree).
- L3-04 oil 53 200 MJ : 40,6 = 1310 kg and the ratio 2,5 vs 40,6 : 17 = 2,4, 2,4 · 0,90 : 0,85 = 2,5 are consistent.
- L3-05 oil 985 → 990 kg and 40,6 : 15 = 2,7 are correct, the answer 940 kg is unchanged.
- The "bensiinissä on yli 40 MJ" wording in the L1 solution is correct (43).
