VERDICT: PASS
CONTENT-HASH: 9c8a2363b0045857
Mode: full (translation review against the reviewed Finnish set)

## Blocking
(none)

## Fixed
- exercises.json L2-08 choice 2: Finnish decimal comma '$0{,}2\,\text{MW}$' -> '$0.2\,\text{MW}$'.

## Polish
(none)

## Checked
L2-08 vs content/fi: kind, tolerance, choices order, correct flag, feedback numbers identical. Recomputed v=10 m/s, A=7854 m2, P=0.5*0.40*1.25*7854*1000=1.96 MW (wind 4.9 MW, 47=36^3/10^3 ratio), answer 2 MW; distractors 0.2 MW (v^2) and 20 kW (v) and 90 MW (unconverted) match. Solution equals Finnish. Colon-for-division kept (check_i18n requires it).
