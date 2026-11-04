VERDICT: FAIL
CONTENT-HASH: 5473a624fb5e15a2

## Blocking
- inquiry.json:471 (Find the error, option "The factor ½ is unnecessary", feedback) — **B**: "In charging the source delivers the energy $QU$, but only half of it is stored in the capacitor; the other half becomes internal energy of the wires and resistors" is stated as general, while the lesson's Formula section now (correctly) limits the half to charging an initially uncharged capacitor from a constant-voltage source through resistance, "not a general law for every way of charging". The task does not say how the capacitor was charged. Fix: "When an empty capacitor is charged from a constant-voltage source through a resistance, the source delivers $QU$, but only half of it is stored …", or drop the half-energy clause and say only that the stored energy is $W = \tfrac12 QU = \tfrac12 CU^2$ because the voltage grows from zero to $U$ during charging.

## Polish
- Lesson: the half "becomes internal energy … and is transferred to the surroundings as heat"; in a real circuit a little also leaves as radiation. C, no change needed.
- Worked example: with $C = 150\,\mu\text{F}$ and $U = 300\,\text{V}$ the energy could be given as $6.75\,\text{J}$; "two significant figures" follows from $t = 1.0\,\text{ms}$ only for the power.

## Checked
- New wording: total charge of the capacitor zero ($+Q$, $-Q$) in Key idea and Common misconception, consistent with Summary and glossary; the half-energy paragraph's condition (uncharged, constant voltage, resistance) is correct; the transfer task (empty capacitor, battery, resistor) meets it and its solution says so.
- Recomputed in one script: $C = 88.5\,\text{pF}$ ($A = 200\,\text{cm}^2$, $d = 2.0\,\text{mm}$); prediction 1 $44 \to 89\,\text{nC}$, $11 \to 44\,\mu\text{J}$; prediction 2 / exp. 3 glass $0.179\,\text{kV}$, $7.9\,\mu\text{J}$; exp. 5 breakdown $3.0\,\text{kV}$; worked example $6.75\,\text{J}$, $6750\,\text{W}$, $Q = 0.045\,\text{C}$, $\ge 3.4\,\text{s}$; paper $160\,\text{V}$; retrieval $150\,\text{kV/m}$; error item $0.034\,\text{J}$; transfer $190\,\mu\text{J}$ (mistakes 381, 0, 42.3); check 3 $12\,\text{J}$; exit $1.2\,\text{mC}$. All agree with lesson-answers.py.
- Dielectric mechanism (polarisation weakens the field), connected/disconnected table and the work done pulling the slab in: correct.
- Every choice has exactly one correct option; distractor feedback right.
- Experiments isolate the varied parameter; sim.js implements $C = \varepsilon_0\varepsilon_\text{r}A/d$, connected/disconnected and breakdown at $E > E_\text{max}$ as the model box says.
- Photos: film capacitor (MKP polypropylene, 275 VAC rating), capacitor bank caption correct.
- Hash at start and end: 5473a624fb5e15a2.
