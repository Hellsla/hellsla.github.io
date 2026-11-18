VERDICT: PASS
CONTENT-HASH: 6f58dd7af67209e9
## Blocking

## Polish
- solutions.md wind tasks (ratio $v^3$, ratio $d^2$, $\eta$ from 758 kW, cold air, student error, $k = P/v^3$) Kaava — the new chain joins steps with commas: "…, joten $P = \eta P_\text{tuuli} = \tfrac12 \eta\rho A v^3$, $A = \pi r^2$, josta $\eta = …$" reads as if $A = \pi r^2$ followed from the previous step. Fix: "Pinta-ala on $A = \pi r^2$." as its own sentence, and one "joten" per sentence.
- solutions.md hydro tasks with $E = Pt$ — "$P = \eta\rho Q g h$, $E = Pt$, joten $E = …$": same comma joining. Fix: "Energia on $E = Pt$, joten …".
- solutions.md L3 pumped storage (context, unchanged) — "$1{,}036 \cdot 10^{9}\,\text{kg} V = …$" lacks a separator between the two results.
- lessons/FY4/fy4-15/answers.py L2-01 comment 96,56 vs 96,53 m³/s (carried over).

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Hydro Kaava now derives as the brief's lesson does: $E_\text{p} = mgh$, $m = \rho Q t$, $P_\text{o} = E_\text{p}/t = \rho Q g h$, $\eta = P/P_\text{o}$, so $P = \eta\rho Q g h$; the time $t$ cancels before substitution; right.
- Wind Kaava: $m = \rho A v t$, $E_\text{k} = \tfrac12 m v^2$, $P_\text{tuuli} = \tfrac12\rho A v^3$, $\eta = P/P_\text{tuuli}$ (the lesson's definition of $\eta$ against the undisturbed wind); right.
- Solved forms unchanged and the ones substituted: $Q = P/(\eta\rho g h) = 96{,}53\,\text{m}^3/\text{s}$; $\eta = 2P/(\rho A v^3) = 0{,}4485$; ratios $(v_2/v_1)^3 = 3{,}375$ and $(d_2/d_1)^2 = 3{,}903$; $E = \eta\rho g h(\Sigma Q)t$.
- $P_\text{o}$ task without efficiency: $\rho Q g h = 2{,}92\,\text{MW}$; right.
- In the $E = Pt$ tasks the $t$ of $m = \rho Q t$ and of $E = Pt$ is the same span at constant flow, so no symbol clash.
- Paragraph splits change no wording or number; no answer, tolerance, task or id changed.
- Hash 6f58dd7af67209e9 at the start and at the end.
