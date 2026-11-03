VERDICT: DONE

Unit fy12-kokeellisuus, "Kokeellinen työ ja sen arviointi" (FY12 chapter 1, order 3). Developer report 2026-11-03.
Content hash at hand-over (round 1): e198735ef8b8ce03 (`python3 scripts/units.py hash fy12-kokeellisuus`).

## Files
- `content/fi/units/fy12-kokeellisuus/unit.json`: course FY12, chapter 1, order 3, kind review, 75 min, physics; no sources (no fact that may change).
- `unit.md`: Miksi question, hero, Ydinajatus (six questions of a plan; error, uncertainty, resolution), Kaava: Mittaustuloksen käsittely (mean, half range, ε, y = kx + b, intercept as systematic error), Yleisiä virheitä, Kertaa tarvittaessa (fy1-8, fy1-3, fy1-4, fy3-13, FY10 heiluri/liukukitka/jousivakio). Theory 519 words.
- `inquiry.json`: hook; 6 Ennusta choice; 1 Tutki interpret (flawed pendulum data set: length to the top of the bob + one miscounted row; explain question); theory; Sovella 4 choice (instrument choice, plan error-spotting, linearisation, thermometer offset) + 4 numeric (ΔT from repeats, g from (l, T²) slope, absolute zero by extrapolation, μ0 = tan α); exercises intro; Tarkista choice, numeric, explain; exit.
- `exit-ticket.json` (3), `teacher.md`.
- `sovella/tasks.json`, `solutions.md`: s1 shoe grip design (12 p), s2 oil c design + calc (14), s3 report critique (13), s4 pendulum data→graph→fit→intercept (16), s5 stone density calc with uncertainty (12), s6 cross-module bicycle braking FY4 + FY1 (15). 82 points.
- `lessons/units/fy12-kokeellisuus/figures.py` (hero, kartta, virhe), `sovella/answers.py`, `sovella/figures.py` (s4, s6 model graphs).

## Numbers (Python, answers.py and the scratch computations)
Interpret: g per row 9,15 / 9,45 / 9,46 / 11,80 / 9,63, mean 9,90 (r = 2,0 cm, row 4 = 9 swings). Sovella: ΔT 0,013 s; g 9,788; θ0 −275,1 °C; μ0 0,416; check Δg 0,276. Tasks: s2 160 s; s3 g 9,695, Δg 0,872; s4 k 4,013, g 9,839, d 4,98 cm (fit 4,020/0,1035); s5 2677 ± 78 kg/m³; s6 a 4,17, μ0 0,425, +10,25 %.

## Checks
practice.py check and figures OK; units.py check OK for this unit; build OK; check_layout 360 OK; 1280 fails only on the teacher box (see Shared issues). Playwright 390/1280: every choice, numeric (right and mistake answers) and explain answered, details opened: no console errors, no .katex-error, no raw $. Figures looked at.

## Open questions
- s4 uses g = 9,81 with simulated data; s6 μ0 of dry asphalt "0,7–0,9" in a reasonableness check is a typical value, not sourced.

## Shared issues
- `scripts/mixer.py` line 22: `{own_module} | {...} - {None}` keeps None for unit tasks (precedence), so `build.py <unit>` crashes after writing the preview.
- No `assets/units/fy12/units.css`: `.unit-teacher` has no max-width, so check_layout 1280 flags the preview-only teacher notes (FY14 has the rule).
- Units are not figcat owners, so a unit's inquiry cannot refer to its own figures by id.

## Round 1 (science FAIL, pedagogy FAIL, visual PASS)
- Science blocking: s5 d) no longer gives the scale resolution as the overflow-can uncertainty; the text and rubric now name about 0,5 cm³ from water left in the can and spout.
- Pedagogy blocking: the Sovella item *Kengän pito* (tilt method, μ0 = tan α0) is replaced by *Riittävän pitkä mittaus* (walking speed, minimum distance 14 m). The mistake feedback for nollapiste −295,1 and −355,1 now names the slip: the measured point's pressure was divided by the slope instead of p0.
- Pendulum use cut:
  - Tutki is now a spring measurement: the initial reading was not subtracted (k rises with load), and one row has a misread value (6,85 cm instead of 8,85 cm). Mean 21,8 N/m; the slope gives about 25 N/m.
  - *Mikä kuvaaja?* and the numeric item now use a spring oscillator, (m, T²): k = 24,7 N/m.
  - *Toistettu ajanotto* uses a cart: ε = 2,29 %.
  - Tarkista 2 is the density of a cube: Δρ = 0,24 g/cm³.
  - Tarkista 3 is about the (F, x) graph.
  - s4 a no longer names the slope method.
- The Ennusta "leikkaus" item is now an untared beaker. The correct options are shortened, and their positions are spread out.
- Science polish:
  - "todennäköisesti todellinen" in s1 b;
  - "b poikkeaa selvästi nollasta";
  - "resoluutio ja epävarmuus" in the *valine* feedback;
  - sisäenergia / lämpö in s2 a;
  - the s2 d methods are given as alternatives;
  - the precision sentence in s6 d;
  - "resoluutio 0,1°" in s1.
- Teacher plan: Sovella does five items in class and three at home; fast students do task 6 at home.
- Visual: the "systemaattinen virhe" label is darkened. All numbers are recomputed in Python.
- Checks: practice.py check OK, units.py check OK for this unit, build OK, check_layout 360 and 1280 OK. Playwright: every task answered, no console errors, no .katex-error, no raw $.
