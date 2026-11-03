VERDICT: FAIL
CONTENT-HASH: 0e1654f7d66a7eee

## Blocking
- inquiry.json `gammaspektri` (figure `fy8-8/spectrum`, capture fy8-8-fig-5-390.png) — the figure the task needs is not translated: the y-axis label reads "fotonien määrä" and the alt text is Finnish ("Kaavamainen gammaspektri koboltti-60-lähteestä ..."), so an English reader gets no usable description and no axis label — fix: English axis label "number of photons" and an English description (the two peaks at 1173.2 and 1332.5 keV, background falling towards higher energy) in the en figure catalogue entry.

## Polish
- inquiry.json `ennuste-1/2` `reveal.min` 6 — the series has 15 steps and the students need only steps 0-5 to see Z, N, A; fine, but the intro could say "at least steps 0-5, which include both alpha and beta" explicitly; as written a student who clicks only alpha steps cannot test prediction 2 (beta first appears at step 2).
- inquiry.json `hook`/`pohdi` — the opening question (americium-241, and why gamma follows) is answered only in the optional reflection; the lesson never names the daughter (neptunium-237) or shows an americium level scheme. Add one line to the Key idea or make `pohdi` non-optional.
- inquiry.json `gammaspektri` hint 3 — "Read the energy of each peak from the figure and add" gives the method away; the figure already prints both energies, so reading is trivial. Drop the printed values and let the student read the peak positions.
- lesson.md "Energy levels of the nucleus" — "hundreds of thousands of times larger" is asserted before any ratio is shown; tie it to the L2-03 ratio or the example (500 nm photon vs 661.7 keV).
- exit ticket Q2 repeats tarkistus-1 style recall (isotope definition); a gamma/alpha item would test the core idea better.

## Checked
- Path: nucleons, Z/N/A, chart, decay types, levels, equations, example; one lesson's load; goals met without extras.
- Predictions are refutable by the series data; each wrong option's feedback repairs its misconception.
- Worked example is staged, one step per stage; the arithmetic checks (1.874 pm).
- Figures legible at 390 px (isotopes, chart, levels); simulation readable on a phone, colour plus symbol.
- Check 1 distractors are misconception-based; explain criteria are observable.
- Find-the-mistake and transfer (U-235, 7 alpha) are correct, with graded hints.
- check_lesson.py was not run (packet says so); not judged here.
