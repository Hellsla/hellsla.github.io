VERDICT: PASS
CONTENT-HASH: 90d7f4085a7303ff

## Blocking

## Polish
- exercises/solutions.md (fy3-6-L2-09, Kuvaajan lukeminen) — "kupari lämpenee ja jäähtyy helposti" is still per kilogram and per kelvin; "samalla massalla ja lämpötilan muutoksella vähän lämpöä" would keep the C-level simplification exact (carried over from the previous report, not blocking).

## Checked
- Diff: the doubled lead-in "Kuvaajan lukeminen kuvasta:" removed in fy3-6-L2-09; no number, symbol or physics changed.
- The reading still gives $c = 385\,\text{J/(kg·K)}$ from the copper bar of `fy3-6/c-bars` (the generator prints 385 beside the bar), and the shortest bar matches the smallest $c$.
- answers.py and every other line of the solution unchanged; earlier PASS stands for the rest of the set.
- Hash same at start and end.
