VERDICT: DONE

# fy9-magnetismi-valo: developer notes

FY9 lesson 14, "Magnetismi, induktio ja valo" (chapter 5, order 3, review, 75 min). It reviews fy7-1 … fy7-16.

## Files
- content/fi/units/fy9-magnetismi-valo/: unit.json, unit.md, inquiry.json, teacher.md, exit-ticket.json,
  sovella/tasks.json, sovella/solutions.md, review/developer.md
- lessons/units/fy9-magnetismi-valo/: figures.py (hero, kartta, siirto, ympyra), sovella/answers.py,
  sovella/figures.py (s3-B, s3-lin)
- preview/fy9-magnetismi-valo.html (unit build only)

## Task counts
- Ennusta: 6 choice. Tutki: 1 data-interpretation numeric (magnet in four tubes).
- Sovella: 4 choice (two reuse catalog figures fy7-7/trace and fy7-2/track-sign) and 4 numeric, each with three
  hints, typical mistakes and a full solution.
- Tarkista: 1 choice, 1 numeric, 1 explain (Thomson ring). Exit ticket: 2.
- Long tasks: 6, total 95 p.
  - s3 *Suoran johtimen magneettikenttä*: graph, linearise, μ0 and intercept, 20 p.
  - s1 hydro generator and transformers, calc, 15 p.
  - s2 optical fibre to the island, calc, 15 p.
  - s4 bubble, rainbow and CD, word, 15 p.
  - s5 grating report critique, 15 p.
  - s6 hospital cyclotron, cross-module with fy5-3, fy5-4 and fy6-12, 15 p.

## Numbers
All numbers are computed in sovella/answers.py; the inquiry values come from the inq-* keys there.
- Hook: 40 kW over R = 0,50 Ω. At 230 V: 174 A, 15 kW lost (38 %). At 20 kV: 2,0 A, 2,0 W lost.
- s3: read slope 2,42 µT·m gives μ0 ≈ 1,27·10⁻⁶ Vs/(Am). The intercept is ≈ 11 µT (the Earth's field component
  plus the sensor offset). The reading at 50 cm is ≈ 16 µT; the solution notes that the long-wire model is about
  10 % off there.
- s6: f = 18,3 MHz, v = 3,91·10⁷ m/s, 80 turns.

## Checks
- practice.py figures/check: OK, 6 tasks, 95 p.
- units.py figures: OK.
- units.py check: no errors for this unit. It reports errors for fy9-moderni, which is another developer's unit
  and still in progress.
- build.py fy9-magnetismi-valo: OK.
- check_layout at 360 and 1280: OK.
- Playwright at 390 and 1280: every task answered correctly and every model and solution opened. 0 console errors,
  0 raw `$`, 0 .katex-error.
- Screenshots reviewed. The hero's right edge was cropped; I moved the cottage and trees inward and updated the alt
  text.
- physics_phrases: 0 sentences to check.

## Open questions
- On a phone, the label of the induction-law row in the concept map (kartta) wraps to a second line. It is readable
  but not tidy.
- At 50 cm the long-wire model is an extrapolation. s3 d asks for it on purpose, and the reasonableness check says so.

## Shared issues
- None.

## Round 1 fixes

### Science
- **Blocking 1 (hook 40 kW sent vs used):** fixed as suggested. `inquiry.json` hook now says "kaapelia pitkin siirretään
  mantereelta enintään 40 kW:n teho", and unit.md Ydinajatus says "Kaapelia pitkin siirretään mantereelta 40 kW:n teho".
  The `siirto` figure (40 kW sent, 25 kW arrives at 230 V) is now consistent with the text.
- Polish 2 (Malus θ): added "Malusin laissa θ on polarisaation suunnan ja analysaattorin läpäisysuunnan välinen kulma",
  and the grating θ now reads "hilassa maksimin suunta".
- Polish 3 (thin film 2nd): added "kun valo tulee lähes kohtisuoraan".
- Polish 4 (sirius 9.925 feedback): now "Käytit kerrointa 10⁻⁶, joka kuuluu mikrometreille."
- Polish 5 (s2 a precision): Vastaus now says a 0,001 change in the index difference moves the angle about 0,3°, so
  the honest precision is about 82° and 8°, the tenth only for comparison; the units_precision rubric accepts both.
  (Checked: 0,014/0,015/0,016 give 82,09°/81,81°/81,54°.)
- Polish 6 (lt-1 feedback): "Tässä tilanteessa vauhtia voisi muuttaa vain sähkökenttä."

### Pedagogy
- Polish 1: same fix as science Blocking 1.
- Polish 2 (swap `virhe-siirto` for a Lenz item): not done. It is a new item with new feedback and needs a new review;
  the hook, Ennusta 2–3, Tarkista 3 and Tutki already cover induction/Lenz. Left for the teacher's decision.
- Polish 3 (Tutki reasoning not checked): not changed. The solution's Järkevyys, opened with the answer, already
  compares all four tubes and explains the slit; hints are already at the limit of 3.
- Polish 4 (`lue-kuvaaja` elimination): each wrong option now has one correct and one wrong claim
  (50 Hz with 8,5 V; 25 Hz with 12 V); the feedback says which half is right.
- Polish 5 (s2 b wording): now "säde, jonka kulma kuidun akseliin on suurin mahdollinen, jolla se vielä pysyy ytimessä".
- Polish 6 (teacher.md minimum): the Sovella bullet names the four-item minimum for everyone (Lue kuvaaja, Mikä
  hiukkanen, Lentokoneen siivet, Sukeltajan ikkuna).

### Visual
- `kartta`: the induction-law row is now at the normal 20 px with its label on the same line (only the
  refraction-law row, which is genuinely long, still uses the two-line layout).
- `siirto`: all bar labels 24 px; the heat-loss bar and labels use a dark brown-red `#8f3b1b` instead of orange
  (acceleration); the alt text says "ruskeanpunainen".
- `ympyra`: the radius formula is inline, r = mv/(qB), at full label size.
- `s3-lin`: the "b ≈ 11 µT" label sits above the intercept right of the axis, clear of the x-axis and the line, with a
  green leader to the intercept dot.
- fy7-7/trace tick size: shared catalog figure, not changed (see Shared issues).

### Checks after the fixes
practice.py figures/check OK (6 tasks, 95 p); units.py figures OK; units.py check no errors for this unit; build OK;
check_layout 360 and 1280 OK; Playwright at 390 and 1280 with all details open: 0 console errors, 0 raw `$`,
0 .katex-error, no horizontal overflow. Screenshots of kartta, siirto, ympyra and s3-lin at 390 looked at.

### Shared issues (added)
- fy7-7/trace tick labels are about 12 px at 390 px (catalog figure owned by fy7-7).
