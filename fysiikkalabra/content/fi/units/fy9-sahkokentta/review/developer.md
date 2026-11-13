VERDICT: DONE

Unit fy9-sahkokentta, "Sähkökenttä ja kondensaattori" (FY9 chapter 5, order 2). It reviews FY6 chapters fy6-10 to fy6-16. Developer report 2026-11-04.
Content hash at hand-over: 63bd93568ec525b8 (`python3 scripts/units.py hash fy9-sahkokentta`).

## Files
- `content/fi/units/fy9-sahkokentta/unit.json`: course FY9, chapter 5, order 2, kind review, 75 min, subjects physics. `sources` is empty because every dataset is an invented example and no fact in the unit is time-dependent.
- `content/fi/units/fy9-sahkokentta/unit.md` contains, in order:
  - the Why question: a door-handle spark in winter has thousands of volts but does no harm;
  - the hero;
  - `## Ydinajatus`: charge makes a field, $\overline{F} = q\overline{E}$, work and potential energy, the capacitor, components and safety; the concept map; the hook answered with the `kipina` figure;
  - `## Kaava: Sähkökenttä ja kondensaattori`, in four subsections: charge, force and field (with the `levyt` figure); potential and energy; the capacitor; components and safety;
  - `## Yleisiä virheitä {Virheet}` (7 items);
  - `## Kertaa tarvittaessa {Kertaa}` (fy6-10 … fy6-16).
  The theory text is about 570 words.
- `content/fi/units/fy9-sahkokentta/inquiry.json`, `exit-ticket.json` (2 questions: an electron through 500 V, a capacitor at double voltage), `teacher.md`.
- `content/fi/units/fy9-sahkokentta/sovella/tasks.json` and `solutions.md`.
- `lessons/units/fy9-sahkokentta/sovella/answers.py` and `figures.py`. The figures are the two s3 model graphs: C(d), and C against 1/d with the fitted line, the circled read points and the 22 pF intercept.
- `lessons/units/fy9-sahkokentta/figures.py`:
  - `hero`: a winter hallway, a wooden door with a brass handle, a hand in a red knitted sleeve and a small spark, a wool rug, a snowy window and a radiator; no text;
  - `kartta`: the concept map, 380 wide, a hub and four boxes;
  - `kipina`: the fingertip (− charges), the handle plate with induced + charges, the green field across about 3 mm, and U, Q, W;
  - `levyt`: plates at 200 V and 0 V, the green uniform field, dashed equipotentials, and a proton and an electron with red forces along and against $\overline{E}$.
- Field green, force red, velocity blue (as in the FY6 figures). The sign of a charge is also shown by + or −.

## Counts
- **Pohdinta:** 1 hook (the door-handle spark).
- **Ennusta:** 6 choice items, one per chapter fy6-10 … fy6-15 (fy6-16 comes in the Sovella numeric *Sähköauton latausaika*). teacher.md maps them. All feedback names the chapter as "luvussa *…*". The correct options are at 2, 1, 2, 0, 1, 0.
- **Tutki:** 1 interpret on the catalog graph `fy6-12/ex-vgraph` (source: model). It reads V = 150 V at 3,0 cm and asks for the electron's speed: 7264 km/s, tolerance 0,03, with 3 mistakes.
- **Teoriatiivistelmä:** 1 theory activity.
- **Sovella:** 4 choice items:
  - find the error in an LED series resistor;
  - read the catalog graph `fy6-13/ex-qu`;
  - the force diagram of a floating oil drop;
  - claims about the fuse and the RCD.

  Then 4 numeric items, each with a full solution, 3 hints and 2–3 mistakes: three charges on a rail 35,95 µN, a dust particle in a precipitator 6,008 pN, the defibrillator voltage 1690 V, and the electric-car charging time 3,865 h.
- **Tarkista:** a choice (the force at the plate is the same), a numeric (paper capacitor, 112,6 mJ) and an explain (a balloon on the wall). All three have practice links. The exit ticket follows.
- **Tehtävät:** 6 tasks, 95 points; every task has `skills` and `links`.
  - s1 Kaksi varattua palloa langoissa (calc, 15)
  - s2 Demonstraatiokondensaattori ja lasilevy (calc, 15)
  - s3 Levyjen etäisyys ja kapasitanssi (data → graph → linearise to 1/d → fit → interpret slope and intercept, 20)
  - s4 Lintu, onkivapa ja pudonnut johdin (word, 15)
  - s5 Aurinkopaneelin hyötysuhde (report critique and design, 15)
  - s6 Satelliitin ionimoottori (cross-module with FY4 momentum, fy4-9 and fy4-4, 15)

## Numbers (answers.py; `practice.py check` compares them with tasks.json)
- s1: α 5,74°, F 0,493 mN, q 18,7 nC (1,17·10¹¹ electrons), after contact 0,2465 mN, new distance 6,35 cm (both the small-angle form and the exact solution).
- s2: C 184,5 pF, Q 0,830 µC, W 1,868 mJ, E 1,50 MV/m (breakdown at 9 kV), with glass U′ 803,6 V and W′ 0,3335 mJ.
- s3: the line read at (0,20; 93) and (1,00; 376) gives k 353,8 pF·mm, so ε₀ is 8,844·10⁻¹² F/m (−0,1 %); the intercept is 22,2 pF. The least-squares fit gives 353,7 and 22,2.
- s4: 1,5 mV between the bird's feet; uniform-field gap 6,7 mm at 20 kV.
- s5: the table's maximum is 0,989 W at 25 Ω, so η is 16,5 %; the student's U_t·I_k gives 1,281 W and 21,35 %.
- s6: v 40,21 km/s, E 1,1 MV/m, 9,988·10¹⁸ ions/s, 2,177 mg/s, F 87,54 mN, Δv 349,1 m/s and Xe 5,644 kg in 30 d, P = UI = ½ṁv² = 1760 W.
- Hook (figures.py): 9,0 kV, 0,90 µC and 4,05 mJ for C = 100 pF; 0,05 C for 50 mA in 1 s, which is 55 000 times more.

## Checks
- `units.py figures` and `practice.py figures` are up to date.
- `practice.py check units/fy9-sahkokentta`: OK, 6 tasks, 95 points.
- `units.py check`: 42 units OK. During the work it reported errors only for fy9-tasavirta, which another agent was writing at the same time.
- `physics_phrases.py` on each file: 0 sentences. No `\vec` or `\mathbf`.
- `build.py fy9-sahkokentta` builds `preview/fy9-sahkokentta.html` as a draft.
- `check_layout.py --width 360` and `--width 1280`: OK. I fixed these first:
  - a label overlap in `levyt`;
  - the axis labels of both s3 graphs, which went outside the figure;
  - crowded 1/d tick labels.
- Playwright (`_browser.launch`) at 390 and 1280:
  - all 11 choice groups answered correctly, all 6 numeric items show "Oikein." (the Tutki item was confirmed in a separate run);
  - all details opened, every "Olen tehnyt ratkaisun" ticked, models and criteria shown;
  - no console errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at the hero, kartta, kipina, levyt and both s3 graphs at 390 and 1280, and at the Ennusta, task and solution sections of the full page. I moved the electron and proton force labels off the equipotential lines.

## Open questions
- All data are invented examples. The s3 noise is about 1 %. The s5 table comes from a ten-cell diode model, so its points are consistent with Ohm's law for each load. The s6 thruster is realistic in its order of magnitude (it resembles NSTAR-class engines) but is not a real engine.
- The hook uses a body capacitance of about 100 pF and a uniform-field breakdown estimate for a 3 mm gap. Both are order-of-magnitude values. The text says "noin", and the field figure is labelled as not to scale.
- s4 b: the 7 mm gap is presented as a lower bound, not as a safe distance. A science reviewer may want the real safety distances for 20 kV lines named; I did not add them because they would need a dated source.
- s3 c: the agreement with ε₀ (0,1 %) is closer than the stated uncertainty. The solution says this is partly chance and gives ±0,3·10⁻¹² F/m.

## Shared issues
- The scratchpad is shared between the parallel unit agents (other units' captures were in the same folder). I kept my builder scripts and captures in `scratchpad/sahko/`. None of this blocks the unit.
- `scripts/physics_phrases.py` takes a file, not a unit folder (as noted in fy9-ympyraliike).

## Round 1 fixes (2026-11-04)

### Blocking
- **Science 1 (s4, 20 kV is the line-to-line voltage).** I used fix (a). The task text now says that the nominal 20 kV is the voltage between the phase conductors, so each conductor is about 12 kV from earth. Rubric a3 now says about 12 kV to earth. Rubric b2 now gives 12 kV : 3 MV/m ≈ 4 mm. Rubric b4 now says 12 kV. In the solution, s4 a and b use 12 kV, and b adds a line that explains 20 kV/√3 ≈ 12 kV. The body current is now about 1,2 A, and the Yleisiä virheitä item says 4 mm. I added a new Yleisiä virheitä item for using 20 kV across the gap. In answers.py I added `s4-U-earth-kV` (11,55), and `s4-gap-mm` is now 4,0 and `s4-I-body` 1,2.
- **Pedagogy 1 / Visual 2 (s1 a has no model force diagram).** I added `fy9-sahkokentta-s1-fbd` to `lessons/units/fy9-sahkokentta/sovella/figures.py`. It has a situation picture and the right ball's force diagram, drawn with `fbd.FBD` (body rectangle, a_dir 0). The diagram shows $\overline{G}$, $\overline{T}$ along the thread and $\overline{F}_\text{s}$, all red, with α. The angle is drawn at 25° and the text says so. It sits under a new **Voimakuvio:** line, right after Kysytty and before any equation.
- **Visual 1 (labels under 14 px at 390).** In kipina the formula rows are now size 34, `\tfrac{MV}{m}` became MV/m and ½ is now `\dfrac`. The captions are now size 28, and the figure height went from 500 to 540. In levyt the voltage ticks went from size 20 to 26, and in kartta the size went from 20 to 22 (the grey words from 16 to 17). I measured the rendered glyphs at 390 with Playwright. Every label in kartta, kipina, levyt and the s3 graphs is now at least 14,2 px, scripts included. In s1-fbd (width 500, size 28) the main labels are 16,7 px and only the subscript s of F_s is 11,7 px.

### Polish
- Science 2 (s3 c precision): the rubric and the Vastaus now give $(8{,}8 \pm 0{,}3) \cdot 10^{-12}$ F/m and accept 8,84 as an intermediate value. I rewrote the Järkevyys paragraph to match.
- Science 3 (s2 d criterion): fixed with the wording the reviewer proposed.
- Science 4 (defibrillaattori): the Vastaus is now 1,7 kV with two significant figures, and 1690 V is accepted as an intermediate value. The numeric answer and its tolerance are unchanged.
- Science 5 (lt-5): the battery is now 3,0 V, and the correct option is "Koko 3,0 V".
- Science 6 (s6 c): the rubric now says 5,64 kg with three significant figures, which matches the solution.
- Pedagogy 2 (oljypisara): I renamed the task "Mikä kuvaus: leijuva öljypisara". It has no figure options yet, because those need four deliberately wrong FBDs.
- Pedagogy 3 (aineisto): hint 2 now asks the student to state the energy principle in words. The formula and the substitution moved to hint 3, so there are still 3 hints.
- Pedagogy 4 (tarkistus-1 option 1 feedback): rewritten. It now says that each plate gives a field that does not depend on the distance.
- Pedagogy 5 (tarkistus-2): the Sijoitus now ends at 0,1126 J, and the only final value is 0,11 J.
- Pedagogy 6 (teacher.md): the Sovella window now names the two calcs done in class and the two left for home.
- Pedagogy 7 (s1 set-up is common): not changed. The numbers and the d part (the new equilibrium, r = r₀/∛2) are original, and the reviewer did not block it.
- Visual polish, kipina spark: added a spark (a glow and a zigzag) in the gap between the field lines, and the alt text mentions it.
- Visual polish, s3 table: the columns are now centred (`|:---:|:---:|`).
- Visual polish, s3 graphs small at 390: not changed. The graphs render 298 px wide inside the solution box, and their labels are already 14,9 px. Making the plot wider would push the axis labels out of the frame.
- Visual polish, Ydinajatus: I split the second paragraph into two, at "9 kV:n jännitteestä."

### Checks rerun
I ran `practice.py figures` / `check` (OK, 6 tasks, 95 points) and `units.py figures` / `check` (44 units ok). I built only `build.py fy9-sahkokentta`. `check_layout.py` passed at 360 and at 1280. Playwright at 390 and 1280: 11 choice groups and 5 + 1 numeric items, no console errors, 0 `.katex-error`, no raw `$`, no horizontal scroll. I looked at s1-fbd, kipina and levyt in screenshots. physics_phrases found 0 sentences.

### Shared issues
- The reused chapter figures `fy6-12/ex-vgraph` and `fy6-13/ex-qu` render their labels at 13 px at 390 px width. They belong to the FY6 chapters, so I did not change them.

## Ratkaisutavan tarkistus (2026-11-12)
- sovella s3 d): Kaavassa pisteen $(1/d_1;\,C_1)$ määrittely.
- inquiry (elektronin nopeus): $V_0$ ja $U = V - V_0$ Kaavaan, Sijoitus $(150\,\text{V} - 0\,\text{V})$.
- inquiry (sähköauton lataus): $W_0$, osuus $s$ ja $t = sW_0/(3\eta UI)$ Kaavaan; luvut $0{,}60 \cdot 64\,\text{kWh}$ vain Sijoituksessa.
- Muut osat (s1, s2, s4–s6, muut inquiry-tehtävät) täyttävät käytännön.
