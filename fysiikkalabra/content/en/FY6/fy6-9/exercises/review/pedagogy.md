VERDICT: PASS
CONTENT-HASH: 30bb671b683987a1
SCOPE: delta added-exercise from 51f6a10c66298771 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- The task says "Assume that the energy is the nominal voltage times the charge", which gives the model; fine for level 2, and it keeps the nominal-voltage simplification explicit.

## Checked
- Level 2: charge from a stepped current graph (three rectangles), then W = UQ in Wh; builds on L1-05 (charge from a graph) and L1-03 (energy from capacity) without repeating them.
- Figure gives 2.0 A for 0-1.0 h, 1.5 A for 1.0-3.0 h and 0.5 A for 3.0-4.0 h on 0.5 gridlines; description matches and does not give the charge or energy.
- Situation first, question last; laptop battery is a recognisable context; the unit Wh is requested.
- Solution complete: given, principle, reading, symbolic formula, durations, substitution (5.5 Ah, 61.05 Wh), significant figures and a two-part reasonableness check.
- Arithmetic verified: 2.0 + 3.0 + 0.5 = 5.5 Ah; 11.1 * 5.5 = 61.05 Wh; the 2 % tolerance fits a read value.
- Fit: the set gains a combined charge-to-energy graph task at level 2, in the lesson's scope (Ah, Wh, charging).
