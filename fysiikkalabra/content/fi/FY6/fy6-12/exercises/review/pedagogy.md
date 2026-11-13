VERDICT: PASS
CONTENT-HASH: 9f84f4124a537fa5
SCOPE: delta added-exercise from 4703625fe3ccea47 base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- exercises.json (fy6-12-L2-09) — the question is not the last sentence ("Kuinka suuri on elektronin nopeus ...? Lue tarvittavat arvot ... ja vastaa yksikössä m/s."). Reorder: "Lue tarvittavat arvot kuvaajasta ja vastaa yksikössä $\text{m/s}$. Kuinka suuri on elektronin nopeus positiivisella levyllä?"
- solutions.md (fy6-12-L2-09, Järkevyys) — the comparison "Jännite 3,0 kV antaisi nopeuden 3,2·10^7 m/s" is arbitrary and the second half ("pienempi jännite antaa pienemmän nopeuden") is trivial; replace with one line: kinetic energy 200 eV, v is 2,8 % of c, so the non-relativistic formula is fine.

## Checked
- Text only (no render) of the added fy6-12-L2-09.
- Recomputed: U = 250 V - 50 V = 200 V; v = sqrt(2 · 1,602·10^-19 · 200 : 9,109·10^-31) = 8,387·10^6 m/s; matches answer 8,39·10^6 m/s and 2 % tolerance.
- Level 2: read two values from the graph, form the potential difference, energy conservation, solve for v; no new idea, each step explained in the solution.
- Figure ex-vgraph: a straight line from the origin to (5,0 cm; 250 V), grid 1 cm and 50 V; gives both values needed, its description matches and does not state U or the answer.
- Solution reads the graph before the formula, explains why the electron gains kinetic energy (moves to higher potential, charge -e).
- Fits the set: L1-05 reads the same kind of graph but needs one step; L2-03/L2-04 use eU = ½mv² without a graph; this joins the two; no repeat of the worked example.
- Finnish and units correct.
- Hash unchanged at the start and end.
