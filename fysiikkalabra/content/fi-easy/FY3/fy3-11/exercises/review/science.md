VERDICT: PASS
CONTENT-HASH: 0fc397895a2ab582

## Blocking
(none)

## Polish
- L2-04 solution: '480 kW on kolmen numeron arvo, koska loppunolla on merkitsevä' is a convention (a trailing zero without a decimal point is ambiguous); 720 kW is unaffected.

## Checked
- Delta: prefix and caption suffix removals in L2-05, L3-02, L3-xx compared by script: no number or symbol changed.
- Solution wording (hukkalämpö siirtyy ympäristöön; paragraph splits) physically right; L2-04 recomputed: P_o = 480/0,400 = 1200 kW, waste 720 kW.
- New L2-10 recomputed: Q1 = eps W = 4,0*2,5 = 10 kWh; Q2 = (eps-1) W = 7,5 kWh (answer 7,5, 2 % tolerance); balance Q2 + W = Q1.
- Motiva PDF fetched: quotes in the solution (COP, 'mitä pienempi lämpötilaero', -25 C gives COP 1-2, yearly 1,4-3, 'lämpökerroin 3,0 ... 300 prosenttia') are in the source.
- Physics of a)-d): COP is not an efficiency, may exceed 1, energy conserved, COP falls with temperature difference and tends to 1; no scope breach.
- Hash same at start and end.
