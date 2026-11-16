VERDICT: PASS
CONTENT-HASH: c0842f06ba77912b
Mode: delta (added aineisto task fy8-9-L2-08)

## Blocking
(none)

## Polish
- exercises/solutions.md:176 — "Caesium-137 disappears from the environment only by radioactive decay" holds for the total amount, but in a given soil layer or food the amount also falls by migration (ecological half-life) — tie it to the task's assumption: "In this model caesium is removed only by decay, as the task says".
- exercises/solutions.md:183 — two figures are justified by "about 30 a", while the task and Given say to take 30 a as exact — give one reason (e.g. the real half-life 30.08 a gives 39.8 %, so two figures are enough).

## Checked
- Recomputed: (1/2)^(40/30) = 0.3969 → 39.7 % → 40 %; answers.py 39.685; relative tolerance 0.03 gives 38.8–41.2 %, which covers 39–41 and 39.7. With T½ = 30.08 a: 39.8 %.
- Decay law N = N0(1/2)^(t/T½) applied with the condition stated in the task (physical decay only); t = 40 a, no conversion needed, correct.
- Part a) source facts (Chernobyl 1986, atmospheric weapons tests 1950s–60s, pre/post-1986 Cs-137, mushrooms still contain Chernobyl caesium, amounts decreasing) match the verified list.
- Table 9.2 values (Helsinki 14–413, 12; Tampere 3.5–670, 13; Rovaniemi 76, 2) match the verified data.
- Part c) is marked as the solution's own reasoning; only the Tampere fallout fact is attributed; rain, soil and mycelium-depth reasons are sound.
- Part d): ratio 670/3.5 = 191 correct; sampling, species, place and counting uncertainty are valid reasons.
- Reasonableness bounds 25–50 % between one and two half-lives correct.
- Hash c0842f06ba77912b at start and end.
