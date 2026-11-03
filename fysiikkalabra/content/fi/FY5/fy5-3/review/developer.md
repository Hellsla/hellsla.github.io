VERDICT: DONE

Round 1 fix.
- sim.js: Δv̄ panel scaled up (longer arrows, labels 1,15-1,25 x larger, triangle centred in its panel, wide rink narrowed to 380 px for a wider panel); v̄1 now the same blue as v̄2 (labels tell them apart; dv figure in figures.py/lesson.md likewise); `before` clamped to release time so Δv̄ = 0 after release. Tests untouched, all pass.
- inquiry.json: tarkistus-3 4th criterion and model sentence removed; koe-1 intro asks for cuts at clearly different places (radius kept as varied parameter); table label $v_\text{irti}$.
- lesson.md: aria-label "samalla keskipisteestä lähtevällä suoralla"; net force points inward (l.216); "pyörimistaajuuden sijoittaminen kierroksina minuutissa ..."; Kaava paragraph "Esimerkiksi ... jolloin", one $\tfrac{1}{\text{s}}$ form.
- exercises: L1-04 replaced by tangent-flight task (answers.py, exercises.json, solutions.md); L1-02 reasonableness is an independent route via T; L3-01 stagger/same-time wording; L3-03 rolling without slipping sentence.
- exit-ticket answer 2: chain on its own line.
Not done: Koe 3 side padding (shared template, not lesson markup).
