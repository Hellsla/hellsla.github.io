VERDICT: PASS
CONTENT-HASH: 48737afd72e651b5

## Blocking
None.

## Polish
- fy8-s3 d (rubric `conclusion`, solution): "the tube can no longer distinguish it from the variation of the background" is borderline at $36\,\text{cm}$ (net $22 \pm 8\,\tfrac{1}{\text{min}}$ in one minute, about $2.7\sigma$); "hard to distinguish with a short count" would be safer (carried from round 1).
- fy8-s3 d: $36\,\text{cm}$ is an extrapolation beyond the measured $2$–$20\,\text{cm}$; one clause would say so (round 1).
- fy8-s3 d (rubric `calculation`): the dose scaling uses $r$, not $r + d$ ($0.23$ versus $0.27\,\mu\text{Sv/h}$); both round to "about $0.2$–$0.3$", so accept either.

## Checked
- Hash 48737afd72e651b5 at start and end; `practice.py check` OK (5 tasks, 84 points).
- Round-2 diff against the version passed in round 1, normalised (aligned rows, `\\`, `&`, `$$` removed): the seven re-broken chains in solutions.md (s1 a, s2, s3, s5 and others) carry the same numbers, signs and units in the same order (category reflow). Content changes are four, all in tasks.json: s2 text constants split into two formulas ($1\,\text{u} = 931.5\,\text{MeV}/c^2$ and $1\,\text{u} = 1.66054 \cdot 10^{-27}\,\text{kg}$), values unchanged; s3 d criterion "$\approx$" reworded; s4 a criterion 4 now asks only "the weak interaction", which is exactly what the task asks (the $W^-$ mediator, not asked, stays in the solution only, correctly); s5 d criterion 4 now asks a justified evaluation (what Oklo supports, what it does not show, that Onkalo's safety rests on studies of its own conditions and barriers), which matches the task's "evaluate the claim" and the solution's *Evaluation* and *What safety is based on* paragraphs. Points per part unchanged.
- One own script recomputed every answer from the task data: s1 ($2.22$, $1.97\,\text{eV}$, $296\,\text{nm}$, $1193$, $1107\,\text{nm}$, $0.83\,\text{eV}$), s2 ($0.006005\,\text{u}$, $5.59\,\text{MeV}$, $2.23 \cdot 10^{15}\,\text{Bq}$, $3.52\,\text{kg}$, $83\,\%$, $1790\,\text{W}$, $98\,\text{W}$, $0.16$, $5 \cdot 10^{7}$, $0.566\,\text{mSv}$), s3 (own fit $d = 1.31\,\text{cm}$, $36.3\,\text{cm}$, $14\,\%$, $2\,\%$, $6\,\%$), s4 ($0.782\,\text{MeV}$, $7.16$, $0.8575$, $135\,\text{s}$), s5 ($3.67\,\%$, $83\,000$ half-lives). All agree with solutions, rubrics and answers.py.
- Physics, scope and guardrails as in round 1; nothing new outside FY8.
