VERDICT: PASS
CONTENT-HASH: 4b7ff3f15187576a

Follow-up review of the fix commit 2c31ff041 (delta from 6ed6d75dae7f928e, whose full review is kept below). Change: solutions.md L1-02 Given, `${|q| = e = 1.602 \cdot 10^{-19}\,\text{C}}$` grouped so it does not break across lines.

## Blocking

## Polish
- solutions.md L1-01, L1-05, L2-01–L3-03 write $qvB$, $qU$, $r = mv : (qB)$ with plain $q$; correct for the positive particles used. One clause in L1-01's Given ("$q = e > 0$, so $|q| = q$") would tie the notation to the lesson's.
- solutions.md L3-02: the speed-independent period holds only while $v \ll c$ (C).
- exercises.json L3-03: the unit "kertaa" is Finnish on the English page (language only).

## Checked
- The braces only group the expression; content and physics unchanged.
- L1-02 gives the electron's charge as magnitude $|q| = e$, $|q|vB = mv^2 : r$, $r = mv : (|q|B) = 7.581\,\text{mm} \to 7.6\,\text{mm}$ (recomputed).
- Recomputed all 12 answers: 1.2015 / 7.581 / 500 / 4.806 / 1.602; 6.463 / 3449 / 200 / 2.049; 4.006 / 22.86 / 1.409. All equal answers.py and lie within tolerance.
- answers.py physics per line: $qvB\sin\alpha$, $r = mv/(qB)$, $v = E/B$, $E = U/d$, $qU = \tfrac12 mv^2$, $qvB = mg$, $f = qB/(2\pi m)$, $r \propto \sqrt{m/q}$.
- Signs: every particle in an energy task is positive; the selector's charge cancels.
- Rounding follows the limiting datum; reasonableness magnitudes right.
- Hash at start and end: 4b7ff3f15187576a.
