VERDICT: PASS
CONTENT-HASH: 9a4783083d3a7ff6

Round 2. Counts still match the plan table: hook 1, Ennusta 6, Tutki 1, theory, Sovella 8 (4 choice, 4 numeric),
Tarkista 3 plus the exit ticket, and 6 long tasks (89 p). Rubric points add up in every part. Options are shuffled
by the page.

## Blocking
None.

## Round 1 Polish, verified
- **Hook disclosure.** `lahto-4` is now a burning candle (h, t). The milk and measuring-cylinder wording is gone, and
  `tiheys-suora` was replaced. The hook's answer now appears first in the theory section (m = ρV + m₀), which is the
  intended teaching step, and Tarkista 3 returns to it.
- **Option lengths** (characters without LaTeX markup). lahto-6: correct 63 against 70/76/78. vakiotermi: 85 against
  80/84/86. aika-kuvaaja: 26 against 25/25/27. lahto-4: 61 against 58/60/65. No correct option is the longest by a
  clear margin.
- **Giveaways.** `aika-kuvaaja` (fixed track, (1/v, t)) practises the inverse-to-reciprocal idea in a motion
  context. s6 b) adds a non-zero intercept (−V₀) that no short task shows, and the theory already states Boyle's
  (1/V, p) form. `jousi-suora` (title "Jousen suora") practises slope against ratio with a length offset, which
  transfers to s3 and Tarkista 3 without giving their answers. "Kuula kourussa" is neutral. s6 b) no longer gives
  the hose hint.
- **Order and timing.** s1 a) now argues the precision from the clock spread, so it no longer needs b). The
  teacher.md timing is realistic: Tutki 10 min, theory 10 min, Sovella 22 min with named items to skip (Kolikkopino,
  Kuula kourussa), Tarkista 13 min, and s3 a–b plotting set as homework after a 5-minute class discussion of the
  data.

## Polish
1. `inquiry.json` › `jousi-suora`: the 48.6 and 8 feedbacks are nearly the same text. Write "toisen pisteen" for
   48.6, and add a chapter pointer for the spring law as the choice items have, for example "Kertaa jousivoima
   luvussa *Jousivärähtelijä ja heiluri*".
2. `inquiry.json` › `lahto-5`, option $\tfrac{1}{t}$, feedback: "kuten Boylen laissa" points ahead to s6 b). Use a
   neutral example, for example "kuten matka-aika vakionopeudella".
3. `sovella/tasks.json` s3 a): "josta voi määrittää myös suoran vakiotermin" already tells the student the data
   lie on a line before b). Write "…josta voi määrittää myös vakiotermin".

## Checked
- Read the whole inquiry.json, tasks.json, solutions.md (s1, s3, s6), teacher.md, unit.md and exit-ticket.json.
- In Playwright at 390 px: checked the aika-kuvaaja options and feedback, and the kolikot, jousi-suora and
  tarkista-2 numeric inputs with the correct value and each mistake value. Every mistake gets its own feedback.
- Looked at lahto-4, aika-kuvaaja and jousi-suora at 390 px with the hints and solution open.
