VERDICT: PASS
CONTENT-HASH: 99322ddd2a419363
Round 3: delta against the version round 2 reviewed (one sentence in s7 d).

## Blocking
- (none)

## Polish
- C (not a finding, for the teacher's information): in the source chart's own data the Opel Grandland (484 km stated, 262 km measured) comes to -45,87 % and the Lucid Air (960 km, 520 km) to -45,83 %, so a student who computes every car from the chart finds the Opel 0,04 percentage points ahead. The sentence is attributed to the report, which makes it true as written; a teacher note or a "noin 46 %" in the solution would forestall the question. The report's text gives 519 km for the Lucid, the chart 520 km (the task uses the chart).

## Checked
- `git diff c502cb9e26 -- content/*/units/fy9-energia`: three files, one line each, only the s7 d sentence. Nothing else changed.
- New sentence: "According to the test report, the range of the car that drove the furthest fell short of its stated range by the largest percentage." Opened the source myself (naf.no, elprix-vinter-2026-rekkeviddetest): "Lucid var også bilen med størst avvik fra WLTP-rekkevidden, med hele 46 prosent." The attribution is accurate, and the same article gives the task's own reasoning (the Lucid had by far the longest time in the coldest surroundings).
- Recomputed from the task's table: Inster -28,89 %, Tesla -42,93 %, Lucid -45,83 %: the sentence agrees with part a and with the 46 % of the report. From the chart data of all 24 cars the Lucid drove the furthest (520 km) and the mean deviation is 38 %, as the task says.
- Part d criteria (source use: -7 to -32 degrees C, short-range car stopped at -16 degrees C; conclusion: not the same conditions, no ranking by percentages) and the model answer are unchanged and agree with the new sentence; they need nothing the task does not give. Points 1 + 1 = 2.
- The round-2 Polish about the claim's scope (en) is settled by the attribution.
- `practice.py check units/fy9-energia` OK (7 tasks, 105 points). Hash the same at the start and the end.
