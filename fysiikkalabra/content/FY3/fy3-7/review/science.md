VERDICT: PASS
CONTENT-HASH: a75fce0322a75a90

## Blocking

## Polish
- exercises.json:22, solutions.md:23 (L1-03) — 45 kg/m² (about 5 cm) is a lot for "syksyn ensimmäinen pakkasyö" — say "kova pakkasyö" or use 15–20 kg/m² (carried over).
- solutions.md:87 (L3-02) — "Muutama kauhallinen" understates the result: one ladle already gives 27 K — write "Jo yksi kauhallinen …" (carried over).
- lesson.md phase-diagram SVG — the liquid/gas fill boundary runs on horizontally from the end of the curve (430.5,128) to the edge, which suggests a boundary above the critical point. Mark the critical point or blend the fills (taste).
- lesson.md phase-diagram SVG — the vaporisation curve leaves the triple point with zero slope (carried over, taste).

## Checked
- Conversion since the last passed version (408e1ea): every number in solutions.md is the same, compared section by section with the markup removed. The only new digits are subscripts. The formulas in L3-01, L3-02 and L3-03 are unchanged.
- The inquiry.json and exit-ticket.json diffs only add $…$ delimiters and replace lesson ids with chapter names. No number, option, `correct` flag or feedback changed. sim.js, sim-spec.md, answers.py and exercises.json are unchanged.
- All 12 answers recomputed in one script, and they match. The Järkevyys figures (2,7 kg, 19 kJ, 90 %, 87 %, 21 °C, 2,45/2,67 MJ/kg, 60 W) are correct.
- Inquiry numbers: pr-lampo 209,5 kJ; pred-1 1130/565 s; pred-2 83,5/565 and 167/1130 s (ratio 6,8); virhe 66,8 kJ; siirto 188 W (27,8; 11 300); check-2 0,597 kg (0,677; 4,04); check-3 ×9,6.
- Worked example: solved symbolically first, gives 2,34 MJ/kg, and the loss argument is correct.
- Heating-curve SVG: the slopes are 1,97 : 0,98 : 1,96, which matches c = 2100 : 4190 : 2000. The Q labels are on the correct plateaus, and the aria-label says the plateaus are not to scale.
- Phase-diagram SVG: the melting line tilts left (water), and sublimation is steeper at the triple point. The ilmanpaine and vuori points lie on the curve, with vuori lower in p and T. The region labels are in the correct regions.
- Experiments: exp-1 locks m and varies P; exp-2 locks P and varies m. simState carries tMelt and tBoil. The speed select changes only the pace (Q = Pt in simulated t).
- The hash was the same at the start and at the end.
