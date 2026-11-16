VERDICT: PASS
CONTENT-HASH: 92b9c1f1d50cdbe8

## Blocking

## Polish
- lesson.md:369 — "With double the radius, 100 m, it is half as large at the same speed, 4.0 m/s²" does not name the speed; the value holds at 20 m/s only — write "at 20 m/s".
- assets/sims/fy5/fy5-4/sim.js:1181–1225, 1297, 1320, 1337 — the controls, readout and canvas labels are Finnish literals ("Käynnistä", "lähtökitka", "Rata ylhäältä"), while the English howto names *Start*, *Mass*, *Surface*. This is not a physics problem; the visual and pedagogy reviewers should confirm what the English page shows.

## Checked
- Recomputed every number in one script with my own formulas, and all agree: worked example (v = 15 m/s, a_n = 5.0 m/s², F_μ = 6000 N, μ0 ≥ 0.5097 → 0.51, rounded up as an "at least" value should be); exp-1 table at 5–30 m/s (F_max = 11 772 N, grip fails from 20 m/s); limit 19.81 m/s, rounded down to 19.8 m/s (71 km/h) as an "at most" value should be; mistakes 22.15 and 392.4; exp-2 ratio 0.920 for every mass; siirto 15.34 m/s (mistakes 18.79, 10.85); check-2 148 N (mistakes 47.12, 294.3); check-3 T = 0.765 N, 0.46 G; exit ticket factor 9.
- Round-2 change: exp-1 records at 25 and 30 m/s, with min 6 and pred-2 reveal.min 6. With μ0 = 0.80 the slide radius v²/(μ0 g) is 79.6 m and 114.7 m. A slide that starts tangent at r = 50 m reaches 109 m and 179 m from the centre, past the asphalt edge in the picture (57 m). At 20 m/s it reaches only 52 m, so the car stays on the asphalt, as the sim-spec says. pred-2's correct option and its feedback ("turns less… straighter the greater the speed") now have evidence the student actually records.
- Calc box: "maximum (fully developed) static friction μ0 N = μ0 mg" uses the guardrail term (P8); the condition and F_μ in both branches match model() in sim.js.
- sim.js: on the track θ̇ = v/r; sliding, the heading turns at μ0 g/v, which gives radius v²/(μ0 g) towards the centre (left normal). The diagram turns the same way as the top view. simState gives an, Ftarve, Fmax and pito at the locked values. The model box states the skid simplification (sliding friction usually smaller than the maximum static friction).
- Experiments: exp-1 locks r, m and surface and varies v; exp-2 locks r, surface and v and varies m. Each isolates its parameter.
- Figures: the a_n(v) graph is to scale (points (10, 2), (20, 8), (30, 18) and (30, 9) on the pixel scale); Δv = v̄2 − v̄1 points to the centre, with equal arrow lengths; hill/dip N = 0.6 G and 1.4 G are consistent with the same v²/r; the worked-example FBD has F_μ/G = 0.51.
- Option figures (figures.py): virhe has N + F_kp = G, so the error sits only in F_kp; valitse-b, c and d each have one error, and d without F_kp equals a. Feedback matches.
- Force diagrams: interactions only, no centripetal or centrifugal arrow, acceleration drawn apart in orange, equations read from the diagrams.
- Definitions: centripetal/normal acceleration, centripetal force as the sum of real forces, centrifugal force as fictitious in a rotating frame; all agree with the glossary. Scope: no ω and no rotational dynamics.
- Content hash 92b9c1f1d50cdbe8 (--lang en) at start and end.
