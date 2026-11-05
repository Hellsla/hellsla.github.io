VERDICT: PASS
CONTENT-HASH: 9659167e822811b0

## Blocking

## Polish
- exercises/solutions.md:169 — fy5-16-L2-07 (replaced): the answer to b) (100 dB → 8 h : 2⁵ = 15 min) is already printed in the lesson's Esimerkki Järkevyys and in this chapter's L3-05 Järkevyys. The error analysis in a) is new, but b) can be read off. Use 103 dB instead: the student gets 18 : 3 = 6 and 8 h : 6 = 1,3 h; the correct time is 8 h : 2⁶ = 7,5 min. Update the solution and answers.py to match.
- exercises/solutions.md:185 — L2-07 Järkevyys: "vaikka taso on selvästi toiminta-arvon yli" does not make sense as a check. Write "ja oppilaan virhe on sallivaan suuntaan, joten se olisi vaarallinen".
- docs/exercise-bank/FY5.md:100 — the plan still says "Virheanalyysi: dB-arvot laskettu yhteen". Change it to "Virheanalyysi: aika jaettu luvulla n eikä 2ⁿ" so the plan matches the set.

## Checked
- Round-1 Blocking resolved: L2-07 is replaced by an error analysis of the exposure-time rule (100 dB, n = 5; the student divides by 5 and gets 1,6 h, the correct value is 8 h : 32 = 0,25 h = 15 min). The direction of the error is explained: the student's time is too long, 96 min against 15 min. It is not a duplicate of fy5-15 (no exposure tasks there) or of any other FY5 chapter: "toiminta-arvo" occurs only in fy5-16.
- Round-1 Blocking resolved: L2-06 b now gives the barrier height (3,0 m). λ₁₂₅ = 2,74 m against 3,0 m and λ₄₀₀₀ = 0,086 m support the model answer.
- Round-1 Polish done: the heading is "Taulukon lukeminen", L3-05 c says the listener keeps the plugs in at 16 m, and the L1-06 distractor is now "puhumaan hiljempaa" with correct feedback.
- Recomputed in one script: L1-07 27 dB; L2-05 T 1,51 s → 0,599 s, 60,3 %; L2-06 11,8 dB; L2-07 15 min; L3-04 D = 3,375, ΔL = 5,26 dB, with the enclosure D = 1,57 (1,96 dB ≈ 2,0 dB); L3-05 100 dB, 1,59 h, 189 %, 47 %. All match answers.py and the solutions.
- Scope: noise dose, reverberation, barrier diffraction and the loudspeaker principle are all in the slot. The assumptions (6 dB per doubling, the same attenuation at every level) are stated and not contradicted.
- The L2-07 capture (L2-1280-9) renders cleanly at 1280 px. The plan 8/7/5 is met.
