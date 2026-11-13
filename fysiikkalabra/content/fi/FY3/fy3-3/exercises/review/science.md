VERDICT: PASS
CONTENT-HASH: 22036945998ce665
SCOPE: delta added-exercise from e1dd7ab8f7baa8e3 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-3-L2-08, Kuvaajan lukeminen) — "Pisteet ovat suoralla": the measured points lie only nearly on one line (pairwise slopes 0,26–0,28 kPa/°C). Per the guardrails, write "Pisteet ovat likimain samalla suoralla" and, ideally, take the slope from the fitted line (the least-squares line gives 54,0 °C; the endpoints give 54,5 °C, so the answer is unchanged).
- exercises/solutions.md (fy3-3-L2-08, Vastaus) — "muulla mittapisteparilla … 53–56 °C hyväksytään": the last pair (75; 100 °C) gives 51,9 °C, which is outside the tolerance. Say "kaukana toisistaan olevalla pisteparilla".
- exercises/exercises.json (fy3-3-L1-10) — as in round 1: the liquid is at its boiling point only when it boils at normal pressure, e.g. in an open dewar. Optional clause "avoimessa astiassa".

## Checked
- Round-1 blocker fixed: L2-08's five points are now in the task text, so the values no longer depend on reading the 25 kPa grid. The figure and its description list the same points and do not give the answer.
- L2-08 recomputed: endpoints $k = 0{,}275\,\text{kPa/°C}$, $\theta = 15/0{,}275 = 54{,}5\,{}^\circ\text{C}$; least squares $54{,}0\,{}^\circ\text{C}$; every other pair gives 53,6–54,3 °C except (75; 100) at 51,9 °C. Tolerance 0,04 (52,3–56,7 °C) accepts the fit and the endpoint and neighbouring-pair methods. answers.py gives 54,5, which matches.
- L2-08 physics: a closed rigid vessel (constant V and n) with a linear $p(\theta)$ stated as an assumption; solved in symbols before substitution; °C throughout, so no conversion needed. Two significant figures and the interpolation check are right.
- L1-10 unchanged since round 1: $-196 + 273{,}15 = 77{,}15\,\text{K} \approx 77\,\text{K}$, MAFY value as checked then.
- Rest of the set unchanged since PASS; hash same at start and end.
