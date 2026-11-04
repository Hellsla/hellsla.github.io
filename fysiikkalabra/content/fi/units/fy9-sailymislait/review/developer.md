VERDICT: DONE

Unit fy9-sailymislait, "Mekaaninen energia ja liikemäärä" (FY9 chapter 3, order 3). It reviews FY4 chapters fy4-7, fy4-8, fy4-15, fy4-9, fy4-10 and fy4-11. Developer report 2026-11-04.
Content hash at hand-over: 82147d0c9120ddde (`python3 scripts/units.py hash fy9-sailymislait`).

## Files
- `content/fi/units/fy9-sailymislait/unit.json`: course FY9, chapter 3, order 3, kind review, 75 min, subjects physics. `sources` is empty because every dataset is an invented example.
- `content/fi/units/fy9-sailymislait/unit.md`: the Why question (two coupling wagons), hero, `## Ydinajatus` (choosing the conservation law, concept map, the hook answered with the to-scale `tormays` figure), `## Kaava: Mekaaninen energia ja liikemäärä` (E_k, E_p, energy principle, W = F∥s, p = mv, impulse, F_ka, 1-D momentum conservation, elastic and inelastic collisions, s_p, a = μg, P = ηρQgh, P = ½ηρAv³, each with its symbols and conditions), `## Yleisiä virheitä {Virheet}`, `## Kertaa tarvittaessa {Kertaa}`. The theory is about 500 words.
- `content/fi/units/fy9-sailymislait/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-sailymislait/sovella/tasks.json` and `solutions.md`. `lessons/units/fy9-sailymislait/sovella/answers.py` and `figures.py`, which draws the two s3 model graphs: s_p(v0), and s_p/v0 against v0 with the fit.
- `lessons/units/fy9-sailymislait/figures.py`: `hero` (a winter railway yard, no text), `kartta` (concept map, 380 wide), `tormays` (the hook to scale: velocity arrows, momentum bars and E_k bars with the half lost as internal energy).

## Counts
- Pohdinta: 1 hook. Ennusta: 6 choice items, one per chapter (mapped in teacher.md). Every option's feedback names the chapter as "luvussa *…*".
- Tutki: 1 interpret on an air-track table of three collisions (`source: example`). The numeric question asks for the share of kinetic energy lost in the velcro collision (41,7 %). The model answer compares all three collisions.
- Teoriatiivistelmä: 1 theory activity with 4 sections.
- Sovella: 4 choice (find the error in a bounce Δp; read the catalog graph `fy4-9/pysaytys`; skaters pushing apart; stopping distance on a wet road). 4 numeric, each with a full solution, 3 hints and mistakes: cyclist downhill 13,5 m/s; small hydro plant 3,30 MW; seat belt 6,48 kN; hockey tackle with opposite signs 1,18 m/s.
- Tarkista: choice (ballistic pendulum: which law in which phase), numeric (slide, 53,6 %), explain (head-on crash against a wall). All three have `practice` links. Exit ticket follows.
- Tehtävät: 6 tasks, 95 points.
  - s1 Vaijeriliuku järven yli (calc, 15)
  - s2 Curlingkiven lyönti (calc, 15)
  - s3 Jarrutuskoe märällä asfaltilla (data → graph → linearise → fit → interpret, 20)
  - s4 Joen voimala vai tuulipuisto (word, 15)
  - s5 Katoaako liikemäärä? (report critique and design, 15)
  - s6 Paalutuskone ja lämpenevä paalu (cross-module: collision, energy principle and fy3-6 Q = cmΔT, 15)
- Every task has `skills` and `links`.

## Numbers (computed in Python: answers.py and scratch generators)
- s1: √(2gh) 26,6 m/s; W −19,7 kJ; F 48,1 N; brake 769 N (0,96 mg).
- s2: μ 0,01015; v2' 0,57 m/s; 85 % of E_k kept; 1,63 m.
- s3: fit t_r 0,864 s, k 0,0799 s²/m. Values read from the line at (10; 1,66) and (25; 2,86) give t_r 0,86 s, a 6,25 m/s² and μ 0,637. s_p(100 km/h) = 85,6 m.
- s4: (9/6)³ = 3,375; P = 9,54 MW, and 12,7 MW at 12 m.
- s5: trial 2 Δp −6,32 %; trials −11,9, −6,3, −3,7 and −2,9 %; equivalent deceleration 0,011 m/s².
- s6: 3,43 m/s; v' 2,61 m/s; loss 4926 J (23,9 %); 916 kN; ΔT 7,1 K after 50 blows.
- Hook: 0,80 m/s; 41 → 20 kJ.

## Checks
- `units.py figures fy9-sailymislait` and `practice.py figures units/fy9-sailymislait` are up to date.
- `practice.py check units/fy9-sailymislait`: OK, 6 tasks, 95 points. `units.py check`: 38 units OK.
- `physics_phrases.py` on the unit finds 0 sentences.
- `build.py fy9-sailymislait` builds the preview.
- `check_layout.py --width 360` passes, with a warning that the 4-column Tutki table scrolls. `--width 1280` passes.
- Playwright (`_browser.launch`) at 390 and 1280:
  - all 11 choice items answered correctly with their feedback, and all 6 numeric items answered ("Oikein.");
  - the explain model, every "Olen tehnyt ratkaisun" box and every details element opened;
  - no console or page errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at the hero, the map, `tormays`, the Tutki section, the cyclist solution and the s3 solution and graphs at 390 px, and fixed these:
  - label overlaps in `tormays`;
  - axis titles that ran off the s3 graphs; their labels are now size 30, about 15 px at 390;
  - an unwrappable √ formula;
  - colliding inline \dfrac in the s3 b solution;
  - an 8-column table, now vertical.

## Open questions
- All data are invented examples (`source: example`). The curling stone mass and μ ≈ 0,01 are realistic orders of magnitude, not measured values.
- The s3 b text says "muodosta suure, jonka kuvaaja … on suora". This prompts the student to linearise without naming the formula. A reviewer may judge whether this is too strong a hint for an Osa III task.
- The s6 40 % share of the lost energy that stays in the pile head is an assumption stated in the task.

## Shared issues
None new. The `fy4-9/pysaytys` catalog figure (reuse "reveals") is used as a Sovella choice figure. This is intended in a review unit.

## Round 1 fixes
Content hash after the fixes: e3a353d8ecfc76ac (reviewed: 82147d0c9120ddde).

### Science
1. Blocking. Changed the last sentence of the tarkistus-3 model. It no longer calls a rigid obstacle more dangerous. It now says "tai törmäys, jossa oma keula rypistyy lyhyemmän matkan, koska se lyhentää pysähtymisaikaa".
2. In the Yleisiä virheitä of unit.md, the −2mv bullet now says "samalla nopeudella kimpoavalle pallolle".
3. In s1 c (tasks.json and solutions.md) the force is now "jarrun vaunuun kohdistama". The solution names the system (laskija, valjaat ja vaunu, 82,0 kg), and the weight is compared with the weight of that whole system.
4. In s6 d the solution's Periaate and Kaava, its Yleisiä virheitä and the rubric's `equation` detail now use $\Delta U = cm\Delta T$ instead of Q. The condition that the state does not change is kept.
5. The tarkistus-2 mistake value is now 7.11.
6. The s2 b Vastaus now says why the result has two decimals: it comes from a difference, and the 0,05 m/s read from the video limits it to about 0,01 m/s.
7. In teacher.md, 15–25 min now reads "lähes vain jousipuskurissa" and "katoaa lähes $m_B:(m_A+m_B)$".

### Pedagogy
1. Blocking. The Miksi question no longer gives the result. It asks why the wagons "jatkavat hitaammin kuin ennen kytkeytymistä".
2. Blocking. The `puskurit` task is rewritten.
   - I could not use a figure without the caption. A unit cannot own a referenced figure (figcat owners are course lessons only), and a variant in `lessons/FY4/fy4-9/figures.py` would be a shared edit.
   - The question now asks the student to read the peak forces and the durations. The correct option is "suurin voima noin nelinkertainen, kesto noin neljäsosa". The distractors are "so the impulse is 4×" and "longer time, so a larger impulse".
   - The caption "yhtä suuret pinta-alat" no longer states the correct option. It only supports the feedback.
3. The correct option of `virhe-kimpoaminen` is shortened. The three options are now 72, 82 and 73 characters.
4. In teacher.md, slow students now do only *Pienvesivoimala* and *Turvavyö kolarissa* in class, and the Tarkista explain task is homework.
5. The Sovellukset display block now holds $P_\text{vesi} = \eta\rho Qgh$ and $P_\text{tuuli} = \tfrac12\eta\rho Av^3$, with all their symbols and the condition for the v³ law.
6. The correct option of tarkistus-1 now has a "Kertaa luvussa *Mekaanisen energian säilyminen ja energiaperiaate*" link.

### Visual
1. Blocking. The third box of `kartta` is renamed "sovellukset". It matches the aria-label, and the törmäys row is kept.
2. `kartta` now uses vector bars: $\overline{p} = m\overline{v}$, $\Sigma\overline{F}\,\Delta t = \Delta\overline{p}$ and $\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}$.
3. In `tormays`, the lost-energy box is a neutral grey (#dee2e6) and its label is MUTED, so it no longer uses the orange of acceleration. The figure now shows the values 51 200 kg·m/s, 41 kJ and 20 kJ.
4. The units in the Kaava "missä" sentences are now LaTeX.
5. Not fixed. `fy4-9/pysaytys` ticks are about 13 px at 390 px. This is a shared figure, so it is listed under Shared issues.

### Checks after the fixes
- `units.py figures`: written. `practice.py figures`: up to date.
- `practice.py check`: OK, 6 tasks, 95 points. `units.py check`: 38 units OK.
- `physics_phrases.py`: 0 sentences.
- `build.py fy9-sailymislait`: builds the preview.
- `check_layout` 360: OK, with the one known scrolling table. `check_layout` 1280: OK.
- Playwright at 390 and 1280:
  - all choices answered, with the expected "Oikein." feedback on the five Sovella and Tarkista choices;
  - all 5 numeric items answered "Oikein";
  - no console errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at `kartta`, `tormays` and `puskurit` at 390.

### Shared issues (new)
- `lessons/FY4/fy4-9/figures.py` `pysaytys`: the axis ticks are about 13 px at 390 px. A variant without the "yhtä suuret pinta-alat" caption, for example `"pysaytys-ilman": lambda: pysaytys(caption=False)`, would let review units ask about the areas.
