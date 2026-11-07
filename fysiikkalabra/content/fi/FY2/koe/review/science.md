VERDICT: PASS
CONTENT-HASH: 13cc91dffc2212dc
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- k5-d model answer opens and closes with "Väite on liioiteltu."; the repetition can go.
- k3-c: "short term, more CO2 than oil" is per unit of fuel energy; per delivered heat it also depends on boiler efficiencies. Fine as written for the given data.

## Checked
- Diff `git diff origin/main...HEAD` of koe/tasks.json, koe/solutions.md, lessons/FY2/koe/answers.py (fi); content hash recomputed and equal to the brief's.
- Ran `python3 lessons/FY2/koe/answers.py` and `python3 scripts/practice.py check FY2/koe` (OK, 7 tasks, 120 points).
- k6-b: $2900\,\text{MW}\cdot24\,\text{h} = 69{,}6\,\text{GWh}$, $69{,}6\cdot10^{6} : 15\,000 = 4640$ homes; k7-b: $150\,\text{W}\cdot3600\,\text{s} : 0{,}25 = 2{,}16\,\text{MJ}$, $: 0{,}45\,\text{MJ} = 4{,}8$ bananas; k7-c: $0{,}80\cdot500\,\text{Wh} : 150\,\text{W} = 2{,}67\,\text{h}$ (motor-only model now stated; sanity note about pedal-assist correct).
- k3-c: no longer leading; criteria (carbon origin, regrowth/stock condition, time horizon: short term more CO2 than oil since $112 > 74\,\text{g/MJ}$) and "Hyväksytään myös" (either conclusion if justified) match the model answer. k5-d: life-cycle criterion (hardware and building emissions) physically right. k6: data marked fictional, consistent with source_note.
- Changed text matches the en and fi-easy versions in substance.
