VERDICT: PASS
CONTENT-HASH: adf179dab48987e9

## Blocking

## Polish

## Checked
- All numbers in exercises.json and solutions.md match the passed Finnish source token for token.
- Recomputed with own formulas: L1-01 143, L1-02 218, L1-03 7, L1-04 20,83 pm, L1-05 10; L2-01 1,057 pm, L2-02 82, L2-03 2,935·10⁵, L2-04 138; L3-01 4, L3-02 1,240 pm (others 2,07 and 3,10 pm), L3-03 87. All agree with exercises.json and answers.py.
- L2-01 reasonableness: exact ENSDF level difference 1173,24 keV, recoil ≈ 0,012 keV — statements correct.
- L2-02 chain Bi-214 → Po-214 → Pb-210 and sim steps 9→11 correct; "heti" fits Po-214 (164 µs).
- L2-04 chain Th-232 → Ra-228 → Ac-228 → Th-228 correct, neutron bookkeeping 142 − 4 = 138 correct.
- L3-03 back-tracking gives Fr-226 → Ra-226 → Rn-222, consistent.
- Every solution states the principle (conservation of A and Z, photon energy = level difference) before substitution; units and conversions right.
- Significant figures justified by the limiting datum in each numeric task (550 nm → 3 figures in L2-03, 1,00 MeV in L3-02).
- Easy-language rewrites keep the physics: β⁻ neutron→proton, β⁺ proton→neutron with positron and neutrino.
