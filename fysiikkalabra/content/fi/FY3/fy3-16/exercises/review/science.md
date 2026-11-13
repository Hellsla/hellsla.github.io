VERDICT: PASS
CONTENT-HASH: dc76a60c8222837b
SCOPE: delta added-exercise from 717b427c7d574c97 base 89bcb63b7431

## Blocking
(none)

## Polish
- solutions.md (L2-09) Kuvaajan lukeminen — "Kuvaaja on suora, joten teho on vakio" turns the inference round: the power is given as constant, and the line is straight because the power is constant, the losses small and $c$ constant. Suggest "Teho on vakio ja häviöt pienet, joten kuvaaja on suora."
- solutions.md (L2-09) Järkevyys — "Oletus häviöttömyydestä tekee todellisesta arvosta hieman pienemmän" is unclear; meant: "Jos osa tehosta siirtyy ympäristöön, todellinen $c$ on hieman pienempi kuin laskettu $900\,\text{J/(kg}\cdot\text{K)}$." (Direction right: losses mean less than $Pt$ reaches the block.)
- L2-10 — "teholla 25 W tasaisesti" is a stated model assumption (by $P = UA\Delta T$ the power is somewhat larger while the ice is below 0 °C); fine as given, optional half-sentence in the solution.

## Checked
- Only L1-09, L2-09, L2-10 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $Q = rm = 2260 \cdot 0{,}30 = 678$ kJ → 680 kJ; MAFY 2260 kJ/kg matches docs/mafy-arvot.tsv (VERIFIED); water already at 100 °C stated, so only $Q = rm$; comparison "yli viisi kertaa" (678/126 = 5,4) right.
- L2-09 recomputed: $c = Pt/(m\Delta T) = 400 \cdot 180 / (2{,}0 \cdot 40) = 900$ J/(kg·K); no-loss assumption stated in the task; value matches aluminium, plausible.
- Figure fy3-6/heating-line: line (0 s; 20 °C)–(180 s; 60 °C) on gridline crossings, to scale; description lists the same end points; no slope or $c$ shown.
- L2-10 recomputed: from the graph $Q = 220$ kJ (ice warming 20,2 kJ + melting 200,4 kJ = 220,6 kJ with $c_\text{j} = 2100$, $s = 334$), $t = Q/P = 8800$ s = 2,44 h → 2,4 h; answers.py 2,444.
- Figure fy3-7/melting-curve: break points (20; 0) and (220; 0) on grid crossings; after-melting slope $80\,\text{kJ}/(4{,}19 \cdot 0{,}60) = 31{,}8$ K matches the drawn (300; 31,9); description matches; neither names melting nor gives the time.
- Solutions complete (given/asked, principle with reason, symbolic before numbers, conversions, substitution with units, rounding reason, real checks); energy-balance form $Pt = Q$ as in the brief.
- Units kJ, J/(kg·K), h and tolerances fit; inside FY3 (lämpeneminen, olomuodon muutokset).
- Hash identical at start and end.
