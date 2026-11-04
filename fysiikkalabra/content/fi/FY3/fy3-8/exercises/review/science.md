VERDICT: FAIL
CONTENT-HASH: ae010b44e9caf534

Full review (20 tasks, 8/7/5), focus on new L1-06..08, L2-05..07, L3-04..05.

## Blocking
- solutions.md:174 (L2-07 b mallivastaus) — A, definition (guardrail: keep mittausvirhe and mittausepävarmuus apart): "mittausvirhe olisi yli puolet tuloksesta (52 %)" calls the tape's 0,5 mm resolution an error; the error is unknown, 0,5 mm estimates the uncertainty. Same in "suhteellista virhettä". — Write "mittausepävarmuus voisi olla yli puolet tuloksesta (52 %)" and "suhteellista epävarmuutta".

## Polish
- solutions.md:174, 198 (L2-07 c, L3-05 a) — "kolme merkitsevää numeroa" names no limiting datum; 0,5 mm, α = 12, r = 0,30 mm, γ = 1,1 suggest 10 m and 76 mm. Justify or round.
- solutions.md:163 (L2-06 b) — use the guardrail sentence "…eivät yleensä sijaitse täsmälleen samalla suoralla mittausepävarmuuden vuoksi"; the plan asks for α "kulmakertoimesta", so a fitted line beats raw end points (fit gives 22,9 too).
- exercises.json:290 vs solutions.md (L3-04 a) — answer 13.2 but Vastaus "≈ 13 mm, kaksi merkitsevää numeroa"; make them agree.
- solutions.md:147, 159, 181 — "Kuvaajan lukeminen" heads table readings; "Taulukon lukeminen".
- L1-07 — "heikot vuorovaikutukset" is a fair simplification; optionally add that at constant pressure faster gas particles need more room. L2-06 near-repeats L2-04 (α → metal), acceptable (graph vs table).

## Checked
- All 18 numeric answers recomputed in one script: agree with answers.py and exercises.json (L1-08 2,3 vs pupil 2,99 mm; L2-05 45·10⁻⁶; L2-06 22,9; L2-07 0,96 mm, 10,4 m; L3-04 13,2/12,0/18 mm, 25,2 mm at −32 °C; L3-05 75,9, 77,8 mm, +2,5 %, water 12,9 mm).
- L2-05 volumes match real water densities 0–10 °C; 4 °C minimum and lake reasoning correct.
- L1-06, L1-07: one correct option, feedback right (steel 12 > glass 9; air ≫ water ≫ steel 36·10⁻⁶).
- L3-04, L3-05 assumptions stated in the task (gap = one rail's ΔL; bulb γ = 3α, constant capillary area and coefficients).
- Scope inside FY3 lämpölaajeneminen; levels and kinds fit the plan; every new task has a complete solution.
- Hash unchanged at start and end.
