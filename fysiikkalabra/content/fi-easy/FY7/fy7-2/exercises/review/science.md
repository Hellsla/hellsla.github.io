VERDICT: PASS
CONTENT-HASH: 18dbe8d3089c1497

## Blocking

## Polish
- solutions.md L1-01, L1-03, L1-05, L2-01…L3-03 use $q$ in $qvB$, $qU$, $r = mv/(qB)$; this is correct because every particle there is positive, but stating "$|q| = q$, koska varaus on positiivinen" once in the given values would mirror L1-02 and the lesson's $|q|$ convention.

## Checked
- All 12 answers recomputed in one call; they agree with answers.py and exercises.json: 1,2 / 7,6 / 500 / 4,8 / 1,6 / 6,5 / 3400 / 200 / 2,0 / 4,0 / 22,9 / 1,41.
- L1-02 electron: magnitude $|q| = e$ used throughout; the proton comparison at about 14 m checked.
- L2-01 and L3-03: $v = \sqrt{2|q|U/m}$ is used before $r = mv/(|q|B)$; L3-03 gives $r \propto \sqrt{m/q}$, ratio $\sqrt2$, and the alpha is slower as stated.
- L2-03: $E = U/d$ before $v = E/B$; L2-04: $qvB = mg$ gives 2,0 mm/s, and the $10^8$–$10^9$ ratio at $10^6\,\text{m/s}$ checked.
- L3-01: $r \propto \sqrt m$ at the same U; the spot separation is twice the radius difference, 4,0 cm, and the figures are justified.
- L3-02: $T = 2\pi m/(qB)$ is independent of v; 22,9 MHz and 44 ns checked.
- Speeds stay at or below 1 % of c, so the classical formulas are valid and the solutions say so.
- Every solution has all seven parts and solves symbolically first.
- Units and tolerances fit the data's significant figures.
