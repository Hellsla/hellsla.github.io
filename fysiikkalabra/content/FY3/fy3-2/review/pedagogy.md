VERDICT: PASS
CONTENT-HASH: e1ab5e19c7f4b103

## Blocking

## Polish
- inquiry.json pred-3 (prompt and feedback of Aino and Cem) — refers to "Selitä-vaihe", but the page stage is named "Teoriatiivistelmä"; a student looks for a stage that does not exist. Fix: "vertaa ennustettasi Teoriatiivistelmä-vaiheen kuvaan ja selitykseen" and "Palaa tähän Teoriatiivistelmässä".
- inquiry.json exp-1 and exp-2 — the simulation only computes W = Fs and P = W/t, so the experiments confirm the program's arithmetic and cannot really refute pred-1 or pred-2. The Joule table is the only data that carries physics. Fix (optional, later): let one run produce W without the formula, for example from the area filled under a measured or noisy F(s) trace.
- inquiry.json pred-2, third option feedback — "mittausten mukaan" refers to model values; write "mallin arvojen mukaan", as in the other options.
- Simulation canvas at 390 px (fy3-2-sim-390.png, exp-exp-1-390.png) — the graph title "W = pinta-ala" is cut off at the top edge of the canvas; move it down or give the canvas more top margin.
- inquiry.json "virhe" — the mistake (8,0 J) was already named at the end of the example's Järkevyys stage, so the item is answered before it is tried. Fix: use a different mistake, for example a student who computes the area of check-1 as 2 × (0,5 · 40 N · 0,10 m). exercises.json L3-01 wording: "keskimääräinen suuruus" is awkward; write "Mikä on voiman keskiarvo matkan suhteen koko 2,0 m:n matkalla?"

## Checked
- Learning path: hook, fy3-1 retrieval (G = mg), predictions, model values, Joule data, theory, example, error item, transfer, exercises; the opening question is answered in reflect and Ydinajatus; scope stays within FY3 (no E_p, cos α).
- Hook question is open and the answer is not disclosed before commitment; pred-3 is clearly marked as untestable in the simulation.
- Prediction options are distinct, each wrong option's feedback repairs its misconception; correct speaker varies (Bea only one correct).
- Joule interpret item uses a real data table, marked as example values, not Joule's own.
- Figures 1-4 are recognisable, uncluttered, labelled in text as well as colour; fig 4 is to scale with axes and units.
- Worked example is staged in five steps, one idea per step, with a sanity check by the mean force.
- Exercises: three levels, no repeat of the example, answers and solutions verified by hand (including 180 J, 100 J, 30 N, 590 J, 45 min); exit ticket tests the core ideas (perpendicular force, area, work vs power).
- Finnish: case after number+unit correct (60 N:n voimalla, 4,0 J:n työn); glossary terms used correctly; reading level suits 16-19-year-olds.
- Phone: sim controls, locked sliders marked "(vakio)", readout and tables fit at 390 px; 1280 px puts the sim beside the experiments clearly.
- Workload is one lesson: three predictions, two experiments, one data item, three checks.
