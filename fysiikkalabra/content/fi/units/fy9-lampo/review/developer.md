VERDICT: DONE

Unit fy9-lampo, "Lämpö ja olomuodon muutokset" (FY9 chapter 2, order 2). Developer report 2026-11-04.
Content hash at hand-over: c908c7c1c4a5b48e (`python3 scripts/units.py hash fy9-lampo`).

## Files
- `content/fi/units/fy9-lampo/unit.json`: course FY9, chapter 2, order 2, kind review, 75 min, subjects physics, `sources` empty (all data are invented examples).
- `content/fi/units/fy9-lampo/unit.md` contains:
  - a Why question: melting snow at a campfire costs almost as much energy as heating the meltwater to boiling;
  - the hero and `## Ydinajatus`, which separates temperature, internal energy and heat and has a concept map;
  - `## Kaava: Lämpömäärä ja energiatase`, covering T = θ + 273,15, ΔU = Q + W, Q = cmΔT, Q = sm, Q = rm, Q_luovutettu = Q_vastaanotettu with the ice–water decision rule, ΔL = αL0ΔT, ΔV = γV0ΔT and P = UAΔT, each with symbols and conditions; the hook is answered here (21 / 334 / 419 kJ) next to a heating curve drawn to scale;
  - `## Yleisiä virheitä`, with 7 items;
  - `## Kertaa tarvittaessa`, linking fy3-3, -5, -6, -7, -14, -8 and -12.
  - It is about 640 words counting headings, link text and each formula as one word, so the prose is about 600.
- `content/fi/units/fy9-lampo/inquiry.json`, `exit-ticket.json` (2 questions) and `teacher.md`.
- `content/fi/units/fy9-lampo/sovella/tasks.json` and `solutions.md`.
- `lessons/units/fy9-lampo/figures.py`: `hero` (a lean-to shelter, a campfire, a kettle of snow and fells), `kartta` and `kayra`.
- `lessons/units/fy9-lampo/sovella/answers.py` and `figures.py` (the model graph for s3).

## Counts
- Pohdinta: 1 hook.
- Ennusta: 6 choice questions, one per chapter: fy3-3, -5, -6, -7, -14 and -8.
- Tutki: 1 interpret question. It reuses `fy3-7/melting-curve`, and its numeric answer is c_jää = 2083 J/(kg·K).
- Teoriatiivistelmä: 1 theory activity with 4 sections.
- Sovella: 4 choice and 4 numeric questions.
  - The choice questions are: spot the error in the melting reasoning, the metal rail vs. the wooden bench, the stuck lid, and the graph of an ice–water glass.
  - The numeric questions are: bath water 14 kg, party ice 2,03 kg, radio mast 180 mm, and a power cut 0,886 K/h.
- Tarkista: 1 choice, 1 numeric (heating cable, 3,88 kg) and 1 explain question, plus the exit ticket.
- Tehtävät: 6 tasks, 95 points.

  | Task | Type | Points |
  |---|---|---|
  | s1 Jäähallin uusi jää | calc | 15 |
  | s2 Varaava takka | calc | 15 |
  | s3 Kiehuvan veden höyrystyminen | data → graph → fit → interpret | 20 |
  | s4 Järvi talvella | word | 15 |
  | s5 Jään sulamislämpö kalorimetrillä | report critique and design | 15 |
  | s6 Jarrut tunturitiellä | cross-module with FY4 mechanical energy | 15 |

## Numbers (computed in answers.py and the scratch inquiry generator)
- s1: 21,9 GJ and 17,4 h. The shares are 82 % freezing, 16 % cooling the water and 2 % cooling the ice.
- s2: 81,6 K, 1,67 kW and 35,8 %.
- s3: the least-squares fit gives k = 0,1326 g/W, so r = 2,26 MJ/kg and P_h = 69 W. Reading the drawn line at (100 W; 4 g) and (1100 W; 137 g) gives r = 2,26 MJ/kg and P_h = 70 W. The single-point result 2,54 MJ/kg is 12,5 % too high.
- s5: the group's result is 371 kJ/kg; with the ice at −18 °C it becomes 333 kJ/kg.
- s6: 31,5 K, 134 K and 40,2 %.

## Checks
- Both `figures` commands are up to date.
- `practice.py check`: OK, 6 tasks and 95 points.
- `units.py check`: no errors for this unit. The errors it lists belong to fy9-kaasut, which is still in progress.
- `build.py fy9-lampo` passes and writes `preview/fy9-lampo.html`.
- `check_layout.py` passes at 360 and 1280. To get there:
  - I turned the s3 data table vertical.
  - I split the long s5 substitution into two lines.
  - I moved the top of the s3 graph down, because its axis label was clipped.
- Playwright at 390 and 1280:
  - Every choice was answered with the correct option and showed its feedback.
  - Every numeric answer was accepted ("Oikein."), including 14 for the bath-water task.
  - The model answer was shown and all solutions were opened.
  - There were no console errors, no `.katex-error` and no raw `$`.
- I looked at the screenshots and fixed what they showed:
  - In `kayra`, the label "Q = sm = 334 kJ" covered the y-axis, so I split it onto two lines.
  - In the s3 graph, the "1200" and "P (W)" labels were clipped and the P_h label overlapped the line. I redrew the graph 480 wide with 26 px labels and moved P_h to a leader line.
  - Figure labels are now at least 14 px at 390: kartta 17, kayra 14,3 and s3 16,1.

## Open questions
- The reused figure `fy3-7/melting-curve` in Tutki has labels of about 13 px at 390, because the interpret layout makes it 324 px wide. It lives in the FY3 module, so I did not change it.
- All datasets are invented examples, marked `source: example`. The material constants are textbook values (c = 4190 and 2100 J/(kg·K), s = 334 kJ/kg, r = 2260 kJ/kg).

## Shared issues
1. Developers working in parallel share one scratchpad, and another unit's developer overwrote my `gen_inquiry.py`. My files now live under `scratchpad/fy9-lampo/`.
2. No `assets/units/fy9/units.css` was found; fy9-energia reported the same. This time `build.py` did not crash in mixer.py.

## Round 1 fixes

### Science
1. Blocking, s5 b mug sign: fixed. solutions.md Vastaus now says that the group's formula would also credit heat taken by the mug to the ice, but that the gap of $1890\,\text{J}$ would need about $70\,\text{J/K}$, while a styrofoam mug has a few J/K, and the corrected value already matches the table. The wrong mistake line is replaced with "the mug is accepted without estimating its heat capacity". The rubric `conclusion` detail in tasks.json now says the same.
2. Blocking, s1 ice thickness with water density: fixed by stating the water layer. tasks.json now reads "ruiskutetaan vettä … yhteensä 3,00 cm:n kerros". solutions.md Annettu says "vesikerroksen paksuus" and the Vastaus line says "kerroksen paksuus". All numbers stay the same, and the answers.py comment is updated.
3. Blocking, phase change "vakiopaineessa": added in unit.md.
4. Polish, validity of the expansion formulas: unit.md now says "kiinteille aineille noin 100 K:n muutokseen asti, nesteen γ vain taulukon lämpötilan lähellä".
5. Polish, exit-ticket item 2: added that wood shortens much less than steel along the grain.
6. Polish, s3 d: "12 %" changed to "13 %".
7. Polish, s5 c: weighing by difference is now tied to ice that melts or drops while it is handled (model answer and rubric criterion).

### Pedagogy
1. Blocking: same fix as Science 1.
2. Polish, aineisto: the solution now says the start point is read between gridlines (±1 °C). Tolerance raised from 0,03 to 0,07, so readings of −15 and −17 are accepted.
3. Polish, Miksi quote: rewritten as a question (which takes more energy, melting or heating to boiling). It no longer gives the answer.
4. Polish, s6 d: "pumppaustyö" removed from the model answer, the Periaate and the rubric. Now only engine friction turns the energy into internal energy and the cooling system releases it.
5. Polish, units in plain parentheses: all of "(K)", "(kg)", "(°C)", "(1/K)" in unit.md are now LaTeX.

### Visual (PASS)
1. melting-curve label size: shared catalog figure (fy3-7), not changed. See Shared issues.
2. Flat sub-heading hierarchy: this comes from the shared template CSS, not the unit. See Shared issues.
3. Plain units: fixed (Pedagogy 5).
4. Desktop column: house layout, no change.
5. kayra labels at 14 px: these meet the brief's minimum of 14 px at 390 px, so not changed.

### Shared issues (added)
- `fy3-7/melting-curve` renders labels at about 13 px at 390 px. It needs a larger-label variant or the full card width.
- Template: `###` under a `## Kaava:` section should look visibly smaller than `##`.

### Checks rerun
- practice.py figures/check: OK (6 tasks, 95 points).
- units.py figures/check: 38 units ok.
- build.py fy9-lampo: built.
- check_layout: OK at 360 and 1280.
- Playwright at 390 and 1280, with all details open and every task answered: no console errors, no raw `$`, no .katex-error, no horizontal overflow.
