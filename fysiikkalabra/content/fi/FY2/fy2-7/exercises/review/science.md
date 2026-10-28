VERDICT: FAIL
CONTENT-HASH: 4afa2160cff0bd47

## Blocking
- exercises.json:4–96 (all 12 texts) — Every number and unit is plain text ("500 MWh", "4,0 %", "2,5 kW"). The teacher's standing rule is that everything is in LaTeX. — Write `$500\,\text{MWh}$`, `$4{,}0\,\%$` and so on, as the fy2-1, fy2-4, fy2-5 and fy2-6 sets do.
- exercises.json:96 / solutions.md:118 (L3-03) — The answer field says 25.2, but the solution's Vastaus says "$25\,\text{MWh}$, kaksi merkitsevää numeroa". — Pick one. With 150 kW taken as three figures, use $25{,}2\,\text{MWh}$ in both places.
- solutions.md:116 (L3-03) — "$25\,200 : 1000\,\text{MWh}$" is not a conversion by substitution, and it reads as dividing by 1000 MWh. — Write $1\,\text{kWh} = 0{,}001\,\text{MWh}$, then $25\,200\,\text{kWh} = 25\,200 \cdot 0{,}001\,\text{MWh} = 25{,}2\,\text{MWh}$.
- solutions.md:75 (L2-03) — The Kaava line puts a number in the equation ($E_\text{häviö} = 0{,}04 \cdot E$), so it is not solved symbolically first. — Write $E_\text{häviö} = p\,E$ (with $p$ the loss share) and substitute $p = 0{,}04$ afterwards.

## Polish
- L2-01, L2-02, L2-04 — The misconception the lesson names (adding $p$ of the *delivered* energy) gives 998,4 / 1984 / 1046. All three are inside the tolerances (0,16 %, 0,8 %, 0,3 %), so the check cannot tell the wrong method from the right one. At $p = 4\,\%$ no tolerance can separate them. If the set should catch the mistake, give one of these tasks a larger loss (a storage round trip, e.g. $\eta = 75\,\%$).
- L2-03 — "noin 4 %" has one significant figure, so say why 3,3 TWh carries two (the 83 TWh), or answer $\approx 3\,\text{TWh}$.

## Checked
- All 12 answers recomputed independently in one script. All match answers.py and exercises.json within tolerance (L2-03 3,32 to 3,3; L2-04 1055 to 1050; L3-01 21,04 to 21).
- L2-03 data verified: Energiateollisuus Sähkövuosi 2024 gives a total use of 83 TWh with losses of 4 %.
- Each solution's principle fits its task: the loss share is taken of the energy sent; power loss times time gives energy; in L3-02 the losses add and the share of power equals the share of energy at steady power.
- The reasonableness checks are real checks (sums back to the input, estimates).
- No FY3 content and no chain-efficiency product. No ×; division is written with a colon; GWh→MWh and the % conversions are written by substitution, apart from L3-03.
