VERDICT: PASS
CONTENT-HASH: ac4d1750f63b5dec
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 45f15bceac913270 base 90f2071

## Blocking

## Polish
- solutions.md (fy2-1-L2-07), Kaava — "$E_\text{alussa} = E_\text{lopussa}$, eli $E_\text{lämpö} = E_\text{sähkö} - E_\text{valo}$" goes from the general law straight to the solved form. The balance $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$ appears only in the Periaate. — Fix: "…, eli $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$, joten $E_\text{lämpö} = E_\text{sähkö} - E_\text{valo}$ kummallekin lampulle …".

## Checked
- Every rewritten Kaava line (L1-01, L1-02, L1-03, L1-05, L2-01…L2-08, L3-01, L3-05) now starts from $E_\text{alussa} = E_\text{lopussa}$, or, in L3-05, from $E_\text{tulo} = E_\text{ulos} + E_\text{lämpö}$ at each step. Each one then solves for the unknown in symbols, and each balance holds the energy forms its Periaate names.
- L2-02: the added condition (at rest at the top, $E_\text{p} = 0$ at the bottom) is correct. L2-05: share = part / whole, and the whole is the sum. L2-06: "laite ei voi tuottaa energiaa tyhjästä" is the right principle for the perpetual-motion claim.
- L1-10: $H = E/m$, so $E = Hm$. The hint names MAFY's table *Polttoaineiden LHV-lämpöarvoja*. The LHV is the right value for an engine, and $43{,}4 \cdot 2{,}0 = 86{,}8\,\text{MJ}$. Dry wood at $16{,}2\,\text{MJ/kg}$ in the Järkevyys and air-dry firewood at 15 MJ/kg in fy2-5 are different kinds of wood, a P9-level difference.
- I recomputed in one script: 43 kJ, 39,2 %, 218 GJ, 4,86 MJ, 14,3 % and 86,8 MJ, and the diff's other substitutions (239, 200, 510, 850 J; 3,0 kJ; 360 J; 29 000 J; 60,0 %; 20 J; 130 J; more than 70 PJ). All agree.
- answers.py matches all 17 numeric answers in exercises.json, each inside its tolerance. No answer, unit or tolerance changed.
- The paragraph splits in L1-04, L1-08, L1-09, L3-03, L3-04 and L3-05 change no claim or number.
- Hash ac4d1750f63b5dec at the start and at the end.
