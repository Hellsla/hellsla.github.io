VERDICT: PASS
CONTENT-HASH: c464157cc013fdd3

## Blocking
- none

## Polish
- solutions.md L1 (3000 mAh to C) — "neljä merkitsevää numeroa kuten 3000 mAh" treats trailing zeros as significant, while 40 kWh and 90 W elsewhere count as two figures; a phone battery rating is not four-figure data. Fix: keep $1{,}1 \cdot 10^{4}\,\text{C}$ (two figures) or state in the task that the capacity is given to four figures.
- solutions.md charging-resistance task — Vastaus is $0{,}2\,\Omega$ but Järkevyys still checks with $0{,}20\,\Omega$; fix: write "$0{,}2\,\Omega$ (tarkemmin $0{,}20\,\Omega$)" in the check.

## Checked
- 4,7 · 10^2 Wh eli 0,47 kWh: correct for 36 V · 13 Ah = 468 Wh.
- Rounding of 1,0 Ω − 0,80 Ω to one decimal follows the subtraction rule and is explained.
- 1,5 Wh justified by two-figure current and time; the explanation is correct and followable.
