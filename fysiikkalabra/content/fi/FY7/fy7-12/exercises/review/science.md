VERDICT: FAIL
CONTENT-HASH: eff1b77a71f529fc

## Blocking
- exercises/exercises.json:56 (fy7-12-L2-02) — A: in binoculars the right-angle (Porro) prism reflects light totally at its two short faces (the legs), each at 45°. Light enters and leaves through the long face (the hypotenuse). "Valo tulee prisman sisällä pitkälle sivutahkolle … kokonaisheijastua siitä" puts the reflection on the wrong face for a binocular prism. The answer 1,414 is unaffected — fix: "osuu prisman lyhyelle sivutahkolle (kateettitahkolle) 45°:n tulokulmassa", or drop "Kiikarissa" and say "suunnanvaihtoprisma".
- exercises/solutions.md:109 (fy7-12-L3-02, Järkevyys) — B: "Siksi tietoliikennekuiduissa ydin tehdään hyvin ohueksi" gives a cause the task's ray model does not support. In the ray model, Δt = (n1 L : c)(n1 : n2 − 1) does not depend on the core's diameter. A thin core helps only through the wave picture (one mode), which is not in FY7. The lesson itself names the small index difference as the remedy — fix: "Siksi tietoliikennekuiduissa ytimen ja kuoren taitekertoimien ero tehdään hyvin pieneksi."

## Polish
- solutions.md L2-02 Vastaus — "kolme merkitsevää numeroa kuten ilman taitekerroin 1,00": the 45° comes from the prism's geometry and is exact, so this is fine. You could say so in one clause.

## Checked
- One script recomputed all 12 answers with my own formulas, and all agree with answers.py and exercises.json: 48,75°, 24,41°, 61,04°, 2,041·10⁵ km/s, 0,50 ms, 1,456, 1,414, 2,007·10⁵ km/s, 1,217 ms, 2,053 m, 67,58 ns, 77,61°.
- Every critical-angle task has n1 > n2 with light going from the denser medium. L3-03 first checks α_r = 62,46° > 60° before applying refraction.
- L3-01 geometry r = h tan α_r is right (Snell's window). L3-02 zigzag path L : sin α_r is right.
- Rounding: L3-02 is given to 2 sig figs because n1 − n2 = 0,020 limits it, which is right. The other answers have 3 sig figs from the data. The relative tolerance of 0,02 accepts the rounded answers.
- Conversions (km→m, s→ms/ns, m/s→km/s) are right. Every solution has 7 steps and solves symbolically first.
- Notation (α_r, n1, n2, v = c : n, t = n s : c) is the same as in the brief. All tasks are within FY7 and the lesson.
- Data are realistic: water 1,33, diamond 2,42, aquarium glass 1,52, fibre 1,46–1,48, PMMA-like plastic 1,49.
