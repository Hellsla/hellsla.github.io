VERDICT: PASS
CONTENT-HASH: 6aace4bb9c76d591

## Blocking

## Polish

## Checked
- Round 3: commit 479d5dabc, checked against the regenerated packet. Read from the text only; nothing was rendered.
- The rewritten physics is correct. Split as $P = \eta \cdot \tfrac12 v^2 \cdot \rho A v$, energy per kilogram times mass flow, both growing with $v$, gives the brief's $\tfrac12\eta\rho A v^3$.
  - $P \propto v^2$ keeps $\tfrac12 v^2$ and treats the mass flow as constant: $\tfrac12\eta\rho A v \cdot v$ with $v = 10$ gives 196 kW ≈ 0,2 MW.
  - $P \propto v$ keeps the mass flow $\rho A v$ and treats the energy per kilogram as constant: 19,6 kW ≈ 20 kW.
- Correction of my round-2 report: I proposed and then passed "Verrannollisuudessa $v$ unohtuvat molemmat … tekijät". That was wrong, because a $P \propto v$ model still keeps one factor of $v$, the mass flow. The pedagogy reviewer was right that it contradicted the feedback. The new text fixes this.
- The 20 kW feedback, the 0,2 MW feedback and the solution paragraph now give the same account, each with the factor it keeps and the factor it forgets. "lukuarvo $10^3$ on 100 kertaa 10" compares numbers only.
- Unchanged: 1,963 MW → 2 MW; 91,6 MW for 36 not converted; the reasonableness checks (4,9 MW wind power; the lesson's 2,3 MW example).
- Hash 6aace4bb9c76d591 at both start and end.
