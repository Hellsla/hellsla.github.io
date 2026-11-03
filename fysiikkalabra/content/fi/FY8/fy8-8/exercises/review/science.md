VERDICT: FAIL
CONTENT-HASH: a5bd2fbf2d60a919

## Blocking
- exercises.json:48, solutions.md:52/56 (fy8-8-L2-01) — A: task cites NNDC NuDat 3 for Ni-60 levels "2505,7 keV ja 1332,5 keV"; ENSDF level energies are 2505,753 and 1332,514 keV, so the upper one rounds to 2505,8. Fix: drop the source attribution and write "noin 2505,7 keV" as the photon-energy sum, or give 2505,8 keV (difference 1173,3 keV, λ = 1,057 pm → 1,06 pm unchanged) and note in Järkevyys that the measured γ is 1173,2 keV because the recoiling nucleus takes ~0,01 keV.

## Polish
- solutions.md L1-04 Vastaus — rounding to three figures while the energy has four; "20,83 pm" as the stated answer would follow the limiting datum.

## Checked
- One-call recompute (own formulas): 143, 218, 7, 20,83 pm, 10, 1,057 pm, 82, 2,935·10⁵, 138, 4, 1,240 pm, 87 — all match answers.py and exercises.json.
- Nuclides: Rn-222 → Po-218, C-14 → N-14, F-18 β⁺ → O-18, Bi-214 → Po-214 → Pb-210, Th-232 → Ra-228 → Ac-228 → Th-228, Fr-226 → Ra-226 → Rn-222 all real decay modes.
- Th-232 series 6 α + 4 β⁻ matches the real thorium series.
- Am-241 59,54 keV and Cs-137 661,7 keV match ENSDF; joule conversions in L1-04, L2-01, L3-02 correct (unlike the lesson's worked example).
- Solutions symbolic first, conversions shown, reasonableness checks are real checks (L3-02 other lines 2,07 and 3,10 pm).
