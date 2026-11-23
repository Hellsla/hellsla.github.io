VERDICT: FAIL
CONTENT-HASH: 2192d48e7a0796ff

## Blocking
- solutions.md:265 (L2-09 Kaava) — A: "energian säilyminen $E_\text{p} = E_\text{b}$" names the wrong principle. Equal energies from 12 kg of petrol and the unknown mass of wood is the task's condition ("jotta vapautuisi yhtä paljon energiaa"), not energy conservation: conservation relates one system's energy before and after, not two separate fuels. Labelling it so teaches a wrong idea of what the law says, and the Periaate on the same task states the condition correctly. Fix: "$E = Hm$ kummallekin polttoaineelle, ja tehtävän ehdon mukaan energiat ovat yhtä suuret, $E_\text{p} = E_\text{b}$, joten …".

## Polish
- solutions.md L3-01, L2-05 Sijoitus — the chain substitutes into $\Delta m = E(1/H_1 - 1/H_2)$ but then writes the two masses from a trailing "missä …" clause; substituting the numbers into the bracket first ($120\,\text{MJ} \cdot (1/15 - 1/40{,}6)\,\text{kg/MJ}$) would follow the "substitute into the last symbolic form" rule (C).
- Earlier items outside this delta (L2-08 104 MJ figures, L1-06 distractor, L2-09 axis wording) are still open.

## Checked
- Hash 2192d48e7a0796ff at the start and the end; solutions.md and three exercises.json captions changed since base 5b3ca4f; answers.py untouched.
- exercises.json: "Esimerkkiaineisto:" removed from three captions (teacher's approval 2026-11-15/16; CLAUDE.md "no provenance badge on example data"). The data are realistic: wood 14,7 MJ/kg at 20 % and 10,4 MJ/kg at 40 % moisture agree with the lesson's 13–15 and the drop with moisture; none is presented as a named statistic.
- Every other rewritten Kaava starts from $\eta = E_\text{hyöty}/E_\text{sisään}$, $E = Hm$, $E = em$, $P = E/t$ and combines symbolically ($\eta H m$, $E_\text{hyöty}/(\eta H)$, $\eta H m / t$, $H \cdot m/t$, $em/12\,\text{MJ}$) before one substitution; each combination is algebraically right.
- L2-01: $E = E_\text{merkintä} \cdot m/m_\text{merkintä}$ keeps the food-label meaning (energy available to the body), as the guardrail requires.
- Recomputed every numeric answer in one script with my own formulas: 86, 96 MJ; 3,1·10⁵ MJ; 4000 MJ; 0,96 MJ; 15 kg; 40 kWh; 13,35 MJ; 480 kJ; 42 kg; 578 MJ; 4,47 kg; 5,63 kg; 18,4 kW; 34,4 kg; 5,04 kg; 3,6; 35 MW; 3313 kg; 937 kg: all agree with answers.py and exercises.json within tolerance.
- L3-04 and L3-05 reworked Sijoitus (one formula per fuel) give the same 3313, 1310, 4024 kg and 3429, 2491, 985, 2824 kg as before.
