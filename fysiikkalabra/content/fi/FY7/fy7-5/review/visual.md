VERDICT: PASS
CONTENT-HASH: 787c4681f8c9b1b1

## Blocking
(none)

## Polish
- [Minor] inquiry.json tarkistus-2, solution, Järkevyys block: the inline `\tfrac` units (m/s, m²/s, Wb/s) render small at 1280 px, but they stay legible. Optional: none required.

## Checked
- Delta round 5. The only text change is the Järkevyys block of the tarkistus-2 solution (moving rod): the two area-rate chains now carry units, `0{,}50\,\text{m} \cdot 4{,}0\,\tfrac{\text{m}}{\text{s}} = 2{,}0\,\tfrac{\text{m}^2}{\text{s}}`. Read the diff.
- Opened `fy7-5-open-tarkista-1280-2.png` and `fy7-5-open-tarkista-1280-3.png`: the solution renders cleanly, KaTeX showed no errors, nothing clipped, decimal comma, `\cdot` and upright units correct.
- Opened `fy7-5-stage-tarkista-390-2.png`: task card, hints and Arvioi block fine at 390 px.
- The five changed pictures (faraday, flux, hero, rod, scene) are teacher-approved and carry over under `teacher-figure`; not reviewed.
- Deterministic layout checks at 360, 390, 768 and 1280 px were already ok in the packet. Hash unchanged during the review.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5

(Written to file by the worker from the reviewer's returned report; the reviewer could not write files.)
