VERDICT: PASS
CONTENT-HASH: ef00abf4751d27fa

## Blocking

## Polish
- lessons/FY4/fy4-15/answers.py:19 — the comment still says 96,56 m³/s; the value is 96,53 (carried from my earlier report) — "96,53".
- solutions.md (L1-04, L2-02, L3-01, L3-02, L2-07, L3-04, L1-09) — the same full derivation of $P_\text{wind} = \tfrac12\rho Av^3$ is repeated word for word in every wind task, and the subscript is written both $P_\text{wind}$ and $P_{\text{wind}}$ — one spelling; the repetition is a pedagogy choice, physics right.

## Checked
- Hash ef00abf4751d27fa at start and end; only solutions.md (and captions in exercises.json, "(example data)" removed) changed; no answer, tolerance, task or id changed.
- Captures: none opened; judged from the text and the packet's diff.
- Hydropower Kaava (L1-01, L2-01, L2-03, L2-04, L2-06, L1-07): $E_\text{p} = mgh$, $m = \rho V = \rho Qt$, $P_\text{o} = E_\text{p}/t = \rho Qgh$, $\eta = P/P_\text{o}$, so $P = \eta\rho Qgh$; correct, $t$ cancels, symbols as in L1-03 ($P_\text{o}$).
- Wind Kaava: $m = \rho Avt$ (cylinder of undisturbed air), $E_\text{k} = \tfrac12 mv^2$, $P_\text{wind} = E_\text{k}/t = \tfrac12\rho Av^3$, $P = \eta P_\text{wind}$; correct and the stated condition (below rated power) kept.
- L2-01: $Q = P/(\eta\rho gh)$ solved symbolically before substitution; $96.53\,\text{m}^3/\text{s}$ unchanged.
- L2-02: $\eta = 2P/(\rho Av^3)$ after $A = \pi r^2$; $0.4485$ unchanged.
- L3-01, L3-02: ratios $(v_2/v_1)^3 = 3.375$ and $(d_2/d_1)^2 = 3.903$ follow, $\eta$, $\rho$ cancel.
- L3-04: $k = P/v^3 = \tfrac12\eta\rho A$, $\eta = 2k/(\rho A) = 0.399$ unchanged; rated-power limit kept.
- L2-06: $E = \eta\rho gh(\Sigma Q)t$ with equal month lengths; $18.8\,\text{GWh}$ unchanged.
- Paragraph splits (L1-06, L2-06 b, L2-07, L3-04, L3-05, L2-08, L2-10) move no claim; no energy "into heat" wording.
