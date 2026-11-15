VERDICT: FAIL
CONTENT-HASH: 4d884b467d055fce

## Blocking
- content/fi-easy/FY3/fy3-1/exercises/solutions.md:19 (fy3-1-L1-02, Järkevyys) — A (definition): "Myös jousivakio täsmää: 2,0 cm / 4,0 N = 0,50 cm/N". Jousivakio is k = F/x (N/m, the FY4 term). The ratio x/F in cm/N is its reciprocal, so calling it jousivakio teaches a wrong definition. — Name it for what it is, e.g. "Myös venymä newtonia kohti täsmää: …", or leave the term out. (The fi and en sets have the same sentence on line 19. They are outside this packet, but the fix should go there too.)

## Polish
- solutions.md:120 (L3-03) — "Maan arvosta, Siksi": a capital letter after a comma. Use a full stop or a lowercase "siksi".
- solutions.md:179 (L3-04) — "$c$ on jousen vakio" is defined in place, so it is not wrong. But beside the jousivakio fix above, "jousesta riippuva vakio" would keep it from being read as k.

## Checked
- Recomputed all 20 numeric answers with my own formulas in one script. They agree with answers.py and exercises.json within tolerance: L1-01 39,24; L1-04 7,0 (from figure points (4 N; 2 cm) and (10 N; 5 cm)); L1-10 316,2 (3,72) and 315,4 (3,71), both inside 4 %; L2-03 1187,6; L3-03 68,75; L3-05 682,3, with Maa 9172 N > 6000 N and a Maa limit of 611,6 kg.
- L2-05: a least-squares fit through the origin gives 9,80 m/s², the same as the solution's line read at (0,50 kg; 4,90 N). L3-04: the fitted slope 10,32 cm/kg gives 3,61 m/s² and the sum ratio gives 3,59. Both are inside 4 % of 3,6, and Mars is the right identification.
- L1-05 changed check: 2,5 · 24,5 N ≈ 61 N, "täsmää suhteen 2,5 pyöristyksen tarkkuudella". The ratio is 2,53, so the claim is correct.
- L1-09: B is the only correct option. G = 4,905 N equals the reading, so the arrows are equal. Each distractor's error is the one its feedback names (F missing, F doubled, the third-law partner F_k drawn on the body), and F_k is correctly said to act on the meter.
- L1-06 and L1-07: exactly one correct option each, and every distractor's feedback is right (mass is invariant; the weight is the Earth–book interaction).
- L2-06: g_Mars = 3,71 m/s². The Kuu row gives 1,59 m/s², a realistic value.
- Units, significant figures and the rounding reasons are right throughout. Everything stays in FY3 scope: G = mg and the proportionality of a spring, no Newton's laws.
- Figures spring-points and weight-points give the needed grid points without the answer, and their descriptions list the same points.
- Hash the same at the start and the end.
