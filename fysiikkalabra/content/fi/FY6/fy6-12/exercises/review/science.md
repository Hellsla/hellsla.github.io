VERDICT: PASS
CONTENT-HASH: e5709d23a5337cd5

## Blocking

## Polish
- solutions.md L1-01 — "kolme merkitsevää numeroa kuten jännitteessä 240 V": 240 is ambiguous. The answer is fine; you could give 2,4·10² V or say the zero is significant.

## Checked
- All 12 answers recomputed independently (e, m_e, m_p as the course constants). They agree with answers.py and exercises.json within 0,01 %.
- L1-05: ex-vgraph (0 → 250 V over 5,0 cm, 50 V gridlines) gives V(4 cm) = 200 V and V(1 cm) = 50 V on gridlines, so the answer is 150 eV. The caption gives the same data and does not give the answer away.
- Signs: L2-01 is −75 eV for a proton moving along the field, and L2-02 is −120 eV for an electron at +120 V. Both are right.
- L3-01 energy conservation with the electron's E_p = −eV: 6,80·10⁶ m/s, and the Järkevyys √12 estimate is sound.
- L3-02 √(m_p/m_e) = 42,9 does not depend on U in the classical regime, and the condition is stated.
- L3-03: the proton (470 eV) stops at 15,7 mm in a 600 V gap, which is 4,3 mm from the + plate. The model and arithmetic are right.
- L2-03 alpha 4,39·10⁵ m/s, and L2-04 284 V.
- Every solution is complete, symbolic first, with correct conversions and real reasonableness checks. Notation (E_p, E_k, W for work) matches the lesson.
- All tasks are within the FY6 contents (potential in a homogeneous field), and speeds stay ≤ 2 % of c, so classical E_k holds.
