VERDICT: PASS
CONTENT-HASH: 4b2e59499271c581

## Blocking
(none)

## Polish
- fy5-4-L3-04 text: "normaalikiihtyvyys laskettiin nopeudesta ja radan muodosta" makes part a) (r = v²/a_n) circular; say "kiihtyvyysanturi mittasi" or "a_n saatiin mittauksesta" so the radius is a result of the data.
- fy5-4-L3-04 Vastaus says "noin 260 N (kaksi merkitsevää numeroa)" while the stored answer is 257,4 N; both pass the 2 % tolerance, but the solution should show 257 N to match the Sijoitus and the "257,4 : 588,6" check.
- fy5-4-L3-05 Kaava now shows the division step; the display math uses $$ in a bold-label line, check it renders (not seen in a capture).

## Checked
- Delta only: L1-08 now 1,0 -> 9,0 m/s² (0,92 g, a realistic limit); solution, Järkevyys and answers.py agree.
- L3-04 energy-consistent data: r = 27,2²/53,2 = 13,91 m, 14,0²/14,1 = 13,90 m, mean 13,90 m; v1² − v2² = 543,8 ≈ 4 g r = 545,6; N1 = 60(9,81+53,2) = 3781 N = 6,42 mg; N2 = 257,4 N; v_min = 11,7 m/s. The earlier Polish item is resolved.
- L2-05: table now on a smooth table (weight and normal force cancel); F/v² mean 0,0312 and least squares both give 25,0 g; the slope is now read from two distant points, resolving the earlier Polish item.
- L3-05 algebra step shown ((sin α + μ cos α)/(cos α − μ sin α) = v²/(g r), then divide by cos α); "Murtolauseke" fixed; answers 48,2 / 97,3 / 81,3 km/h unchanged.
- L1-08 Järkevyys rewritten clearly (3² = 9).
