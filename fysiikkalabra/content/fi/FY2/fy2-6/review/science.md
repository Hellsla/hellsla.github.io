VERDICT: PASS
CONTENT-HASH: 9276338c11c76304
## Blocking
## Polish
- inquiry.json:79 (data-fi) — table header `$E$ (TWh)` leaves the unit outside LaTeX, while data-viikko writes `$(\text{GW})$`; write `$E\ (\text{TWh})$` for consistency with the teacher's LaTeX rule.
- inquiry.json:82 (data-fi) — 2024 was a leap year ($8784\,\text{h}$); the prompt states $8760\,\text{h}$ so the answer is consistent ($2{,}30$ vs $2{,}31\,\text{GW}$, inside tolerance), but a sharp student may ask. Optionally say "noin $8760\,\text{h}$" or note it in the solution.
- inquiry.json:165 (data-viikko Järkevyys) — Monday's "others" $0{,}6\,\text{GW}$ in January is only possible as a net value with heavy export (CHP and hydro run several GW in winter); and a daily mean wind of $6{,}4\,\text{GW}$ of $8\,\text{GW}$ is near the hourly record. Example-labelled, so fine; consider $5{,}5\,\text{GW}$ wind on Monday or call $P_\text{m}$ "muiden tuotanto ja nettotuonti".
- inquiry.json:330 (tarkistus-3 model) — "Kumpaakaan ei voi säätää nopeasti" is not true downward for wind (turbines are curtailed in seconds); write "kumpaakaan ei voi nostaa nopeasti".
- exit-ticket.json:8 — $17{,}52 \cdot 10^{6}\,\text{kWh} \approx 18\,\text{GWh}$ skips $= 17{,}52\,\text{GWh}$; add it so the conversion is a visible substitution, as in the worked example.
## Checked
- Hash unchanged start to end. Round-2 blocker fixed: worked example now shows $1598\,\text{kW} = 1{,}598 \cdot 1000\,\text{kW} \approx 1{,}6\,\text{MW}$ and $43\,800\,000\,\text{kWh} = 43{,}8 \cdot 10^{6}\,\text{kWh} = 43{,}8\,\text{GWh}$; round-2 polish taken (week consumption now $10{,}8$–$13{,}1\,\text{GW}$, below the winter peak; tarkistus-2 $9 \cdot 1000\,\text{MWh}$; table cells in LaTeX).
- Recomputed all lesson-answers.py values independently in one script: 1598 kW, 0,320, 43,8 GWh, 2,306 GW, 320, 8,4 GW, 14,016 TWh, 17,5 %, 8,76 GWh, 17,52 GWh, world ratio 35,8; table sums to 79,9 TWh. All match.
- Every numeric mistake value reproduces its stated wrong path (2306 MW, 0,0023, 0,0031, 8,8, 12,7, 0,6, 14016, 0,00018, 8760).
- Sig-fig statements and tolerances: rounding to the data's figures stays inside 2 %.
- Worked example: seven stages, $P_\text{ka} = E/t$ solved symbolically, colon division in substitution, conversions by substitution, 32 % capacity factor realistic.
- Data: Tilastokeskus 2024 (nuclear 31 ≈ 39 %, wind 20,2 ≈ 25 %, fossil+peat 4,3 % = "muutama prosentti"), wind capacity ≈ 8 GW end 2024, OL3 1600 MW.
- Figures: fi-bars 10,5 px/TWh exact; log chart 70 px/decade, points at log10 P (89, 299, 390, 474); "kaksi ja puoli askelta" = log10 320 = 2,51; plants figure has G for turbines, none for PV, heat arrow from every plant.
- Correct options and feedback physics: nuclear largest; hydro fastest to raise; nuclear base load; error item E·t vs E:t, 123 000 GW ≈ 36 × world mean.
- Formula $E = P \cdot t$ with constant-P condition; mean power defined; scope stays FY2 (no W = Fs, Q = cmΔT, chain efficiencies); no ×; fractions only in symbolic solutions.
- Provenance: data-fi `statistics` with source_note; data-yksikko and data-viikko `example`.
