VERDICT: PASS
CONTENT-HASH: 46e452c734acb155

## Blocking

## Polish
- exercises.json:272 (fy5-4-L3-04) — the wording says a_n "laskettiin nopeudesta ja radan muodosta", and part a) then asks for the radius from v and a_n, which is circular — write instead "kiihtyvyysanturin lukemasta on vähennetty painovoiman osuus" (carried over from the previous round, still optional).
- solutions.md (L3-04 Järkevyys) — the energy check could name its source: "mekaanisen energian säilyminen: ½mv₁² = ½mv₂² + mg·2r" (carried over, optional).

## Checked
- The diff since the last science review (commit 1847106e2 → HEAD) touches only solutions.md in fy5-4, 3 insertions and 1 deletion, all in L3-05.
- L3-05: the old single display formula is split into $\dfrac{\tan\alpha+\mu_0}{1-\mu_0\tan\alpha} = \dfrac{v^2}{g\,r}$ followed by $v_\text{max} = \sqrt{g\,r\,\dfrac{\tan\alpha+\mu_0}{1-\mu_0\tan\alpha}}$. The maths is identical, and dropping the ⇒ loses nothing, because the second line follows directly by solving for v.
- L3-05 numbers recomputed: tan 8,0° = 0,1405, g r = 1275,3 m²/s², fraction 0,5727, v_max = 27,03 m/s = 97,29 km/h; v₀ 48,2 and flat 81,3 km/h are unchanged.
- Both display formulas are on their own paragraphs with blank lines, consistent with the other display math in the solution.
- Nothing else in exercises.json, solutions.md or answers.py has changed, so the earlier PASS findings (L1-08, L2-05, L3-04 data consistency, MC options, scope, 8/7/5) still hold.
- The content hash is 46e452c734acb155 at both the start and the end.
