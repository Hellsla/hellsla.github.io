VERDICT: PASS
CONTENT-HASH: b7cca4eb5d885eb4

## Blocking

## Polish
- meta.json:30 — The box says "Ihanteellisessa muuntajassa", but the lesson (lesson.md:147, 155, 215, 302, 349) and the glossary say "Ideaalisessa". The physics is the same. Optional fix for consistent wording: "Ideaalisessa muuntajassa".
- meta.json:34 — siirtohäviö is defined as "Teho" here but as "Energia" in the glossary (E_häviö). The box's own statement about current squared concerns power. Optional fix: "Energia, joka muuttuu … Samassa johdossa häviöteho kasvaa virran neliön mukana."
- meta.json:38 — "Hyvin suuri jännite": the glossary gives a limit of over 1 kV. Optional.

## Checked
- Round-2 delta: meta.json key_concepts. The rest of the lesson is as passed.
- muuntosuhde: the round-1 A and B are fixed. It now reads "N₁ : N₂", matching lesson.md:219 and the glossary. The equality with U₁ : U₂ is now limited to the ideal transformer, which is correct.
- siirtohäviö: the round-1 condition "Samassa johdossa" is now stated, so P = RI² with fixed R applies. Correct.
- muuntaja, suurjännite: unchanged and correct. For the same transmitted power the current and the RI² losses are smaller.
- Rendering at 390 px (own capture of #kasitteet): the box is 358 px wide, KaTeX N₁ : N₂ and U₁ : U₂ render inline, scrollWidth is 390, and nothing overflows.
- The hash was identical at the start and at the end.
