VERDICT: FAIL
CONTENT-HASH: e1dc2c62317a56e9

## Blocking
- inquiry.json:48-49 (Kertaa, option "$6{,}4\cdot10^{-4}\,\text{m}^3$") — A: the feedback says this comes from using the area conversion $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$, but $64 \cdot 10^{-4}\,\text{m}^3 = 6{,}4\cdot10^{-3}\,\text{m}^3$, not $6{,}4\cdot10^{-4}$. The option's number does not come from the mistake its feedback names. A student who made that mistake finds no matching option. — Fix: make the option "$6{,}4\cdot10^{-3}\,\text{m}^3$" and keep the feedback. Correct the mistakes comment in lessons/FY1/fy1-7/lesson-answers.py:7 to match.

## Polish
- inquiry.json:26 — the title "Kertaa: suoraan verrannollisuus" no longer matches the item, which now asks for a volume and a unit conversion; maybe "Kertaa: tilavuus ja yksikkömuunnos".

## Checked
- Recomputed $V = (4{,}0\cdot10^{-2}\,\text{m})^3 = 6{,}4\cdot10^{-5}\,\text{m}^3$ (two figures, like the 4,0 cm side). lesson-answers.py kertaus-V matches.
- The $64\,\text{m}^3$ distractor (the value in cm³ with no conversion) and the $0{,}64\,\text{m}^3$ distractor ($64\cdot10^{-2}$) are wrong, and their feedback says why correctly.
- Exactly one option is correct. The item belongs to the Pohdinta phenomenon (the recycling-point cubes, viivoitin).
- Approved figures and md-paragraphs not judged. The hash was the same at the start and the end.
