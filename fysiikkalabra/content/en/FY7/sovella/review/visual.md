VERDICT: PASS
CONTENT-HASH: c64721b1d12a7789

## Blocking
(none)

## Outside this change (docs/clipped-formulas.tsv, work queue 5d)
- [Major, outside this change] solutions.md s3 d, "Alumiinin määrä" / aluminium mass: `2700 kg/m^3 · 5,0·10^4 m · 150 · 10^-` still runs past the 390 px edge (cut at `10^{-`); also the tsv rows for the s3 d Järkevyys `6,0 MW − 0,85 MW` line and the s5 `0,780 : 1300 nm` row. Not touched by the reflow; fix in 5d.

## Polish
- [Minor] s5 d Mallivastaus — the two re-broken rows start with a bare expression (`1667 nm · sin 20,6° ≈ 586,5 nm`); begin the row with the quantity, e.g. `\lambda_{20{,}6^\circ} = `, as the "every chain shows what it computes" rule asks.
- [Minor] s3 a Järkevyys — `6,0 MW − 0,85 MW` and `≈ 5,2 MW` are two inline formulas on two lines; one chain would read better once 5d reaches it.
- [Minor] s1 d Annettu — a list of four values runs on as comma-separated rows; acceptable, but a short list would scan faster.

## Checked
- English captures do not exist (captured in Finnish only); judged from the English solutions.md source (identical structure, $$ count, decimal point and units) against the Finnish captures s1 #5, #6, s3 #3, #4, #8, s5 #6. Language read from the source: natural English, consistent with the Finnish set.
- Re-broken formulas judged: s1 b, c, d (Kaava, Muunnokset, Sijoitus rows), s2 a, b, e, s3 a (aligned R row, separate I and P_h chains, Osuus), s3 b, c, e (B, F/l, G/l aligned rows), s4 c, s5 d (two rows). Numbers, signs and units match the earlier chains; = signs sit in one column, nothing else clipped; decimal point (en)/comma, \cdot and colon division correct.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
