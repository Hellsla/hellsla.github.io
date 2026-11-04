VERDICT: PASS
CONTENT-HASH: b942c369bb9ab315

Round 2 (delta review of round 1 fixes; round 1 hash e6caa2c8759c5df1). Science review of fy9-moderni.

## Verified
1. (Blocking 1, fixed) `sovella/solutions.md` s1 "Yleisiä virheitä": now "$3{,}2 \cdot 10^{7}$-kertaisesti liian vähän (vuoden sekuntimäärä)". Recomputed: 1 a = 3,156·10⁷ s, so the factor is right.
2. (Blocking 2, fixed) s2 "Yleisiä virheitä": now "noin $10^{-25}\,\text{m}$, noin $10^{19}$ kertaa liian pieni arvo". Recomputed: hc/1,889 = 1,05·10⁻²⁵ m, the ratio to 656 nm is 6,2·10¹⁸ ≈ 10¹⁹.
3. (Polish 3) s3 c `reasonableness` now asks to compare with 6,626·10⁻³⁴ J s and judge against the reading accuracy; the fit gives k·e = 6,61·10⁻³⁴ J s, and the accepted 6,4–6,8 is −3,4 %…+2,6 %, so no false claim remains.
4. (Polish 4) s5 a range is 145–157 s in both tasks.json and solutions.md.
5. (Polish 5) s2 text says "joista voimakkain".
6. (Polish 6) s6 data list states the condenser assumption; it matches the c criterion and the solution.
7. (Polish 7) s6 d `reasonableness` says about 200 MeV per fission vs a few eV per combustion; recomputed 5,26·10⁹ kg / 1653 kg = 3,18·10⁶ ("yli kolme miljoonaa kertaa") OK.
8. s3-fit figure: f₀ label 5,43·10¹⁴ Hz = 2,243 V / 4,127·10⁻¹⁵ V s = 5,435·10¹⁴ Hz OK; intercept −2,24 V OK.
9. Pedagogy and visual fixes (moved correct options lt-4 → A and tarkistus-1 → C, exit-ticket chapter lines, kartta $H_\text{T} = w_\text{R} D_\text{T}$, fotonit labels) introduce no physics error. Exit ticket: F-18 → O-18 and 3,1 eV still correct.
10. Built with `python3 scripts/build.py fy9-moderni`; page at 390 and 1280 with all details open: 0 .katex-error, 0 console errors, no raw $, no horizontal overflow. Fixed texts appear in the built page.

## Blocking
(none)

## Polish
(none new)

## Shared issues
None.
