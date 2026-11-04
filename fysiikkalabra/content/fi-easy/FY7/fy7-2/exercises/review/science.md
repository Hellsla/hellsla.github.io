VERDICT: PASS
CONTENT-HASH: 208276c111678272

Follow-up review of the fix commit 2c31ff041 (delta from 18dbe8d3089c1497). Change: solutions.md L1-02 Annettu, `${|q| = e = 1{,}602 \cdot 10^{-19}\,\text{C}}$` grouped so it does not break across lines.

## Blocking

## Polish
- solutions.md L1-01, L1-03, L1-05, L2-01…L3-03 use $q$ in $qvB$, $qU$, $r = mv/(qB)$; correct because every particle there is positive, but "$|q| = q$, koska varaus on positiivinen" once would mirror L1-02.

## Checked
- The braces only group the expression; content and physics unchanged. L1-02 $r = mv/(|q|B) = 7{,}581\,\text{mm} \to 7{,}6\,\text{mm}$ recomputed; proton comparison about 14 m.
- All 12 answers recomputed earlier: 1,2 / 7,6 / 500 / 4,8 / 1,6 / 6,5 / 3400 / 200 / 2,0 / 4,0 / 22,9 / 1,41; agree with answers.py and exercises.json.
- L2-01, L3-03: $v = \sqrt{2|q|U/m}$ before $r = mv/(|q|B)$; L3-03 $r \propto \sqrt{m/q}$, ratio $\sqrt2$.
- L2-03 $E = U/d$, $v = E/B$; L2-04 $qvB = mg$, 2,0 mm/s; L3-01 spot separation 4,0 cm; L3-02 22,9 MHz, 44 ns.
- Speeds at or below 1 % of c; every solution symbolic first; units and tolerances fit.
- Hash same at start and end.
