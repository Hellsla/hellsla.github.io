VERDICT: PASS
CONTENT-HASH: 205540ba7c16d868

## Blocking
(none) The earlier blocking finding is resolved. The 70–100 table now fits at 360 px: row 97 breaks *quatre-vingt-/dix-sept* at its own hyphen, and every sum is visible (60 + 10, 60 + 11 …). No table scrolls at 360, 390 or 1280.

## Polish
1. [Minor] The summary table at 390: the shared `td{hyphens:auto}` rule still hyphenates the English "un-der one euro". The pilot accepted this.
2. [Minor] Hero: the seller's head sits partly behind the price tags. Optional fix: move the tags up by about 30 units.
3. [Minor] In the components, French number words break only at their own hyphens. This is correct, and I am not asking for a change.

## Checked
- Fresh captures for this hash and the contact sheets.
- The 70–100 table opened at 360 px.
- A word-break audit at 360, 390 and 1280: no auto-hyphenation inside `lang="fr"`.
- The untagged-French scan: *euros* and *centimes* in the summary are now tagged.
- The hero at 390 and 1280. The three model answers, opened after writing.
- No console errors, no `.katex-error`.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
