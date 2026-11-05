VERDICT: PASS
CONTENT-HASH: 8f45e577d831e5c3
Round: 2

## Blocking
(none)

Round 1 had no Blocking items; the round-2 changes were checked and are correct (L1-06 and L1-07 option order, L1-08 Kaava with the unit written as $1\,\text{eV}$, L2-05 Vastaus, L2-06 source line and caption, L3-04 rescaled table and cesium/strontium framing, L3-05 split text and two-significant-figure answer $540\,\text{kg}$).

## Polish
- [Minor] solutions.md L3-05 (11-20) — Vastaus gives $1500\,\text{MW}$ and $1000\,\text{MW}$ (two figures) while Sijoitus and Järkevyys keep $1536\,\text{MW}$, $1029\,\text{MW}$ and "$1029 > 507$"; harmless, but say "noin" in Vastaus or use the same values.
- [Minor] exercises.json L2-06 (11-14) — caption "nettosähköteho (MW) (TVO:n ja Fortumin verkkosivut, tilanne 2024)" has two parentheses in a row; "nettosähköteho (MW); lähde: TVO:n ja Fortumin verkkosivut, tilanne 2024".
- [Minor] exercises.json 11-8, 11-19 — unit labels beside the answer fields ("10^-11 J", "a") are plain text; project-wide field convention — leave.
- [Minor] for science: L3-04 (11-19) — $30\,000\,\tfrac{\text{TBq}}{\text{t}}$ at ten years is high compared with typical spent-fuel values; as example data it is acceptable, but the science reviewer may want the label "esimerkkiaineisto" kept prominent.

## Checked
- 1280 px captures with every solution open: L3 part 6 (11-19 Kuvaajan lukeminen, Sijoitus a to c, Vastaus with the L3-03 reference) and L3 part 7 (11-19 Järkevyys, 11-20 task in three paragraphs, answer field, Annettu). Chains, aligned rows and answer boxes render cleanly; no clipping or red KaTeX.
- Diff of exercises.json and solutions.md against 0f82a5dd8 read in full; the numbers in L3-04 (ln values, slope, $249{,}7\,\text{a}$) recomputed and match. Only 1280 px exercise captures exist; 360 px rests on check_layout (ok).

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
