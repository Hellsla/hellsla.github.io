VERDICT: PASS
CONTENT-HASH: 775b15e10f821e0e

## Blocking

## Polish
- content/fi-easy/FY4/fy4-15/exercises/solutions.md (wind Kaava steps @@ -63, -93, -103, -172, -184, -234) — one sentence chains six formulas with "ja … joten … joten …", and the area is appended after the result ("…$= \tfrac12\eta\rho A v^3$, $A = \pi r^2$, josta …"); for S2 readers split it: the reference power, then the efficiency, then the area.
- solutions.md (@@ -93 and -103, ratio tasks) — the cancellation assumes $\eta$ (and $\rho$, $A$ or $v$) the same in both cases; the Kaava step could say so in four words ("kun $\eta$ ja $A$ pysyvät samoina"), as the brief's lesson does for the cube law.
- solutions.md (@@ -83, -158) — $t$ in $m = \rho Q t$ and in $E = Pt$ is the same span here, but the chain does not say it; "sama aika $t$" would avoid a doubt.
- Earlier polish (answers.py L2-01 comment 96,56) still open; not part of this change.

## Checked
- Hash 775b15e10f821e0e at the start and the end; since 062f457c28^ only `**Kaava:**` lines of solutions.md changed (numbers, answers, tolerances, tasks, ids, exercises.json, answers.py unchanged).
- Hydro chain: $E_\text{p} = mgh$, $m = \rho Q t$, $P_\text{o} = E_\text{p}/t = \rho Q g h$, $\eta = P/P_\text{o}$ → $P = \eta\rho Q g h$: the brief's derivation, assumption of small kinetic energy unchanged from the lesson.
- Wind chain: $m = \rho A v t$, $E_\text{k} = \tfrac12 mv^2$, $P_\text{tuuli} = \tfrac12\rho A v^3$, $\eta = P/P_\text{tuuli}$ → $P = \tfrac12\eta\rho A v^3$; $\eta$ defined against the undisturbed-wind reference power, as the brief says.
- Rearrangements right: $Q = P/(\eta\rho g h)$, $\eta = 2P/(\rho A v^3)$, $\eta = 2k/(\rho A)$ with $k = P/v^3$, $E = \eta\rho g h(\sum Q)t$, $P = \tfrac12\eta\rho\pi r^2 v^3$.
- Every Sijoitus substitutes into the last symbolic form; no number changed.
- Notation as in the brief ($P_\text{o}$, $P_\text{tuuli}$, $\eta$).
- Captures: none opened (fi-easy judged from text and the packet).
