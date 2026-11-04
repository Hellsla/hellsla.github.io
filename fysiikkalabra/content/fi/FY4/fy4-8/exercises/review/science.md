VERDICT: PASS
CONTENT-HASH: 030248d9a1c7200f

## Blocking

## Polish
- exercises/solutions.md:150 fy4-8-L2-05 — the rounding reason "kuten korkeuksissa h (esimerkiksi 0,05 m)" cites a datum with one significant figure — say "kuten nopeuksissa ja korkeuksissa (esim. 0,30 m, 2,41 m/s)" or give the reason as the spread of the fitted points.
- exercises/solutions.md:160 fy4-8-L2-06 — "kolme merkitsevää numeroa kuten korkeuksissa ja nopeuksissa": h = 6,0 m, 3,0 m and v = 1,5 m/s have two — give −20 kJ (2 sf), or justify 3 sf from 18,0 m and 14,6 m/s and say why the others do not limit.
- exercises/exercises.json:74 fy4-8-L1-07 — same skill (W_kok = ΔE_k from two speeds) as L1-04; the plan's L1 items "nopeus pudotuskorkeudesta / korkeus nopeudesta" were already covered by L1-01/02, so the deviation is defensible, but note it in docs/exercise-bank/FY4.md.
- exercises/exercises.json:308 fy4-8-L3-04 — "kitkavoima vakio sekä rinteessä että vaakasuoralla" is stated (OK); the Järkevyys "kitkakerroin noin 0,08" could add "(rinne on loiva, joten tukivoima on lähes mg)".
- solutions.md:153/174/184 — lint warns L2-06, L3-04, L3-05 at 316–362 words; acceptable for multi-part tasks, trim Sijoitus if wanted.

## Checked
- Recomputed all 8 new answers in one script (own formulas): L1-07 −1,044 kJ; L2-05 LSQ k = 19,53 → g = 9,77 m/s²; L2-06 E_mek 74,6/69,5/62,5/54,7 kJ, W = −19,93 kJ, F 94/107/157 N; L2-07 k = 0,2185 s²/m → F = 1,144 N; L3-04 s̄ = 30,07 m, F = 54,89 N, v = 6,87 m/s (√(2gh) = 10,85); L3-05 shares 0,642/0,636/0,653/0,625, mean 63,9 %, ΔE₁ = 0,240 J — all match exercises.json, solutions and answers.py; tolerances fit.
- L1-06, L1-08: exactly one correct option; every distractor wrong and its feedback right (normal force does no work; friction work uses path length, not height).
- Conditions stated in every task (no friction/air drag, constant friction, line through origin with reason in L2-05 c).
- Energy principle used with the lesson's notation (E_k,1 + E_p,1 + W_muut = E_k,2 + E_p,2, W_kok = ΔE_k); friction → internal energy, total energy conserved (guardrail).
- Scope: all inside FY4 energy principle; no later-course physics.
- Levels: L1 one formula, L2 data/graph tasks, L3 multi-step YO-style modelling; 8/7/5 = 20; no duplicate of an existing task; plan items (pendulum + photogate, roller-coaster data, sled-type friction-work task, bouncing ball) present.
- Hash identical at start and end.
