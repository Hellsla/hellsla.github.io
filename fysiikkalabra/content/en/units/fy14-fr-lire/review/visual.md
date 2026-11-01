VERDICT: PASS
CONTENT-HASH: f5bc3f119dc791ac

## Blocking
(none) The earlier blocking finding is resolved. The endings now use non-breaking hyphens (*‑ité*, *‑ique*, *‑ity* …). At 1280 the strategy wraps between whole items, and the audit finds no split ending at 360, 390 or 1280.

## Polish
1. [Minor] News texts: a number can still be separated from its unit at a line break ("500 / mégawatts" at 390). Fix: put a no-break space between number and unit (`500 mégawatts`, `50 mégawatts`, `22 minutes`).
2. [Minor] False-friends table at 390: the shared `td{hyphens:auto}` rule hyphenates the English "even-tually" and "construc-tion". This is harmless.

## Checked
- Fresh captures for this hash and the contact sheets.
- selita-1280-1 at full size: the endings, the false friends and the maths ($10^{9}$, $10^{12}$).
- The news text at 390. The hero.
- A word-break audit and an untagged-French scan at 360, 390 and 1280: the true/false prompt is now tagged.
- The new *How much* opening line renders correctly.
- No console errors, no `.katex-error`.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues (all four units)
- `templates/site.css:327` `th,td{hyphens:auto}` below 48 rem hyphenates English in table cells.
- `scripts/screenshot.py` makes no `fig-N` captures for course units.
- `templates/inquiry.js`: the reflection list repeats "Commit now; …" (known from the pilot).
