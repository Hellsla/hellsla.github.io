VERDICT: DONE

Unit fy9-liike, "Liike kuvaajina" (FY9 chapter 3, order 1). Developer report 2026-11-04.
Content hash at hand-over: 365135079757531a (`python3 scripts/units.py hash fy9-liike`).

## Files
- `content/fi/units/fy9-liike/unit.json`: course FY9, chapter 3, order 1, kind review, 75 min, subjects physics; `sources` empty (all data are invented examples).
- `content/fi/units/fy9-liike/unit.md`: Why question (tram (t,v) graph, distance between stops), hero, `## Ydinajatus` (concept map, hook answer 450 m), `## Kaava: Liikkeen yhtälöt ja kuvaajat` (v_ka = Δx/Δt, x = x0 + vt, a = Δv/Δt, v = v0 + at, x = x0 + v0t + ½at², Δx = (v0+v)/2·t, x_A(t) = x_B(t), a = 2A from a quadratic fit; slope and area figure), `## Yleisiä virheitä {Virheet}` (7), `## Kertaa tarvittaessa {Kertaa}` (fy1-5, fy4-1, fy4-2, fy4-12, fy1-4, fy1-3). About 560 words.
- `content/fi/units/fy9-liike/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-liike/sovella/tasks.json`, `solutions.md`; `lessons/units/fy9-liike/sovella/answers.py`, `figures.py` (model graph of s3).
- `lessons/units/fy9-liike/figures.py`: `hero` (tram), `kartta` (concept map), `kuvaajat` ((t,x) and (t,v) pair with tangent and area), `ratikka` (Tutki graph, pasted into inquiry.json by `paste_ratikka()`).

## Counts
- Pohdinta: 1 hook. Ennusta: 6 choice (diagnostic, each option names the chapter). Tutki: 1 interpret (tram (t,v) graph, `source: example`, numeric 450 m).
- Teoriatiivistelmä: 1 theory activity.
- Sovella: 4 choice (average speed 30 km/h, graph shape, tangent `fy4-2/ex-tangent` 4,0 m/s, who is ahead), 4 numeric (scooter `fy4-2/ex-tv` 22,5 m, moose braking 46,8 m, dog 8,0 s, baseball −1,81 m/s), each with solution, hints, mistakes.
- Tarkista: choice, numeric (lift 16,0 m), explain ((t,v) intersection vs meeting); `practice` links on all three; exit ticket (54 km/h = 15 m/s; a = −2,0 m/s²).
- Tehtävät: 6 tasks, 95 points: s1 Kiihdytyskaista (calc, 15), s2 Kaksi palloa aulassa (calc, 15), s3 Lähijuna saapuu asemalle (data → graph → fit → interpret, 20), s4 Keskinopeusvalvonta (word, 15), s5 Kärry kaltevalla radalla (experimental report critique + design, 15), s6 Pudotus puhelimen videolla (cross-module FY1 fit/uncertainty + FY4, 15).

## Numbers (computed in Python: answers.py, scratch generators)
s1 12,0 m/s; 1,25 m/s²; never level within the lane (discriminant −43,75), lead 17,5 m; overtaking 15,4 s at 307 m. s2 8,84 m/s; meeting 0,625 s at 7,08 m; velocities 5,87 and −6,13 m/s. s3 fit k = −2,3125 km/h/s, b = 112,75 km/h; read slope −0,645 m/s²; braking starts 9,8 s, stops 48,8 s; braking distance 481 m (read), 487 m (fit). s4 81,8 km/h; ±0,59 km/h (3,0 km) vs ±17,8 km/h (100 m). s5 a = 0,94 m/s² (range 0,74–1,22). s6 A = −4,44 m/s² → g = 8,88 ± 0,10 m/s²; scale-corrected 9,77 m/s²; two-point 8,92 m/s². Inquiry: Tutki 450 m; scooter 22,5 m; moose 46,77 m; dog 8,0 s; baseball −1,81 m/s; lift 16,0 m.

## Checks
- `units.py figures fy9-liike`, `practice.py figures units/fy9-liike`: up to date. `practice.py check units/fy9-liike`: OK, 6 tasks, 95 points. `units.py check`: no errors for this unit (errors only in other units in progress).
- `build.py fy9-liike`: writes `preview/fy9-liike.html` and the preview index pages; no mixer crash this time.
- `check_layout.py fy9-liike` at 360, 390, 1280 px: OK.
- Playwright at 390 and 1280: all 11 choices answered correctly with feedback, 6/6 numeric "Oikein", explain model and all solutions opened; no console errors, no `.katex-error`, no raw `$`, no horizontal scroll. `screenshot.py fy9-liike --no-build` captures looked at (hero, map, kuvaajat, Tutki, s3 model graph); fixed label overlaps, overflowing key text and small labels (s3 graph redrawn 440 wide).

## Open questions
- No real data: the train, tram, cart and video data are invented and marked `source: example`. A reviewer may want one real measurement series.
- Sovella reuses catalog figures `fy4-2/ex-tv` and `fy4-2/ex-tangent`; check that their numbers stay as quoted (22,5 m, 4,0 m/s).
- The Tutki graph is an inline SVG pasted into inquiry.json (regenerate with `PYTHONPATH=scripts python3 lessons/units/fy9-liike/figures.py`), as in fy9-energia.
- teacher.md headings keep plain "min" times (preview only, as in fy9-energia).

## Shared issues
- figcat ids cannot name a unit's own figures, so a unit figure in inquiry.json has to be pasted as SVG.
- Seen in passing (not this unit): `check_layout.py` over all previews fails fy9-voimat at 360 px (svg-text overlap).
