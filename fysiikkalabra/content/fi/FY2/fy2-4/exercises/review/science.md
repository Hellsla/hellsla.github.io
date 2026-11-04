VERDICT: PASS
CONTENT-HASH: bb79df8de9f7fc6e

## Blocking
(none)

## Polish
- exercises.json:154 (fy2-4-L2-05) — the halogen lamp at 4,2 W / 42 W = 10 % is twice the incandescent lamp's efficiency and gives more light than the 60 W bulb. A real halogen is only about 1,3–1,5 × an incandescent (≈ 7 % on this scale) — for example 40 W with 2,8 W (7,0 %), giving a ratio of 4,3; update answers.py and solutions.md:148ff to match.
- solutions.md:180 (fy2-4-L3-04) — "Hyötyenergiat ovat lähes yhtä suuret ... koska molempien on ajettava sama matka" holds only for cars of similar size and speed (B) — add "samankokoisten autojen".
- docs/exercise-bank/FY2.md:29–30 — the plan's kettle task (temperature rise, i.e. c·m·ΔT) and its chain-efficiency tasks (overall chain, and the error "sum instead of product") break the FY2 scope note (FY3 fy3-15). The set correctly avoids them (L2-06 motor table, L3-05 LED error analysis); update the plan.
- fy2-4-L3-05 — the physics is fine, but the computation is one subtraction and one ratio; it sits at the light end of level 3.

## Checked
- Recomputed all 20 answers in one script with my own formulas. All agree within tolerance: new 9,0 kJ, 200 kW, 3,0, 79,2 %, 3,14 and 30,1 %.
- L2-06: row ratios 0,80/0,787/0,798/0,792 and a fit through the origin of 0,793. 79 % at 2 significant figures is justified.
- L3-05: light = E_o − E_h on every row gives 0,296–0,306, consistent with 30 %. The error identified (loss share taken as efficiency) is the real one, and it matches the lesson's LED value of 30 %.
- L3-04: 192 MJ = 53,3 kWh, ratio 3,14. Useful energies are 15,3 and 13,3 kWh and the loss is 40 kWh. The consistency check 3,6 : 1,15 = 3,1 holds. The tank-to-wheel boundary is stated in the task.
- L1-06 and L2-07: exactly one correct option, and every distractor's feedback is right (η ≤ 100 %, ratio not size, loss powers 0,5 kW vs 100 W).
- Levels 8/7/5 and no new task duplicates an existing one. FY2 scope: one device's η = E_a/E_o = P_a/P_o and E_o = E_a + E_h only. There is no product of efficiencies, no c·m·ΔT and no mgh in any task.
- Guardrail wording "enintään 100 % ... jää usein alle" is used in L1-06.
- The unknown is solved symbolically first, percentage conversions are shown.
