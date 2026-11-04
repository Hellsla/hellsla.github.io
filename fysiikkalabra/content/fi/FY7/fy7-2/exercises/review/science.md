VERDICT: FAIL
CONTENT-HASH: 6a120d8900e19ff7

## Blocking
- exercises.json:126 and solutions.md:126 (L2-05) — **A**, unrealistic data. Protons at 2,0·10⁵ m/s have about 210 eV and stop in a cloud chamber's gas within a fraction of a millimetre, so they leave no 4–8 cm circles. Track 2 would be a negative particle with the proton's m : q, which in a cloud chamber could only be an antiproton. — Fix: keep the numbers in a vacuum chamber with a position-sensitive detector (an ion beam), and name track 2 an H⁻ ion in the Järkevyys line. Or keep the cloud chamber with MeV-range speeds and a stronger field.

## Polish
- solutions.md:182 (L3-04) — "kolme merkitsevää numeroa kuten kentässä": the 2-sig-fig radii limit the result. — Give about 23 u and name the radii as the limiting data.
- exercises.json:299 (L3-05) — "Proton ylittää" and "montako kertaa proton" should read "Protoni". — Also store the answer as 1.57 (exact 1,575), not 1.6.
- L3-05 overlaps L3-02: the same B = 1,50 T and the same T = 43,7 ns, explained again.
- solutions.md:142 (L2-07) — "yhtä ajassa" should be "yhtä lyhyessä ajassa".

## Checked
- I recomputed the new answers in one script (0,4265 mT; 1,786 ns; 1,025·10⁻⁸ kg/C; 78,9 %; 22,81 u; 1,575 µs). They match answers.py and exercises.json.
- L2-05: with B into the page and the motion to the right, the force on a positive charge points up, so tracks 1 and 3 are positive. m : q is 1,025 against the proton's 1,044 (·10⁻⁸ kg/C), and r₃ : r₁ = 2,05.
- L2-06: m ∝ d gives 25,1 u and 25,9 u. The shares 78,9 / 10,0 / 11,1 % match natural Mg.
- L3-04: r² = 2mU : (qB²) is correct. The fit through the origin gives 22,8 u and a free fit 22,7 u. Na-23's slope is 0,1192 cm²/V, so the identification and the reason for passing through the origin are sound.
- L3-05: v = 2,87·10⁷ m/s, E_k = 4,31 MeV and n = 71,8 ≈ 72 crossings, which is 36 revolutions, so t = 1,57 µs. The relativistic E_k for the same qBr is 0,23 % lower, so "alle prosentin" holds. Relativity appears only in a side clause.
- L1-06 and L2-07: each has one correct option, and every distractor's feedback is right.
- There are 8/7/5 tasks and the kinds match the plan. The L3 captures at 1280 px render without overflow.
