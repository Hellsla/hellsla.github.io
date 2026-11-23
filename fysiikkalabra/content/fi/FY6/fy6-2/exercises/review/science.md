VERDICT: PASS
CONTENT-HASH: f57c156658def7ed
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 7a0d19ceab83f0dd base e238aa9

## Blocking

## Polish
- solutions.md:85 — L2-04's Kaava now opens with $\Sigma U = 0$ and $U_\text{lamppu} = R_\text{lamppu} I$. The physics is right (signed loop sum, $I \approx 0$), but neither Kirchhoff's loop law nor $R I$ is in this chapter's brief: both are taught in later chapters. Level 2 should need only what the lesson teaches. Fix: open with "pariston jännite jakautuu mittarille ja lampulle: $U_\text{paristo} = U_\text{m} + U_\text{lamppu}$", as the Periaate already says it in words. The same applies to the $(\Sigma U = 0)$/$(\Sigma I = 0)$ tags in L3-04 (line 209), which is less of a concern at level 3.
- solutions.md:25, :191, :209 — the symbol $s$ means three different things: a relative error limit (L1-03), the half-range estimate of scatter (L2-07, new) and the relative decrease (L3-04, new). The lesson uses $\tfrac{\Delta x}{x}$ for a relative error limit. Fix: use distinct symbols, or keep the words, in L2-07 and L3-04.

## Checked
- Hash read at start and end: f57c156658def7ed, unchanged.
- Every changed Kaava step (L2-01, L2-03, L2-04, L2-05, L2-07, L3-04, L3-05, L2-10) starts from the error-limit formula $\Delta x = p x + n r$ or from the circuit relations, and solves in symbols. Every row is algebraically right.
- L3-04: the chain $U_0 = U_1 + U$, $I_1 = I_2 + I_\text{m}$, … ends at $U = U_0 / (1 + R_1/R_2 + R_1/R_\text{m})$. It is correct. The algebra moved out of Sijoitus has not been lost: it now sits in Kaava.
- L3-05: $\Delta R/R = \Delta U/U + \Delta I/I$ (the quotient rule for error limits), then $\Delta R = (\Delta R/R) R$. This is correct.
- I recomputed all 10 answers touched by the diff in one script, and they agree with answers.py: $10{,}57\,\%$, $3{,}20$, $9{,}0\,\text{V}$, $2{,}17\,\%$, $0{,}1522\,\text{V}$, $0{,}08245\,\text{V}$, $4{,}76\,\%$, $2{,}90\,\Omega$, $0{,}02685\,\text{V}$ and $2{,}98$.
- The paragraph splits in L3-03, L1-06, L1-07, L2-07, L3-04 and L3-05 change no claim or number. The physics is the same as before: the series ammeter, the fuse, OL, and the limit compared with the meter's loading.
- Caption change: the esimerkkiaineisto marker was removed by the teacher's approval. The multimeter figure still gives $1{,}37\,\text{V}$ on the $20\,\text{V}$ range, as L2-09 and L2-10 read it.
