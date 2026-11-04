VERDICT: PASS
CONTENT-HASH: aca1e5e86a2b06fb

## Blocking

## Polish
- solutions.md:103 (L3-03): the rounding is justified "kuten kentissä 53 µT ja 55 µT", but the inclination limits the precision. With 82,5° ± 0,5°, cos I gives a ratio of 1,88–2,14. Fix: say that the steep inclination 82,5° limits the precision, so the answer is "noin 2".
- solutions.md:78 (L2-04): the same kind of issue. The 10° angle limits the result (9,5°–10,5° gives 9,3–10,4), so "noin 10" is the honest precision. Fix: name the 10° angle as the limiting datum, or keep 9,8 and say why.

## Checked
- I recomputed all nine numeric answers in one script with my own formulas: 6,0·10⁴; 13,7; 50,0; 60,8°; 49,7; 53,4; 9,82; −11; 2,03. They agree with answers.py and solutions.md. Every rounded answer falls inside its tolerance (L1-02: 14 against 13,7 is a 2,2 % difference, inside 3 %).
- L2-03 now uses B_v = 52 µT, which gives B = 53,4 µT and B_h ≈ 12 µT. These match WMM2025 for Rovaniemi.
- L3-03: Helsinki 53 µT and 74°, Longyearbyen 55 µT and 82,5°. These agree with WMM2025 to the stated rounding. The reason the compass works worse there (only the horizontal component turns it) is correct.
- L3-01: beside the middle of a magnet whose N pole points north, the field points south. 14 − 25 = −11 µT, so the needle reverses. The sign convention is stated.
- L2-02: B_z < 0 is consistent with a field pointing down when the phone lies flat. The horizontal part is 13 µT, which is realistic.
- L2-04: the condition that the fields are perpendicular is stated, so B_h cancels. The answer is the ratio tan 60° : tan 10°, and the wrong ratio of 6 is discussed.
- L1-04 and L1-05 word answers: the poles at the cut and the needle pointing away from the N pole are correct.
- L3-02: hard steel keeps the alignment. The Curie wording now reads "riittävän kuumaksi (… noin 770 °C)", as round 1 asked.
- Notation is the lesson's: B_h, B_m, B_v, I, θ from north, and tan θ = B_east : B_north. Every numeric solution solves symbolically before substituting.
