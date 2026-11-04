VERDICT: PASS
CONTENT-HASH: d1021d5831c47cfe

Round 2 (delta review of round 1 fixes; round 1 hash 365135079757531a). Visual and editorial review of fy9-liike. I rebuilt `preview/fy9-liike.html` and checked it in Playwright at 390 and 1280. I took element captures of `kartta`, `kuvaajat`, the Tutki graph and the s3 model graph, and measured the effective label size of each SVG (font size × rendered width ÷ viewBox width).

## Round 1 Blocking findings, verified
1. **`kuvaajat` tangent.** Fixed. The tangent, the dotted line down to $v_\text{P}$ and the label "$k = v_\text{P}$" are velocity blue. The label sits right of the tangent's end, clear of the curve.
2. **`kartta` colours.** Fixed. The $(t,x)$ row is ink, $(t,v)$ is blue and $(t,a)$ is orange. Solid means tasainen and dashed means tasaisesti kiihtyvä, and the key is in neutral ink. Δx and Δv (pinta-ala) are green, the same as the area in `kuvaajat`.
3. **Label size at 390 px.** Fixed or confirmed. The smallest effective label sizes at 390 px are: `kartta` 18,8 px, `kuvaajat` 17,1 px, Tutki 15,5 px and s3 graph 16,3 px, all at least 14 px. The captures read clearly at phone width.
4. **`aineisto` wording.** Fixed: "Kuvaajassa on raitiovaunun nopeus pysäkiltä seuraavalle pysäkille." The text "alun raitio" no longer appears in the preview.

## Round 1 Polish, verified
5. $x$ is used throughout ($x = x_0 + vt$ in prior, Virheet, Kertaa). 7. The s3 label "$k \approx -2{,}3$ (km/h)/s" is in free space, and "48,5 s" is muted and clear of the axis label. 8. The s6 frame-rate sentence is fixed.

## Still open (Polish, not blocking)
- Shared: the fy4-2 catalogue figures `ex-tangent` and `ex-tv` have an effective label size of 13,0 px at 390 px. Raise the size in the shared catalogue.
- The hero road edge is unchanged (optional).

## New problems from the fixes
None. There is no horizontal scroll at 390 or 1280, no `.katex-error`, no raw `$` and no console errors. `check_layout` passes. The tables fit.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
