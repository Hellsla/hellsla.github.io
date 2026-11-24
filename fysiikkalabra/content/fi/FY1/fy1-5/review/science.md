VERDICT: PASS
CONTENT-HASH: 1814c2be4d581b22

## Blocking

## Polish
- lesson.md:217, inquiry.json hook — "nopeus oli ylityksen aikaan $15{,}341\,\text{km/s}$ (NASA/JPL)": 15,341 km/s is JPL's mission-status (present-day) value. The lesson's own Periaate stage says the probe slowed by about 0,1 km/s in 2018–2026, so at the crossing it was nearer 15,4 km/s. Effect on the result about 0,1 AU, so not blocking. Fix: write "nopeus Aurinkoon nähden on noin $15{,}341\,\text{km/s}$ (NASA/JPL)" and leave out "ylityksen aikaan".
- Scope note vs lesson — the brief gives 119,7 AU (NASA/JPL). The lesson uses 119,0 AU (Burlaga ym. 2019), which matches the published value, and then honestly compares 142,6 AU (from the Sun) with 143,05 AU (from Earth). No change needed in the lesson, but the scope note should be brought into line so it does not lead later chapters back to 119,7.
- inquiry.json siirto solution — "kaksi merkitsevää numeroa kuten ajassa $45\,\text{s}$": a time span set by the task is exact (house rule). The limiting data are 120 m and 21,6 km/h, so the answer has three figures. 390 m stays the same; only the reason should change.
- sim.js:817 — the wheel turns 0,9 rad/m, but rolling at this scale needs about 1,4 rad/m. This is cosmetic and nothing is measured from it.

## Checked
- One Python run recomputed: 15,341 km/s = 0,0088602 AU/vrk; 2922 days (2020 and 2024 leap days) → 144,89 AU ≈ 144,9 AU = 2,17·10¹⁰ km; 15 Feb 2026 → 142,56 AU; gravitational Δv over 8 a at about 130 AU ≈ 0,09 km/s, consistent with the "noin 0,1 km/s" in the text; reasonableness check ≈ 25–26 AU.
- Every inquiry number: ennuste 8/4, 14 vs 20/12; virhe 11 → 33 wrong, 23 right; siirto 6,0 m/s, 390 m, mistakes 1092 and 270; tarkistus-2 v = 3,0 m/s, s₀ = 4,0 m, mistakes 7 and 3; koe-2 ratios 5,0 and 3,5; pysähdy 18 m and 25 m/s; 72 km/h = 20 m/s; exit ticket 30 km and 10 m.
- Every choice item has exactly one correct option, and each distractor's feedback names the actual misconception (paikka vs matka, vaakasuora (t,s) = levossa).
- Graph figure is to scale, measured from the SVG coordinates: 3 m/s, s₀ = 5 m, Δt = 2 s gives Δs = 6 m, and the lines are parallel. The motion figure has equal spacing, and its Δs brackets match.
- sim.js implements s = s₀ + vt and ds = vt, and simState carries s0, v, t, s and ds. The slope triangle over 2–6 s gives Δs/Δt = v. Every experiment's range fits inside 0–60 m (largest 10 + 5·10).
- koe-1 and koe-2 lock s0 and v and vary only t; the koe-2 capture shows s = 6,0 m and Δs = 0 at t = 0.
- Model limits are stated (no friction or acceleration, full speed from the start, positive direction; Voyager slowed by the Sun's gravity). Earth- vs Sun-distance caveat is correct (≤ about 1 AU).
- Scope stays inside FY1 (linear model, direct proportionality, no vectors or forces). Glossary distinction paikka/matka is kept throughout: theory, summary, misconception, checks, exit ticket.
- Content hash was identical at the start and the end.
