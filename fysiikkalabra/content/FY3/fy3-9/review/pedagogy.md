VERDICT: FAIL
CONTENT-HASH: 23ee674947cc5bdb

## Blocking
- solutions.md, `## fy3-9-L2-03` (Kuvaajan lukeminen / Sijoitus) — the graph task's key step is a jump a student who could not do it cannot follow: "Suora kulkee pisteen (0,100; 201 kPa) kautta" appears from nowhere, and 201 is neither a data point (pV values are 1980–2030) nor derived. The solution never shows how the fitted line is chosen, and the answer 2,01 J follows from a number the student cannot reproduce. Fix: compute the six pV (or p/(1/V)) values in the solution, state that the through-origin line is placed so the points lie evenly on both sides (or take the mean of the six, about 2000 kPa·ml), and read the slope from that line (e.g. "mean ≈ 2,00 J"); then the answer 2,0 J follows from visible numbers.

## Polish
- solutions.md, L2-04 Vastaus — muddled: it names ΔT = 90 K as limiting, then says the direct difference formula gives 3 figures, and the Sijoitus shows "890,0 m³" (false precision). Say once: ΔV = V₁(T₂−T₁)/T₁ = 2800·90/283,15 ≈ 890 m³, two figures from 2800 m³ and 90 K.
- solutions.md, L3-02 and L3-03 Vastaus/Muunnokset — the sum/difference significant-figure reasoning ("yksiköiden tarkkuus", "kymmenesosasenttimetri") is dense for a 16-year-old; one short sentence each would carry it.
- solutions.md, L2-03 Kaava — "k = Δp/Δ(1/V) = p/(1/V)" is never used afterwards; either use it (slope between two far-apart points on the line) or drop it.
- The unit `\textsf{l}` looks like a digit 1 or a bar at 390 px ("0,80 l", "6,8 l"); consider "L" or "litraa" in the first occurrences. Shared style, not a lesson fix.
- exp-2 question: the 1/293 vs 1/273 choice is subtle and "γ ei ole vakio" is a heavy claim to land in one feedback; fine for a stronger group, optional there.

## Checked
- Worked example at 390 px: seven stages, one step each, bold lead-ins, symbols solved before numbers, conversion stage says none needed, sig figs justified, check recomputes pV; a student can follow it.
- Opened L2-01 solution at 390 px: all seven steps present, wraps cleanly, nothing clipped.
- Read all 14 solutions (12 exercises, siirto, check-2): each has Annettu, Periaate with reason, symbolic Kaava, Muunnokset, Sijoitus with units, Vastaus with figures justified, Järkevyys; Periaate explains why Boylen/isobaric/isochoric applies.
- check-2 and siirto numeric solutions follow step by step; check-2 explains the graph reading.
- Celsius/kelvin and gauge/absolute traps are explained in the solutions (L1-04, L2-02, L3-02), not just named.
- Levels: 5/4/3, none repeats the example (siirto is the same law, different context).
- Exit ticket tests the core idea and the kelvin trap; Finnish reads correctly in the parts reviewed.
- Learning path, prediction/experiment design and syringe-data item are sound; opening question answered in Ydinajatus and reflect.
- Hash unchanged at the end.
