VERDICT: DONE

Unit fy9-voimat, "Newtonin lait ja voimakuvio" (FY9 chapter 3, order 2). Reviews FY4 chapters fy4-3, fy4-4, fy4-5, fy4-13, fy4-6 and fy4-14. Developer report 2026-11-04.
Content hash at hand-over: 85c6ce246c4dc32e (`python3 scripts/units.py hash fy9-voimat`).

## Files
- `content/fi/units/fy9-voimat/unit.json`: course FY9, chapter 3, order 2, kind review, 75 min, subjects physics; `sources` empty (all data are invented examples).
- `content/fi/units/fy9-voimat/unit.md`: Why question (a car and its trailer: why do action and reaction not cancel?), hero, `## Ydinajatus` (method: body → interactions → axes → ΣF_x = ma_x, concept map, the hook answered at the end), `## Kaava: Newtonin lait ja voimat` (laws I–III, G = mg, F_μ = μN, F_μ0 ≤ μ0N, slope components with the `kalteva` figure, coupled bodies, terminal speed), `## Yleisiä virheitä {Virheet}`, `## Kertaa tarvittaessa {Kertaa}`. About 530 words.
- `content/fi/units/fy9-voimat/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-voimat/sovella/tasks.json`, `solutions.md`. `lessons/units/fy9-voimat/sovella/answers.py` and `figures.py` (the s3 model graph).
- `lessons/units/fy9-voimat/figures.py`: `hero`, `kartta` (concept map, 380 px wide), `kalteva` (sled on a slope with its force diagram and dashed components), `hihna` (deliberately wrong force diagram, made with `FBD(wrong=...)`, pasted into the inquiry text by running the file).

## Counts
- Pohdinta: 1 hook. Ennusta: 6 choice questions (diagnostic, each mapped to a chapter in teacher.md).
- Tutki: 1 interpret. It reuses `fy4-14/vt` (two skydivers, `source: simulated`) and has a numeric question about the drag at terminal speed (981 N) with a force-diagram solution.
- Teoriatiivistelmä: 1 theory activity.
- Sovella: 3 choice (find the error: slope; coffee filters; two blocks, T ≈ 23,5 N), 1 interpret with a choice question (find the error: box on a belt, using the pasted wrong force diagram), 4 numeric (crane 6,77 kN; slanted pull μ 0,360; sledding hill 3,31 m/s²; volleyball 12,0 m/s²). Each has a solution with a voimakuvio block, at most 3 hints and common mistakes.
- Tarkista: choice (car uphill at constant speed), numeric (two boxes pushed, 48,0 N), explain (tan α0 = μ0); `practice` links on all three; exit ticket (friction when walking; N = 85,0 N on a 30° slope).
- Tehtävät: 6 tasks, 95 points. s1 Veneen vinssaus (calc + force diagram, 15), s2 Moottorikelkka ja kaksi rekeä (coupled bodies, 15), s3 Vaunu ja voima-anturi (data → graph → fit → interpret, 20), s4 Mikä vie eteenpäin? (word, 15), s5 Puhelin kirjan kannella (experimental, 15), s6 Liukurimäki (cross-module with fy4-2 kinematics, 15).

## Numbers (computed in Python: answers.py and the scratch generators)
s1 G 2746,8 N, G_x 664,5 N, N 2665,2 N, F_μ 666,3 N, b 1330,8 N; c α0 19,29° (tan 0,2493). s2 b 118,48 N, c 296,2 N. s3 fit k = 1,175 1/kg, b = −0,2807 m/s² → M 0,851 kg, F0 0,238 N; d μ 0,0285. s4 a(ice) 0,981 m/s², a(dry) 7,85 m/s². s5 μ0 = tan 22,5° = 0,414 (range 0,384–0,445). s6 a 10,09 m/s, b 64,8 m (v 36,3 km/h). Teacher extra: m_p ≈ 0,12 kg.

## Checks
- `units.py figures fy9-voimat`, `practice.py figures units/fy9-voimat`: up to date. `practice.py check units/fy9-voimat`: OK, 6 tasks, 95 points. `units.py check`: 37 units OK. fbdspec blocks check OK.
- `build.py fy9-voimat` builds the preview. `check_layout.py --width 360` and `--width 1280`: OK.
- Playwright (`_browser.launch`) at 390 and 1280: all 11 choice questions and 6 numeric questions answered correctly ("Oikein."), explain models and solutions opened. No console errors, no `.katex-error`, no raw `$`, no horizontal scroll.
- Looked at hero, theory, concept map, `kalteva`, `hihna`, the nosturi solution diagram and the s1–s3 diagrams and graph at 390 px. Fixed label overlaps (sledding hill axes) and raised the figure labels to size 28 (≥ 14 px at 390).

## Open questions
- Sovella *Etsi virhe: laatikko hihnalla* is an interpret activity with a choice question, not a plain choice question with a figure, because a unit figure cannot be referenced by id (see Shared issues). Its SVG is pasted into the text.
- The spring 2025 task 4.1 scoring note in teacher.md is from memory of the published marking guide; a reviewer may want to check the task number.
- The Tutki curves are the model values of the simulation (`source: simulated`); every other dataset is an invented example.

## Shared issues
1. figcat `owner()` cannot resolve unit figures (`lessons/units/<unit>/figures.py`), so a unit cannot use its own figure as a choice figure, an option figure or a `model_figure` by id. Workaround: paste the SVG into the text.
2. `scripts/inquiry.py` and `scripts/test_inquiry.py` only accept lesson folders, not unit ids, so the inquiry checks the brief lists cannot run on a unit. I used `units.py check` and my own Playwright script instead.
