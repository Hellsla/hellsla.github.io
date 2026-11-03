VERDICT: PASS
CONTENT-HASH: 9b7b3cfd647b8aba

## Blocking
- (none)

## Polish
- lesson.md:120 — "Kenttä on silloin lähes homogeeninen, eli se on joka paikassa samanlainen" can be read as "everywhere", though the sentence before limits it to inside the coil — write "joka kohdassa käämin sisällä samanlainen" (the next paragraph and the Kaava section already say the ends give about half).

## Checked
- Simplification against the passed fi version: every condition kept (long wire, other wires far; long coil, air inside, far from the ends; strong field compared with Earth's for the compasses); the electromagnet mechanism (domains aligned, soft iron loses its magnetisation, permanent magnet keeps it) intact; the measurement and uncertainty paragraph complete. The only additions are correct definitions (tangentti, alkeisalue, kierrostiheys).
- Every number in inquiry.json, exercises.json, solutions.md and exit-ticket.json is the same as in the fi version (number multiset diff empty); figures.json changes only alt-text wording, with the same values.
- One script with my own formulas: sim on load 1,232 mT (long coil 1,257); koe 1: 4,67/2,46/1,66/1,25 mT; koe 2: 2,46/2,41/1,25 mT, 0,363 mT at x = 12 cm; fit A = 2,465 mT/A, B₀ = 0,035 mT, ΔA = 0,0121; μ₀ = 1,233·10⁻⁶, 1,74 %, finite-coil factor 0,983 → 1,254.
- Worked example 12,57 mT, 251×, 3 sf/2 sf reasons right; Etsi virhe 5,03·10⁻⁵ T vs 5,03 mT; siirto 0,2653 A (mistakes 26,5, 3,33); check 2 1,5 mT (0,015, 9,42); wire graph 200/100/50 µT; hook 3 A at 1 cm ≈ 60 µT → ~77° against 14 µT, fits "lähes poikittain".
- Directions: wire-field side and top view CCW for upward current, compass N ends tangent and CCW; coil-field ⊙ top / ⊗ bottom gives B right, N right; sim dir = 1 (front strands down) gives +x, N right, outside lines N→S.
- Predictions: exactly one correct in ennuste-1, ennuste-2, kertaus, virhe, tarkistus-1; every distractor's feedback is right and quotes model values.
- Experiments: koe-1 varies only l, koe-2 only x; simState carries B and n.
- Exit ticket: N·I unchanged → B unchanged; CCW seen from the end → that end N.
