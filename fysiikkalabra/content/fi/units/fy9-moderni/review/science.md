VERDICT: PASS
CONTENT-HASH: 2551e46149b68b40
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- C: s7 c rounding reason: 80 K is the difference of the given 20 °C and 100 °C; "koska lämpötilat on annettu kahdella merkitsevällä numerolla" would name the given data. The present sentence is acceptable.

## Checked
- s7 d part text now also asks "kuinka paljon sähköenergiaa vapautuneesta energiasta saataisiin lämpövoimalan hyötysuhteella", so criterion 3 (about 1 MJ, under half a percent of the grid energy) asks only what the task asks; the one-third efficiency is given in the task's Lisätietoja. Recomputed: 3,15 MJ / 3 = 1,05 MJ; 1,05 / 300 = 0,35 %; 3,15 / 300 = 1,05 %; 2,05 / 300 = 0,68 %. The solution's Kysytty line states both questions and the model answer gives both.
- s7 c: new rounding reason (temperature difference 80 K known to two figures) is a valid reason for two figures; m = 3,15e6 J / (4190 · 80 J/kg) = 9,397 kg.
- Task text: the three facts are now full sentences under "Lisätietoja:"; values unchanged (4,19 kJ/(kg·K), about 300 MJ, one third).
- s7 e criterion 1: accepts either reason (no electricity produced, or a grid-connected plant is decades away); both are true and in the material.
- `practice.py check` OK (7 tasks, 110 points).
