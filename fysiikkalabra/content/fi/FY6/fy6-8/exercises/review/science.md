VERDICT: FAIL
CONTENT-HASH: e8166f6d6acb7bb8

## Blocking
- content/fi/FY6/fy6-8/exercises/exercises.json:346 — (B, data provenance; guardrails "Say whether each number is measured, simulated or calculated" and "Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla suoralla") fy6-8-L2-09 calls its five points "mittauspisteet", but figures.py draws them exactly from U = 12 V − 0,020 Ω · I, all on one line. Presented as measurements they contradict the lesson's own sentence on real series, and the solution's step "pisteiden kautta piirretty suora" hides that a fit was never needed. The same set already labels such points correctly in fy6-8-L1-05 ("mallista lasketut pisteet"). — Write "(mallista lasketut pisteet)" instead of "(mittauspisteet)" in the task (and "Mittauspisteet ovat" → "Pisteet ovat" in the figure's alt text in lessons/FY6/fy6-8/figures.py), or give the points a realistic scatter and keep the reading from the drawn line.

## Polish
- content/fi/FY6/fy6-8/exercises/solutions.md (fy6-8-L2-09, Vastaus) — "kaksi merkitsevää numeroa, koska arvot luetaan ruudukolta" is thin: the difference 4 V is read exactly on gridlines; say that the readings lie exactly on gridline crossings, so 0,020 Ω is justified.

## Checked
- Hash e8166f6d6acb7bb8 at start and end; delta: only fy6-8-L2-09 judged.
- Model: U = E − R_s I, slope −R_s; the solution derives R_s = (U₁ − U₂) : (I₂ − I₁) from two equations before numbers, reads two far-apart points on the line, and warns that one point's U : I is the load resistance. All as the lesson teaches.
- Figure generator: points (50; 11), (100; 10), (150; 9), (200; 8), (250; 7) on the drawn line from (50 A; 11 V) to (250 A; 7 V), gridlines 50 A and 1 V; the line is drawn only over the data, so neither E nor I_k is shown; alt text gives the same points.
- Recomputed: R_s = 4 V : 200 A = 0,020 Ω; answers.py agrees; unit Ω and tolerance 4 % fit.
- Magnitudes: E = 12 V, R_s = 20 mΩ, 7 V at 250 A — a realistic, somewhat weak starting battery under cranking load; the check through the third point and E = 12 V is a real check.
