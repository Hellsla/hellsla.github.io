VERDICT: PASS
CONTENT-HASH: 54bf1031ed79eec6

## Blocking

## Polish
- content/en/FY6/fy6-15/lesson.md:408 — the sentence says the potential difference between the feet is very small but not why. Optional: add "because the resistance of the conductor between the feet is very small". This is C-level and not a finding.

## Checked
- Previous blocking item (internal consistency, bird): lesson.md:408 (High-voltage lines) and :570 (Common misconception) now say "almost the same potential / potential difference very small / only a very small current". This matches ennuste-2's correct option and all four of its feedbacks (inquiry.json:91–100). No "no voltage / no current" claim remains in the lesson, the inquiry or the exit ticket.
- ennuste-1, ennuste-2, kertaus, virhe, tarkistus-1, tarkistus-2: exactly one correct option each, and the distractor feedback is right.
- Compared with fi by script: in inquiry.json the answers, tolerances, mistake values, correct flags, figures and reveal order are identical. The numeric content of lesson.md, inquiry.json and exit-ticket.json is the same set as in fi.
- Recomputed in one script with my own formulas (shared lesson-answers.py): 2300 W and 3680 W limits; 8.70 A; kitchen 13.9 A, all devices 22.6 A; skin 1.15, 11.5 and 230 mA; example 19.6 A, estimate 22.5 A; virhe 12.6 A; siirto 14.8 A and 131 W; mistakes 0.0719, 45.4 W, 88.2 kW; exit 2.56. All agree.
- Models and conditions: rms values for in-phase loads; E_max·d in a uniform field; the TN system is named; the effect table is tied to 50 Hz, duration and IEC 60479-1; the shoes condition is stated; the protective extra-low voltage limits are 50 V AC and 120 V DC.
- Mechanisms: the fuse protects the cable through RI²; the RCD compares the line and neutral currents, with its L–N limitation; the step voltage comes from the ground's potential gradient.
- Model answers and the exit ticket agree with the theory.
- Hash identical at start and end.
