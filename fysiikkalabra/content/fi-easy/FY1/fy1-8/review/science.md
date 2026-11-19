VERDICT: PASS
CONTENT-HASH: 01607ed274d08372
Mode: delta (three new `pysahdy` boxes, worked-example knowns split into two paragraphs, inquiry.json presentation only)

## Blocking
- none

## Polish
- content/fi-easy/FY1/fy1-8/lesson.md:16 — the hypothesis box answers "Kelpaa" on testability alone, but the lesson and glossary define a hypothesis as *perusteltu ja* testattava; the given statement has no reason — add one to the prompt ("Auto liikkuu vakionopeudella, joten jos matka kaksinkertaistuu, kulkuaika kaksinkertaistuu.") or say in the answer that its reason is the constant-speed model.

## Checked
- Box 1 (hypothesis): the doubling prediction gives a measurable result that a measurement could show wrong; the falsifiability reasoning matches the theory paragraph above it.
- Box 2 (two variables): distance and batteries changed together, so neither can be named as the cause. Correct, and it matches the text's distance-and-batteries example and the "vain muutettava muuttuja vaihtuu" rule.
- Box 3 (minimum time): t ≥ Δt/ε_max = 0,2 s / 0,020 = 10 s (recomputed: 10,0). Symbolic form first, the same as the display formula ε = Δt/t, t ≥ Δt/ε_max. It is exact, so the "vähintään" rounding question does not arise.
- Box 3 uses the time's relative uncertainty with hand timing Δt = 0,2 s, which matches the guardrail value and the epävarmuus figure (ε = 0,2 s/t).
- Worked example: the knowns and the question are now separate paragraphs. The numbers did not change (v = 0,42 m/s, Δt = 0,2 s, ε_max = 0,050).
- inquiry.json: only presentation changed, so no physics content changed.
- Hash checked at start and end with `--lang fi-easy`: 01607ed274d08372 both times.
