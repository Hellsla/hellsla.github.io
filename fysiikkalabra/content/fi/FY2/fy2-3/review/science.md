VERDICT: PASS
CONTENT-HASH: 65d19b8aad653586

## Blocking

## Polish
- lesson.md:179–180 (Kilowattitunti) — the hand split puts both rows' `&` at the left edge, so the second `=` sits under "1 kWh" and not under the first `=`. CLAUDE.md "Readability" also says never to split a chain by hand for the layout. The maths is correct. — Either align on the `=` (`1\,\text{kWh} &= 1000\,\text{W}\cdot 3600\,\text{s}\\ &= 3\,600\,000\,\text{J}`) or go back to one inline chain and let mathlayout wrap it.
- inquiry.json (tarkistus-2 mistake 0.8 and solution Järkevyys) — $90\,\text{min} = 1{,}5\,\text{h}$ is still written without a substitution step. — Write $90 \cdot (1\,\text{h} : 60) = 1{,}5\,\text{h}$ once.
- inquiry.json (siirto mistake 21900) — "tulos 21 900" is a bare number. — Write $21\,900\,\text{Wh}$.
- inquiry.json (siirto solution Järkevyys) — $60\,\text{Wh} = 0{,}06\,\text{kWh}$ has no substitution step. — Write $60 \cdot 10^{-3}\,\text{kWh}$.
- lesson.md (Esimerkki, Tulos) — the two significant figures are said to come from "teho ja päivittäinen käyttöaika", but $80\,\text{W}$ is ambiguous. — Base the count on $4{,}0\,\text{h}$ and $20\,\text{snt/kWh}$.

## Checked
- The hash was `65d19b8aad653586` at the start and at the end.
- The new two-row display is correct: 1 kWh = 1000 W · 3600 s = 3 600 000 J, which agrees with the glossary, the summary (3,6 MJ) and exit ticket 2.
- I recomputed all 21 lesson-answers.py values with my own formulas in one script, and every one matches: 0,54 MJ, 0,864 MJ, 15 h, 120/60/4,8 kJ, 1000 W, 9,6 kWh → 1,92 €, 21,9 kWh (mistakes 21 900 and 0,9125), 4,38 €, 800 W (mistake 13,3), 0,24 and 0,15 kWh, and 800 000 kettles.
- Exit ticket: 2000 W; 43,8 kWh against 36,5 kWh.
- Every correct option and every distractor's feedback is right: 1 h is under 1/10, 150 h gives 5,4 MJ, 5 h gives 0,18 MJ, and dividing by three still gives 300 €.
- Graph figure: ticks at x = 212,7 and y = 216,7; the line ends at 60 s are 120, 60 and 4,8 kJ, so the slopes are 2000, 1000 and 80 W; ΔE = 40 kJ over Δt = 20 s. The bar figure is 400 : 200 : 16 px, which is to scale.
- The worked example has seven stages, is solved symbolically first, converts by substitution, and its check is real (1 kWh runs the television 12,5 h).
- Magnitudes are realistic: appliance powers, standby power, Olkiluoto 3 at about 1600 MW, and 20 snt/kWh labelled as an example price against Tilastokeskus 2025 at about 18 snt/kWh.
- Scope is FY2: P = ΔE/Δt, E = Pt, kWh and price, with no work or force. The data are labelled as model values.
