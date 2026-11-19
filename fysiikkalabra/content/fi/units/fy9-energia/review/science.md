VERDICT: PASS
CONTENT-HASH: 0fb7773df145af69
SCOPE: delta: the new Sovella itsenäisesti tasks s8 (skater on a half-pipe, figure fy2-1/kitka-pylvaat) and s9 (two devices on an energy meter, figure fy2-3/graph-ab) with solutions, answers.py, and the changed intro sentence (fi); s1-s7 not re-judged.

## Blocking
- (none)

## Polish
- s8 a, "Reasonableness" in the model solution: "Sisäenergiaa syntyy suunnilleen yhtä paljon kummallakin osamatkalla, mikä sopii kitkan tasaiseen vaikutukseen" is not supported by the task: the path lengths A-B and B-C are not given, and in the figure's parabola A-B is the shorter arc (about 40 % of the path) yet gets as much (100 J) as B-C. Suggest dropping the clause or saying only that energy is produced on both parts. Same sentence in en and fi-easy.
- s8: the energies are read from bars on a 100 J grid (700, 300, 500 J) and v is given with two figures "like the mass"; defensible since the bars end on gridlines, but a teacher note that the bar values are exact would forestall the question.
- s8: the 3,4 m path is not tied to a drop height; the figure is schematic, so no check is possible. Not an error.

## Checked
- Hashes at start and end identical (0fb7773df145af69); `practice.py check units/fy9-energia` OK (9 tasks, 134 points, all three languages).
- Recomputed s8: Em 700/600/500 J; dB 100 J, dC 200 J; v = sqrt(1000/45) = 4,71 -> 4,7 m/s; F = 200/3,4 = 58,8 -> 59 N; weight 441 N, 13 %; v0 = sqrt(1400/45) = 5,58 -> 5,6 m/s; 200/700 = 29 %. All match tasks.json, solutions and answers.py. Energy wording follows P1 (internal energy, transferred as heat; "muuttuu lämmöksi" only as a listed mistake).
- Figure kitka-pylvaat: bars A 700/0, B 300/300, C 0/500 on 100 J gridlines, B placed at height 300/700 of the rim; alt text names A, B, C as the task does; the figure shows no thermal energy or total, so nothing is given away. Task text does not name the method.
- Recomputed s9: PA 120/80 = 1,5 kW, PB 0,50 kW; 90 h; 135 and 45 kWh; 21,6 -> 22 EUR and 7,2 EUR; E_hyoty = 150*9,81*20 = 29,4 kJ; eta 0,7358 -> 74 %; P_hyoty 368 W; loss 132 W -> 0,13 kW (26 %, eta + 26 % = 100 %). Consistent in all files; accepted alternatives (73,6 %, 132 W) correct.
- Figure graph-ab: lines through the origin to (80 s; 120 kJ) and (80 s; 40 kJ), labels A and B as in the task, no powers or slope triangle; alt text consistent. Times (3,0 h, 30 days) are exact-ish given with two figures; results rounded to two figures.
- Intro: "Yhdeksän" / nine / "Kaksi viimeistä" agree with 9 tasks where only s8 and s9 carry a figure; s7 is still the source task. Same in all languages.
- en and fi-easy: numbers, point splits, criteria and answers identical to fi; only wording differs.
- Limit: the committed captures (shots.md) show the unit page without the independent tasks, so layout with solutions open at 360 px is not judged here (visual reviewer's role).
