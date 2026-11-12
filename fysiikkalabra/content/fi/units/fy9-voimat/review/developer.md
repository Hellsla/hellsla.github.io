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

## Round 1 fixes

### Blocking (pedagogy)
1. **s4 answered before the student reaches it.** Exit ticket q1 replaced: no walker any more; it now asks for the third-law partner of a book's weight on a table (Maa, not the table's normal force). Cut the car sentence ("Auton eteenpäin vie tien lepokitka vetäviin pyöriin …") from `unit.md` Ydinajatus; the hook is now answered with the trailer's forces only. `teacher.md` Pohdinta line no longer gives the car answer and points to the long task *Mikä vie eteenpäin?*. Also took "tien lepokitka vetäviin pyöriin" out of the `tarkistus-1` correct-option feedback ("eteenpäin vievä voima").
2. **Exam-marking claim and named YTL task.** Dropped from `unit.md` and `teacher.md` ("kevät 2025, tehtävä 4.1" removed). Both now say: "Kokeessa voimakuvion pisteet menetetään puuttuvasta, ylimääräisestä tai väärään suuntaan piirretystä voimasta."
3. **Correct option longest.** `tarkistus-1` correct option shortened to 65 characters (distractors 63, 67). `kaksi-kappaletta` correct option drops "noin 24 N" (65 vs 66–70); the value 23,5 N stays in its feedback.

### Polish (science)
1. s5 a Vastaus: "puolet tulosten vaihteluvälistä (0,384–0,445)"; rubric `uncertainty` line says "epävarmuus on puolet vaihteluvälistä".
2. s6 text: added "Rinteen ja pellon välinen kohta on loiva, eikä nopeus muutu siinä."; s6 b Periaate says the same.
3. s4 d criterion 3 and solution: "eteenpäin vievä lepokitka vaikuttaa vain vetäviin etupyöriin".
4. s5 b Johtopäätös: "puhelin lähtee liukumaan jo noin 22°:n kulmassa".
5. s5 a Periaate: the quick lift presses the cover against the phone, raising N and the friction limit briefly, and the angle is read late, so 33° is not the slip limit.
6. Static friction labels: the shared `voimakuvio` renderer cannot draw `F_{μ0}` (`F_mu0` becomes `\overline{F}_{mu0}`), so took the reviewer's alternative: `unit.md` now says once that $\overline{F}_\mu$ in force diagrams means either static or kinetic friction.

### Polish (pedagogy)
- Timing: teacher.md Sovella step now does *Nosturi* and *Jyrkkä pulkkamäki* in class; *Pulkan veto vinossa* and *Ylös lyöty lentopallo* are optional in class, homework otherwise.
- Correct option first in source: moved to positions 3/2/4/3/2 in virhe-rinne, hihna, suodatin, kaksi-kappaletta, tarkistus-1.
- lt-6: "Nolla, …" distractor lengthened to 45 characters.
- Tutki part b (60 kg plateau): not done; the interpret activity takes one question, and the Järkevyys of the solution already compares the 60 kg terminal speed (48 m/s).
- Cross-chapter synthesis: no change (reviewer: fine).

### Polish (visual)
- Units in parentheses in `unit.md` are now LaTeX: ($\text{N}$), ($\text{kg}$).
- `kartta`: the coupled-bodies entry is now `\Sigma F_x = m_i a_x`, the component (scalar) form like the hub `\Sigma F_x = ma_x`; the vector laws keep overlines.
- `fy4-14/vt` small labels at 390 px: shared figure, see Shared issues 3.
- `hihna` taller viewBox: not changed; labels are 15 px and legible.

### Also fixed
- `check_layout` now reported a 2 px overlap of the v and a labels in `kalteva`; moved the arrows apart (offsets 42 and 86).

### Checks after the fixes
`units.py figures`, `practice.py figures`: written / up to date. `practice.py check units/fy9-voimat`: OK, 6 tasks, 95 points. `units.py check`: 38 units OK. `build.py fy9-voimat` OK. `check_layout` 360 and 1280: OK. Playwright at 390 and 1280: 11 choices and 6 numerics answered "Oikein.", all models and details opened, 0 console errors, 0 `.katex-error`, no raw `$`, no horizontal scroll. Looked at `kartta` and `kalteva` at 390 px.

### Shared issues (added)
3. `fy4-14/vt` (catalogue figure): axis ticks and curve labels are about 10 px at 390 px; enlarge the fonts there.
4. `voimakuvio` blocks cannot label static friction `F_{μ0}` (`scripts/fbdspec.py` `tex_of`: a subscript like `mu0` is not mapped to `\mu 0`).

Content hash after Round 1: db8ff4439951f193.

## Ratkaisutavan tarkistus (2026-11-12)
- s5 a): Kaavaan keskiarvo $\alpha_\text{ka}$ ja epävarmuus $\Delta\mu_0$ symboleilla (ennen vain $\mu_0=\tan\alpha_\text{ka}$ ja luvut sijoituksessa).
- s3 d): lisäpunnus saa symbolin $m_\text{x}$; ennusteen $k'$ ja $F_0'$ kaavat Kaavaan (ennen vain Vastauksessa).
- inquiry tarkistus-2: $a$ ratkaistu symboleilla ennen sijoitusta.
- Vastaukset eivät muuttuneet. fi-easy ja en vastaavasti.
