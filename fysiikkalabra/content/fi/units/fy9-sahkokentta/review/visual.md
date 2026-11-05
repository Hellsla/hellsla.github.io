VERDICT: PASS
CONTENT-HASH: 9c10b36b9630971c

## Delta review
Delta review, 2026-11-04 (previous PASS hash 29b45f18108766eb). `git diff HEAD -- content/fi/units/fy9-sahkokentta lessons/units/fy9-sahkokentta` shows one changed line: `sovella/tasks.json`, s1 b rubric criterion `calculation` (1 p). The long formula with the fraction inside the square root is now three formulas: $F_\text{s} = 4{,}93 \cdot 10^{-4}\,\text{N}$ ja $k = 8{,}988 \cdot 10^{9}\,\text{N}\cdot\text{m}^2/\text{C}^2$, joten $q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k} \approx 1{,}87 \cdot 10^{-8}\,\text{C}$ ja $n \approx 1{,}2 \cdot 10^{11}$. Nothing else changed in the unit.
- Built the preview and opened it in Playwright at 360 and 1280 px with every details element open. At 1280 px the criterion reads cleanly on two lines. `check_layout.py fy9-sahkokentta --width 360` and `--width 1280`: OK for `preview/fy9-sahkokentta` (en and fi-easy also OK).
- **Polish (not blocking):** at 360 px the third formula, $q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k} \approx 1{,}87 \cdot 10^{-8}\,\text{C}$, is still about 319 px wide in a 278 px column. `flFitMath` puts it on its own scrolling line (kx-wide), so the page does not overflow and the check passes, but the end of the result ("· 10⁻⁸ C") is hidden until the reader scrolls. The same happens at 390 px (16 px). Fix if wanted: split once more, e.g. `$q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k}$ eli $q \approx 1{,}87 \cdot 10^{-8}\,\text{C}$`, with the same change in en and fi-easy. I did not edit it, because the translations follow this source.

## Previous review

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
