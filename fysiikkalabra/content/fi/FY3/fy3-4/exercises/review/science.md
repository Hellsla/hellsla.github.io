VERDICT: PASS
CONTENT-HASH: 89a47ad1ed9999a9

Round 2 (after 6bbde30c5). Both changes in fy3-4 fix the round-1 width finding in L1-09. The correct option's feedback is split into two equations, and the solution's chain is now a two-line aligned display. The numbers did not change.

## Blocking

## Polish
- exercises.json (L1-09, the 10⁶ Pa feedback) — round 1 carried over and still optional: "kilometri on muunnettu metreiksi kymmenen kertaa liian pieneksi" is a contrived route to 10⁶ Pa; the physics is right.

## Checked
- Round-1 finding fixed. Widths at 390 px (Playwright on the rebuilt preview, 23:15, solution and feedback opened, maths rendered):
  - Feedback: 237 px and 158 px.
  - Aligned solution block: 286 px inside a 302 px box with no overflow (scrollWidth = clientWidth).
  - Both fit within the ~300 px limit.
- Recomputed: ρgh = 1000 · 9,81 · 1000 = 9,81·10⁶ Pa (9,8·10⁶ in the feedback), nearest 10⁷ Pa. Exactly one correct option; the distractors' feedback is right.
- Everything else is from the regenerated packet text; the rest of the set is unchanged.
- The hash is the same at the start and the end.
