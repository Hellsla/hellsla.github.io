VERDICT: FAIL
CONTENT-HASH: c63477ece610534e
Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at 83e0790e263a8568.

## Blocking
1. inquiry.json, task with solution (electron at x = 3.0 cm), Kaava/Formula line: the symbol U now has two meanings in one solution. Principle (and hint 1, hint 2, the distractor feedback, the earlier tasks) use U as the positive potential difference travelled, with "potential energy decreases by eU" and "1/2 mv^2 = eU", U = 150 V. The rewritten line sets U = V_0 - V = -150 V, so "decreases by eU" would be negative and "W = eU" no longer holds. A student reading Principle then Formula meets a contradiction and an unmotivated sign flip.
Fix: keep U for the positive difference and take the sign step with another symbol, e.g. "Elektronin varaus on Q = -e. Kenttä tekee työn W = Q(V_0 - V) = e(V - V_0) = eU, kun U = V - V_0 on kuljettu potentiaaliero. Työ muuttuu liike-energiaksi ..." (same in en and fi-easy). Or change Principle and hints to the same convention.

## Polish
The sign argument itself (Q = -e, start minus end) is the right one and staged well; only the symbol must be consistent.

## Checked
Diff of the Kaava line only, read against Principle, hints, feedback and Substitution in the same task. Algebra e(V - V_0) and the final formula are correct; Substitution unchanged and consistent. Not read: other tasks beyond grep.
