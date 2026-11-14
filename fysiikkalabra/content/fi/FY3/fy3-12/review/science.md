VERDICT: PASS
CONTENT-HASH: 337e48e6aa0cc5a4

## Blocking
- none

## Polish
- content/fi/FY3/fy3-12/lesson.md:155, 225, 233, 266 — the worked example and the U-value paragraph still say "lämpö johtuu" / "läpi johtuu teho" for the same $P = UA\Delta T$. That is a fair simplification (C), because conduction dominates in an insulated wall. To match the new wording, "siirtyy" could replace it there as well (the same holds for en and fi-easy if they have the same lines).

## Checked
- Hash 337e48e6aa0cc5a4 at the start and at the end.
- The diff changes only one word, "johtuva" to "siirtyvä", in the Kaava section and the Tiivistelmä. No numbers or symbols changed.
- The physics is better now. A U-value is a combined thermal transmittance: it includes surface convection, radiation, and conduction and convection in window gaps. So "siirtyvä" is more accurate than "johtuva".
- It agrees with the glossary's U-arvo definition ("lämpötehoa siirtyy neliömetrin läpi") and with the paragraph at line 155.
- The condition "Kaava pätee, kun lämpötilat … pysyvät vakioina" stays next to the formula.
- The en ("conducted" to "transferred") and fi-easy diffs are the same change in the same two places.
