VERDICT: PASS
CONTENT-HASH: db95bbe75962f18c

## Blocking
None.

## Polish
None.

## Checked (delta 5, 2026-11-23)
- Diff (`git diff HEAD`, investigation.md only, 6 lines): every change replaces `\ ` with the thin space `\,` between a number and its unit (e, c, h known value, 1 nm = 10^-9 m, d = 1 mm / N, the h ± Δh result form). No number, symbol, formula or unit changed.
- Values still correct: e = 1,602 176 634·10^-19 C, c = 2,997 924 58·10^8 m/s, h = 6,626 070 15·10^-34 J·s (exact SI values); 1 nm = 10^-9 m; d = 1 mm/N.
- The remaining `\ ` are in table headers of the form quantity (unit) (U (V), I (mA), λ (nm), 1/λ (1/m), U_k (V)): a word space between the symbol and the bracketed unit reads correctly and is no number–unit pair.
- The rest of the physics (U_k = hc/(eλ), slope k = hc/e in V·m, h = ek/c, the E–f alternative with slope h, the stated model conditions) is unchanged since the earlier PASS.
