VERDICT: FAIL
CONTENT-HASH: a099757b3027bdc5

## Blocking
- A (quantitative and internal consistency): content/fi/FY8/fy8-7/inquiry.json:33 and :37. The prompt (line 28) now uses the He-Ne neon atom at $633\,\text{nm}$, but the feedback for the correct option and for distractor 2 still says "aallonpituutta $650\,\text{nm}$ vastaa energia … $\approx 1{,}91\,\text{eV}$". For the stated 633 nm, hc/λ = 1,96 eV. The student is shown a number for a wavelength that is not in the task. The same stale text is in content/en/FY8/fy8-7/inquiry.json:33, :37 and content/fi-easy/FY8/fy8-7/inquiry.json:33, :37. Fix: in all three languages, change it to "$633\,\text{nm}$ … $\approx 1{,}96\,\text{eV}$" (lesson-answers.py `kert-633-eV` already gives 1,96 eV).

## Polish
- lessons/FY8/fy8-7/lesson-answers.py:37–38: the comment and `kert-656-eV` (hydrogen 3 → 2) no longer belong to the Kertaa item. Remove them, or relabel them if another place uses them.

## Checked
- The prompt's physics: He-Ne lasers emit red light at 633 nm from neon, and an atomic level transition is the right model (round 1 finding resolved).
- I recomputed hc/λ with h = 6,626·10⁻³⁴ Js, c = 2,998·10⁸ m/s and e = 1,602·10⁻¹⁹ C: 633 nm gives 1,959 eV and 650 nm gives 1,908 eV. lesson-answers.py `kert-633-eV` agrees.
- Exactly one correct option. "Energia on tasojen erotus, väri määräytyy tasoista" is right.
- Distractor 2 ("ylemmän tason energia") is wrong, and its feedback reasons correctly except for the stale number.
- Distractor 3: spontaneous emission goes in random directions. The revised last sentence ("atomien itsestään lähettämä valo leviää kaikkialle") fits the prompt, so the round 1 polish item is resolved.
- Distractor 4: spontaneous decay in about 10⁻⁸ s is correct for an allowed transition, and the feedback is right.
- en and fi-easy prompts match the Finnish change.
