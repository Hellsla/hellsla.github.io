VERDICT: PASS
CONTENT-HASH: 237d1351779316d8
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 96c26f38f6eaa964.

## Blocking
(none)

## Polish
1. `inquiry.json`, `sovella/tasks.json` and `sovella/solutions.md` still write the fuel energy as $E = Hm$, while the theory and the map now use $Q = Hm$. The physics is the same. Fix: change these to $Q = Hm$.

## Checked
$Q = Hm$ is MAFY's form. $Q$ is defined in J, and the conditions (complete burning, the heating value for the actual moisture) are kept. The map's fuel node says $Q = Hm$. No other formula changed. The other rows are unchanged.
