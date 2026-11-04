VERDICT: FAIL
CONTENT-HASH: 774f599797081eff

## Blocking
- exercises.json:272/291 (fy5-4-L3-04) — A: the data break energy conservation, which the task itself assumes ("ilmanvastus ja vierimisvastus jätetään huomiotta", a circular loop). With r ≈ 13,9 m, the top needs v_ala² − v_ylä² = 4gr = 547 m²/s², but the data give 288. A frictionless circular loop always gives N_ala ≥ 6mg; the data give 4,5mg. Fix: keep the top row and make the bottom row energy-consistent: v = 27,2 m/s, a_n = 53,4 m/s². Then N_ala = 3,79 kN ≈ 6,4mg. Update a), b), the Vastaus, the bottom FBD length and the Järkevyys.
- exercises.json:106 + solutions.md:184 (fy5-4-L1-08) — A, internal inconsistency: the task says the rider rides the curve at triple speed, and the Järkevyys says that this "ei ole todellisessa kaarteessa mahdollinen" (27 m/s² ≈ 2,8g). Fix: start from a₁ = 1,0 m/s², which gives 9,0 m/s² ≈ 0,92g, possible on dry asphalt. Update answer 9.0, answers.py and the Järkevyys.

## Polish
- exercises.json:153 (L2-05) — "Naru oletetaan vaakasuoraksi", but with m = 25 g the weight (0,25 N) is about the same as F at 3 m/s, so a free string would hang about 40° below the horizontal. Fix: let the stopper slide on a smooth horizontal table, which makes the model exact.
- solutions.md:190 (L2-05) — the line is chosen to pass through a raw point. Say it was drawn by eye through the origin and that it happens to pass (49; 1,53); the least-squares value is also 25,0 g.
- exercises.json:272 (L3-04) — an accelerometer measures N/m (specific force), not a_n. Write "kiihtyvyys laskettiin nopeusmittarin ja radan muodon avulla", or say that gravity has been removed from the reading (B).
- solutions.md:254 (L3-04) — "kolme merkitsevää numeroa": 14,1 − 9,81 = 4,29 loses a digit, so give 2 sig. figs (≈ 260 N) or justify 3.
- exercises.json:305 (L3-05) — "ympyrän muotoinen ja vaakasuora" next to "kallistettu" reads as a contradiction; write "kaarre on vaakatasossa".

## Checked
- One script recomputed all new answers (L1-08 27; L2-05 24,98 g, LSQ 25,01; L2-06 0,5477; L2-07 3672 N; L3-04 257,4 N, 2664,6 N, 11,70 m/s; L3-05 48,2/97,29/81,3 km/h): all match answers.py.
- L3-05 FBD: friction down the slope at v_max, N = mg/(cos α − μ₀ sin α) = 1,07mg; the limits μ₀ = 0 and α = 0 hold. The render was checked.
- L1-06/L1-07 MC: one correct option each; the feedback has no centrifugal force and the friction direction is right.
- Scope fits the FY5 plan (FY4 force components at level 3); no duplicates; 8/7/5.
