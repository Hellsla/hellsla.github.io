VERDICT: PASS
CONTENT-HASH: addb9d598021ee63

## Blocking
None.

## Polish
- "Substitute into the last symbolic form" is still not followed in four Sijoitus steps, although the Kaava chains now end in one closed form (numbers all correct):
  - k3-c: $F = IlB$ and $P = Fv$ are computed stepwise, not from $F = e\,lB/R$ and $P = e\,lBv/R$.
  - k4-c: $I_1$ uses $I_2U_2/U_1$, not the final $P/U_1$.
  - k6-a: $P_\text{h} = RI^2$ is used, not $RP^2/U^2$; the share $P_\text{h}/P$ is not in the Kaava although the question asks for it.
  - k6-c: Sijoitus uses $S = (E_\text{A}-E_\text{B})\,p$ from Muunnokset, not the last form $(P_\text{h,A}-P_\text{h,B})\,t_\text{käyttö}\,p$ or $t_\text{takaisin}$ with it.
  Either substitute into the last form or label the intermediate results as deliberate steps.
- k6-c: $t_\text{käyttö}$ is now distinct, but $t_\text{takaisin}$ still reads as the same letter; $T_\text{takaisin}$ or $n$ would be clearer.
- k4-b: the Kaava now gives $e_0 = NBA\cdot 2\pi f$ straight from $\Phi = BA\cos(2\pi f t)$; Periaate names the law, so it is followable, but opening with $|e| = N\Delta\Phi/\Delta t$ would show the basic principle.
- k6 statement: "tehon $12\,\text{MW}$ vastaavan energian vuodessa $4000\,\text{h}$ ajan" is awkward; "Puisto tuottaa tehoa $12\,\text{MW}$ vuodessa $4000\,\text{h}$ ajan" reads more naturally.

## Checked
- Read all of tasks.json and solutions.md; the changed steps k3-c, k4-b (now one chain, B = e0/(NA 2πf) = 0,0516 T), k4-c, k6-a, k6-c and their neighbours.
- Symbolic chains end in closed forms for the asked quantities; the N factor in k4-c (2789 from 12,37 V, 2788 exact, answer "noin 2790") is within tolerance and explained in Annettu.
- Numbers, points and rubrics unchanged and match answers.py (0,30 V; 0,060 N; 0,15 W; 12,37 V; 3,72 A; 600 A; 1,728 MW; 334 175 €; 8,98 a).
- Tasks still demand independent application: unnamed models, source data, rising parts, evaluation endings (k6-d, k7-e); variety across the four basic tasks (graph, induction, generator, grating) and two applied tasks (societal numbers, experimental data) is good; Lenz direction in k3-b is correct.
- Finnish, overline notation, units in LaTeX and decimal comma intact; workload fits 120 min.
