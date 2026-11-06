VERDICT: PASS
CONTENT-HASH: fd9abba3faab2137
Round: 1 (new task fy6-1-L1-09, true/false statements; the rest of the set was PASS before and is unchanged).

## Blocking

## Polish

## Checked
- Hash fd9abba3faab2137 at start and end.
- answers.py run against exercises.json: all 15 numeric answers agree within tolerance (one python call).
- L1-09 recomputed: Q = 0,30 A · 60 s = 18 C, E = 3,0 V · 18 C = 54 J; truth values 1 F, 2 T, 3 T, 4 F, 5 F are right, and `answer` matches.
- Statement 3 is true only because wire and cell resistances are neglected; the task states that condition, and the feedback repeats it (guardrail: a law's conditions).
- Both of the lesson's warned mistakes are the false statements 1 (current used up in the lamp) and 4 (electrons must travel from the cell to the lamp); statement 5 catches V read as energy per minute. Each feedback says why it is false, in the lesson's own words.
- 3,0 V and 0,30 A are realistic flashlight values; I = Q/t, U = E/Q and e notation as in the lesson; no capacitor or later-chapter content.
- Solution complete (Kysytty · Periaate · Mallivastaus), symbolic before numbers.
- Inline formula widths measured (KaTeX render of each $…$ at 17 px, 1.21 em, my own script): widest 244 px (`E = UQ = …`), under 300 px. Page layout itself not rendered; everything else checked from text.
