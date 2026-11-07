VERDICT: PASS
CONTENT-HASH: 7701b8401cab51a9
Mode: translation
Round: 2

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-07 round 4 (three small fixes): L1-04 Substitution now ΔT = (45 − 20) K = 25 K: correct and consistent with the round 3 Formula ΔT/K = (θ_2 − θ_1)/°C. Hashes equal at start and end.
- delta review 2026-11-07 round 3 (fixes to round 2 findings): round 2 Blocking resolved. L1-04 now ΔT = T_2 − T_1 with T/K = θ/°C + 273,15, the constant cancelling to ΔT/K = (θ_2 − θ_1)/°C: correct. L2-04 ratio has θ/°C + 273,15 in numerator and denominator: correct (100,15 K and 400,15 K, ratio 4,00 unchanged). L2-01 T_2 = (288 + 45) K = 333 K, θ_2 = 59,85 °C correct. Page now uses the numerical-value equation throughout. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): every changed Kaava/Muunnokset/Sijoitus line: T/K = θ/°C + 273,15 and its inverse correct; all 32 substitutions (a ± 273,15) K/°C = b recomputed by script, no mismatch; L1-05-type T_2 = T_1 + ΔT form correct. Two unchanged lines keep the old form (Blocking). Hashes equal at start and end.
- Scripted comparison of fy3-3-L1-09 against the reviewed Finnish: same answer (kPa/K), 4 choices, one correct flag, kind, numbers (120 kPa, 300 K, 0.40 kPa/K) and decimal marks.
- Dimensional analysis redone: c = p/T gives kPa/K, c*T in kPa; distractors give kPa*K^2, K^2/kPa and kPa*K for c*T, each feedback correct.
- Solutions.md follows the Finnish step by step; p = cT for a rigid closed container is stated in the task, so the condition is given.
- fi-easy follows NOTES.md 12: shorter sentences and a plain-words gloss added, physics unchanged; no term or number differs from Finnish.
- check_i18n.py: no message for fy3-3; build.py fy3-3 succeeds.
