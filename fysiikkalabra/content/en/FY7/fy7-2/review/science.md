VERDICT: PASS
CONTENT-HASH: ca6809a1c3c3421d

Follow-up review of the fix commit 2c31ff041 (delta from 01ef6bfd64671ffb, whose full review is kept below). Change: inquiry.json:141, simulation `calc` box.

## Blocking

None.

## Polish
- Particle accelerator: "In a ring accelerator … the magnetic field is strengthened so that the radius stays the same" describes a synchrotron; the cyclotron photo after it has a growing radius. "In a synchrotron, a ring accelerator such as the LHC, …" would prevent the clash.
- Inquiry items writing $qvB$, $qU$, $r = mv : (qB)$ concern positive particles only (correct, $q = |q|$); a note in the reflect prompt would match the lesson. Glossary entries still read $qvB\sin\alpha$, $mv/(qB)$.

## Checked
- Earlier blocking item resolved: "the magnetic force, whose magnitude is $|q|vB$" and "The forces $F_\text{m} = |q|vB$ and $F_\text{s} = |q|E$ in the readings"; the electric force stays the signed vector $q\overline{E}$. Correct for the negative hydrogen ion and matches sim.js (`Math.abs(P.q)`).
- Consistency: grep of plain $qvB$/$qE$/$qU$ — lesson.md uses them only in the worked example ("$|q| = q$" for Ne⁺); no inquiry item with plain $q$ involves a negative particle.
- lesson.md notation: $\overline{F}_\text{s} = q\overline{E}$ signed, $F_\text{s} = |q|E$, $|q|U = \tfrac12 mv^2$, $F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$, selector, $m = |q|B_2r/v$; Summary, exit ticket and contribution agree.
- Recomputed: proton $3.2 \cdot 10^{-14}\,\text{N}$, $5.2\,\text{cm}$, weight ratio $2 \cdot 10^{12}$; graph $10.4$/$20.9\,\text{cm}$; example $3.00 \cdot 10^5\,\text{m/s}$, $20.01\,\text{u}$, Ne-22 $27.4\,\text{cm}$; LHC $1.09 \cdot 10^{-6}\,\text{J}$; retrieval $4.38 \to 8.75 \cdot 10^5\,\text{m/s}$; koe-2 $24$/$48\,\text{fN}$; error item $4.57 \to 6.46\,\text{cm}$; transfer $0.225\,\text{T}$ (mistakes 0.159, 0.00712); check 3 $6.22\,\text{cm}$; exit $3.0 \cdot 10^5\,\text{m/s}$. All agree with lesson-answers.py.
- Directions in figures and check 2 agree with $\overline{F} = q\overline{v} \times \overline{B}$; one correct option each; experiments lock all but the varied parameter; sim.js Boris integration, non-relativistic.
- Hash at start and end: ca6809a1c3c3421d.
