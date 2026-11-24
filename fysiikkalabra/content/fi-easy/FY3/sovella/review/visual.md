VERDICT: PASS
CONTENT-HASH: 51c86aaf9a3b697c

## Blocking

## Polish
- [Minor] solutions.md s3 b/c (rows 197, 202, 203, 213) — the rate `20\,\text{l/min}` still sets the litre as a roman `l`; next to `\textsf{l}` quantities it is inconsistent and can read as "1/min" — write `20\,\textsf{l}/\text{min}` (lint does not flag it).
- [Minor] Kaava blocks (s1 c, s2 d, s3 a): rows with a fraction sit slightly off the `=` column of the plain rows; acceptable.
- [Minor] fi-easy Sovella cannot be captured; judged from the Finnish captures of the same layout plus the fi-easy source.

## Checked
- Round 2 delta: all `\text{l}` quantities are now `\textsf{l}` (grep over fi-easy/FY3/sovella: tasks and solutions; `6{,}0`, `12{,}0`, `725` litre values fixed). The s3 d Kaava is a one-step-per-row aligned block (source read).
- Earlier round captures: contact-1; page-390-5, -8, -12, -14, -22 (Finnish): Kaava/Sijoitus/Vastaus blocks, no clipping or horizontal overflow. The figure is unchanged and was not reopened.
- The fi-easy captures were not re-made, as instructed.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
