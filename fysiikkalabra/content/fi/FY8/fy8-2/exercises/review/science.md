VERDICT: FAIL
CONTENT-HASH: ca5e96a8a17d1b90

## Blocking
- exercises.json:451 (fy8-2-L3-06), solutions.md:230–240 — **A**: the task assumes that the violet and green lines "syntyvät siirtymistä kahdelta eri ylemmältä energiatilalta samalle alemmalle tilalle". The figure, though, shows mercury's real lines (figures.py MERCURY: 405, 436, 546 nm). In mercury all three of these lines come from the same upper state, 7³S₁, and go to three different lower states, 6³P₀, 6³P₁ and 6³P₂. In this chapter's L2-05 the student identifies exactly this lamp as mercury, so the task teaches a level structure that the drawn spectrum contradicts. The Järkevyys line, "such a transition would be in the infrared, about 1570 nm", then describes an upper-to-upper transition that does not exist here. The number itself is right: 6³P₂ − 6³P₀ = 5,461 − 4,667 = 0,79 eV. — Fix: reverse the assumption to "syntyvät siirtymistä samalta ylemmältä energiatilalta kahdelle eri alemmalle tilalle". In b), ask for the energy difference of the two lower states. Rework c), the Periaate, the Kaava (E_y cancels) and the Mallivastaus to match. The answer stays 0,79 eV. Also drop or reword the infrared claim.

## Polish
- solutions.md:223 (L2-09) — "energian toinen desimaali on varma" does not hold. A misreading of ±3 nm moves E by about ±0,02 eV (433 nm gives 2,86 eV, 439 nm gives 2,82 eV). — Say the second decimal is uncertain by about 0,02 eV. That error is still inside the 3 % tolerance.
- solutions.md:223 — "Sininen viiva on viiva, joka on lähimpänä arvoa 436 nm" is circular: the student does not yet know 436 nm. — Describe the reading only from the scale: 14 nm to the left of the 450 nm label.
- solutions.md:238 — the reason given for two significant figures is garbled. — Give it as "a ±3 nm reading changes ΔE by up to about 0,04 eV".

## Checked
- Delta scope: only the two added exercises were judged: fy8-2-L2-09 and L3-06.
- L2-09: hc/(436 nm) = 2,844 eV, so the answer 2,84 is right and the 3 % tolerance fits the reading uncertainty. The figure's line is at 436 nm on a scale with 10 nm divisions ✓.
- L3-06 numbers: E(405 nm) = 3,062 eV and E(546 nm) = 2,271 eV, so ΔE = 0,791 eV and the answer 0,79 is right. A worst-case misreading of ±3 nm on each line gives 0,756–0,826 eV, which is within the 5 % tolerance ✓.
- answers.py lines 311–312 compute these values from the readings at 405, 436 and 546 nm ✓.
- I checked the mercury levels against standard values (7³S₁ 7,730 eV; 6³P₀,₁,₂ 4,667 / 4,886 / 5,461 eV). They reproduce the 405, 436 and 546 nm lines.
- I recomputed every answer in one independent Python script.
- The hash was ca5e96a8a17d1b90 at the start and at the end.
