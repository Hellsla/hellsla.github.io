VERDICT: FAIL
CONTENT-HASH: 688464c5a7f5edd4

## Blocking
- [Major] inquiry.json exp-1–exp-4, generated "Alkutila" line (exp-exp-1-390-1, exp-exp-4-390-1, lab-1280-1) — the mass is plain text, "$m$ = 1 kg", and in Koe 4 "$m$ = 0.5 kg" with a decimal point. The speed is "3 m/s" although the card's own text says $3{,}0\,\text{m/s}$ and $0{,}50\,\text{kg}$ — wrong decimal mark in Finnish, a quantity outside LaTeX, and a precision that contradicts the instruction a line above — format select values like numeric ones (take the option label or pass the value through the numeric formatter in scripts/inquiry.py) so the line reads $m = 0{,}50\,\text{kg}$, $v_0 = 3{,}0\,\text{m/s}$.

## Polish
- [Minor] lesson.md Kaava, "$m g h = m g \cdot \tfrac{v^2}{2g} = \tfrac12 m v^2$" (theory-1280-2) — the inline chain wraps after "$mg\,\cdot$" at 1280 px — make this derivation step a display equation.
- [Minor] figs ek-kuvaaja and pallo-ek (fig-4-390, fig-6-390) — the curve runs past the last gridline (beyond $4\,\text{m/s}$ / $8\,\text{J}$, beyond $6\,\text{m/s}$) — end it at the last gridline or extend the grid.
- [Minor] Esimerkki, Järkevyys (example-390-2) — the two estimates merge into one box and the "ja" between them disappears, so the sentence jumps from "luvuilla" to "yhteensä" — keep the connector visible (e.g. "…$\approx 5\,\text{kJ}$. Potentiaalienergia on $E_\text{p} \approx …$").
- [Minor] Finnish — "…muutoksella, ja se ei riipu nollatasosta" → "…muutoksella, eikä se riipu nollatasosta"; Tiivistelmä bullet 3 "jonka energia riippuu vain paikasta" is ambiguous → "ja johon liittyvä potentiaalienergia riippuu vain paikasta".
- [Minor] simulation canvas (sim-390, sim-1280) — the $h$ axis "0" is half hidden by the ground strip — lift the label or the axis origin by a few pixels.

## Checked
- contact-1…6; top-390, top-1280, intro-1280 (hero labels v, v/2, v = 0, ¼h/¾h consistent with the text)
- fig-1…fig-6-390 at full size: ramppi h:4h and v:2v to scale, polut, ek-kuvaaja (2,0 J / 8,0 J correct for 1 kg), nollataso to scale (3,9/−3,9 J), pallo-ek grid points readable
- theory-1280-1…3 (figures beside text, display formulas, Tiivistelmä)
- example-390-1/2 (aligned rows, rounding, order principle → formula → substitution → result → Järkevyys)
- sim-390, sim-1280, lab-1280-1/2 (sticky panel scrolls by design; colours: velocity blue, energy bars orange/green/grey)
- exp-exp-1-390-1, exp-exp-4-390-1 (canvas blank in these and tutki-390-1, shown in exp-2/exp-3: probably capture timing, worth a glance)
- stage-herata-390, open-ennusta-1280-1, open-tarkista-1280-2, open-exit-1280

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
