VERDICT: PASS
CONTENT-HASH: 9bc1f95d58539988

## Blocking

## Polish
- inquiry.json:92 — pred-2 feedback calls simulation output "mittausten" — write "mallin arvojen mukaan".
- inquiry.json:232 — "mittauksiisi": the student recorded model values — "kirjaamiisi mallin arvoihin".
- sim.js:81 — at 390 px the scaled "W = pinta-ala" caption is clipped at the canvas top (exp-2 shot) — clamp y to at least ts(14).
- inquiry.json exp-1/exp-2 — the sim computes W = Fs directly, so the experiments confirm arithmetic — say so at the point of use and name the Joule table as the evidence.
- lesson.md:116 — "kasvaa täsmälleen nostotyön verran" — optionally add "(tasaisella nopeudella)".

## Checked
- All 12 answers recomputed in one script: they agree with exercises.json and answers.py within 2 %.
- Inquiry numbers: 98 N; 600/1200 J; 120 → 30 W; 240 W (mistakes 9,6 and 0,24); 180 J (mistakes 240 and 120); check-1 ratio 3; exit ticket 98 J and 20 J.
- Joule table: 19,6 J per drop, Q/W ≈ 0,99, labelled as example values.
- Formulas W = Fs, area under (s,F), W = Gh = mgh, P = W/t = Fv: conditions stated, within FY3 scope.
- solutions.md: formula stated symbolically first; units, conversions and plausibility magnitudes correct.
- Worked example: symbolic first, average-force cross-check; the figure is to scale (0,20 m ↔ 302,5 px, 40 N ↔ 171 px).
- Figures: F = G arrows equal (58 px); h marked between the correct edges; the A₁/A₂ areas are right.
- pred-3: Bea correct; the Cem feedback states the "no air resistance" assumption.
- sim.js: W = Fs and P = W/t; the graph and arrow scales are consistent; the constant-speed note is present; simState holds F, s, t, W, P.
- exp-1 locks F and t and varies s; exp-2 locks F and s and varies t: each isolates its parameter.
