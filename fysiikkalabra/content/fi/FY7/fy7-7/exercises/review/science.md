VERDICT: PASS
CONTENT-HASH: c2299a6720da2db8
ROUND: 1

## Blocking

## Polish
- solutions.md:215 (L1-09) — "kahden peräkkäisen samaan suuntaan tapahtuvan nollakohdan välistä" is awkward — "kahden peräkkäisen nollakohdan välistä, joissa käyrä on nousemassa".

## Checked
- New task L1-09 only (additions only since b032dcb83~1). Checked from the text, figures.py and the catalog descriptions; I did not render the graphs.
- Recomputed: e₀ = 5,0 V · √2 = 7,07 V ≈ 7,1 V, T = 1/40 Hz = 25 ms, so there are 4 periods in 0–100 ms. figures.py draws peak·sin(2πt/T) from 0 rising, which matches e = e₀ sin(2πft) and "nolla ja kasvamassa".
- Options: 2 × 2 (peak 5,0 or 7,1 V; T 25 or 40 ms), so every feature appears in two options and the right one cannot be found by its form. Distractor C is the chapter's warned mistake (effective value drawn as the peak).
- Each option figure has a full description (axes, ticks, peak and when, zero crossings, period, number of periods, minimum). The values agree with the drawn curves (6,25 ms and 10 ms peaks; 2,5 periods for T = 40 ms).
- Feedback of every option is right; T = 1 : f and the √2 factor are the lesson's notation (U = U₀ : √2, e₀).
- answers.py: all 19 numeric answers agree with exercises.json; the L1-09 comment is right.
- Hash c2299a6720da2db8 at start and end.
