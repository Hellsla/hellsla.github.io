VERDICT: FAIL
CONTENT-HASH: 8b7579d82180d059

## Blocking
- [Major] inquiry.json 'model' (Mallin oletukset, Tutki) — `$\begin{aligned}T_2 &= ... \approx 329\,\text{K}\end{aligned}$` is set inline inside a running sentence: at 390 px the rows interleave with the text ('...antaa T_2 = ... / = 293 K·(4/3)^0,4, kun ilmalle γ ≈ 1,4; / ≈ 329 K'), so the last row of the chain stands after the next clause and reads out of order — the equation cannot be followed — put the chain in its own display: `... Sille fysiikka antaa $$\begin{aligned}...\end{aligned}$$ Tässä ilmalle $\gamma \approx 1{,}4$; simulaatio antaa ...` (the fy2-2 and fy3-5 'Etsi virhe' prompt already do this).

## Polish
- [Minor] 'Etsi virhe' prompt/choice now use `$$...$$` and render well; a full stop after a display ('$$. Missä') is lifted into its own row, check it is not orphaned.

## Checked
batch delta review (hash changed during my review; judged the current version 8b7579d8…): Etsi virhe prompt and choice at 390 px (fixed, good); Mallin oletukset at 390 px (defect above). Figures unchanged, not reopened.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
