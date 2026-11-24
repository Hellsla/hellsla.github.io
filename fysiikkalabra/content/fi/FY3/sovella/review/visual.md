VERDICT: PASS
CONTENT-HASH: 2bcc336fe1b09523

## Blocking
(none) Round 1's Major is resolved: tasks.json and solutions.md now have `\textsf{l}` everywhere (0 `\text{l}` left), and the captures show a letter l.

## Polish
- [Minor] page-390-24, s3 c Kaava — the eight rows have their `=` signs a few px apart, so the block looks centred and a little ragged, not one column; the `&=` source is correct, so check whether the build re-centres it. Optionally put a thin gap between the symbolic groups.
- [Minor] litre `\textsf{l}` — in the serif maths it is a plain vertical bar and still close to a capital I ("20 l/min", "725 l"); `\ell` is clearer. Note that NOTES §1 fixes `\textsf{l}`, so this is only an implication.
- [Minor] solutions.md fy3-s1 a) — "Jokainen rivi on yksi erillinen piste." — "Jokainen taulukon rivi on yksi erillinen piste."
- [Minor] fig fy3-s1-graph — the y axis starts at 10 with no stated axis break — say so in the aria-label.
- [Minor] fy3-s1 d) / fy3-s3 a) Sijoitus — a lone "ja" between two display blocks — join the chains or end with a full sentence.

## Checked
- Stamp and packet hash both 2bcc336fe1b09523; sources (13:29) are older than the captures (13:31), so the captures are current.
- Opened page-390-22, page-390-23, page-390-24 (s3 a, b, c: Kaava, Muunnokset, Sijoitus, Vastaus) and page-1280-17 (s3 a Kaava, Muunnokset, Sijoitus).
- Litre: "6,0 l", "12,0 l", "725 l", "20 l/min" and "15 l:aan" all render as a letter l. No red KaTeX source, no clipping at 390 or 1280 px.
- Kaava blocks of s3 a and s3 c: fractions and subscripts legible, nothing clipped.
- Not reopened: the s1 and s2 captures, which are unchanged since round 1 apart from the litre fix.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
