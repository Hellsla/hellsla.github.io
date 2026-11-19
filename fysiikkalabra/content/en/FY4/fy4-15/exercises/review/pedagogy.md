VERDICT: PASS
CONTENT-HASH: ef00abf4751d27fa

## Blocking
(none)

## Polish
1. exercises/solutions.md (the ratio tasks: power at a different wind speed, at a different rotor diameter) — the full five-equation derivation of $P = \tfrac12\eta\rho A v^3$ is repeated before a one-line ratio; for these two a shorter row ("the power is $P = \tfrac12\eta\rho A v^3$ (derived in the worked example)") would keep the ratio visible. Same for the repeated hydropower derivation in the flow-rate and monthly-energy tasks.
2. exercises/solutions.md (repeated Formula rows) — "$P_{\text{wind}}$" and "$P_\text{wind}$" are both used; use the second form throughout.
3. exercises/solutions.md (the monthly-energy task) — the row ends "$E = Pt$, so $E = \eta\rho g h\,(\sum Q)\,t$" after the derivation of $P$; add one clause saying that $\eta$, $\rho$, $g$ and $h$ are constant so the flow rates can be summed.

## Checked
- Delta: the Kaava rewrite plus paragraph splits only; numbers, answers, ids, tasks and tolerances unchanged (exercises.json: only the teacher-approved removal of the example-data marker from captions).
- Wind tasks now start from $m = \rho A v t$, $E_\text{k} = \tfrac12 mv^2$, $P_\text{wind} = E_\text{k}/t$ and $\eta = P/P_\text{wind}$; water tasks from $E_\text{p} = mgh$, $m = \rho V = \rho Q t$, $P_\text{o} = E_\text{p}/t$ and $\eta = P/P_\text{o}$; the derivations are correct and the cancellation of $t$ is shown.
- The solved-for forms ($Q$, $\eta$, $E$, $k$ and $\eta = 2k/\rho A$) follow from the combined formula in the order shown, and each Substitution still uses them.
- The reflection that the combined formula is now derived in every solution matches the teacher's rule (basic laws, then combined formula, simplify to the end).
- Paragraph splits (Principle, Model answers, Reasonableness) give one idea per paragraph.
- Captures: none opened (derivation/presentation rewrite judged from the diff).
