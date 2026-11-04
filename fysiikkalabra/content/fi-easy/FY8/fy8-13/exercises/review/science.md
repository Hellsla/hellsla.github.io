VERDICT: PASS
CONTENT-HASH: 6f9c91031189e5cf

## Blocking

## Polish
- exercises/solutions.md:34 (L1-04, Periaate) — the added gloss "annosnopeus pienenee etäisyyden neliön verran" reads literally as a subtraction of r² and is imprecise next to the correct "kääntäen verrannollinen etäisyyden neliöön" — replace with e.g. "Se tarkoittaa, että kun etäisyys kaksinkertaistuu, annosnopeus pienenee neljäsosaan."
- Packet: `check_lesson.py has not been run`; run the deterministic checks before release.

## Checked
- One script recomputed all 12 answers with own formulas; all agree with exercises.json and answers.py within tolerance (4,17→4,2; 12,77→13; 18,92→19).
- Units and 2 % tolerances fit the data's significant figures.
- Point-source / no-air-attenuation and narrow-beam half-value-layer conditions stated or inherited from the brief; d½ given where used.
- L2-01 thyroid-only effective dose and L3-03 lung-alpha + whole-body-gamma sum (Σw_T = 1) correct.
- L2-03/L3-02 state proportionality and equal-occupancy assumptions; STUK figures consistent with the brief.
- L1-03 approximate dose rate flagged; result called a suuruusluokan arvio.
- Every solution complete, symbolic first, conversions right, sig-fig reasons and real reasonableness checks.
- Notation same as the brief (D, H_T, H_E, w_R, w_T, Ḣ, d_{1/2}, H_ka).
- Simplified-language splits keep every number and assumption of the Finnish set.
