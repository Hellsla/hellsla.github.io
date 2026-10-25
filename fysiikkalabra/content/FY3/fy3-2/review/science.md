VERDICT: PASS
CONTENT-HASH: 0e6f5c36e1389db3

## Blocking

## Polish
- inquiry.json:56,61,65,88,92,96 — pred-1/pred-2 feedback calls the simulation's numbers "mittaukset", contradicting the sim activity ("mallin arvoja, eivät mittauksia") and the brief (sim = model values, Joule = measurements) — say "Mallin arvot näyttävät/tukevat…".
- lesson.md:32 — "Joule vaihteli sekä painoa että pudotuskorkeutta … havaitsi lämpenemisen olevan aina verrannollinen näiden tuloon" overstates the historical record (Joule mainly fixed the weights and repeated drops; the work concept predates him) — hedge, e.g. "Joulen kokeen tapaisissa mittauksissa lämpeneminen on verrannollinen painon ja pudotusmatkan tuloon".
- lesson.md:92 — "nostovoima on yhtä suuri kuin paino" holds for constant velocity; "hitaasti" carries it, but "tasaisella nopeudella" would state the condition exactly.
- sim.js:30 — the friction/heat explanation is a plain paragraph, not behind a "Lisätietoja" button, and the animated sim has no speed control (form rule 3; a speed control must not change the model time t shown in P = W/t).

## Checked
- All 12 exercise answers recomputed independently in one script; all match answers.py and exercises.json within tolerance (largest deviation L3-03 0,9 %).
- Units/sig figs: kJ, kW, min conversions correct; data sig figs support the rounded answers.
- Worked example: triangle area ½·40 N·0,20 m = 4,0 J, symbolic before substitution, SVG scaled to 0,20 m / 40 N; 5 stages.
- Kaavat: W = Fs (force along motion, constant), area rule, W = mgh, P = W/t = Fv with conditions stated; within FY3 scope.
- Solutions: reasoning and sanity checks (e.g. 360 kJ ≈ 1000 kg to 37 m, 850 kg ≈ 8,3 kN) correct.
- Inquiry: retrieval 98 N, pred-1 600/1200 J, pred-2 120→30 W, pred-3 W = 0 (Aino 1960 J), check-1 3×, check-2 180 J, siirto 240 W, mistake values 9,6 / 0,24 / 240 / 120 correctly diagnosed.
- Joule table: 19,6 J per drop (≈ 2 kg · 1 m), Q/W ≈ 0,99, labelled as example values; L3-02 588,6 J → 590 J.
- Experiments: exp-1 locks F, t and varies s; exp-2 locks F, s and varies t; values 5–20 within slider ranges; simState exposes W and P.
- sim.js: W = F·s, P = W/t, animation lasts t, area fills linearly; screenshot shows 60 N, 10 m, 600 J correctly.
- Exit ticket: 98 J, 20 J, equal work / double power correct.
