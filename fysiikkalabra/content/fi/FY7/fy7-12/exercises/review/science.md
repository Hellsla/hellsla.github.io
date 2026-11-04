VERDICT: PASS
CONTENT-HASH: cc1d7dd0d3487a39

## Blocking

## Polish
- solutions.md L2-02 Vastaus — "kolme merkitsevää numeroa kuten ilman taitekerroin 1,00": the 45° angle is exact from the prism's geometry, which could be said in one clause (optional).

## Checked
- Round-1 fixes: L2-02 now has light entering through the hypotenuse and reflecting totally at a leg (kateettitahko) at 45°, which is right for a Porro prism. L3-02 Järkevyys now names the small difference in refractive index as the remedy, which the ray model supports.
- One script recomputed all 12 answers with my own formulas. They agree with answers.py and exercises.json: 48,75°, 24,41°, 61,04°, 2,041·10⁵ km/s, 0,50 ms, 1,456, 1,414, 2,007·10⁵ km/s, 1,217 ms, 2,053 m, 67,58 ns, 77,61°.
- Every critical-angle task has n1 > n2, with light leaving the denser medium. L3-03 first checks α_r = 62,46° > 60° and only then applies refraction.
- L3-01 uses r = h tan α_r (Snell's window). L3-02 uses the zigzag path L : sin α_r. Both are right.
- Rounding: L3-02 gives 2 sig figs because n1 − n2 = 0,020 limits it. The other answers give 3, which fits the data. The 0,02 tolerance accepts the rounded answers.
- The unit conversions are right. Every solution has 7 steps and solves symbolically first.
- The notation matches the brief, and the data are realistic.
