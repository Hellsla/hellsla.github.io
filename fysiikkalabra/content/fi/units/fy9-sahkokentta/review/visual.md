VERDICT: PASS
CONTENT-HASH: 29b45f18108766eb

Round 2 (delta review of round 1 fixes; round 1 hash 63bd93568ec525b8). Visual and editorial review of fy9-sahkokentta, 2026-11-04. I built `preview/fy9-sahkokentta.html` and opened it in Playwright at 390 and 1280 px, with every details element open and every solution shown.

## Blocking from round 1
1. **Label sizes at 390 px: fixed.** The smallest rendered label sizes at 390 px are now:
   - kartta 16,0 px
   - kipina 16,7 px
   - levyt 14,3 px
   - s1-fbd 16,7 px (the subscript s is smaller, which is acceptable)
   - s3-cd and s3-lin 14,9 px

   kipina now writes MV/m and ½ with `\dfrac`, which reads clearly.
2. **s1 a model force diagram: fixed.** `fy9-sahkokentta-s1-fbd` shows a situation picture beside the force diagram. The forces are red and the labels are clear at 390 px. The alt text is complete.

## Polish from round 1, verified
- kipina now shows a spark (a glow and a zigzag) in the gap, and the alt text mentions it.
- The s3 table columns are centred.
- The Ydinajatus paragraph is split into two.
- The s3 graphs are not widened. The developer's reason is acceptable, because the labels are already 14,9 px.

## Checks
- No console errors and 0 `.katex-error` at either width.
- No raw `$`.
- scrollWidth is 390 at 390 px and 1280 at 1280 px, so there is no horizontal scroll.
- Colours follow the convention: field green, force red.
- The Finnish of the changed sentences reads naturally.
- I corrected one sentence in s4 b myself; see science.md.

## Shared issues
- The reused FY6 figures `fy6-12/ex-vgraph` and `fy6-13/ex-qu` render their labels at 13 px at 390 px. They belong to the FY6 chapters, so they do not block this unit.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
