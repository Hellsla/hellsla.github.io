VERDICT: PASS
CONTENT-HASH: 5a0b887af3361976

## Blocking
- None.

## Polish
- None.

## Checked
- Delta review, round 4: the only new change is johtopäätös criterion 3 (inquiry.json:262). The round-3 changes in the diff (ennuste-1 and koe-1 `optional`, the koe-1 hint in kJ, the johtopäätös rewritten for koe-2) are as I checked them before.
- The criterion is fixed. It now asks for the lamp's efficiency (about 5 %, only a small share useful). That is what koe-2's table gives and what the prompt's "annoin laskun luvuilla" leads to. It no longer needs the optional engine experiment.
- The model answer meets all three criteria: η as the useful share, with numbers; time cancels; 5 % with 95 % losses.
- Recomputed: η = 0,05 at P_o = 40 W gives t = 10 s: 400 J and 20 J, and t = 20 s: 800 J and 40 J. Both ratios are 5 % = 2 W : 40 W. This matches sim.js (`lamppu` eta 0.05).
- koe-1 hint: 0,75 · 60 kW · 10 s = 450 kJ of 600 kJ, giving 0,75. Right.
- Physics of the criterion: "pieni osa hyötyä" agrees with the glossary's definition of hyötysuhde and with the lesson's lamp numbers. It states no new claim that would need a condition.
- The content hash was the same at the start and the end.
