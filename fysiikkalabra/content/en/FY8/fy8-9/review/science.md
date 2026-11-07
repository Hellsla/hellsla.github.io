VERDICT: PASS
CONTENT-HASH: ae13cefaf40e4841
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed)

## Polish
- inquiry.json tarkistus-3 criteria: "in a year hundreds of half-lives pass" vs model ~1460 half-lives; "over a thousand half-lives" (carried from the earlier report; in fi, not edited here).
- inquiry.json tarkistus-3 model: "dropped to zero" -> "practically zero" (carried, in fi).

## Checked
- figures.json change (four new option-figure descriptions of the (t,A) graph) checked against lessons/FY8/fy8-9/figures.py and the data: A line 800 -> 400 kBq at 2 h -> 0 at 4 h; B 800(1 - t^2/8) = 400 at 2 h, zero at sqrt 8 = 2.83 h (about 2.8 h), steeper; C 400/200/100/50 kBq at 2/4/6/8 h; D 800 e^-1 = 294 (about 290), 800 e^-2 = 108 (110), 800 e^-4 = 14.7 (15). All description numbers right, axes (0-8 h, 0-900 kBq, grids) as drawn.
- Descriptions give a reader who cannot see the figure the same data without naming the right graph; consistent with fy8-9-L1-09 text, feedback and solution (A zero at 4 h, B steeper, D lacks ln 2).
- en and fi-easy figures.json: same four keys as fi, values correct in each language (en decimal point).
- New photos: cloud-chamber alpha tracks of radon (random positions and directions) and a Geiger-Mueller survey meter; captions physically right: count rate proportional to activity at a fixed position (detector efficiency and geometry constant); licences in photos.json (CC BY-SA 4.0, public domain).
- Rest of the lesson unchanged by the diff; earlier PASS findings stand: decay law, lambda = ln2/T, A = lambda N, fit values, sim model values.
- check_i18n: nothing for fy8-9; build.py fy8-9 succeeds.
