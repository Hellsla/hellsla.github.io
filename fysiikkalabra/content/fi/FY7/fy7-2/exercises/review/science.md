VERDICT: PASS
CONTENT-HASH: 6f5c46b3a62a89ae

Full review of the exercise set (scope: a changed line carries a formula). This round changed L1-02 (electron: $|q| = e$, $|q|vB = mv^2/r$, $r = mv/(|q|B)$) and two chapter references (L2-03, L3-02).

## Blocking

None.

## Polish

None.

## Checked

- L1-02 now uses the charge magnitude for the electron, as the brief's Kaava ($F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$) does; every other task concerns a positive particle (proton, alpha, deuteron, ions), where $q = |q|$, so their $qvB$, $qU$ are right.
- Recomputed all twelve answers in one script with my own formulas: $1{,}20\cdot10^{-14}$ N; $7{,}58$ mm; $500$ km/s; $4{,}81\cdot10^{-16}$ J; $1{,}60\cdot10^{-13}$ N; $6{,}46$ cm; $3{,}45\cdot10^3$ km/s; $200$ km/s; $2{,}05$ mm/s; $4{,}01$ cm; $22{,}9$ MHz; $1{,}409$. All agree with answers.py and exercises.json within tolerance.
- Models: selector $v = E/B$ (L1-03, L2-03 with $E = U/d$); acceleration from rest $qU = \tfrac12mv^2$; L3-01 $r \propto \sqrt{m}$ at the same $U$, $q$, $B$, spots $2r$ apart; L3-02 $T = 2\pi m/(qB)$ independent of $v$ (non-relativistic); L3-03 $r \propto \sqrt{m/q}$. All conditions are met by the task texts.
- Checks are real: L1-02 proton on $\approx 14$ m; L2-04 ratio $\approx 5\cdot10^8$ at $10^6$ m/s; L3-01 $17\,\%$ heavier, $8\,\%$ larger radius.
- Significant figures justified by the limiting data; units and tolerances fit.
- Chapter references (*Homogeeninen sähkökenttä*, *Ympyrärata: jaksonaika ja ratanopeus*) carry no physics change.
- Hash same at start and end.
