VERDICT: PASS
CONTENT-HASH: b23b73f81e2a6b5b

## Blocking

## Polish
- solutions.md:107 (L3-02 Sijoitus) — the chain ends "$= 2{,}0\,\mu\text{m}$" while Vastaus gives "$2\,\mu\text{m}$". End the chain at $2\,\mu\text{m}$, or add "≈".
- solutions.md:28 / exercises.json L1-03 — a student who applies the lesson's rounding enters $0{,}4\,\text{s}$, which is 14 % off with tolerance 0.02. The task asks for the half-range itself and the solution explains this, so the answer is not wrong. A wider tolerance (0.15) would accept both.
- solutions.md:68 (L2-02) — "kolmen lukeman keskiarvo kantaa yhden numeron lisää" is not a sound rule (open since round 2).
- solutions.md:49 (L1-05) — "ei voi olla asteikkoväliä suurempi" is too absolute; and :99 (L3-01) "lähes kokonaan" means two thirds cancel. Both are open since round 2.
- solutions.md:18 (L1-02) — the task asks for the sign, so give $+0{,}3\,\text{cm}$ in Vastaus. Spelling: :58 writes "virhearvio".

## Checked
- Round-3 blockers re-judged against the lesson's convention (one figure, two if the first digit is 1). L3-02 now gives $2\,\mu\text{m}$ with one figure, and answer 2.0 accepts it. L3-03 now gives $0{,}025 \approx 0{,}03\,\text{cm}$ (first digit 2, so one figure), and "noin kymmenesosa" (0,03 : 0,26) is right.
- Every other estimate follows the same convention. L1-03 says the estimate rounds to $0{,}4\,\text{s}$; L1-05 gives $0{,}5\,\text{mm}$; L2-01 gives $0{,}09\,\text{s}$ and $5\,\%$ (accepted, 3,5 % off); L2-04 gives $0{,}2$ and $0{,}02\,\text{cm}$.
- L1-02 now names a worn tape start. Physics right: when the start is worn away the tape reads too long, so the sign is positive, as in L2-02.
- One script recomputed all 12 answers independently, and each matches answers.py and exercises.json. Tolerances accept the solutions' rounded answers.
- The systematic corrections (L2-02 10,7 mm; L3-03 0,26 cm) are subtracted from readings, not reported as uncertainties, so keeping them at the data's precision is right.
- Signs and magnitudes: L3-01 −0,06 s (late start shortens the reading); paper 100 µm, so the error is 2 %; tape about 1 %. Conversions are done by substitution.
- No ×, \times or ÷; \cdot in products; the error symbols are Δx, Δt, Δt_sys, ΔL_sys and Δh.
- Content hash is identical at the start and the end.
