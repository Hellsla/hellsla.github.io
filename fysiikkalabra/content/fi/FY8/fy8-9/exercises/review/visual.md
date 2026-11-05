VERDICT: PASS
CONTENT-HASH: be3f59b3a9eff3ee
Round: 3 (delta)

## Blocking
(none)

Delta: only the Järkevyys arrows of 9-7 changed (`\to` to `\!\to\!`); it reads well, nothing else changed.

## Polish
- [Minor] solutions.md 9-7 Järkevyys — the tight arrows sit close to the percent signs but stay clearly visible and do not touch the numbers; leave.
- [Minor] exercises.json L2-07 (9-15) — unit label beside the answer field is plain "1/s" while the answer shows $\tfrac{1}{\text{s}}$; project-wide field convention — leave.
- [Minor] solutions.md L2-06 (9-14) — the Järkevyys block now says "a) Tulos ... sopii taulukkoon", followed by a separate bold "Selitys kohtaan b)" block; fixed as asked in round 1. A plain "Järkevyys:" without the "a)" prefix would read more naturally.
- [Minor] solutions.md L2-05 (9-13) Vastaus — "noin $\pm 8\,\%$" is the spread of the net count $64$ only ($8/64$ is $12{,}5\,\%$, the effect on $T_{1/2}$ is about $8\,\%$); say "arvion hajonta on noin $8\,\%$" to avoid the reading that the count error is $8\,\%$.
- [Minor] solutions.md L3-05 (9-20) — the $0{,}140\,\tfrac{1}{\text{d}}$ in Sijoitus and $0{,}1398\,\tfrac{1}{\text{d}}$ in Järkevyys are the same value at two roundings; use one.

## Checked
- 1280 px capture fy8-9-open-exercises-1280-7/-8 (9-7 task, Sijoitus, Vastaus, Järkevyys with the arrow chain; 9-8 below it intact). Arrows visible, not touching numbers; no red KaTeX, no clipping.
- Diff (solutions.md only) read; earlier rounds' checks stand. `check_layout.py fy8-9 --site --width 360` ok. Only 1280 px exercise captures exist; 360 px rests on check_layout.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
