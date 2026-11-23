VERDICT: PASS
CONTENT-HASH: f4c96813537f2d5f
SCOPE: delta caption-label,md-paragraphs,numbers,typography from 7a6a4a96cc364108 base 5b3ca4f

## Blocking
- none

## Polish
- content/fi/FY6/fy6-9/exercises/solutions.md (L3-03, Kaava) — $U = R_\text{s} I$ reuses $U$, which in this chapter is the terminal voltage ($U = E + R_\text{s}I$) — write $U_\text{s} = R_\text{s} I$.

## Checked
- Hash f4c96813537f2d5f at start and end. Round-1 blocker fixed: all five voltage-law Kaava blocks (L2-01, L2-02, L2-07, L3-02, L3-05) now open with $\sum \Delta V = 0$, the lesson's Kirchhoff notation; no $\Sigma U = 0$ is left in fi, en or fi-easy.
- The signed row after it, $U_\text{lat} - RI - R_\text{s}I - E = 0$, has the right signs for charging (the current crosses the battery from + to −), and every rearrangement to $I$, $R_\text{s}$, $R_\text{kok}$ and $I_k$ is algebraically correct.
- The other new Kaava blocks start from $Q = It$, $W = UQ$, $W = Pt$, $P = UI$ and $\eta = W_\text{akku}/W_\text{lat}$, as the lesson writes them, and end in the symbolic form that is substituted.
- L3-04: $E = U_\text{ka} + R_\text{s}I$ matches the lesson's discharge relation $U = E - R_\text{s}I$; it gives $0{,}10\,\Omega$ and $E = 3{,}75\,\text{V}$ for both currents.
- Recomputed every answer in one script with my own formulas: 16 h, 4,0 Ah, 5,2 h, 5,0 A, 0,20 Ω, 97,5 min, 84 %, 9,3225 Wh, 1,5 Wh, 0,40 Ω, 61,05 Wh, 4,2 h, 1,28, 33,3 %, 3,24 kJ, 77,45 %, 7,125 h (and 6,0 h). All agree with answers.py.
- The split paragraphs (L1-06, L3-01 c–d, L3-04) keep the same claims and the safety wording; the energy wording follows the guardrail (sisäenergiaksi, joka siirtyy lämpönä).
- Captions: only the marker esimerkkiaineisto was removed; the data are unchanged.
