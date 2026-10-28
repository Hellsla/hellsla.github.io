VERDICT: PASS
CONTENT-HASH: d4871eb2be378354

Delta review over the audit's PASS (106a6f42772f0a62): check-c2 added from the exit-ticket "lämpöä kivessä" question, exit ticket 3 → 2, titles renumbered.

## Blocking
- none
## Polish
- inquiry.json:366 — "Se mittaa hiukkasten keskimääräistä liike-energiaa" (said here of a stone and water) is a fair simplification, but lesson.md says it more carefully (lämpöliikkeen voimakkuus; mean kinetic energy in a gas). Suggest "Se kuvaa hiukkasten lämpöliikkeen voimakkuutta" to match the guardrail.
## Checked
- check-c2 (kuuma kivi veteen): exactly one correct option; "kivessä on paljon lämpöä", "lämpö on kadonnut" and "lämpötilaa siirtyy" are each wrong, and their feedback keeps heat (energy in transfer) and internal energy apart, as the guardrail requires.
- Net direction (hot → cold) and energy conservation stated correctly; no claim that a body holds heat.
- exit-ticket.json now 2 questions and the exit stage says "Lopuksi kaksi"; the removed question is the one converted into check-c2.
- later tarkista titles renumbered 3. and 4.; LaTeX unit conversions in inquiry.json are mathematically unchanged.
