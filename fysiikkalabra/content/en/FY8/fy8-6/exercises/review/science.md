VERDICT: PASS
CONTENT-HASH: ab442a1660bb0c08

## Blocking

## Polish
- exercises.json:65 — L2-03 stores 39.4 mW while the solution's answer is "about 39 mW, two significant figures" — store 39 or state the answer as 39.4 (tolerance covers both).
- exercises.json:99 — L3-03 stores 22.1 % while the solution says "about 22 %, two significant figures" — same alignment.

## Checked
- Exercise brief in the packet is empty (tool bug); judged against the English lesson's formula, example and misconception sections instead.
- Recomputed all 12 answers in one script with my own formulas (E = hc/λ, eU_k ≈ hc/λ, h = ek, P = (I/e)·hc/λ, least-squares fit for L3-01: k = 4.212e-15 V s, b = −0.164 V): all within 0.12 % of exercises.json and answers.py.
- L2-02 single-LED h = 6.30e-34 J s and its explanation (U_k slightly below hf/e, so use the slope) is correct physics.
- L2-04 fluorescence heat 0.541 eV and L3-03 external efficiency 22 % (≤ 100 %) are physically sound; assumptions stated in the task text.
- L3-02 half-range uncertainty 2.4e-35 J s; accepted value inside (6.6 ± 0.2)e-34 J s.
- Every solution solves symbolically first, converts units, gives a sig-fig reason and a genuine reasonableness check.
- Scope: within FY8 (photon energy, LED threshold, Planck constant from data).
