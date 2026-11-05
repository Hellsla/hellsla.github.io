VERDICT: PASS
CONTENT-HASH: f8d708bbfe33cab0

## Blocking
None. All three round-1 items are fixed:
1. fy4-k1 a: the task is now a low-friction cart, with rolling resistance and air resistance negligible. The Perustelu argues from constant forces along the slope. Graph B is still the only correct option, and the explanations of A, C and D are unchanged and right.
2. fy4-k3 a: fbd_magnitudes now reads "jos kiihtyvyys on piirretty, se on erillinen nuoli eikä voima". It no longer asks for something the task does not ask.
3. fy4-k7 a: the Järkevyys now compares 1,50 m with the height of a cyclist's head above the ground, which is correct.

## Polish
- `figures.py` docstring of `graphs()` still says "a ball that rolls" (internal only, not shown to students).

## Checked
Delta from round 1. Hash f8d708bbfe33cab0 at start and end.
- k1 i and k5 b: "sisäenergiaksi (vaunut ja puskurit lämpenevät)" now follows the guardrail, in the Perustelu, the criterion and the Vastaus.
- k6 d: the criterion and Hyväksytään myös now accept h from the student's own c result. 2,3–2,6 m/s gives 0,27–0,34 m, recomputed.
- k7 d: the clause about 613 and 603 m/s² is right.
  - For a half-sine pulse the stopping distance is s = vT/2. So v²/(2s) = v/T, and the distance average equals the time average.
  - The difference comes only from rounding the exact 2,44 cm to 2,4 cm, as the clause says. This corrects my round-1 wording that they are "different averages".
  - The ratio π/2 ≈ 1,57 is exact for a half-sine (950/603 = 1,575). 1,57 · 1472 = 2311 m/s², inside the accepted 2200–2400, and the conclusion (passes, margin about 6–7 %) does not change.
- answers.py output is unchanged and agrees with my script: 2,46 m/s, 0,309 m, 603 m/s², 3063 N, 2280 m/s².
