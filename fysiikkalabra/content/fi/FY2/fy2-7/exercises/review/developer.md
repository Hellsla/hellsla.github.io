VERDICT: DONE

Round 1 (fix).
- exercises.json: all 12 texts in LaTeX (values, units, percentages). Level 2 now has a real second step and tests the wrong base with large losses: L2-01 (20 %, find the loss from the delivered energy), L2-02 (80 %, GWh to MWh), L2-03 (invented example, 2,40 TWh, 4,0 % -> mean loss power in MW, replacing the 83 TWh task), L2-04 (20 %); the wrong method now falls outside the 0,02 tolerance. Level 3: L3-02 is a decision between two networks (difference of delivered energy), L3-03 puts the loss in context (how many houses' yearly heating, answer in kpl) instead of a repeated power-times-time; L3-01 kept.
- answers.py: recomputed for the changed tasks first.
- solutions.md: L2-01..04, L3-02, L3-03 rewritten; L3-03 converts by substitution (1 kWh = 0,001 MWh), L2-03 Kaava is symbolic with the loss share p; significant-figure reasons name the least precise datum (also L1-02).
- Not done: a purely conceptual task (schema is numeric only); L1-01 left as is (level 1 one-step).
lint_lesson and check_solutions: ok.
