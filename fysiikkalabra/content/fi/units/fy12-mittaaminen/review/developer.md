VERDICT: DONE

# fy12-mittaaminen — developer report

## Files
- content/fi/units/fy12-mittaaminen/: unit.json, unit.md, inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json, sovella/solutions.md, review/developer.md
- lessons/units/fy12-mittaaminen/: figures.py (hero, kartta, anatomia, linearisointi), sovella/figures.py (s3-pisteet, s3-sovitus, s5-kuvaaja, s6-kuvaaja), sovella/answers.py (recomputes every answer)

## Counts
- Pohdinta 1, Ennusta 6 (lahto-1..6), Tutki 1 interpret (tutki-kaasu, figure fy3-3/extrapolation-points, -270 °C), teoriatiivistelmä 1
- Sovella 8: choice 4 (virhe-tulos, aika-kuvaaja, vakiotermi, virhelaji), numeric 4 (kolikot 2,7 %, jousi-suora 79,0 N/m, kuula-kouru 1,24 m/s², kattila 10,0 min)
- Tarkista 3 (choice, numeric 28 kg/m³, explain) + exit ticket (2 questions)
- Tehtävät 6, 89 p: s1 Käsiajanotto (calc 14), s2 Kopiopaperi (calc 15), s3 Tuntematon neste (data→graph→fit 17), s4 Keittiövaaka (word 12), s5 Leluauto videolta (experimental 14), s6 Ilma ruiskussa (cross-module FY3 17)

## Key numbers (answers.py)
- s1 v = 7,29 ± 0,12 m/s; s2 102 ± 2 µm, 79,8 g/m², 780 kg/m³
- s3 k = 0,919 g/cm³, m0 = 118,6 g, Δρ = 0,012 g/cm³, 1,50 l → 1,38 kg
- s4 correction factor 1,02 (765 g reads ≈ 750 g); s5 0,477 ± 0,014 m/s (origin-forced fit 0,634 shown as the error)
- s6 V0 = 1,8 ml, n = 1,06·10⁻³ mol, pV rises 8 %

## Checks
- units.py figures/check (no errors for this unit), practice.py check + figures OK, build.py fy12-mittaaminen OK, check_layout 360/1280 OK
- Playwright 390 and 1280: 11 choices answered, 6 numeric forms answered → all "Oikein.", all details/model answers opened; 0 console errors, 0 .katex-error, no raw $, no horizontal scroll

## Open questions / shared issues
- Units cannot own catalog figures, so the Tutki figure reuses fy3-3/extrapolation-points; units do not support [[ohje:]] links, so the TVT guides are named in plain text.
- unit.json sources is empty: the proxy blocked the source URLs so none could be verified.
- ACCIDENT: `python3 -c "import build"` ran a full build and modified ~349 files in site/, plus untracked site/FY12.html, site/yo-sekoitin.html, site/en/yo-sekoitin.html, site/fi-easy/yo-sekoitin.html, site/module-icons/fy12.svg. My revert was blocked; the coordinator must run `git checkout -- site/` and remove those 5 files.

## Round 1
Blocking:
- kolikot: 0,27 now gets the "divided Δd by the stack height" feedback; 0,027 added as its own mistake (multiply by 100 %).
- Figure labels: Fig size 26–27 in the unit figures and 30 in the task figures. Measured at 390 px: kartta 15,5 px, anatomia and linearisointi 16,1 px, s3/s5/s6 14,9 px. The only label under 14 px on the page is the catalog figure fy3-3/extrapolation-points (13 px), which is not this unit's.
- Collisions: in anatomia, jyrkin/loivin moved into a legend in the empty corner; y ticks 15/30/45/60 so the b ring no longer covers a tick. In s6, the k label moved to the empty upper left, −V0 moved below the axis (y from −8) and only the x ticks 4/8/12 are labelled. linearisointi: k = a/2 moved below the line. s3 "alkaa 100 g" is enlarged. s5 y ticks are now 0,6/1,2/1,8, so the ring at the intercept no longer covers a tick. check_layout is OK at 360/390/1280.

Polish:
- Science:
  - s6 a criterion and the s6 Periaate/Yleisiä virheitä now argue a steady one-way growth.
  - tarkista-2 now reads "lähes puolivälissä, kuten yleensä".
  - The s3_fit description now says eight points.
  - s3 a prompt: "…josta voi määrittää myös suoran vakiotermin".
  - kattila and anatomia use θ for °C.
  - Figure aria-labels now have no LaTeX `{,}`.
  - The lahto-4 units point is moot because the item was rewritten.
- Pedagogy:
  - lahto-4 is now a burning candle (h = −0,80 cm/h · t + 18,0 cm).
  - tiheys-suora is replaced by jousi-suora, a spring (L, F) line: k = 79,0 N/m, with mistakes 0,79, 48,6 and 8.
  - boyle-kuvaaja is replaced by aika-kuvaaja (fixed track: (1/v, t)).
  - kuula-kouru is retitled "Kuula kourussa".
  - s6 b no longer has the giveaway sentence.
  - Option lengths are balanced in lahto-6 and vakiotermi.
  - s1 a precision is argued from the clock spread, so it no longer needs b.
  - teacher.md timing: Tutki and teoria are 10 min each and Tarkista is 13 min. Only the s3 data is discussed in class, and plotting it is homework. The plan names the Sovella items to skip.
- Visual: the hero's uncertainty bars are longer. The s5 description says the bars are smaller than the points.
Checks rerun:
- units.py figures/check, practice.py check (89 p) and build.py fy12-mittaaminen all pass.
- check_layout at 360/390/1280: OK.
- Playwright at 390/1280: 11 choices and 6 numeric items, all answered "Oikein."; 0 console errors, 0 katex errors, no raw $, no horizontal scroll.
- lint (plain quantities) is clean.
