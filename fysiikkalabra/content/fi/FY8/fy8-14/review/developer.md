VERDICT: DONE

Round-1 fixes.

- Sim seed 4 -> 73 (`sim.js`, `lesson-answers.py`): over seeds 1-100 the model's median distance is 4,2 cm at N = 10, 1,4 cm at 20, 1,0 cm at 50, all within 1,5 cm by N = 150; seed 73 is typical and monotonic (18,4 / 4,0 / 1,4 / 0 cm at N = 10/20/50/200). `tests/sims/fy8-14.json` updated, N = 20 assertion added (21 pass).
- `inquiry.json`: ennuste-2 "Kymmeniä", feedback and johtopäätös values and criterion; chance variation stated (calc, feedback, model); koe-1 records N = 10, 20, 50, 200; time-of-flight in ennuste-1 feedback and sim model ("malli ei käytä saapumisaikojen eroa").
- `lesson.md`: characteristic X-rays in the definition, heading and summary; time-of-flight PET (0,3 ns -> a few cm); Kaava and Esimerkki rewritten with halving counts n = d : d½ and 2^(n_B - n_A), no nested exponents; Järkevyys via the transmitted fractions.
- `glossary.json`: röntgensäteily includes characteristic X-rays.
- `exit-ticket.json`: PET localisation question replaces the X-ray contrast one.
- Exercises: L3-02 mammography 30 kV, mean about 20 keV, 30 keV assumed; L1-03 5,1 mSv; logarithm step shown in L2-01, L2-02, L3-03.
