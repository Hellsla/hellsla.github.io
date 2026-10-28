VERDICT: FAIL
CONTENT-HASH: 5b64360e6e9a794d

## Blocking
- inquiry.json:133, 293, 351 (solutions of "kl", "siirto" and "tarkistus-2") — Each "Sijoitus" line writes a division of numbers as a fraction: `\dfrac{3{,}3\,\text{TWh}}{36{,}0\,\text{TWh}}`, `\dfrac{1{,}8\,\text{kWh}}{12{,}0\,\text{kWh}}` and `\dfrac{375\,\text{MWh}}{0{,}75}`. The teacher's rule says written division uses a colon, and only a formula solved in symbols may keep its fraction. The exercise set's solutions already follow this. — Keep the symbolic `\dfrac` on the "Kaava" lines. In each substitution, write the numbers with a colon, for example `\text{osuus} = 3{,}3\,\text{TWh} : 36{,}0\,\text{TWh} = 0{,}0917`.

## Polish
- inquiry.json:293 ("siirto" solution) — The step `0{,}150 = 15\,\%` converts to percent with no substitution, while "kl" writes `0{,}0917 \cdot 100\,\% = 9{,}17\,\%`. — Write `0{,}150 = 0{,}150 \cdot 100\,\% = 15{,}0\,\%`, so the two solutions convert the same way.
- inquiry.json:182 ("jannite" correct feedback) — "$400$-kertaa pienemmäksi" has a stray hyphen. — Write "$400$ kertaa pienemmäksi", as the third option's feedback does.
- exit-ticket.json:3 (answer) — The answer uses $t = 24\,\text{h}$ without showing that $1\,\text{vrk} = 24\,\text{h}$. — Add $t = 1\,\text{vrk} = 24\,\text{h}$ to the chain.
- lesson.md:190 — The text writes $P = \tfrac{E}{t}$, but the prior-knowledge list in inquiry.json has $P = \Delta E : \Delta t$. — Use one form in both places.

## Checked
- I recomputed every number in lesson.md, inquiry.json and exit-ticket.json in one script, and all 24 keys match lesson-answers.py. Worked example: 222,95 → 223 MWh and 22,05 → 22 MWh. kl: 9,17 → 9,2 %. siirto: 15 %. tarkistus-2: 500 MWh. Exit ticket: 768 MWh and 48 kWh.
- Every mistake value lies outside its tolerance: 10,1 and 3,3; 85 and 17,6; 281 and 469. The exact answers lie inside.
- The "jannite" model table follows the $1 : U^2$ scaling (0,80 → 0,0264 → 0,0020 MW), so 8,0 %, 0,26 % and 0,020 % are correct. The table is labelled as model values.
- The data matches the round-1 check: about 83 TWh with about 4 % losses, and 36,0 → 32,7 TWh of district heat. The 9 % is marked as an estimate. The "sahko" comparison holds: about 3 TWh lost in each network, and 83 : 36 > 2.
- The grid voltages are correct (110–400 kV, 20 kV, 0,4 kV, 230 V). The high-voltage argument is qualitative and correct.
- The Sankey diagram is to scale: 77 + 3 and 73 + 7 out of 80. The flow arrows in the district-heating figure point the right way. All figure labels are in LaTeX.
- Every correct option and every feedback in kertaus, ennuste-1/2, sahko, virhe, tarkistus-1/3 and johtopäätös is physically right. Energy is conserved throughout, and losses always go to heat in the surroundings.
- The worked example is solved symbolically first. Its rounding is justified for each datum, and its reasonableness check is a real check.
- Scope: there is no FY3 content (no Q = cmΔT, U-value, chain product or $P = I^2R$).
- Every quantity in the prose and the tasks is in LaTeX. There is no ×, and the % → decimal conversions are written by substitution.
