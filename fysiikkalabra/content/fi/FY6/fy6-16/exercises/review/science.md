VERDICT: PASS
CONTENT-HASH: 7de922d922addd67
Round: 2, science, mode full. Scope: fy6-16-L2-08, redesigned in commit 57a66480d from an order-of-magnitude task into a computed-value choice (5,1 / 11 / 13 / 15 h). The rest of the set is unchanged. Checked from text only, no renders.

## Blocking

## Polish
- fy6-16/exercises/exercises.json (L2-08 choices) — the options rise in value and the correct 15 h comes last as the largest. A student who knows only "häviöt pidentävät" could pick it without computing. It is still physics-correct, so this is for pedagogy to decide: it could shuffle the order (e.g. 13 / 15 / 5,1 / 11 h) if the answer-position check allows.

## Checked
- I recomputed every option: 5,115 h from P = 3UI used for a single-phase socket, 11,09 h from multiplying by η, 13,04 h with η left out, and 15,35 h, which is the correct t = W_akku : (ηP). Each option's feedback names its own error and is right.
- The chapter's warned mistake (×η instead of ÷η) is now a distractor, so the round-1 polish item is resolved. The 3UI and lossless slips come from the lesson's own formulas.
- The stem now asks "Kuinka kauan lataus kestää?". It states the constant-power assumption the lesson requires, and its data are realistic: an 8 A cable and 85 % efficiency.
- Solution: complete, with a real reasonableness check (≈1,6 kWh per hour). The 11 h chain `0,85 · 24 kWh : 1,84 kW` is evaluated left to right and is unambiguous. The notation W_akku, η and P = UI is the lesson's.
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
- Inline width (text estimate): all rows are under about 230 px.
