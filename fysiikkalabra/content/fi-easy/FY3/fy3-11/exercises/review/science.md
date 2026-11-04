VERDICT: PASS
CONTENT-HASH: d6c59949a7a14871

## Blocking
(none)

## Fixed
- L2-05, L2-07, L3-04 task texts: only added a plain-language explanation (hyötysuhde, ilmalämpöpumppu, lämpökerroin) and split a long sentence; no number, unit or answer changed.

## Polish
- None.

## Checked
- Scripted comparison of exercises.json against the Finnish for all 8 new tasks: ids, kinds, answers, units, tolerances, correct flags, choices, table cells and every number equal.
- Solutions (243 lines): every number, unit and formula equals the Finnish; same structure.
- Recomputed: lämpökerroin 3,25, suurin hyötysuhde 31,4 %, Q_ulko 20,9 kWh, kauden lämpökerroin 2,74, Delta U 0,74 kJ.
- Terms and symbols (W_k, E_s, Q_sisälle, Q_ulko) as in the Finnish. check_i18n fi-easy: 0 errors.
