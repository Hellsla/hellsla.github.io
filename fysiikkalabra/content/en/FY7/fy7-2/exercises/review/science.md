VERDICT: PASS
CONTENT-HASH: 6ed6d75dae7f928e

## Blocking

## Polish
- solutions.md L1-01, L1-05, L2-01–L3-03 write $qvB$, $qU$, $r = mv : (qB)$ with plain $q$, while the lesson now writes $|q|$. For the positive particles used (proton, deuteron, alpha, C ions) $q = |q|$, so nothing is wrong; one clause in L1-01's Given ("$q = e > 0$, so $|q| = q$") would tie the notation to the lesson's.
- solutions.md L3-02: the speed-independent period holds only while $v \ll c$; the reasonableness check could say so (carried over, C).
- exercises.json L3-03: the unit "kertaa" is Finnish on the English page; use "times" (language only, carried over).
- The packet's exercise brief came out empty (the extractor found no Formula/Example sections in the English lesson); worth fixing in `review_packet.py` so notation can be checked against the lesson text.

## Checked
- Full review (changed lines with symbols since fa87d35): L1-02 now gives the electron's charge as magnitude $|q| = e$ and uses $|q|vB = mv^2 : r$, $r = mv : (|q|B)$. Correct: for a negative charge the radius uses the magnitude; the value is unchanged ($7.581\,\text{mm} \to 7.6\,\text{mm}$).
- Chapter references changed to *Uniform electric field* (FY6) and *Moving in a circle: period and speed* (FY5): both titles exist.
- Recomputed all 12 answers in one script with my own models: 1.2015 / 7.581 / 500 / 4.806 / 1.602; 6.463 / 3449 / 200 / 2.049; 4.006 / 22.86 / 1.409. All equal `answers.py` and lie within tolerance.
- answers.py physics per line: $qvB\sin\alpha$, $r = mv/(qB)$, $v = E/B$, $E = U/d$, $qU = \tfrac12 mv^2$, $qvB = mg$, $f = qB/(2\pi m)$, $r \propto \sqrt{m/q}$.
- Signs: every particle in an energy task ($E_\text{k} = qU$) is positive, so no signed-$q$ issue arises; the velocity selector's charge cancels.
- Rounding follows the limiting datum; reasonableness magnitudes right ($v/c$ 0.1–1.2 %, proton radius 14 m, ratio $\sim 5 \cdot 10^8$, $T \approx 44\,\text{ns}$).
- Every solution complete and symbolic first; scope FY7 with FY6/FY5 prerequisites.
- Hash at start and end: 6ed6d75dae7f928e.
