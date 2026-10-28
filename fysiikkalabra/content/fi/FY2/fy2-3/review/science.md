VERDICT: PASS
CONTENT-HASH: 30b2bdfd7f154305

## Blocking

## Polish
- inquiry.json:271, 275, 278 (tarkistus-2) — the mistake feedback and the reasonableness check still use $90\,\text{min} = 1{,}5\,\text{h}$ with no substitution step. — Write $90\,\text{min} = 90 \cdot (1\,\text{h} : 60) = 1{,}5\,\text{h}$ once.
- inquiry.json:217 (siirto mistake) — $2{,}5\,\text{W} = 0{,}0025\,\text{kW}$ has no substitution step, and "tulos 21 900" is a bare number. — Write $2{,}5 \cdot 10^{-3}\,\text{kW}$ and $21\,900\,\text{Wh}$.
- inquiry.json:224 (siirto solution, Järkevyys) — "$60\,\text{Wh} = 0{,}06\,\text{kWh}$" has no substitution step. — Write $60 \cdot 10^{-3}\,\text{kWh}$.
- lesson.md:150 (Tulos) — the text says the 2 significant figures come from "teho ja päivittäinen käyttöaika", but 80 W is ambiguous (it could have 1 or 2 significant figures). — Base the count on $4{,}0\,\text{h}$ and $20\,\text{snt/kWh}$, or write the power as $80\,\text{W}$ with two significant figures stated.

## Checked
- I recomputed every number in lesson-answers.py in one script with my own formulas, and all 21 match: 0,54 MJ, 0,864 MJ, 15 h, 120/60/4,8 kJ, 1000 W, 9,6 kWh → 1,92 €, 21,9 kWh (mistakes 21 900 and 0,9125), 4,38 €, 800 W (mistake 13,3), 0,24 and 0,15 kWh, and 800 000 kettles.
- Exit ticket: 2000 W; 1 kWh = 3,6 MJ; 43,8 kWh against 36,5 kWh. The round-3 blocker is fixed: W → kW is now converted by substitution.
- Every correct option is right, and so are the numbers in every distractor's feedback: 1 h gives 1/15 of the energy, 150 h gives 5,4 MJ, 5 h gives 0,18 MJ (1/3), and the "jakaa kolmella" option still gives 300 €.
- Graph figure: the ticks fall at their values (20 s → x = 212,7, 40 kJ → y = 216,7), the line ends are 120, 60 and 4,8 kJ at 60 s, so the slopes are 2000, 1000 and 80 W, and the marked ΔE = 40 kJ over Δt = 20 s. The bar figure is 400 : 200 : 16 px, which is to scale.
- The text's step 40 kJ → 40 000 J is now done by substitution.
- The worked example has all seven stages, is solved symbolically first, converts W → kW and snt → € by substitution, and its check is real (1 kWh runs the television about 12,5 h).
- Magnitudes are realistic: typical appliance powers, a sauna stove of 8 kW, standby under 1 W to a few W, Olkiluoto 3 at about 1600 MW, and the Tilastokeskus 2025 price of about 18 snt/kWh, with 20 snt/kWh labelled as an example price.
- Scope is FY2: P = ΔE/Δt, E = Pt, kWh and price. There is no work, force or efficiency chain. The data are labelled as model values, not measurements.
