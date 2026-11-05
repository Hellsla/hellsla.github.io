VERDICT: PASS
CONTENT-HASH: bab5b2b5c4d76a57
Round: 2

## Blocking
(none)

## Polish
- exercises.json:321 and :325 (feedback D, "ei virhettä") — still "koska pullossa on huoneenlämpöistä ilmaa" / "ei sovi suljettuun pulloon", but the task does not say the air is at room temperature. State it in the task, or phrase it as "574 °C olisi uunin lämpötila". Carried over.

## Checked
- Round-1 Polish resolved: V is now $2{,}00\,\textsf{l}$ = $0{,}00200\,\text{m}^3$ in the task text, in rows 1 and 3, in the row-1 feedback and in the solution (Mallivastaus rows 1 and 3), so the three-figure "$T \approx 301\,\text{K}$" is justified and row 4 is the only wrong row.
- Recomputed: pV = 200 J, nR = 0,6648 J/K, T = 300,8 K ≈ 301 K; θ = 27,7 °C ≈ 28 °C; the wrong row gives 574 °C.
- Exactly one correct option (row 4); "Laskussa ei ole virhettä" is last; the other feedback and the solution are unchanged and right.
- Commit 6bbde30c5 touches only these lines in fy3-10; answers.py and the other tasks unchanged since the earlier PASS.
- Text only this round: I did not open the new captures; the change is to digits inside existing inline formulas (row 3 grows by one character).
- Hash identical at start and end.
