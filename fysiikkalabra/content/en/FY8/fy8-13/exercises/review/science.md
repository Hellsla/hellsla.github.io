VERDICT: PASS
CONTENT-HASH: ff5af81cc1f9f12e

## Blocking

## Polish
- Packet: the "Exercise brief" block is empty in the English packet (review_packet.py seems to extract the lesson sections by their Finnish headings Kaava/Esimerkki/…); the brief was judged from the lesson packet instead — fix the packet tool, not the exercises.
- Packet: `check_lesson.py has not been run` for the translation; run the deterministic checks before release.

## Checked
- One script recomputed all 12 answers with own formulas; all agree with exercises.json and answers.py within tolerance (L2-02 4.17→4.2, L2-03 12.77→13, L3-02 18.92→19).
- Units and tolerances fit: mGy, mSv, µSv, µSv/h, h, mm; 2 % tolerance covers the stated rounding.
- L1-04/L2-02/L3-01 state or inherit point source and negligible air attenuation; L1-05/L2-04/L3-01 use the narrow-beam half-value-layer model with d½ given.
- L2-01: thyroid only, w_R 1, w_T 0.04, 30 mGy → 1.2 mSv; L3-03 adds lung-only alpha (0.24 mSv) to whole-body gamma (0.50 mSv) correctly using Σw_T = 1.
- L2-03/L3-02 state the proportionality and same occupancy assumptions; STUK 94 Bq/m³ ↔ 4.0 mSv and others 1.9 mSv consistent with the lesson.
- L1-03 flight dose rate flagged as approximate; answer called an order-of-magnitude estimate.
- Every solution has Given/Asked/Principle/Formula (symbolic first)/Conversions/Substitution/Answer with sig-fig reason/Reasonableness; reasonableness checks are real (halving chains, back-substitution).
- Notation (D, H_T, H_E, w_R, w_T, Ḣ, d_{1/2}) same as the lesson.
- Content and numbers identical to the Finnish exercise set.
