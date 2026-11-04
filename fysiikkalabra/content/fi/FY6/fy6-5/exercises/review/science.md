VERDICT: PASS
CONTENT-HASH: b025248b5c0201e8

## Blocking

## Polish
- solutions.md:188 (fy6-5-L3-05 b) — "alle 0,01 V:n poikkeamalla": 4,01 V − 4,00 V is exactly 0,01 V, not under it — write "0,01 V:n poikkeamalla" or "mittaustarkkuuden rajoissa".
- solutions.md:189 (fy6-5-L3-05 Vastaus) — "Pienempi kuorma laskisi potentiaalin" is ambiguous (a smaller load usually means less current, which is the opposite) — write "Pienempi kuorman resistanssi".
- exercises.json:150 / solutions.md:145 (fy6-5-L2-05) — the Ohm check of each branch ($I = U : R$ with 12 V across every resistor) assumes an ideal source and ideal ammeters; the task does not say so (B-type, minor: the data agree with it) — add "Lähde, johtimet ja virtamittarit oletetaan ideaalisiksi."
- docs/exercise-bank/FY6.md plan, level 3 — the plan's error analysis "silmukka väärään suuntaan → negatiivinen virta" is not in the set; L3-05 (loaded voltage divider) replaces it. Update the plan or note the swap.

## Checked
- Hash b025248b5c0201e8 at start and end.
- All eight new answers recomputed in one script with my own formulas (node-voltage method for L3-04) and compared with exercises.json and answers.py: L1-08 3,0 V; L2-05 0,59 A; L2-06 40 Ω; L2-07 −3,0 V; L3-04 I₂ = 0,30 A (I₁ = 0,20 A, I₃ = 0,10 A, V_PQ = 6,0 V, 3,3 W = 3,3 W); L3-05 250 Ω. All agree within tolerance.
- L3-05 table checked against the divider model: 5,71 / 4,00 / 2,91 V against 5,72 / 4,01 / 2,91 V, labelled as example data; R_k = 236…266 Ω for V_P = 4,95…5,05 V, so 2 s.f. and 3 % fit.
- L3-04 signs: both loop equations follow the lesson's ΔV rules; the energy balance assumes the ideal sources the task states.
- L2-05: the branch readings equal U/R, so A₀ is the inconsistent one.
- L2-06: B and C are joined by a wire, so ΔV = 0; R₁ = R₃ = 30 Ω.
- L2-07: the student's error is the sign of the drop; −3,0 V and the −9,0 V minus pole are consistent.
- L1-06 and L1-07: exactly one correct option each; every distractor is really wrong and its feedback names the reason.
- Notation (V_A, U_AB, ΔV, RI, I₁ = I₂ + I₃) matches the lesson; scope within FY6 Kirchhoff and the LOPS note on branched circuits; no new task duplicates an existing one, and the levels fit.
