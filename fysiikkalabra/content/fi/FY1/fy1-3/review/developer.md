VERDICT: DONE

Round 1 draft; `check_lesson.py fy1-3` is ok on every line.
- glossary.json: added mittaus, mittausvirhe, systemaattinen virhe, satunnaisvirhe, toistettavuus, oikeellisuus (not in meta.json glossary).
- lang/fi.json: `sims.fy1-3` texts.
- assets/sims/fy1/fy1-3/sim.js: ramp, stopwatch and dot plot (readings, mean, true value T = 2,40 s as model value). Sliders n, random error, systematic error; fixed series of random deviates; adapter n, sat, sys.
- tests/sims/fy1-3.json: 39 assertions.
- lessons/FY1/fy1-3: answers.py, figures.py (4 figures), sim-spec.md.
- content: lesson.md (staged example 3,18 ± 0,12 s), inquiry.json (2 predictions, experiments 1-2 core, 3 optional, thermometer data, conclusion, transfer, 3 checks), exercises.json 5/4/3, solutions.md, exit-ticket.json.

Notes: the sim's readings are model values; G in sim.js and answers.py must stay identical. Error estimate is the half-range (simple course-level method).
