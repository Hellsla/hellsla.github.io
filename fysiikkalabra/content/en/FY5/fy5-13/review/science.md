VERDICT: PASS
CONTENT-HASH: bfcc0c8af7db8314

## Blocking

## Polish
- inquiry.json:120 (`simulaatio.calc`) — "$a = 1.0\,\text{mm}$" reads as the loudspeaker's amplitude for the tubes too. In the tube formulas, though, $U(0) = a\cot kL$ or $a\tan kL$, and at $200\,\text{Hz}$ the closed tube's mouth is near a node. Add "for the tubes $a$ only sets the scale".

## Checked
- One script recomputed the sim's steady state:
  - Peaks are $16.7\,\text{mm}$: string at 100, 200 and 300 Hz; closed tube at 100, 300 and 500 Hz; open tube at 200 and 400 Hz.
  - Off-peak values are $1.0\,\text{mm}$, except $1.41\,\text{mm}$ for the closed tube at 150 Hz.
  - Nodes: 2, 3 and 4 on the string; node and antinode counts 1/1, 2/2 and 3/3 in the closed tube.
  - Every number in the prediction feedback and the conclusion's model answer matches.
- sim.js implements the stated model, and the natural frequencies emerge rather than being fed in. In the tubes $v = 340\,\text{m/s}$ is fixed, so each experiment varies only $f$. `simState` gives A, solmut, kuvut and lambda. The English canvas shows N/A, as the howto says.
- Worked example: $143\,\text{m/s}$ and $0.433\,\text{m}$, solved symbolically first, with justified rounding and a real check.
- siirto: $170\,\text{Hz}$, and the 113, 227 and 56.7 Hz mistakes are right. tarkistus-2: $0.80\,\text{m}$, and the 0.4 and 2.4 m mistakes are right.
- Every choice item has exactly one correct option, and each distractor's feedback is right.
- Theory, summary, glossary and exit ticket agree on:
  - phase inversion at a fixed end and the $\lambda/2$ and $\lambda/4$ spacings;
  - no energy transport under ideal reflection;
  - closed or open ends as displacement nodes or antinodes;
  - the end correction, stated as neglected;
  - the closed pipe sounding an octave lower.
- Figures:
  - The superposition rows scale 1, 0.707 and 0 at $0$, $T/8$ and $T/4$.
  - The string modes are correct.
  - The open-tube $f_2$ nodes are at $L/4$ and $3L/4$, and the closed-tube $f_3$ node is at $L/3$ from the mouth.
- Scope is inside the FY5 central contents.
- Hash unchanged at the end.
