VERDICT: PASS
CONTENT-HASH: 5bb1cae33420a27f

## Blocking

## Polish
- inquiry.json:182 ("jannite" correct feedback) — "$400$-kertaa pienemmäksi" has a stray hyphen. — Write "$400$ kertaa pienemmäksi", as the third option's feedback does.
- exit-ticket.json:12 (answer 3) — The answer uses $t = 24\,\text{h}$ without showing that one vuorokausi is 24 h. — Write $t = 1\,\text{vrk} = 24\,\text{h}$ in the chain.
- lesson.md:190 vs inquiry.json:10 — The text writes $P = \tfrac{E}{t}$, but the prior-knowledge list writes $P = \Delta E : \Delta t$. — Use one form in both places.
- inquiry.json:368 (hook) — "satoja kilovoltteja" doesn't fit the 110 kV lines well. — Write "110–400 kilovolttia", as the lesson text does.

## Checked
- One script recomputed every number in lesson.md, inquiry.json and exit-ticket.json from the task data, and all 24 keys match lesson-answers.py. Worked example: 222,95 → 223 MWh and 22,05 → 22 MWh. kl: 9,17 → 9,2 %. siirto: 15 %. tarkistus-2: 500 MWh. Exit ticket: 768 MWh and 48 kWh.
- Every mistake value lies outside its tolerance: 10,1 and 3,3; 85 and 17,6; 281 and 469. Each exact answer lies inside.
- The round-3 blocker is fixed. The substitutions in the kl, siirto and tarkistus-2 solutions now divide with a colon, and only the symbolic Kaava lines keep $\dfrac{}{}$. The siirto solution's percent conversion is now written out, as kl's is.
- The "jannite" model table follows $1 : U^2$ scaling: 0,80 → 0,0264 → 0,0020 MW, which gives 8,0 %, 0,26 % and 0,020 %. The table is marked as model values, and its magnitudes are plausible (about 0,3 Ω/km).
- The data is about 83 TWh of consumption with about 4 % losses (about 3,3 TWh), and 36,0 → 32,7 TWh of district heat (an estimate, and marked as one). In "sahko", the "about equal TWh, more than twice the share" conclusion holds (83 : 36 = 2,3).
- The Sankey diagram is to scale: 77 + 3 and 73 + 7 out of 80 px. The flow arrows in the district-heating figure point the right way. The grid voltages (110–400 kV, 20 kV, 0,4 kV, 230 V) and the storage figure are correct.
- Every correct option and every feedback in kertaus, ennuste-1/2, sahko, jannite, virhe, tarkistus-1/3 and johtopäätös is physically right. Energy is conserved throughout, and losses always go to heat in the surroundings.
- The worked example is solved symbolically first, and each answer's rounding is justified from its data (three figures, and two from 9,0 %). Its reasonableness check is a real check (the 10 % estimate and the energy sum).
- The misconception section is correct: the sent energy is $245 : 0{,}910$, not $245 \cdot 1{,}09$.
- Scope: there is no FY3 content (no $P = I^2R$, $Q = cm\Delta T$, U-value or chain product). The high-voltage argument is qualitative.
