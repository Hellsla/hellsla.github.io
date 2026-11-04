VERDICT: PASS
CONTENT-HASH: 29c50a8511d2f29a

## Blocking
- (none)

## Polish
- (none)

## Checked
- Recomputed all 12 answers with my own formulas: L1 80 µT, 3,02 mT, 10 µT, 0,100 mT, 1,005 mT; L2 3,98 A, 8,57 cm, 2,50 mT (N = 198,9), 80 µT; L3 2,02 A, 15,0 km (N = 4775), 4,0 cm. All agree with exercises.json within tolerance.
- Every solution keeps all eight steps (Annettu … Järkevyys, 12/12, same as fi); every number identical to the fi version.
- Conditions kept in the simplified text: long straight wire, other conductors ignored (L1-03, L1-04), long coil (L1-02, L1-05, L2-01, L3-02 "Oleta käämi pitkäksi"), single layer with wire thickness ignored (L2-03), wire field perpendicular to B_h (L3-01).
- Superposition directions: L2-04 opposite currents add at the midpoint; L3-03 parallel currents cancel between, nearer the weaker current.
- Finite-coil caveats correct: L2-03 l = 5d (factor 0,98), L3-02 l = 1,6d (factor 0,848, "noin 85 %", more wire needed).
- Rounding reasons name the limiting data; symbolic solve before substitution everywhere.
