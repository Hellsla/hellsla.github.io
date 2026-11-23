VERDICT: PASS
CONTENT-HASH: ae3268c24422105d
SCOPE: full. The change is three new `pysahdy` boxes in unit.md, judged first against the Finnish boxes (fi PASS c66703f1d31a22ae). After that the unit text, unit.json and the Sovella task set s1–s8 were judged with them.

## Blocking
None.

## Polish
- Box 2 says "lukuvirheen osuus". The Finnish box says "lukemisvirheen". "Lukuvirhe" can be read as an arithmetic error. "Lukemisvirhe" (reading error) matches the rest of the unit. This is wording only, not physics.
- Box 1 asks "Poistaako toisto virheen". The Finnish box names "kellon systemaattisen virheen". The answer explains both error types, so nothing is wrong. Naming the systematic error in the question would match fi exactly.
- The old Polish items from round 3 still stand: s8 a criterion 5 against the model answer, and s7 c detail $1{,}2/30{,}0$. Both are carried and neither is an error.

## Checked
- Box 1, a clock that always runs fast: the physics is the same as fi. Averaging repeated readings reduces the effect of random error. A systematic error has the same direction in every reading, so it stays in the mean. This agrees with the paragraph above the box and with key_concepts "systemaattinen virhe" (category 6).
- Box 2, why the slope is read from the line and not from data points: the physics is the same as fi. The points scatter around the line, the fitted line represents all the data, and far-apart points give large $\Delta x$, $\Delta y$, so the reading error is a small share. This agrees with the paragraph above the box, the figure "anatomia" and the graph_read criterion.
- Box 3: $s = \tfrac12 a t^2$, so $k = a/2$ and $a = 2k$. The condition (start from rest, time from the start of the motion) is stated in the paragraph just above the box, and the box says the line goes through the origin. This is the same as fi, and the "linearisointi" figure ($a = 0{,}50$, $k = 0{,}25\,\text{m/s}^2$) agrees.
- No box gives a wrong option or a misleading picture. Each answer stays inside the unit's scope (FY1 measurement and graphs; kinematics from FY4 is only revised).
- Since the passed commit 4576e24f0, solutions.md has changed only by paragraph splits (carried as md-paragraphs). I read the diff and every number, sign and unit is unchanged.
- Recompute: an independent numpy script (scratchpad rc.py) checked s1 v and Δv, s2 thickness, areal density and density, the s3 fit with row 60 ml excluded and the 1,50 l mass, the s4 calibration slope and corrected 765 g, the s5 fit without 1,5 s, the s6 $V(1/p)$ slope, $V_0$ and $n$, the s7 $k = 1/\text{slope}$ and the 4,5 N extension, and the s8 $g = 2k$. All agree with answers.py. The fi-easy part answers equal the fi ones, and `practice.py check` is OK (8 tasks, 116 points).
- The hash is ae3268c24422105d at the start and at the end.
