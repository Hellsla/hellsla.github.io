VERDICT: PASS
CONTENT-HASH: 6c4d981f2b165061

## Blocking
None.

## Polish
- fy6-s1 text: the sentence "It is not the same thing as the drift velocity of charge carriers" is a clarification nobody asked for and sits oddly in a task statement. Cut it, or move it to the solution as a short note. The same goes for the solution's definition of "rate of change of the voltage" and the drift-speed figure in part d. Both interrupt the error analysis.
- fy6-s1 d: the creep estimate (0.06 ohm) leans on one repeat reading at 0.10 A, which is fine. Say in the solution that the correction is an upper bound because the drift is not necessarily linear in time.
- fy6-s2 b: the answer is "16.7 W" in tasks.json and "17 W" in the solution. Both are accepted by the tolerance, but one form would be cleaner.
- fy6-s3 c: the claim that air resistance "approximately equals the electric force" at 5 m/s is asserted, not checked. A one-line remark that the model is only qualitative would suffice.
- fy6-s4 d: the three-point 0.30 A estimate is flagged as idealised, which is good. The fourth point (conclusion) repeats it, so the two could be merged.

## Checked
- All four tasks are authentic and unfamiliar (battery measurement, cable and lamps, spray painting, flash capacitor). Each has connected parts of rising demand: model choice, then calculation, then evaluation or error analysis. No heading or prompt names the formula. s1 a asks the student to "choose a suitable model", s2 c and s4 d ask for judgements, and s3 b only says "state your assumptions".
- The rubrics are specific and observable. Shared keys are used with task-specific `detail`, and nothing earns points for irrelevant things. Points per part (3 or 4) match what the criteria demand.
- s1 d, s3 c and s4 d test competencies (experiment, concept, transfer) that calculation-only tasks would miss. The task set varies in kind (graph, circuit analysis, field and energy, capacitor and safety).
- The worked solutions follow house rule 7: given, principle, symbolic formula, conversions, substitution, rounded answer with its reason, reasonableness check. s2 b checks the power balance (30 W) and s3 b checks via acceleration. The common mistakes are real and likely (R = P:U, forgetting the cable drop, kV not converted, energy "lost").
- Numbers are consistent with answers.py output (4.6 V, 1.2 ohm, 2.0 W, 13 %, 2.5 A, 16.7 W, 4.3 A, 1.8e-7 N, 13.4 m/s, 3.2e-9 N, 14.85 J, 6.86 J, 46.2 %, 26.4 A).
- The round-2 changes hold. The R_k label is consistent in the text, criteria and figure. Drift velocity is separated from creep. s4 significant figures agree between the answer and the solution (14.85 J and 14.9 J; 26 A with two figures). The mass wording in s3 is correct.
- The task figures give the setup without results. The s2 figure shows only the lamp ratings, and the model graph appears only in the solution.
- Workload is about 60 to 75 minutes for four tasks with 14 to 15 points each. That fits the module-end course scope (2 op).
- I did not review `docs/coverage/FY6.md` because the packet does not carry it. The checks on coverage gaps are out of scope for this round.
