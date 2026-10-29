VERDICT: PASS
CONTENT-HASH: 049706003240df2d

## Blocking
(none)

## Polish
- exercises.json fy2-1-L3-02 — the task does not state the model assumption (sound ignored) that L2-03 and the lesson's data item state; add "Ääntä ei oteta huomioon." The solution's "pallo, lattia ja ilma ovat eristetty systeemi" already assumes it.
- solutions.md fy2-1-L3-02 Järkevyys — "ja lasku hidastuu" is ambiguous (the energy loss per bounce shrinks, the fraction stays one fifth); say "lämpöenergiaksi muuttuva määrä pienenee".
- solutions.md fy2-1-L2-01 — "paljon polttomoottoria tehokkaampi" is an unsupported comparison for a reasonableness check (C); harmless.

## Checked
- Recomputed all ten numeric answers independently: 50, 239, 200, 510, 850, 3,0 kJ, 360, 29 000, 130, 0,20 J; all match answers.py, exercises.json and solutions.md.
- L1-03: A 700 J + 0, C 0 + 500 J from the figure description and generator; B 300+300 gives 100 J thermal, consistent with the solution.
- Conversions (kJ to J and back) and the rounding reasons are right for each task.
- Every task states its isolation or ignored effects (air resistance, sound) except L3-02 (polish).
- L1-04 and L3-03: energy chains correct; solar panel mostly heat, nuclear plant about one third electrical, remainder heat to sea water, with no false "unavoidable" claim.
- Scope: only energy balance and kJ/J; no E_k or E_p formulas, vectors or work.
- Symbolic-first solutions with a real reasonableness check in each.
