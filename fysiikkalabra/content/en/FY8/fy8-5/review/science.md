VERDICT: FAIL
CONTENT-HASH: e6a225e13958a986

## Blocking
- inquiry.json:6 (`learn[1]`, shown as "In this lesson, you will learn to …") — **B / consistency**: "interpret an orbital as a region inside which the electron is detected with a chosen probability" still defines the orbital as the drawn region, which this round corrected in the lesson: "An orbital describes the quantum state of the electron … The drawn region is an illustration, not the definition of the orbital" (Key idea and Summary). Fix: "interpret an orbital as a quantum state of the electron and its picture as a region inside which the electron is detected with a chosen probability."

## Polish
- contribution: "how random hits build up an orbital" — better "build up the picture of an orbital" (not student-facing).
- Common misconception: "the boundary of an orbital is an agreed probability boundary" — "the boundary drawn in an orbital picture" would match the new definition.
- Check 1 assumes 90 % for "a blue sphere" in a chemistry book; "usually 90 %" in the correct option would match the lesson's "chosen probability".

## Checked
- New wording: orbital = quantum state (allowed standing wave) that sets the detection probabilities; 90 % region an agreed illustration with about a tenth of hits outside; consistent with Summary, the 2p remark, check 1 and check 4 model answers.
- Recomputed in one script: worked example $E_3 - E_2 = 1.889\,\text{eV}$, $\lambda = 656.47\,\text{nm} \to 656\,\text{nm}$; 1s 90 % radius $0.141\,\text{nm}$ (2.66 $a_0$), most probable $r = a_0 = 0.053\,\text{nm}$; 2s peak $0.277\,\text{nm}$, 2p peak $0.212\,\text{nm}$, both 90 % extents $0.483\,\text{nm}$, 2s gap $0.096$–$0.118\,\text{nm}$; prediction 1 spread (σ ≈ 0.95 pp at $N = 1000$, sim series 90.1–91.8 %); transfer 2700 (mistakes 5400, 3000); error item 18; check 3 $10.2\,\text{eV}$ (mistakes 17.0, 3.4), 3–6 × visible. All agree with lesson-answers.py.
- Nodes: $n - 1$ in total, 2s spherical, 2p planar; energy grows with nodes in hydrogen, with shape held fixed in many-electron atoms: correct.
- Shell table $n^2$, $2n^2$, Pauli, filling order and C/N configurations correct; 3d→2p and 3s→2p give the same hydrogen line (both allowed).
- Every choice has exactly one correct option with right feedback; experiments lock all but the varied parameter; the sim model box states the see-through projection and that real position measurement is not this direct.
- Hash at start and end: e6a225e13958a986.
