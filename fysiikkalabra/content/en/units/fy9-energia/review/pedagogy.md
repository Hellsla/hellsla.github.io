VERDICT: PASS
CONTENT-HASH: e22d2e4b5a939769
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: sovella/tasks.json s7 c, criterion "Electricity": one point requires both the heater ($P = UI$ for the whole drive) and the internal resistance of the cold battery. Accepting either one, with the other as a bonus in the model answer, would be fairer for 1 p.
- A: s7 b: the car's "range in mild weather" is shortened by a percentage that the source measures against the WLTP value. One clause ("use the same percentage as a model") would make the simplification visible.
- C: s7 a and e: "tell what the comparison shows", "Tell also how": "say" reads more naturally.

## Checked
- Item 18 hunks (figures.json, inquiry.json, unit.md, solutions.md, tasks.json): each "becomes heat" sentence now says internal energy, or internal energy transferred to the surroundings as heat. Wrong options and the quoted misconception stay wrong. Feedback and criteria are still readable and reveal nothing new. The fridge share is $1.08 : 1.54 \approx 70\,\%$.
- s7 in full: the source is useful (chart or table in a, route temperatures in d, the 2025 test in e). Parts progress from reading and comparing, to a model with an assessed assumption, to an explanation in three fields, to a confounded variable, to the limits of one test. No overlapping parts. Points 3+4+4+2+2 = 15, and criteria sum to each part.
- Recomputed: $-28.9\,\%$, $-42.9\,\%$, $-45.8\,\%$, mean $39.2\,\%$; $16.67$ and $26.88\,\text{kWh}$, $279\,\text{km}$, $600\,\text{N}$; air density ratio $+16\,\%$; $15\,\text{kWh}$ is a fifth of $75\,\text{kWh}$.
- No repeat of s1–s6: s3 "Frost and the electricity bill" is house heating data. Nothing beyond FY1–FY8.
- 390 px render of s7 from preview/en (statement, table, part a): the table fits and nothing overflows.
- Hash identical at start and end.
