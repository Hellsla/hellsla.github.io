VERDICT: DONE

Round 1 (fix). check_lesson.py fy4-3: every line ok.

- lessons/FY4/fy4-3/figures.py: new figure `kone` (aircraft force diagram, fbd.py); auto figure description "takasivulta taaksepäin".
- lesson.md: `kone` figure and F_1, F_2, F_v naming in the Esimerkki Periaate stage; tukivoima and kitkavoima explained at first use; air resistance noted; auto aria-label fixed.
- inquiry.json: siirto "Voimakuvio:" step and "tien voiman renkaisiin" wording; pred-1/exp-1 min 4 (frictionless row required); "Massa ei tee voimista erisuuria"; virhe optional; check-3 second step optional.
- exercises.json / solutions.md: Voimakuvio steps in L1-03 and L1-05; L2-02 varied (weight and buoyancy as distractors); L2-01 "13 N"; L3-01 prompt names size and direction; L1-04 "kymmenen newtonin tarkkuudella".

Not fixable here: sim readable at 390 px with graph and diagram stacked. It needs a taller canvas, but test_sims.py and tests/sims/fy4-3.json fix the canvas at 600x400. A larger label font at narrow widths made labels overlap, so it was reverted. sim.js is unchanged.
