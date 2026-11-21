VERDICT: PASS
CONTENT-HASH: ca2665cbfde69ecd

## Blocking

## Polish
- Box "kaksi pistevarausta": the substitution now uses $k = 9{,}0 \cdot 10^{9}$ instead of $8{,}988 \cdot 10^{9}$; with two-figure data this is fine ($0{,}0999\,\text{N}$ vs $0{,}100\,\text{N}$, both $0{,}10\,\text{N}$).

## Checked
batch delta review: Pysähdy-box Coulomb substitution recomputed ($F = k q^2/r^2 = 0{,}10\,\text{N}$ with either $k$); three-charge box: round-2 fix correct (equal same-sign outer charges both repel or both attract the middle one from opposite sides, equal magnitudes, net force zero, independent of the middle charge's sign); no guardrail breaks.
