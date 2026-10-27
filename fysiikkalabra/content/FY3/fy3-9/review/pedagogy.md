VERDICT: PASS
CONTENT-HASH: 35f7cbd9c952c5d4

## Blocking

## Polish
- solutions.md, L2-04 Vastaus/Sijoitus — still muddled: it names ΔT = 90 K as limiting, then says the direct formula gives three figures, and Sijoitus shows "890,0 m³" (false precision). Say once: ΔV = V₁(T₂−T₁)/T₁ = 2800·90/283,15 ≈ 890 m³, two figures from 2800 m³ and 90 K.
- solutions.md, L2-03 Kaava — "k = Δp/Δ(1/V) = p/(1/V)" is never used afterwards (the solution uses p/(1/V) only); drop the Δ form or use it.
- solutions.md, L2-02, L3-02, L3-03 Vastaus — the sum/difference figure reasoning ("yksiköiden tarkkuus", "kymmenesosasenttimetri") is dense for a 16-year-old; one plain sentence each ("erotuksessa desimaalien määrä ratkaisee") would carry it.
- The unit \textsf{l} reads like a 1 or a bar at 390 px ("0,80 l", "6,8 l"); "L" or "litraa" at first occurrences. Shared style, not a lesson fix.
- inquiry.json, exp-2 question — the 1/293 vs 1/273 choice and "γ ei ole vakio" are heavy for one feedback; optional for a stronger group.

## Checked
- Round-1 Blocking (L2-03 graph jump) is fixed: the six pV values (2030 … 1980) are computed, the mean 12 013/6 ≈ 2000 is stated, the line through (0,100; 200) is checked against the point (0,100; 203), and the slope is read from the line, not a point. I recomputed the pV values and sum.
- Worked example at 390 px: seven stages, one step each, bold lead-ins, symbols solved before numbers, "no conversion needed" stated, figures justified, check recomputes pV; a student can follow it.
- Read all 14 solutions (12 exercises, siirto, check-2) as rendered in the build (each behind its own Näytä ratkaisu): Annettu, Kysytty, Periaate with reason, symbolic Kaava, Muunnokset, Sijoitus with units, Vastaus with figures, Järkevyys; nothing skipped.
- Tasks that ask for a justification (L3-01 diver, L3-02 gauge pressure, L3-03 pump) answer it in the solution (Järkevyys or Periaate).
- check-2 explains how the slope is used and which datum limits the figures; siirto follows step by step.
- Celsius/kelvin and gauge/absolute traps are explained, not only named (L1-04, L2-02, L3-02).
- Levels 5/4/3; none repeats the example; exit ticket tests the core idea and the kelvin trap.
- Learning path, predictions/experiments, syringe-data item sound; opening question answered in Ydinajatus and reflect.
- Hash unchanged at the end.
