VERDICT: PASS
CONTENT-HASH: 89df6326aca699a5

## Blocking

## Polish
- solutions.md L1-04 Vastaus — rounds to three figures while 59,54 keV has four; "20,83 pm" would follow the limiting datum (the line says both are right, so not an error).
- solutions.md L2-03 Järkevyys — "Ytimen tasojen erot ovat satojatuhansia kertoja suurempia kuin atomin elektronien tasojen erot": true for outer-electron (visible) transitions, not inner shells (keV); "kuin näkyvän valon fotonien energiat" says what the brief says.

## Checked
- Round 2 blocking fixed: L2-01 Järkevyys now attributes the 0,1 keV to rounding of the levels (exact 1173,24 keV) and the recoil to ≈ 0,01 keV (recomputed E²/(2Mc²) = 0,0123 keV); aallonpituus unchanged at three figures (1,0568 vs 1,0569 pm).
- One-call recompute with own formulas: 143, 218, 7, 20,83 pm, 10, 1,057 pm, 82, 2,935·10⁵ (→ 2,93·10⁵ correct), 138, 4, 1,240 pm, 87 — all match answers.py and exercises.json within tolerance; 1332,5 keV → 0,931 pm right.
- Joule conversions L1-04, L2-01 (1,8796·10⁻¹³ J), L3-02 (1,602·10⁻¹³ J) correct.
- Real decay modes: Rn-222 → Po-218, C-14 → N-14, F-18 β⁺ → O-18, Bi-214 → Po-214 → Pb-210, Th-232 → Ra-228 → Ac-228 → Th-228, Fr-226 → Ra-226 → Rn-222; Th series 6 α + 4 β⁻.
- Conservation of A and Z stated with the e/positron charge numbers; antineutrino/neutrino included as in the brief.
- Solutions symbolic first; exact counts stated plainly; reasonableness checks are real checks; notation matches the brief.
