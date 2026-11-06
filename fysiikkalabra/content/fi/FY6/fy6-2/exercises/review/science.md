VERDICT: PASS
CONTENT-HASH: e2a4b4fa15ee78b7
Round: 1 (new task fy6-2-L2-08, error finding; the rest of the set was PASS before and is unchanged).

## Blocking

## Polish
- content/fi/FY6/fy6-2/exercises/solutions.md:202 — the 10 A error limit is kept as 0,033 A although the lesson rounds an error limit to one significant figure (0,03 A); fine as an intermediate value — say "välitulos" or write ≈ 0,03 A and keep "noin kaksikymmenkertainen".

## Checked
- Hash e2a4b4fa15ee78b7 at start and end.
- answers.py run against exercises.json: all 16 numeric answers agree within tolerance (one python call).
- L2-08 recomputed: 10 A range 0,020 · 0,14 A + 3 · 0,01 A = 0,0328 A; 200 mA range 0,010 · 140,0 mA + 2 · 0,1 mA = 1,6 mA; ratio ≈ 20. Row 3 is the only wrong line.
- Rows 1, 2 and 4 are right physics (ammeter in series; start on the largest range; 4,38 V needs 20 V since the 2 V range shows at most 1,999 V with 0,001 V resolution). The ranges and error limits are exactly the lesson's table.
- The wrong row is the lesson's first warned mistake (largest range always best); the row-1 feedback names the second (ammeter in parallel → short circuit).
- Δx = p·x + n·r, OL and "pienin alue, jolle lukema mahtuu" are all taught in this lesson.
- Real meters often need the red lead moved to a separate 10 A jack; leaving it out is a fair simplification (C).
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 294 px (solutions.md ΔI on the 200 mA range), just under 300 px. Page layout not rendered; the rest from text.
