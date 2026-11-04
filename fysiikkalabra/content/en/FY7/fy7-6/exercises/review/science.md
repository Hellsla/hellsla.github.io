VERDICT: PASS
CONTENT-HASH: 5d735ce13b92c2f3

## Blocking

## Polish
- exercises.json:56 (L2-02) — "the magnetic flux through the coil" is read in the solution as the flux through one turn; "through each turn" would remove the ambiguity (same in fi).
- exercises/review/packet-science.md:53 — the "Exercise brief" block is empty in the en packet (the generator looks for Finnish section names); a review_packet.py fix, not the exercise set.

## Checked
- Numeric answers, units and tolerances identical to fi; the three word answers (L1-02, L1-05, L3-02) translate the Finnish ones faithfully.
- Recomputed in one script: L1 0.39 N, 100.8→1.0·10² kJ, 74 mW; L2 29 mW, 0.20 A, 0.151→0.15 m/s, 4.17→4.2 MW; L3 0.0727→0.073 K, 0.60 N (Fv = RI² = 1.8 W).
- Models: steady speed ⇒ F = mg (first law), P = Fv, Q = ΔEp − Ek, no heat loss and no change of state stated in L3-01; Lenz directions in L1-02 and L2-02 correct.
- L3-02 (Waltenhofen pendulum) and L1-05 (hob) model answers name the mechanism: eddy currents, Lenz braking, closed loops cut by the slits, glass an insulator.
- Solutions complete with symbolic solving, conversions, sig. figs and real reasonableness checks.
