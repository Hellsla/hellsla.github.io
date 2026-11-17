VERDICT: FAIL
CONTENT-HASH: 2e0c597a985386a4

## Blocking
- [Major] content/en/FY3/fy3-10/inquiry.json, Pohdinta recap card (lines 26, 39, 43) — the litre is written `\text{l}`, so the page shows "$3.0\,\text{l}$" as "3.01" and "2.01" (prompt, correct feedback and the ratio feedback; seen at 390 and 1280 px) — a symbol that reads as the digit 1 in new text, and the lint forbids it (NOTES.md §1) — write `\textsf{l}` in all three places (the lesson's own solutions already do).

## Polish
- [Minor] Recap card — otherwise the display chain (\dfrac, 100 kPa · 3.0 l / 2.0 l) is well aligned at 390 px.

## Checked
batch delta review: opened my own captures of the Pohdinta recap card with feedback open, correct option at 390 px and wrong option at 1280 px; the litre misreading is visible in both; the shipped captures lacked the feedback-open state. Hash unchanged at the end.
