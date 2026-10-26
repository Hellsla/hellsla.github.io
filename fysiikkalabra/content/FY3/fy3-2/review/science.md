VERDICT: PASS
CONTENT-HASH: f500230f9e9593b2

## Blocking

## Polish
- inquiry.json:94 — pred-2 feedback says "mittausten mukaan" for the simulation's P values; the brief asks that sim numbers be called model values — write "mallin arvojen mukaan".
- lesson.md:149 — "(kaava alla), Sama lämpeneminen" — comma should be a full stop.
- lesson.md:180 — "muuttaa sähköenergiaa lämmöksi" sits awkwardly beside the Joule item that insists heat is a transfer, not a stored substance — consider "muuttaa sähköenergiaa kiukaan ja ilman sisäenergiaksi" or "siirtää lämpönä 6000 J joka sekunti".

## Checked
- W = Fs stated for a constant force along the motion, area under (s,F) for a varying force, W = Gh = mgh with F = G at constant speed, P = W/t = Fv for uniform motion; no E_p, E_k, cos α or work–energy theorem named, so inside the FY3 scope note.
- Worked example symbolic first: W = ½F_max s = 4,0 J, average-force check and the 8,0 J error explained.
- answers.py recomputed in one script: all 12 answers match, rounding within tolerance.
- solutions.md: unknowns isolated before substitution (s = W/F, W = Pt, t = mgh/P, F_ka = W/s); sanity values right.
- Figures: spring-work graph to scale (75,6 px per 0,05 m, 42,75 px per 10 N, line to (0,20 m; 40 N)); lift figure F and G arrows equal (58 px); work-graphs triangle + rectangle schematic consistent with A₁ + A₂.
- Simulation: W = F·s, P = W/t, Wdone = W·u, the (s,F) area fills in proportion to distance; speed control changes only the pace (u advances by Δt·speed/t); model box states constant speed with friction equal to the pull and that values are computed from the formulas.
- exp-1 locks F, t and varies s (W ∝ s); exp-2 locks F, s and varies t (W constant, P ∝ 1/t); simState carries W and P.
- Predictions: 600 → 1200 J; 120 W → 30 W; carrying horizontally W = 0 with air resistance neglected; Aino's 1960 J ≈ 2,0 kJ.
- Joule table consistent with 2,0 kg × 1,0 m × 10 drops = 196 J, ΔU/W ≈ 0,99; Joule's 1850 value ≈ 4,16 J per g·°C vs 4,19 today.
- siirto 240 W; check-1 triangle 1:4 → 3×; check-2 120 + 60 = 180 J; exit ticket 98 J, 20 J, equal work and double power.
