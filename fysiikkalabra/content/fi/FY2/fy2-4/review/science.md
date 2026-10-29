VERDICT: PASS
CONTENT-HASH: 1780061339aa30c3

## Blocking

## Polish
- inquiry.json koe-1 / johtopaatos — the engine's 25 % is an input of the model, so "Mitä koe kertoi bensiinimoottorista?" and ennuste-1 are tested only by the model's own constant (the intro and model answer say so). Phrase the criterion as "mitä malli antaa", not what the experiment showed about a real engine.
- inquiry.json ennuste-1 feedback — "tasaisessa maantieajossa noin 25 %" is a typical rounded value (best-point engines reach ~30-35 %); fine at FY2, but name the source or say "esimerkki" if kept.
- inquiry.json virhe / exercises L1-02 — same numbers (8,0 W, 2,4 W); physics right, variety only.

## Checked
- Fig 1 and fig 2 geometry recomputed: input 120/96/16 px, useful 5 % and 30 % of it, loss the rest; ratio 6:1 and equal green arrows hold.
- All lesson-answers.py values recomputed independently (1200 J, 150/450 kJ, 250 W, 1250 W, 15 000 W, 80 %, 20 %, 125 %, 30 %): agree.
- Worked example: E_o 360 kJ, E_a 324 kJ, E_h 36 kJ; symbolic first, 2 s.f. justified.
- Efficiency limit and resistance heater worded per guardrails; patteri check has exactly one correct option, distractors' feedback right.
- ennuste-2: tasaisella teholla aika supistuu; feedback honest that the sim assumes constant eta.
- sim.js: P_a = eta P_o, E = P t, arrows to scale; simState keys match experiments; koe-1/koe-2 locks isolate t; initial values lie in slider ranges.
- Scope: no work, no chain efficiencies, no Carnot; consistent theory, summary, glossary, model box.
