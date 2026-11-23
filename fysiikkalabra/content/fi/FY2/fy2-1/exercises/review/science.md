VERDICT: PASS
CONTENT-HASH: 488edba2bc8932a7
SCOPE: delta md-paragraphs,numbers,typography,wording from 575f3df5f4e893ad base 29cd249

## Blocking

## Polish
- solutions.md L2-07 Kaava — "$E_\text{alussa} = E_\text{lopussa}$, eli $E_\text{lämpö} = E_\text{sähkö} - E_\text{valo}$" jumps straight to the solved form; the balance $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$ is only in Periaate. Add "eli $E_\text{sähkö} = E_\text{valo} + E_\text{lämpö}$, joten" as in the other solutions (C, not wrong).
- Earlier open items outside this delta (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3, L1-10 table name in hint vs solution) were not part of this diff.

## Checked
- Hash 488edba2bc8932a7 at the start and the end; only solutions.md changed since base 29cd249 (exercises.json and answers.py untouched).
- Every rewritten Kaava now opens from $E_\text{alussa} = E_\text{lopussa}$ (or $H = E/m$ in L1-10, the share definition in L2-05, the per-step balance $E_\text{tulo} = E_\text{ulos} + E_\text{lämpö}$ in L3-05) and then gives the situation's balance; each balance matches the energy forms named in its Periaate.
- L2-02: the added condition "yläpäässä levossa, alapäässä potentiaalienergia nolla" is what $E_\text{p} = E_\text{k} + E_\text{lämpö}$ needs.
- L2-06: "laite ei voi tuottaa energiaa tyhjästä" is the right principle for the perpetual-motion claim; $E_\text{luotu} = 100\,\text{J} - 80\,\text{J} = 20\,\text{J}$.
- L3-01: $E_\text{A} = E_\text{p} + E_\text{k} + E_\text{lämpö}$ at each point is correct (E_A = 900 J at rest), giving 20 J and 150 J, difference 130 J.
- Recomputed every numeric answer in one script with my own balances: 50, 239, 200, 510 J; 86,8 MJ; 850 J; 3,0 kJ; 360 J; 29 000 J; 60 %; 20 J; 43 kJ; 14,3 %; 130 J; 0,20 J; 39,2 %; 4,86 MJ: all agree with answers.py and exercises.json, units and tolerances unchanged.
- The md-paragraph splits (L1-04, L1-08, L1-09, L3-03, L3-04, L3-05) change no physics or number.
