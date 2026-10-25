VERDICT: PASS
CONTENT-HASH: cd403913f7e9f945

## Blocking

## Polish
- inquiry.json:92 — pred-2 option "Työ ja teho pysyvät samoina" still says "mittausten mukaan" for the simulation's numbers; the other prediction feedbacks now say "Mallin arvot" — change to "mallin arvojen mukaan".
- sim.js:30-31 — the friction/heat explanation is still a plain paragraph rather than behind a "Lisätietoja" button, and the animated sim has no speed control (hidas · normaali · nopea) (form rule 3). A speed control must change only the playback rate, not the model time t used in P = W/t.

## Checked
- All 12 exercise answers recomputed independently in one script; they match answers.py and exercises.json within tolerance (largest deviation L3-03, 0,9 %).
- Units/sig figs: kJ, kW and min conversions correct; L2-03 250,155 kJ → 250 kJ and L3-02 588,6 J → 590 J both within 2 %.
- Worked example: triangle ½·F_max·s = 4,0 J, solved symbolically before substitution; average-force cross-check correct; SVG scaled to 0,20 m / 40 N.
- Formulas: W = Fs (constant force along the motion), area under (s,F), W = Gh = mgh (now "tasaisella nopeudella"), P = W/t = Fv (uniform motion, force along the motion). All conditions stated and within FY3 scope.
- Joule paragraph (lesson.md:32) is hedged now; Joule table labelled as example values, 19,6 J per drop, Q/W ≈ 0,99, correct option and feedback right.
- Inquiry numbers: retrieval 98 N, pred-1 600/1200 J, pred-2 120 → 30 W, pred-3 W = 0 (Aino 1960 J ≈ 2,0 kJ), siirto 240 W (mistakes 9,6 and 0,24 diagnosed correctly), check-1 3×, check-2 180 J (mistakes 240, 120), check-3 model answer correct.
- Experiments: exp-1 locks F and t and varies s; exp-2 locks F and s and varies t. Suggested values are inside the slider ranges and steps, and simState exposes W and P.
- sim.js: W = F·s, P = W/t, the animation lasts t, and the area fills linearly with u. The adapter's reset matches the experiments' initial values.
- Solutions: reasoning and sanity checks correct (2000 J ≈ 20 kg to 10 m, 360 kJ ≈ 1000 kg to 37 m).
- Exit ticket: 98 J, 20 J, and equal work with double power are all correct.
