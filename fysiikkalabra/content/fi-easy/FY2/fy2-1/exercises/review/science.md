VERDICT: PASS
CONTENT-HASH: ac4d1750f63b5dec
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 45f15bceac913270 base 90f2071

## Blocking

## Polish
- solutions.md (fy2-1-L2-07), Kaava: "$E_\text{alussa} = E_\text{lopussa}$, eli $E_\text{lämpö} = E_\text{sähkö} - E_\text{valo}$" jumps from the general law to the solved form. The balance it skips, $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$, appears only in the Periaate. Fix: "…, eli $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$, joten $E_\text{lämpö} = E_\text{sähkö} - E_\text{valo}$ kummallekin lampulle …".
- solutions.md (fy2-1-L1-10), Järkevyys: dry wood is now "$16{,}2\,\text{MJ/kg}$" from MAFY, while fy2-5 uses $15\,\text{MJ/kg}$ for air-dry firewood. Both values are correct for their kind of wood (P9 allows a small difference like this), and the word "kuivaan" here keeps them apart. Nothing needs to change.

## Checked
- Every rewritten Kaava line (L1-01, L1-02, L1-03, L1-05, L2-01…L2-08, L3-01, L3-05) now starts from $E_\text{alussa} = E_\text{lopussa}$ (or, at each step, from $E_\text{tulo} = E_\text{ulos} + E_\text{lämpö}$) and then solves for the unknown in symbols. Each balance has the energy forms its Periaate names.
- L2-02: the added condition (at rest at the top, $E_\text{p} = 0$ at the bottom) is right, and the solution correctly says the formula is already solved for $E_\text{p}$.
- L2-05: share = part / whole, and the whole is the sum. This is a correct basic definition, and the order of the formulas is fine.
- L2-06: "laite ei voi tuottaa energiaa tyhjästä" is a correct statement of the conservation principle for the perpetual-motion claim, and $E_\text{luotu} = 100\,\text{J} - 80\,\text{J} = 20\,\text{J}$ is unchanged.
- L1-10: $H = E/m$, so $E = Hm$, is the right definition. The hint now names MAFY's table *Polttoaineiden LHV-lämpöarvoja*. The LHV is the right value for an engine, and it agrees with answers.py (43,4 MJ/kg).
- I recomputed every substitution in the diff: 239, 200, 510, 850 J; 3,0 kJ; 360 J; 29 000 J; 60,0 %; 20 J; 43 kJ; 14,3 %; 130 J; 39,2 %; 218 GJ; more than 70 PJ; 4,86 MJ and 86 %. All agree with the solutions.
- answers.py, run with `python -I`, matches all 17 numeric answers in exercises.json, and each answer is inside its tolerance. No answer, unit or tolerance changed.
- The paragraph splits in L1-04, L1-08, L1-09, L3-03, L3-04 and L3-05 change no claim or number.
- Hash ac4d1750f63b5dec at the start and at the end.
