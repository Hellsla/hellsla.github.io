VERDICT: PASS
CONTENT-HASH: b942c369bb9ab315

Round 2 (delta review of round 1 fixes; round 1 hash e6caa2c8759c5df1). Visual and editorial review of fy9-moderni. Round 1 had no Blocking visual finding; I checked the round-1 polish fixes in the built preview.

## Verified
1. Built `python3 scripts/build.py fy9-moderni`; opened preview/fy9-moderni.html at 390 and 1280 with every details element open: 0 console errors, 0 .katex-error, no raw $, scrollWidth = clientWidth at both widths.
2. kartta: capped width (608 px element at 1280), no overlap, $H_\text{T} = w_\text{R} D_\text{T}$ matches the theory, bottom line "joka haarassa: yksi hiukkanen, sitten lukumäärä" readable.
3. fotonit: name/value rows no longer overlap at 390 or 1280; "logaritminen asteikko" under the axis.
4. s3-fit: f tick numbers below the axis and clear of the points; $f_0 \approx 5{,}43 \cdot 10^{14}\,\text{Hz}$ below the axis, legible at 390 (298 px figure) and 1280.
5. All eight figures captured at both widths; none clipped.
6. Finnish of the changed sentences (s1/s2 common mistakes, "joista voimakkain", s6 condenser assumption, s6 d reasonableness, s3 c criterion, exit-ticket chapter lines, teacher plan) is natural, uses decimal comma and LaTeX for every number with unit.

## Blocking
(none)

## Polish
(none new)

## Shared issues
- Numeric table columns are not right-aligned in the shared table style (carried over from round 1; not a unit issue).
