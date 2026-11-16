VERDICT: FAIL
CONTENT-HASH: 017d78a5adc4730f

## Blocking
- [Major] solutions.md fy5-8-L3-02, Järkevyys (own capture at 1280 px) — the wide form shows `0,050 kg · 9,81 m/s² ·` pushed to the right on row 1 and `0,1835 m ≈ 0,090 J.` at the left on row 2: a product broken across two staggered rows on a card where the whole line fits — it looks broken and the student has to reassemble the product — `join_wide` joins the `≈` row to the continuation `0,1835 m` and `align_equals` then aligns row 1 to the `≈`. Fix: `&0{,}050\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\ &\quad \cdot 0{,}1835\,\text{m} \\ &\approx 0{,}090\,\text{J}` (tried: wide gives one row).
- [Major] solutions.md fy5-8-L2-03 (task 8-11), Sijoitus (fy5-8 contact-7 #78, own capture at 1280 px) — wide: `ΔE_p = ½ ·` then `150 N/m · ((0,090 m)² − (0,030 m)²)` at the left margin: the first `=` is out of the column of the others and the row ends in a dangling `½ ·` — against "every = in one column" (teacher 2026-11-13). Fix: `\Delta E_\text{p} &= \tfrac{1}{2}\cdot 150\,\tfrac{\text{N}}{\text{m}} \\ &\quad \cdot\left(…\right) \\ &= …` (tried: wide gives `ΔE_p = …` on one row; check the phone row at 360 px).

## Polish
- [Minor] fy5-8-L2-03 at 390 px — `ΔE_p` alone on row 1 and the continuation `150 N/m · (…)` flush left under `= ½ ·`; readable and unclipped, the fix above tidies it too.

## Checked
- Delta: the two re-broken formulas (L2-03 Sijoitus, L3-02 Järkevyys), opened with ?ratkaisut=1 on the preview of this hash; own element captures at 390 and 1280 px (scratchpad v/M-fy5-8-390.png, M-fy5-8-1280.png).
- 390 px: nothing clipped, page scrollWidth 390, no formula scrolls.
- Packet contact-7 (level 2 at 1280 px): cards around the opened solutions intact.
- The caption change is the teacher's approved category; not judged here.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
