VERDICT: PASS
CONTENT-HASH: d656d012098aaf16

## Blocking
None. Both round-1 items are fixed:
- s5 c now asks for the OL3 time: 3,5 a, tolerance 0,05, consistent everywhere.
- s4 d now gives about three minutes and asks for the comparison.

## Polish
- **s2 e (C).** The model is a stated 10 Bq lung burden kept for one year, all α energy in 1,2 kg, w_R = 20 and w_T = 0,12 (ICRP 103). The result is one year's effective dose, not ICRP's 50-year committed dose, and the text does not claim otherwise.
  - PuO₂ (Type S) clears over years and partly moves to bone and liver, so the total dose would be larger.
  - Suggest one sentence in Järkevyys saying that dose also accrues in later years (the committed dose).
  - The magnitude is realistic. 10 Bq is about 16 pg of Pu-238, and ICRP 72 gives e(50) ≈ 1,6·10⁻⁵ Sv/Bq for inhaled Type S. Only 10–20 % of an intake deposits deep in the lungs, so 0,57 mSv a year from this burden is consistent.
- **s2 source_note** gives no source for w_R and w_T (ICRP 103) or for the 5,9 mSv (STUK, year), which the scope note requires.
- **s4 c "Hyväksytään myös":** "noin 2 min" (120 s) lies outside 136 s ± 5 %. It is fine as a verbal rounding, but a numeric checker would reject it.

## Checked
Hash d656d012098aaf16 at start and end. I recomputed the changed parts with my own script.
- s2 e:
  - E 2,83·10⁻⁴ J, D 2,36·10⁻⁴ Gy, H_T 4,71 mSv, H_E 0,566 mSv (9,6 % of 5,9 mSv).
  - The 5,5 MeV alternative gives 0,556 mSv, inside the tolerance.
  - Q includes the recoil energy, which is deposited locally, so that is correct. The skin dead-layer argument is correct.
  - Points total 20.
- s4: c 136,1 s (Vastaus ≈ 140 s); d 271,5 s. About 3 min in BBN models is correct.
- s5: c 3,49 a and a factor of 43 000; d 82 988 half-lives. Pu-239 →α U-235 is correct.
- s3: the residuals from the generating model are +,+,+,−,+,+,−,−,+ (within ±1,1 σ), now irregular.
  - Least squares gives d = 1,31 cm.
  - With d = 1,0–1,6 cm, r = 36,0–36,4 cm and H ≈ 0,23 µSv/h.
  - The tables and alt texts match.

Everything else is unchanged from round 1 and still agrees.
