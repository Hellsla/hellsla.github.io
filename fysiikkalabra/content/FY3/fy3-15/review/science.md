VERDICT: PASS
CONTENT-HASH: 3e4a29379cd99c5d

## Blocking

## Polish
- solutions.md:108 (L3-02) — the Vastaus line counts the conversion 1 GWh = 3,60·10¹² J as a three-figure datum, but it is exact (and L2-03 rightly calls the hour exact) — name only 36,0 GWh, 0,380 and 25,0 MJ/kg as limiting.
- solutions.md:69 (L2-02) — "lähellä lauhdevoimalaitoksen tavallista 40–45 %:n arvoa" compares the steam-cycle efficiency with a whole-plant range — say "höyrykierron tyypillistä 0,42–0,46" or drop it.
- lesson.md:269 (worked example, Järkevyys) — "lauhdevoimalaitoksen tavalliseen 35–45 %:iin" differs from the tyypit table (0,38–0,42; ydinvoimala 0,35) — use one range.
- inquiry.json:26 (kertaus) — "Laskit lämmöt yhteen: Q₁ + W" — W is work, not heat: "Laskit lämmön ja työn yhteen".
- inquiry.json:315 (siirto) — answer 8.64 vs Vastaus 8,6 MW; both inside tolerance, consistency only.

## Checked
- All 12 exercise answers recomputed in one script; match answers.py and exercises.json within tolerance; L3-01 η_kok 67,6 %.
- Worked example: 0,38038 · 600 = 228 MW, 38,0 %, 372 MW; P₁ − P₂ = 306 MW; estimate and balance; rounding justified.
- Inquiry numerics: ketju 248,4 MW (balance 40 + 248,4 + 11,6 + 200), kaukolampo 48 MW (difference keeps MW precision), tarve 130 MW, siirto 8,64 MW → 8,6 from the 0,050 difference, check-2 216 MW; mistake values match their feedback.
- Choice items: kertaus 520 MJ, virhe 0,342 / 900 / 360 / 540 MW, pred-1, pred-2 (40/232 = 0,17), tyypit and check-1 correct options and feedback physics right.
- Figures to scale: Sankey 40 px/100 MW (500, 460, 211,5, 200; losses 40, 248,5, 11,5), stacked graph (1,84 px/MW, 0,6 px/MW; 194, 218, 78,8), bars 0,5 px/MW; product 0,40, mean 0,78.
- Solutions L1–L3: principle stated and its reason right (series chain → product; steady state energy balance; Q = cmΔT without phase change; linear CHP interpolation; heat-pump ε = Q/E_s), symbolic before substitution, conversions right (MW→W, MJ/kg, h→s, t, GWh→J, kt).
- Rounding: differences given the decimals of the difference (L1-04, kaukolampo, L3-01 via 60 MW → 34 MW), others limited by three-figure data.
- Reasonableness checks are real: balances, limiting cases (P_k = 232/348 MW), back-substitution (L2-02, L2-04), magnitudes (46 kg/s, 7 m³/s, 270 wagons, 263/111 kWh).
- Magnitudes realistic (condensing 38–42 %, CHP 85–90 %, hydro 90 %, wind 40–45 % below Betz, PV 20 %); exit ticket 0,432, 85 %, 15 MW.
- Scope: efficiency, energy conservation, power, Q = cmΔT, heat engine/heat pump in FY3; no sim (justified).
