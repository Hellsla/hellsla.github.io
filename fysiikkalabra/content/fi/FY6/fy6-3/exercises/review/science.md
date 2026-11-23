VERDICT: PASS
CONTENT-HASH: 58ff29a1ecb104bc
SCOPE: delta md-paragraphs,numbers,typography,wording from 2eb18a63c0e1ad44 base 5b3ca4f

## Blocking

## Polish
- exercises.json (fy6-3-L2-08): "samalla kytkennällä tehty esimerkkimittaus" still reads as if the table had been measured; "laadittu" would be exact. This was in the earlier report.
- solutions.md:153, :163, :173, :201 — these Kaava steps are still written as prose with "ja". They already start from $R = U/I$, so this is only a matter of consistency with the new aligned form.

## Checked
- Hash read at start and end: 58ff29a1ecb104bc, unchanged.
- Every changed Kaava step starts from $R = U/I$ or $R = \rho l/A$ and solves in symbols. Each row is right: $U = RI$, $I = U/R$, $A = \rho l/R$, $r = d/2$ with $A = \pi r^2$, $\rho = (R/l)A$, and $I_2 = U/R_2$ with $R_2 = 2R_1$.
- L3-01 (stretched wire): $l_2 = 2l_1$ and $A_2 = A_1/2$ (the volume is the same) give $R_2 = 4R_1 = 3{,}2\,\Omega$. This is correct.
- L2-08: $R = U/I$, $I = U/R$ and the slope $\Delta I/\Delta U = 1/R$ give $R = 40{,}0\,\Omega$. This is consistent with the stated axes: $U$ is on the horizontal axis, and the chapter's characteristic curve has its axes the other way round.
- The paragraph splits in L1-07, L2-05, L2-07, L1-10 and L2-08 change no claim or number. The diode, lamp and resistor reasoning still matches the brief (resistance is $U : I$ at each point, not the slope).
- I recomputed all 10 answers touched by the diff in one script, and they agree with answers.py: $3{,}3\,\text{V}$, $10\,\text{A}$, $0{,}375\,\text{A}$, $1{,}7\,\text{mm}^2$, $7{,}96\,\Omega$, $3{,}2\,\Omega$, $3{,}0\,\text{A}$, $0{,}30\,\text{A}$, $40{,}0\,\Omega$ and $38{,}1\,\%$.
