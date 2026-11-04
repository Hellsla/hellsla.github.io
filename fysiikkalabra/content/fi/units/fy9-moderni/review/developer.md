VERDICT: DONE

# fy9-moderni: Kvantti-ilmiöt, ydin ja säteily (FY9, chapter 6, order 1; reviews fy8-1 to fy8-16)

## Files
- content/fi/units/fy9-moderni/unit.json, unit.md (theory about 590 words), inquiry.json, exit-ticket.json, teacher.md
- content/fi/units/fy9-moderni/sovella/tasks.json, solutions.md
- lessons/units/fy9-moderni/figures.py (hero, kartta, fotonit, puolitus)
- lessons/units/fy9-moderni/sovella/figures.py (fy9-moderni-s3-p, fy9-moderni-s3-fit), sovella/answers.py
- preview/fy9-moderni.html (built)

## Task counts
- Ennusta: 6 choice (diagnostic, one per chapter group)
- Tutki: 1 interpret (half-value layer of lead, 5,79 mm, background and beta removed)
- Sovella: 4 choice + 4 numeric (hints ≤ 3, typed mistakes), exercises activity
- Tarkista: choice + numeric (Cs-137 mass 57,81 ng) + explain (fission/fusion with the binding-energy graph), exit ticket
- Long tasks: 6, total 95 p
  - s1 Cesium metsäsienissä (15, calc)
  - s2 Vedyn viivat kaukaisessa galaksissa (15, calc + word)
  - s3 Valosähköinen ilmiö ja Planckin vakio (20, data → graph → fit → interpret; cross-module with fy6-12 eU = E_k)
  - s4 Radon taloyhtiön kokouksessa (15, word)
  - s5 Barium-137m:n puoliintumisaika (15, calc + evaluate report + design)
  - s6 Ydinvoimalasta sähköä (15, calc; cross-module with fy3-15 efficiency, fy3-5 Q = cmΔT and fy2-5 heating value)

## Numbers computed (answers.py; practice.py check OK)
- s1: λγ 1,873 pm; A(2026) 1047,6 Bq/kg; dose 0,0681 mSv (1,15 % of 5,9 mSv); N 1,436e12; m 0,327 ng
- s2: 656,5 nm; z 0,02362; v 7080 km/s; d 101,1 Mpc; cyan 497,58 nm
- s3:
  - fit k 4,127e-15 V s, b −2,243 V
  - read points (0; −2,24 V) and (8,0e14 Hz; 1,06 V) give h 6,608e-34 J s (−0,27 %)
  - W 2,24 eV; f0 5,43e14 Hz (552 nm); 590 nm gives 5,08e14 Hz and 2,10 eV
- s4: 30 d is 7,89 half-lives, so 0,42 % remains; 450 : 300 = 1,5
- s5: net two-point T 150,8 s; all-point fit 153,1 s; raw 154,9 s; group's reading 166 s
- s6: η 37,21 %; 1,342e20 fissions/s; U-235 1653 kg/a; Δm 1,51 kg; sea water 58 581 kg/s; coal 5,26e6 t

## Checks run
- practice.py figures/check: OK (6 tasks, 95 p)
- units.py figures/check: 44 units ok
- build.py fy9-moderni: built
- check_layout 360 and 1280: OK. The data tables are now vertical (they scrolled before), and the s3 axis labels were moved inside the figure.
- Playwright at 390 and 1280:
  - all 11 choice and 6 numeric items answered "Oikein"
  - explain model answer and criteria opened; all solutions and details opened
  - 0 console errors, 0 .katex-error, no raw `$`, no horizontal scroll
- Screenshots viewed: hero, kartta, fotonit, puolitus, s3 graphs, s3 task and theory. Overlapping labels were fixed in fotonit, puolitus (1/8) and s3-fit.

## Open questions
- unit.json `sources` is empty. These figures may change and should be checked against STUK before publishing: 5,9 mSv mean annual dose, about 3 mSv from radon, the 300 Bq/m³ reference level and the Cs-137 ingestion coefficient 1,3e-8 Sv/Bq.
- The hero greenhouse lamps are red and blue (typical grow lights), while the hook says "punaiset kasvivalot". Blue photons (about 2,8 eV) are also far below 12,6 eV, so the physics still holds.
- s5 a: the solution accepts 145–157 s (any far-apart net pair or a full fit), which matches the 4 % tolerance around 151 s.

## Shared issues
- `python3 scripts/build.py fy9-moderni` also rebuilds preview/index, preview/en and preview/fi-easy module pages. That is outside preview/fy9-moderni*, but it is unavoidable with the prescribed command.
- The build raises BrokenPipeError when its output is piped to `head` (a cosmetic print at build.py:927). The unit page itself is written first.
- `scripts/physics_phrases.py` crashes when given a file path; it works with a directory.

## Round 1 fixes

Science
1. (Blocking) s1 "Yleisiä virheitä": factor corrected to $3{,}2 \cdot 10^{7}$ (seconds in a year), solutions.md.
2. (Blocking) s2 "Yleisiä virheitä": now "noin $10^{-25}\,\text{m}$, noin $10^{19}$ kertaa liian pieni arvo".
3. s3 c `reasonableness`: now "Vertaa eroa taulukkoarvoon … ja arvioi, onko se kuvaajan lukutarkkuuden rajoissa."
4. s5 a range unified to 145–157 s in tasks.json.
5. s2 text: "joista kirkkain" → "joista voimakkain".
6. s6 data list: added the condenser assumption line.
7. s6 d `reasonableness`: "noin $200\,\text{MeV}$ … muutaman elektronivoltin reaktiota kohti".

Pedagogy
1. Same as science 1–2, fixed once.
2. teacher.md: Tutki 15–30 min, Teoriatiivistelmä 30–40, Sovella 40–55 with only *Hammasröntgen* and *Gammalähde varastossa* in class; *Järvestä löytynyt ruuhi* and *Kahden deuteriumytimen fuusio* are home tasks for everyone. Slow-students line updated.
3. Concept map: bottom line "joka haarassa: yksi hiukkanen, sitten lukumäärä" (and aria-label).
4. Correct option moved: lt-4 → A, tarkistus-1 → C (B now 4/11). Feedback does not cite letters.
5. exit-ticket.json: both answers end with "Kertaa tarvittaessa luku *…*".
6. s5 b `uncertainty` criterion now begins "Toteaa, että tausta olisi pitänyt vähentää: …".

Visual
1. kartta capped at max-width min(100%, 420px) (420 × 808 px at 1280).
2. fotonit: all labels 24 (name/value rows re-spaced to avoid overlap), "logaritminen asteikko" added under the axis; height 360 → 392.
3. s3-fit: f tick numbers drawn below the axis, clear of the points; label now "$f_0 \approx 5{,}43 \cdot 10^{14}\,\text{Hz}$", moved below the axis.
4. source_note prefix dropped in Tutki and s3. s1 kept: its note says which values are invented and which are real.
5. Shared table style: not mine to change (Shared issues: right-align numeric table columns).
6. kartta now writes $H_\text{T} = w_\text{R} D_\text{T}$ like the theory.

Checks rerun: units.py figures, practice.py figures, practice.py check (6 tasks, 95 p), units.py check (44 ok), build fy9-moderni, check_layout 360 and 1280 OK, Playwright at 390/1280 with all choices answered and details open: 0 console errors, 0 .katex-error, no raw $, no horizontal overflow; kartta, fotonit and s3-fit screenshots checked.
