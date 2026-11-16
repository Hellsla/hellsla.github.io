VERDICT: PASS
CONTENT-HASH: e8b07db9213260ed

## Blocking
None.

## Polish
- [Minor] solutions.md fy4-s1 d) Mallivastaus and fy4-s3 c) Järkevyys — the two re-broken chains are bare numeric expressions ($0{,}02\,\text{m/s}^2 : 9{,}786\,\text{m/s}^2 \approx 0{,}002$; $7{,}86\,\text{m/s} : 0{,}12\,\text{s} \approx 66\,\text{m/s}^2$); the house rule wants a chain to open with its quantity — start them "$\Delta\mu = …$" and "$a_\text{ka} = …$" at the next content edit (not in a reflow, it would no longer be one).
- [Minor] solutions.md fy4-s2 a) and b) Järkevyys — "muuttuu lämmöksi" (queued in physics-phrases-known.tsv, work queue 18) — "muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön" when queue 18 reaches it. For science: same.
- [Minor] solutions.md fy4-s2 c) Sijoitus — "B-kohdan mukaan", capital B mid-sentence — "b-kohdan mukaan".
- [Minor] fy4-s1-fbd (fig-3-390) — the label G_x sits on the dashed arrow tip; move it a few px right/below.
- [Minor] fy4-s1-graph (fig-1-390) — both lines blue, told apart by marker and dash only; a short in-figure legend would help.

## Checked
- Delta, round 2: the diff since the PASS at bbc2878b1964517a is two chains in solutions.md (lines 187 and 490) turned into two-row aligned display blocks; numbers, signs and units are unchanged and in the same order. The packet file itself says "full" and carries no diff; the diff was read from git (b17b8125a1).
- Captures are of the fi page only (current for fi hash e8cec9743308859a; the fi diff is the same two blocks, layout and figures shared); the fi-easy sentences around the blocks were judged from the source.
- page-390-7 (fy4-s1 d): the block breaks before "≈", both rows left-aligned, nothing clipped, the full stop sits inside the block after 0,002, the next sentence starts a clean paragraph.
- page-390-28 (fy4-s3 c Järkevyys): two rows inside the Järkevyys panel, units whole ("m/s²" not cut), the sentence continues "eli lähes 7g" under it.
- page-1280-6 (fy4-s1 d wide): the chain is one row, the neighbouring text and the e) graph undisturbed.
- contact-3 and contact-9 for the surrounding layout at 390 and 1280 px: cards, rubric rows and figures as before.
- Decimal comma, colon division, upright units with thin space, LaTeX number+unit hold in both edited places.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
