VERDICT: DONE

# fy9-kaasut: developer notes

## Files
- content/fi/units/fy9-kaasut/: unit.json, unit.md (hero, Ydinajatus, Kaava, Yleisiä virheitä, Kertaa), inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json, sovella/solutions.md, review/developer.md
- lessons/units/fy9-kaasut/: figures.py (hero, kartta, rengas, kone), sovella/answers.py, sovella/figures.py (s3-graph, s3-extra, s6-vaaka, s6-pysty)

## Task counts
- Ennusta (diagnostic): 6 choice items, one per chapter (fy3-4 ×2, fy3-9 ×2, fy3-10, fy3-11).
- Tutki: 1 interpret item (reused figure fy3-10/pt-suorat, numeric answer n_A = 0,0602 mol).
- Sovella: 4 choice and 4 numeric items, each with hints and mistakes.
- Tarkista: 1 choice, 1 numeric and 1 explain item. Exit ticket: 2 questions.
- Long tasks (sovella/tasks.json), 6 tasks, 95 p:
  - s1 Paineilmanostin: calc, 15 p.
  - s2 Maatilan biokaasumoottori: calc, 15 p.
  - s3 Ilma lasiruiskussa: data → graph → fit → interpret, 20 p.
  - s4 Meriveden lämmöllä kulkeva laiva: word, 15 p.
  - s5 Ilman moolimassa punnitsemalla: experiment, 15 p.
  - s6 Alipainenostin ja lasilevy: cross-module with fy4-4/5/6, pressure force plus friction and Newton II with a force diagram, 15 p.

## Numbers computed (answers.py)
- s1: a 562 kPa; b 21,2 kJ; c gauge 650 kPa (total 751 kPa).
- s2: a 34,9 kg; b 175 kW; c 84,0 %.
- s3: fit k = 0,135 ml/°C, b = 37,7 ml, θ0 ≈ −279 °C; the extreme lines give −265 and −294 °C (±15 °C). c 1,65 mmol.
- s4: b 6,0 %.
- s5: a 25,4 g/mol.
- s6: m 72,0 kg; a 11,2 kPa; b 18,7 kPa.
- Inquiry:
  - Sovella numerics: 17,7 kN, 152 kPa, 832 kg, 750 J.
  - Tarkista: 58,3 kW.
  - Hook: 331 kPa · 253 K : 293 K ≈ 286 kPa total, gauge about 185 kPa.

## Checks
- Passed: practice.py figures, units.py figures, practice.py check (6 tasks, 95 p), units.py check (35 units ok), build.py fy9-kaasut, and check_layout at 360 and 1280.
- Playwright at 390 and 1280: every choice and numeric item was answered correctly, and every solution, model answer and detail was opened. There were no console errors, no .katex-error and no raw $.
- After looking at the screenshots:
  - I resized the solution figures to a 420-wide viewBox, so labels are 16–17 px at 390. Before this they were 10–12 px.
  - I fixed clipped axis labels, the extreme-line label crossing the lines and binary-minus spacing in s3-extra.
  - I moved the rengas temperature labels off the y axis.

## Open questions
- s4 and s5 rely on invented data and say so. The hot-air balloon numeric (Sovella) avoids Archimedes and uses density × volume only.
- I did not add a teacher-facing extra figure for the fast-students question in teacher.md (V(−25 °C) ≈ 34 ml, read from the line).

## Shared issues
- The reused FY3 figures fy3-10/pt-suorat and fy3-11/pv-isobaari have labels of 13 px at 390, below the 14 px rule. They are not in this unit's folders.
- There is no assets/units/fy9/units.css. At 1280 the solution figures fill the whole column (about 570 px) and the content column sits left with empty space on the right.
- build.py <id> also rewrites preview/index.html and the module pages (preview/en, preview/fi-easy), not only preview/<id>.html.
- In this run the mixer.py crash reported earlier for fy9-energia did not occur.
