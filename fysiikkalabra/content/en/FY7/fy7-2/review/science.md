VERDICT: FAIL
CONTENT-HASH: 01ef6bfd64671ffb

## Blocking
- inquiry.json:141 (simulation, `calc` box) — **B**: "the magnetic force, whose magnitude is $qvB$" and "The forces $F_\text{m} = qvB$ and $F_\text{s} = qE$ in the readings" use the signed charge for a magnitude, while the simulation offers the negative hydrogen ion ($-e$) and sim.js itself computes the readings with `Math.abs(P.q)`. For that ion the stated formula gives a negative magnitude, which is the exact signed-$q$ vs $|q|$ mix this round removed from the lesson. Fix: "whose magnitude is $|q|vB$" and "The forces $F_\text{m} = |q|vB$ and $F_\text{s} = |q|E$ in the readings …" (keep "the electric force $q\overline{E}$", which is a signed vector and correct).

## Polish
- Particle accelerator: "In a ring accelerator … the magnetic field is strengthened so that the radius stays the same" describes a synchrotron; the cyclotron photo right after has a growing radius at a constant field. Naming it ("In a synchrotron, a ring accelerator such as the LHC, …") would prevent the clash.
- The inquiry (predictions, conclusion, reflect, check 3, check 4, transfer) writes $qvB$, $qU$, $r = mv : (qB)$ for positive particles only, which is correct ($q = |q|$); a note "for positive particles $|q| = q$" in the reflect prompt would match the lesson's notation. The glossary entries (magneettinen voima, ympyrärata) still read $qvB\sin\alpha$, $mv/(qB)$.

## Checked
- New $|q|$ notation in lesson.md: $\overline{F}_\text{s} = q\overline{E}$ signed with direction by sign, $F_\text{s} = |q|E$, $|q|U = \tfrac12 mv^2$, $F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$, selector $|q|E = |q|vB$ (passes either sign), $m = |q|B_2r/v$, accelerator $|q|U$; Summary, exit ticket and contribution say the same. Worked example states $|q| = q$ for Ne⁺.
- Recomputed in one script: proton $3.2 \cdot 10^{-14}\,\text{N}$, $5.2\,\text{cm}$, weight ratio $2 \cdot 10^{12}$; graph $10.4$ / $20.9\,\text{cm}$; worked example $v = 3.00 \cdot 10^5\,\text{m/s}$, $m = 3.324 \cdot 10^{-26}\,\text{kg} = 20.01\,\text{u}$, Ne-22 at $27.4\,\text{cm}$; LHC $1.09 \cdot 10^{-6}\,\text{J}$; retrieval $4.38 \to 8.75 \cdot 10^5\,\text{m/s}$; koe-1 $d$ $10.44$/$20.89\,\text{cm}$; koe-2 $24$/$48\,\text{fN}$; error item $4.57 \to 6.46\,\text{cm}$; transfer $0.225\,\text{T}$ (mistakes 0.159, 0.00712); check 3 $6.22\,\text{cm}$; exit $3.0 \cdot 10^5\,\text{m/s}$. All agree with lesson-answers.py.
- Directions: force-dir, circle-path and spectrometer figures and check 2 (field into page, curves down → negative) agree with $\overline{F} = q\overline{v} \times \overline{B}$.
- Every choice has exactly one correct option with right feedback; experiments lock all but the varied parameter; sim.js integrates $m\,d\overline{v}/dt = q(\overline{E} + \overline{v} \times \overline{B})$ (Boris), non-relativistic as its model box says.
- Hash at start and end: 01ef6bfd64671ffb.
