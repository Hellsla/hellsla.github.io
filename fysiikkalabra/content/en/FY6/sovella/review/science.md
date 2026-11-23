VERDICT: PASS
CONTENT-HASH: df919dc21827521b

## Blocking
None.

## Polish
None new. The polish items from round 2 are unchanged and remain optional.

## Checked
- Delta since my round-2 PASS: `git diff <round-2 commit> -- content/en/FY6/sovella` changes only solutions.md, fy6-s4 b Substitution. The inline `ΔE = 14.85 J − 7.99 J = 6.86 J` is now a two-row aligned block (`ΔE &= …` then `&= …`). The numbers, units, order of reasoning and the fraction 0.46 are unchanged. No other task, rubric, tasks.json or answers.py line changed.
- Recomputed with my own formulas: E₁ = ½·330 µF·(300 V)² = 14.85 J, E₂ = ½·330 µF·(220 V)² = 7.986 J, ΔE = 6.864 J, share 46.2 % against a 26.7 % voltage drop, ΔQ = 26.4 mC, P = 6.86 kW over 1.0 ms. All agree with the solution and answers.py.
- Each aligned row is a correct equality, and the last row is the answer used in the next step.
- The physics, scope, significant figures and rubric are as judged in round 2, so the round-2 verdict still holds.
- practice.py check: OK. Hash df919dc21827521b at start and end.
