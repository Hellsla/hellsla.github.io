VERDICT: PASS
CONTENT-HASH: 1931c445d9c3b481

## Blocking

## Polish
- exercises/solutions.md (fy8-9-L2-05 Answer) — the scatter of the net count 64 is taken as $\sqrt{64}$; the scatter comes from the measured count ($\sqrt{72} \approx 8.5$), and the initial value 283 (about 6 %) adds to it, so "about ±8 %" is slightly low (nearer 10 %) — write $\sqrt{72}$ and "about 10 %", or call the estimate rough.
- exercises/solutions.md (fy8-9-L3-04 a) — $\ln(71.2 : 32.8) = 0.7751$ gives $64.39\,\text{h}$, the solution has $64.38\,\text{h}$; the answer $2.68\,\text{d}$ is unchanged — correct the intermediate value.
- exercises/solutions.md (fy8-9-L3-05 c) — $\left(\tfrac{1}{2}\right)^{8.0/8.02} = 0.5009$, not $0.5008$; the result $50.1\,\%$ is right.
- exercises/solutions.md (fy8-9-L3-01 Answer) — three significant figures are justified by $38.0\,\%$ alone; the precision of $5700\,\text{a}$ is ambiguous — say the half-life is read to at least three figures.
- packet — the exercise brief of the English packet is empty and its deterministic checks say "check_lesson.py has not been run"; notation was judged against the standard symbols ($N$, $A$, $\lambda$, $T_{1/2}$), not against the English lesson text — regenerate the packet after the checks if the gate needs them.

## Checked
- All 19 numeric answers recomputed from the English task texts and tables with own formulas (one script): every one agrees with exercises.json and answers.py, well inside its tolerance; units and tolerances fit the data.
- Numbers, tables, units and decimal points of the English tasks and solutions carry the same physics as the computation; no step or justification dropped.
- L2-05: net counts, two-point 149 s vs log-linear fit of all points 150 s (inside 6 %); L2-06 net data follow 60 s, the student's 70 s reproduced; L2-07 sum 80, 5.4 %.
- L3-04: table consistent with 800 MBq (6.0 h) + 200 MBq (64.4 h); short-lived part 0.012 MBq at 96 h; other point pairs inside 5 %.
- L3-05: $T_\text{eff} = 3.06\,\text{d}$, $T_\text{bio} = 4.96\,\text{d}$, decay constants add to 0.2262 1/d; the additive model is stated in the task.
- L1-06 and L1-09: exactly one correct option; each distractor wrong for the reason its feedback gives; graph functions give 400/200/100/50 kBq (C), 294/108/15 kBq (D), zero at 4 h (A) and 2.8 h (B).
- Half-lives realistic; Co-60 $\lambda$ matches 5.27 a; Am-241 mass 0.29 µg.
- Conditions stated in the tasks: no new radon, daughter decays excluded, constant background, activity per gram of carbon.
- Symbolic solution before substitution in every numeric solution; scope inside the FY8 decay law.
