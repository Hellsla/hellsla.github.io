VERDICT: PASS
CONTENT-HASH: 5adb89f5eac07ee8
SCOPE: delta added-exercise from 753ff998604d8f0a base 611fb7d5c174

## Blocking
(none)

## Polish
- exercises.json fy2-8-L2-09 — the S2 version adds a definition that the Finnish lacks: "Elinkaaren päästö tarkoittaa kaikkia päästöjä rakentamisesta polttoon asti". The same set defines it in L2-08 as "polttoaineen hankinnasta sähköntuotantoon asti". A life-cycle factor also includes fuel extraction and decommissioning. — Fix: use one wording in both tasks, e.g. "kaikki päästöt voimalan rakentamisesta ja polttoaineen hankinnasta sähköntuotantoon ja purkamiseen asti".

## Checked
- Hash taken at the start and at the end with `--lang fi-easy`; it did not change.
- fy2-8-L1-09: E = Hm = 47 MJ/kg × 2,0 kg = 94 MJ, and m = eE = 55 g/MJ × 94 MJ = 5170 g = 5,17 kg. My recomputation, answers.py and exercises.json agree. The answer is given to two significant figures, as the data allow. The check of about 2,6 kg CO₂ per kg of gas is consistent: pure methane gives 44/16 = 2,75. The cause given (the carbon in the fuel combines with oxygen) is right. The unnamed source of the emission factor is not reported (teacher's decision 2026-11-12).
- fy2-8-L2-09: `fy2-8/emissions` prints 820 for coal and 490 for gas (g CO₂-ekv./kWh). (820 − 490) × 20 000 kWh = 6,6 × 10⁶ g = 6,6 t. The intermediate values (16,4 t and 9,8 t) are right. The solution forms Δm = (e₁ − e₂)E symbolically first. The 3 % tolerance fits.
- Compared with the reviewed Finnish: answer, unit, tolerance, figure, lookup, level and every number in the task text and the solution are identical. The added explanations of "päästökerroin" and "elinkaaren päästö" keep the physics; see Polish.
