VERDICT: PASS
CONTENT-HASH: 37c379ba50e81e4a

Science review of the English translation of fy9-koe (source content/fi/units/fy9-koe/, reviewed PASS).

Method: compared every text field of inquiry.json, exit-ticket.json, sovella/tasks.json, unit.md, solutions.md, teacher.md and figures.json with the Finnish source; `check_i18n.py` gives en: 0 errors (answers, units, tolerances, correct options, formulas, sections, figures equal to the source). Recomputed in one Python call: bath 4.7254 kWh; scooter 71.1 N; density 2700 kg/m³; 0.60 kW; 26.25 MJ; 458 805 J; 277.39 kPa; 7.8125 m/s²; 8.9286 m/s; 0.77955 m; 10 lg 2 ≈ 3.01 dB; 72.0 Ω; 28.90°; 0.30 N; 656.47 nm; 0.444 m/s²; task 1: 36 198.9 J, 134.07 W, 214.07 W, 262.7 kJ; task 2: least-squares slope 4.025 s²/m, intercept 0.062 s², g = 9.807 m/s², L-intercept −1.54 cm, single-point g = 9.07 m/s²; task 3: 1.4549 W; task 4: η = 0.8621. All agree with the translation.


Re-review (2026-11-04) after the inquiry.json "fold" tags were translated ("Kertaustesti FYn" -> "Review test FYn", 24 fields, the only change since the last review): the tags only group the questions by module and carry no physics; module ids FY1–FY8 and the grouping (3 questions per module, in source order) are unchanged. `check_i18n.py` en: 0 errors (it now checks fold as text); `units.py check` 77 units ok; `practice.py check` OK. No earlier Blocking finding existed; nothing regressed.

## Blocking
None.

## Polish
1. Physics wording is faithful and correct throughout: "work–energy principle", "interaction energy between the particles" (not "bonds"), "net transfer of energy from warmer to colder", "magnitude of the acceleration", "force pair of the same interaction", "the energy of the atom can have only certain values". No physics was added or lost.
2. inquiry.json activities[22].solution (Reasonableness) and activities[5].choices[2].feedback, solutions.md s2 "Yleisiä virheitä": division written with a colon (5.0 : 1.68$,  : t$, ^2 : L$) is a Finnish convention; English readers expect ÷ or a fraction. Keep it if check_i18n requires identical formulas; otherwise use $15.0 / 1.68$.
3. tasks.json fy9-koe-s3 text "at $13.00$": a clock time rendered as a decimal number in LaTeX; "at 1 pm" (or 13:00) in plain text would read better (check that check_i18n accepts the change).
