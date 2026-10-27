VERDICT: DONE

Changes (uncommitted):
- assets/sims/fy1/fy1-2/sim.js: new true-scale solar system sim (1 px = 3474 km), drag/wheel/arrows/jump buttons, log slider 10^6-10^11 km, light-speed trip with hidas/normaali/nopea, Voyager 2 model by date (source: model), LaTeX labels, adapter params n, pvm, nopeus.
- tests/sims/fy1-2.json: 62 assertions for controls, readouts, jumps, Voyager dates, trip, speed.
- lang/fi.json: sims."fy1-2" block (own keys only).
- glossary.json: 6 entries (suure, yksikkö, SI-järjestelmä, etuliite, merkitsevä numero, astronominen yksikkö).
- lessons/FY1/fy1-2/: answers.py (all answers), figures.py (3 figures), sim-spec.md.
- content/fi/FY1/fy1-2/: lesson.md (Ydinajatus, Kaava: Yksikkömuunnokset, 7-stage Esimerkki Neptune, misconception, summary), exercises.json (5/4/3), solutions.md (complete), exit-ticket.json, inquiry.json (19 activities, predictions with reveals, Voyager interpret as model).
- meta.json untouched.

check_lesson.py fy1-2: all ok.
