VERDICT: FAIL
CONTENT-HASH: 6b96bf94e77d0b06

## Blocking
- solutions.md:110 (L1-06) — **A**: "eikä niiden alkeisalueita järjestetä tällä tavalla" says that Al and Cu have domains. They have none, and the option feedback says so. — Fix: "niissä ei ole alkeisalueita, jotka magneetin kenttä voisi järjestää, joten magneetti ei vedä niitä."
- exercises.json:309 (L3-05) — **B**: "…kompassin itäpuolella akselillaan, joten sen kenttä osoittaa kompassin kohdalla itään". The field points east only when the S pole faces the compass. — Fix: add "etelänapa kompassia kohti".

## Polish
- solutions.md:134 (L2-05) — the Vastaus recommends 15 µT, but the page shows 14,5 (step 0,1, tolerance 3 %), so 15 gets only "Lähellä". — Show 15 µT, or set tolerance 0.04.
- exercises.json:106 (L1-08) — Oulu is 52 µT, 76° here and 53 µT, 76° in the L3-04 table. — Use one value.
- L1-08 is the sin twin of L1-02 and L2-03. The plan's level-1 task was the compass deflection tan θ = B_m : B_h with a new magnet and distance. — Consider swapping it.
- L3-04 repeats L3-03's conclusion (smaller B_h in the north, worse compass). — Acceptable. Optionally ask for the angle error that a 5 µT disturbance causes in Helsinki and in Utsjoki.

## Checked
- I recomputed the new answers in one script (50,46; 14,50; 70,72; 64,98; 61,61; 16,16). They match answers.py and exercises.json.
- L2-05 data: B_m r³ ≈ 2,3–2,7·10⁴ µT·cm³, and the 10→20 cm ratio is 8,5, as stated.
- L3-05: the log–log slope is −3,10 and k = 59,1·10³ µT·cm³, so r₀ = 16,2 cm. The field points south with the N pole toward the compass, and the needle reverses for r < r₀. Both are correct.
- L2-06: 48,5 / 50,6 / 70,7 µT, with iron at the desk, is correct. The constant phone orientation is stated.
- L2-07: the swapped ratio gives 25,0° and the correct angle is 65,0°. The >45° check is right.
- L3-04: B_h is 14,6 / 12,8 / 10,8 µT and θ is 53,9° / 57,3° / 61,6°. B_v ≈ 51 µT everywhere.
- L1-06 and L1-07: each has one correct option, and every distractor's feedback is right.
- There are 8/7/5 tasks, and every numeric solution is solved symbolically first.
