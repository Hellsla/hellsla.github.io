VERDICT: FAIL
CONTENT-HASH: 705e49cae9093336

## Blocking
- inquiry.json:104 (simulaatio.model) — A. The text says the crushable bumper's force "kasvaa tasaisesti suurimpaan arvoonsa ja pienenee tasaisesti nollaan". In this lesson "tasaisesti" means at a constant rate, i.e. a straight line: "tasaisesti kiihtyvä" in lesson.md:405, the triangle graphs in figures.py:141/153, and check-2's reasonableness step "puolet huippuarvosta, kuten tasaisesti kasvavalle ja pienenevälle voimalle kuuluu". The sim's pulse is a half-sine (calc text, model.js), and its mean force is (2/π)·F_max = 0,637·F_max (50,9 N for the hard bumper), not F_max/2 (40 N, which would give I = 1,57 N·s instead of 2,00 N·s). So the model box describes a different pulse shape from the one the calc box and the graph show. — Fix: "kasvaa pehmeästi nollasta suurimpaan arvoonsa puolivälissä törmäystä ja pienenee pehmeästi nollaan juuri, kun kärry pysähtyy (sinikäyrän muotoinen pulssi)".

## Polish
- lessons/FY4/fy4-9/sim-spec.md:1 — "kokonainen tasainen pulssi" has the same ambiguity — "kokonainen pehmeä (sinimuotoinen) pulssi".
- assets/sims/fy4/fy4-9/model.js:49,53 — the step where contact begins in "pysahtyy" adds dt, then f·dt, then (1−f)·dt to s.t, so the clock gains 2·dt, about 0,1 ms (confirmed: final t is 0,47937 s, expected 0,47927 s). Δt, I and the readout are unaffected. — Drop `s.t += f * dt` and add `s.t -= (1 - f) * dt` (or back out the dt) before the recursive call.
- model.js:71 — the comment "both bumpers: ½ m v1² = ½ k c², F = k c" is wrong for the crushable bumper, which crushes only (π/4)·v1√(m/k) and has F ≠ kc. The value v1√(km) is right by definition. — Say "the spring's peak; the crushable pulse is given the same F_max".
- inquiry.json:104 (calc) and sim-spec — "liike lasketaan … pienin aika-askelin" does not hold for the crushable bumper, whose v(τ) and c(τ) come in closed form from the prescribed pulse (exactly equal to the stepped result). — Say so in one clause.
- model.js:7 — "as measured for real crash absorbers" has no source. Many absorbers are designed for a flat-top force. — Drop it or soften it.

## Checked
- Pulse kinematics re-derived: v = v1(1+cos πτ/Δt)/2 and c = (v1/2)(τ + (Δt/π)sin πτ/Δt) match model.js. v reaches 0 exactly at Δt, and the final crush is v1Δt/2.
- Impulse: ∫F dt = −2F_maxΔt/π = −m v1, the closed-form area in model.js. I = Δp in every run.
- Energy: E_k + E_b stays at ½ m v1² to 5 digits all through each run (node script). E_b is the absorbed work.
- Node model test passes (652 checks). My script reproduces exp-1 (0,0393/0,0785/0,157 s; 80,0/40,0/20,0 N; −2,00 N·s), exp-2 (−2,00/−4,00; v = −2,00 m/s) and exp-3 (28,3/40,0/56,6 N; −1/−2/−4 N·s).
- The quarter-spring model in lesson-answers.py gives the same Δt, F_max and I as the half-sine. The comment says so correctly.
- Largest crush in the crushable mode is 0,222 m and in the spring mode 0,283 m, both inside the 0,32 m bumper. The longest contact, 0,444 s, is inside the 0,5 s axis.
- Pysaytys figure: pixel scale gives 80 N/0,039 s and 20 N/0,157 s, half-sines with their minimum at Δt/2. The areas are equal (−2,0 N·s) and the shape matches figures.py:77.
- Predictions, experiment options, feedback numbers, Johtopäätös ("neljäsosa voimasta"), worked example (870 N, 145 N), siirto (80/4,0/0,20/800/400 N) and check-2 (12 m/s, 24, 5,4, 12 000) recomputed.
- Experiment setups lock m, v1 and type as intended, and simState gives dt, Fmax, I, v2, dp and p1.
