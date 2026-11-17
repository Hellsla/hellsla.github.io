VERDICT: PASS
CONTENT-HASH: 674123fb01d9ff37
SCOPE: delta added-exercise from 9fd9fa6cd5fce3bb base 5b3ca4f81c77

## Blocking

## Polish
- exercises.json fy8-14-L2-08 — the stated reading accuracy (0,1 cm) used on the bone half-value layer can push the answer just outside the 6 % tolerance: 1,0/3,5 gives 1,43 cm and 1,2/3,3 gives 1,82 cm. On the 0,5 cm grid (about 46 px/cm) a careful reading is about ±0,05 cm, which stays inside, so this is not blocking. Option: tolerance 0.08, or say "noin 0,05 cm".
- exercises.json fy8-14-L2-09 — the same for T½: 105…115 min gives 315…345 min, and the tolerance of 4 % allows 317…343 min. Option: tolerance 0.05.
- solutions.md fy8-14-L2-09 Vastaus — "kolme merkitsevää numeroa kuten luetussa puoliintumisajassa": a T½ read to ±5 min hardly supports three figures. "330 min (noin 5,5 h)" with a note on the reading accuracy would be more honest.

## Checked
- Hash 674123fb01d9ff37 at the start and at the end. Delta: only L2-08 and L2-09 were judged.
- L2-08 recomputed with my own model: (1/2)^(5,0/3,4) = 0,361, and the solution reads 0,36. Equal transmission means n_luu = n_kudos, so d_luu = 5,0 · 1,1/3,4 = 1,618 → 1,6 cm, matching answers.py. On the bone curve the reading at 1,6 cm is 0,365, so the graph check holds.
- The figure kontrasti-points uses DT = 3,4 cm and DB = 1,1 cm from lesson-answers.py, the same as the lesson's example and the task. The half-value layers are not marked, so the figure does not give the answer away. Its description is enough for a reader who cannot see it.
- L2-09 recomputed: t = T½ · log₂(A₀/A) = 110 · log₂ 8 = 330 min. A(110) = 240 MBq and A(330) = 60 MBq on the plotted curve. The value 480 MBq is marked at t = 0.
- The fdg figure plots 480 · (1/2)^(t/110), which fits F-18 (109,8 min). The task states the assumption "vain hajoamisen takia", which is right for a syringe, so the decay law applies.
- Both solutions are complete (given and asked, principle, symbolic solution, no conversions needed, substitution with units, rounding, a real check), and they use the lesson's notation (n = d : d½, A = A₀(1/2)^(t/T½)).
- Scope: X-ray attenuation and the decay law are both within the FY8 central contents and this chapter. No guardrail breaks.
- Units, unit fields (cm, min) and the relative tolerances fit both tasks.
