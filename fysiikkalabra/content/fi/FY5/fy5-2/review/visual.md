VERDICT: FAIL
CONTENT-HASH: 74371b1509fa1a16

## Blocking
- [Major] inquiry.json line 328 (ponnahduslauta, hint: "F_p · 1,50 m = m_h g / · 2,50 m / + m_L g / · 0,50 m.") — four rows at 390 and at 1280 px, each product cut between m g and its arm although "F_p · 1,50 m = m_h g · 2,50 m" fits a phone row — the moment equation no longer reads as two moments; on a wide screen a one-row equation stands as a staircase — break only before the plus: `F_\text{p} \cdot 1{,}50\,\text{m} &= m_\text{h} g \cdot 2{,}50\,\text{m} \\ &+ m_\text{L} g \cdot 0{,}50\,\text{m}`.
- [Major] inquiry.json line 344 (Sijoitus and Järkevyys), wide form (≥ 700 px) — "· 0,50 m = 147,15 Nm", "· 2,50 m = 1471,5 Nm," and "− 588,6 N = 1079,1 N," appear as rows of their own: the "=" is outside the column and the row reads as a false equation — misreadable on a laptop or projector — mark continuation rows `&\quad \cdot 0{,}50\,\text{m}`, `&\quad - 588{,}6\,\text{N}` so join_wide joins them to the row before, or fix `mathlayout.join_wide` (shared) so a relation row never joins a continuation row.

## Polish
- [Minor] rows that start with "·" (390 px) — FY5-1 ends the row with the dot and starts at the quantity; choose one form for the course.
- [Minor] lesson.md, untouched: "N_2(x_2 − x_1) − G(2,0 m − x_1) − F_k(x_k − x_1) = 0" at 390 px is a staircase with the last minus set tight as a sign.

## Checked
- own captures of preview/fy5-2.html at 390 and 1280 px, every details and feedback opened, one tile per block holding a display formula (/tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/v/fy5-2-*.png); the standard set has no opened solutions at 390 px: fy5-2-lesson-390-1, -390-2, fy5-2-lesson-1280-1, -1280-2; review/shots/contact-7.png.
- Delta: Pohjatiedot feedback (M = Fr, good at both widths), hint rows 327–328, Sijoitus and Järkevyys of the guided example. Nothing clipped at 360/390 px; punctuation inside the last row.

## Scores
illustrations – (not in delta) · typography 2 · Finnish 5 · accessibility 4
