VERDICT: FAIL
CONTENT-HASH: da9ba5eb24ac7a54

Scope: lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js, sim-spec.md of fy3-1, checked against standard physics and the MAOL FY3 text (force as measure of interaction; weight = strength of the Earth-body interaction, not a cause of acceleration; scalar force; spring balance; G = mg).

Findings

1. sim.js:37 — BLOCKING physics error. `stretch = SPRING.maxLen * (G / (m * G_MAX))` simplifies to `maxLen * g / G_MAX`, so the spring stretch does NOT depend on the mass slider at all. A 1 kg and a 100 kg body on Earth stretch the spring identically, although G differs 100-fold. This contradicts the lesson (lesson.md:8 and the summary: spring extension is directly proportional to the force), the comment on sim.js:3 ("The spring stretches in proportion to G") and sim-spec.md ("jousi venyy painon mukaan"). Students moving the mass slider would see no change in the scale, which teaches the wrong relation. Fix: make stretch proportional to G itself, e.g. `stretch = SPRING.maxLen * G / (100 * G_MAX)` (full scale = 100 kg on Jupiter, G = 2480 N), and optionally give the spring a visible minimum length so 1 kg on the Moon is still visible; keep the bar chart normalised per mass (that one is fine, it compares bodies for equal m) or normalise it by the same full scale. Reread the readout text afterwards.
2. lesson.md:17 — non-blocking. "sama luku kuin FY1:ssä mittaamasi putoamiskiihtyvyys 9,81 m/s²" is numerically correct (1 N/kg = 1 m/s²) and does not call weight the cause of acceleration, so it is within FY3 scope. Optional: add "(yksiköt N/kg ja m/s² ovat yhtä suuret)" and keep causal wording out.
3. lesson.md:19-24 — non-blocking. The table header "Taivaankappale | g (N/kg)" does not say "pinnalla"; g depends on the distance from the centre. Values are correct for the surface (Kuu 1,62, Mars 3,71, Maa 9,81, Jupiter 24,8; for Jupiter at the 1 bar level, no solid surface). Suggest header "g pinnalla (N/kg)". Same for sim.js:8 labels (optional).
4. lesson.md:8 — non-blocking. Proportionality of spring extension to force holds only within the elastic range (Hooke). Suggest "tavallisella voima-alueella" or "kun jousta ei venytetä liikaa". Optional; the exercises (L1-04, L2-04) are all inside a linear range by assumption.

Checked and correct (no action)
- "1 N is about the weight of a 100 g apple": 0.100 kg * 9.81 = 0.981 N. OK.
- g values Kuu 1,62, Mars 3,71, Maa 9,81, Jupiter 24,8 N/kg are standard (surface gravity 1.62, 3.71 [3.72], 9.81, 24.8 [24.79]). OK.
- Astronaut weighs about one sixth on the Moon: 9.81/1.62 = 6.06. OK.
- Example: 120 kg: 1177 N (1177.2) ~ 1,2 kN; Mars 445 N (445.2). OK.
- "painan 70 kiloa" -> about 690 N (686.7, 2 sf). OK.
- Weight as measure of interaction, scalar treatment, no Newton's laws or vectors in lesson/solutions: in scope. Arrow in SVG is allowed by MAOL ("voimia havainnollistavia nuolia").
- L3-02 lifting-force assumption is stated explicitly in the task text (force equals the weight of 22,0 kg on Earth), no hidden Newton's-law reasoning; answer 133 kg. OK.
- L3-03 scale calibration is stated explicitly; answer 0,99 kg correct.
- Units, sig figs and tolerances: all answers lie within 0.62 % of the recomputed value (tolerance 2 %); L2-03 1190 N is 3 sf of 1187.55. OK.
- solutions.md: reasoning and sanity checks all correct (245 N / 38 %, 83 % drop, 2,5-fold, one-sixth etc.). exit-ticket.json: 29 N, 4,9 N, 6,0 cm, 690 N all correct.
- sim.js g values (1.62, 3.71, 9.81, 24.8) and G = m * g (line 36) correct; readout text and note (sim.js:27, "Massa on sama kaikkialla...") physically sound; only the spring stretch (finding 1) is wrong.

Python output (python3 -I, g = 9.81, answers recomputed from problem text before reading solutions.md)
    L1-01 39.24 39 rel.err=0.0061 OK
    L1-02 8.1 8.1 rel.err=0.0000 OK
    L1-03 92.75 93 rel.err=0.0027 OK
    L1-04 1.5 1.5 rel.err=0.0000 OK
    L1-05 62.0 62 rel.err=0.0000 OK
    L2-01 4.9949 5.0 rel.err=0.0010 OK
    L2-02 0.5886 0.59 rel.err=0.0024 OK
    L2-03 1187.55 1190 rel.err=0.0021 OK
    L2-04 5.886 5.9 rel.err=0.0024 OK
    L3-01 6.80734 6.8 rel.err=0.0011 OK
    L3-02 133.22222 133 rel.err=0.0017 OK
    L3-03 0.99083 0.99 rel.err=0.0008 OK
    example 1177.2 445.2 686.7 6.055555555555555 moon ratio
