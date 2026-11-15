VERDICT: PASS
CONTENT-HASH: 282cb05b89558507

## Blocking
None.

## Polish
- fy8-s3 d (solution answer, rubric `conclusion`): "the tube can no longer distinguish it from the variation of the background" is borderline exactly at $36\,\text{cm}$: there the net rate is $22 \pm 8\,\tfrac{1}{\text{min}}$ in a one-minute count (about $2.7\sigma$). Safer: "farther away / with a short counting time it is hard to distinguish". A student who says the source is still detectable with a longer count should get the point.
- fy8-s3 d: $36\,\text{cm}$ is an extrapolation beyond the measured range ($2$–$20\,\text{cm}$); the guardrails ask this to be said in one clause.
- fy8-s3 c (rubric `error_sources`): "about $6\,\%$" presupposes $r + d = 3.3\,\text{cm}$; a student using $r = 2.0\,\text{cm}$ gets $10\,\%$. Accept $6$–$10\,\%$.
- fy8-s3 a (rubric `conclusion`): the "most probable reason" is first given in part b; the model answer says "for example", so the point should not require that reason.
- fy8-s5 b: "decreased from $0.720\,\%$ to $0.440\,\%$" compares present-day values; the fissions lowered it at the time from about $3.7\,\%$ (fair simplification, one clause would close it).
- fy8-s5 text: $0.720 + 99.274 = 99.994$; "the remaining" skips uranium-234 (harmless).

## Checked
- Hash 282cb05b89558507 at start and end; `practice.py check` OK.
- One own script recomputed every number from the task data: s1 ($2.22$ and $1.97\,\text{eV}$, $296\,\text{nm}$, $1193$, $1107\,\text{nm}$, $0.83\,\text{eV}$); s2 ($\Delta m = 0.006005\,\text{u}$, $Q = 5.594\,\text{MeV}$, $A = 2.23 \cdot 10^{15}\,\text{Bq}$, $m = 3.52\,\text{kg}$, $83\,\%$, $1791\,\text{W}$, $98.5\,\text{W}$, $0.16$, $5 \cdot 10^{7}$, $0.566\,\text{mSv}$, alternative $0.556$); s3 (all nine rows of both tables, own least-squares fit $d = 1.31\,\text{cm}$, read line $-1.30\,\text{cm}$, $K = 3.15 \cdot 10^{4}$, $36.2\,\text{cm}$, $0.23$ and $0.27\,\mu\text{Sv/h}$, $14\,\%$, $2\,\%$, $6\,\%$); s4 ($0.782\,\text{MeV}$, $T_{1/2} = 609\,\text{s}$ from $878.4\,\text{s}$, $7.16$, $0.8575$, $135\,\text{s}$, $0.735$, $271\,\text{s}$); s5 ($7.16$, $1.364$, $3.67\,\%$, $3.49\,\text{a}$, $43\,000$, $4.7 \cdot 10^{17}\,\text{J}$, $5.8\,\text{t}$, $83\,000$). All agree with solutions, rubrics and answers.py.
- Physics: oxygen levels, lifetimes and collisional quenching; photon threshold versus intensity; atomic-mass Q value with electron bookkeeping; $A = P/Q = \lambda N$; equivalent and effective dose; inverse-square law with an effective detection point; counting statistics; weak decay $d \to u$ via $W^-$; helium mass fraction; moderator and self-regulation at Oklo. Source values (NIST, AME2020, PDG, MMRTG, STUK, OL3 $4300\,\text{MW}$, caesium dose rate) are realistic.
- Scope: inside FY8 central contents; no de Broglie, no later-course physics. s3 data is declared model-generated in its source note.
- Rubrics: criteria per part sum to the part's points; each asks what the task asks and the solution shows; other methods accepted. Figures agree with the data (fit line, marked points, level scale).
