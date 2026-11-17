VERDICT: FAIL
CONTENT-HASH: c09510655da596f8

## Blocking
- [Major] content/fi-easy/FY3/fy3-10/inquiry.json, Pohdinta "Kertaa: Boylen laki" (prompt, correct feedback, wrong feedback) — the litre is written `\text{l}`, which renders as "3,01", "2,01" and in the fraction "100 kPa · 3,01 / 2,01": the unit reads as the digit 1, so the volumes look like 3,01 and 2,01 (seen at 390 px and 1280 px) — an ambiguous number in new text (NOTES §1: `\text{l}` is a lint error, the litre is `\textsf{l}`) — change every `\\text{l}` in these three strings to `\\textsf{l}` (fy3-11 already does).

## Polish
- [Minor] wrong-answer feedback — "$3{,}0/2{,}0 = 1{,}5$" is a division with a slash in a sentence; house rule is a colon: "$3{,}0 : 2{,}0 = 1{,}5$".

## Checked
batch delta review: Pohdinta card (Kertaa: Boylen laki) with feedback open at 390 px and 1280 px (correct and wrong answer), plus stage-herata-390. Captures made by me from preview/fi-easy. Layout, fraction chain and card are otherwise clean.
