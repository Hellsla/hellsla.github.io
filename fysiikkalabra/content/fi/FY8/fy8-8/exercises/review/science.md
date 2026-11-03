VERDICT: FAIL
CONTENT-HASH: 041806ccd347a404

## Blocking
- solutions.md L2-01 Järkevyys — A (causality, magnitude): "ero 0,1 keV syntyy, koska ydin saa fotonin lähtiessä rekyylin". The recoil of Ni-60 for a 1173 keV photon is $E^2/(2Mc^2) \approx 0{,}012\,\text{keV}$; the 0,1 keV between 1173,3 (from the rounded levels 2505,8 − 1332,5) and the measured 1173,2 keV is almost all rounding: the exact ENSDF level difference is 2505,753 − 1332,514 = 1173,24 keV. Fix: "Mitattu gammafotoni on 1173,2 keV; ero johtuu lähes kokonaan tasojen pyöristyksestä (tarkka tasojen erotus on 1173,24 keV), ja ytimen rekyyli vie vain noin 0,01 keV. Ero ei muuta aallonpituutta kolmen numeron tarkkuudella."

## Polish
- solutions.md L2-01 Sijoitus — printed 1,9865/1,8796 gives 1,0569, full precision 1,0568; either is fine, but 1,057 is the stated value, so the fifth figure could be dropped.
- solutions.md L1-04 Vastaus — rounding to three figures while 59,54 keV has four; "20,83 pm" would follow the limiting datum (unchanged from round 1).

## Checked
- Round 1 fixed: L2-01 gives the level as 2505,8 keV (ENSDF 2505,753) with no false source attribution; answers.py uses 2505,8 − 1332,5; answer 1,06 pm (recomputed 1,0568) within tolerance.
- One-call recompute with own formulas: 143, 218, 7, 20,83 pm, 10, 1,057 pm, 82, 2,935·10⁵, 138, 4, 1,240 pm, 87: all match answers.py and exercises.json.
- Joule conversions L1-04, L2-01 (1,8796·10⁻¹³ J), L3-02 correct.
- Nuclide chains Rn-222 → Po-218, C-14 → N-14, F-18 β⁺ → O-18, Bi-214 → Po-214 → Pb-210, Th-232 → Ra-228 → Ac-228 → Th-228, Fr-226 → Ra-226 → Rn-222 are real decay modes; Th series 6 α + 4 β⁻.
- Solutions symbolic first, Vastaus lines now state exact counts plainly; reasonableness checks are real checks.
