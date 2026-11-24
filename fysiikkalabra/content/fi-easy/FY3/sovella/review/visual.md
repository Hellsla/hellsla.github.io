VERDICT: FAIL
CONTENT-HASH: c75053d468fb5e32

## Blocking
- [Major] solutions.md fy3-s3 b), c) Annettu/Sijoitus/Vastaus; tasks.json fy3-s3 b), c) — litre written `\text{l}` (`6{,}0\,\text{l}`, `12{,}0\,\text{l}`, `20\,\text{l/min}`, `725\,\text{l}`); it renders as the digit 1 ("6,01", capture page-390-22) — a quantity reads as another number; NOTES §1 makes it a lint error — write `\textsf{l}` everywhere (also `\text{l/min}` -> `\textsf{l}/\text{min}`).

## Polish
- [Minor] Kaava blocks (s1 c, s2 d, s3 a): rows with a fraction sit slightly off the `=` column of the plain rows (page-390-5); acceptable, no change needed unless the aligned rows are re-built.
- [Minor] Captures exist only for the Finnish page (screenshot.py cannot capture fi-easy Sovella); fi-easy judged from the same layout plus source.

## Checked
- contact-1; page-390-5, -8, -12, -14, -22 (Kaava, Muunnokset, Sijoitus, Vastaus blocks, aligned multi-row Kaava of s1 c/d, s2, s3 a at 390 px). Fi captures, fi-easy source read in full; fig-1-390 not separately opened (unchanged figure).
- The new aligned Kaava blocks render cleanly: no clipping, no horizontal overflow, one step per row, readable at 390 px.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
