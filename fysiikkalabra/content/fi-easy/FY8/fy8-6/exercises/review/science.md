VERDICT: PASS
CONTENT-HASH: 492ee88e14080d3d

## Blocking

## Polish
- exercises.json L2-03 / L3-03 — stored answers 39.4 mW and 22.1 % carry three figures while solutions.md rounds to "noin 39 mW" and "noin 22 %" (two, from 20 mA and 15 mW); tolerance 2–3 % accepts both, so harmless — unchanged from the passed Finnish source.

## Checked
- All numbers, answers, units and tolerances identical to the passed Finnish source; only wording changed.
- Recomputed in one script with own formulas: L1 3,124e-19 J; 2,362 eV; 4,612e14 Hz; 873,2 nm; 6,568e-34 J s. L2 2,638 V; 6,304e-34 J s; 39,36 mW; 0,541 eV. L3 least-squares k = 4,212e-15 V s, b = −0,164 V, h = 6,748e-34 J s; Δh = 2,403e-35 J s; 22,08 %. All agree with answers.py and solutions.
- Principles in simplified wording stay correct: eU = work by the field; photon energy ≈ E_g; one electron gives at most one photon; fluorescence energy difference to heat (positive, ≈ one fifth).
- L2-01 and L2-02 state that measured U_k is ≈ 0,1 V below hf/e, so the single-LED h is low (−4,9 %) and the slope method is preferred — consistent with the lesson.
- L3-02: half the range of slopes, h = (6,6 ± 0,2)·10⁻³⁴ J s contains the accepted value.
- Every solution solves symbolically before substitution; conversions (nm→m, mA→A, J↔eV) correct; reasonableness checks are real (1240 V nm estimates, infrared beyond 700 nm, efficiency < 100 %).
