VERDICT: FAIL
CONTENT-HASH: 9074195cdd27281d
SCOPE: delta caption-label,md-paragraphs,numbers,typography from 7a6a4a96cc364108 base 5b3ca4f

## Blocking
- content/fi/FY6/fy6-9/exercises/solutions.md:57, 67, 107, 189, 275 — (B, consistency) five Kaava blocks open with $\Sigma U = 0$. The lesson's latauspiiri section and the chapter *Kirchhoffin lait ja potentiaali virtapiirissä* state the voltage law as $\sum \Delta V = 0$, with signed potential changes. A sum of voltages, which are positive here, is not zero. The row also does not match the lesson's statement. Fix: write $\sum \Delta V = 0$, or "Jännitelaki:", on the first row. The signed row that follows, $U_\text{lat} - RI - R_\text{s}I - E = 0$, is right.

## Polish
- content/fi/FY6/fy6-9/exercises/solutions.md (L2 internal-energy task, Kaava) — $U = R_\text{s} I$ reuses $U$, which in this chapter is the terminal voltage ($U = E + R_\text{s}I$). Write $U_\text{s} = R_\text{s} I$.

## Checked
- Hash 9074195cdd27281d at start and end. Delta: the Kaava blocks of 15 tasks and the split paragraphs (L1-06, L3-01 c–d, L3-02).
- Every new derivation is algebraically correct and starts from $Q = It$, $W = UQ$, $W = Pt$, $P = UI$ or $\eta = W_\text{akku}/W_\text{lat}$, as the lesson writes them.
- L2 slope task: $I = U_\text{lat}/R_\text{kok} - E/R_\text{kok}$ gives slope $1/R_\text{kok}$, so 0,40 Ω.
- Discharge cell: $E = U_\text{ka} + R_\text{s}I$ matches the lesson's $U = E - R_\text{s}I$. It gives 0,10 Ω, and E = 3,75 V for both currents.
- Recomputed: I = 5,0 A; $R_\text{s}$ = 0,20 Ω; 97,5 min; 3240 J. answers.py runs; answers unchanged.
- The split paragraphs (c, d, Vastaus) keep the same claims and the safety wording.
