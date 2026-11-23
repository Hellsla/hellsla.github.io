VERDICT: PASS
CONTENT-HASH: 11a5edfc26a94f6a
SCOPE: delta wording from 750761aac39f869c base a2442fe

## Blocking
- none

## Polish
- content/en/FY6/fy6-9/exercises/solutions.md (internal-energy task, Formula) — $U = R_\text{s} I$ reuses $U$, the terminal voltage in this chapter — write $U_\text{s} = R_\text{s} I$, as in fi.

## Checked
- Hash 11a5edfc26a94f6a at start and end. The diff changes only the first row of five voltage-law Formula blocks, $\Sigma U = 0$ to $\sum \Delta V = 0$, matching the lesson's Kirchhoff notation (signed potential changes) and the Finnish version; no $\Sigma U = 0$ is left.
- The signed rows that follow, $U_\text{ch} - RI - R_\text{s}I - E = 0$ and $U_\text{ch} - R_\text{tot}I - E = 0$, have the right signs for charging; the rearrangements to $I$, $R_\text{s}$, $R_\text{tot}$ and $I_k$ are unchanged and correct.
- Recomputed the touched answers: 5.0 A, 0.20 Ω, 33.3 %, 0.40 Ω, 7.125 h; they agree with answers.py.
