VERDICT: PASS
CONTENT-HASH: d64ab1c8503f8cb7

Science review of `fy12-energia`, round 2 (hash checked at start and end, unchanged). Round 1 had no Blocking items.
I recomputed every number again in one Python script with my own formulas (the files are untracked, so no diff was
available and I re-read everything): hook ($7{,}5 \cdot 43 = 322{,}5\,\text{MJ} = 89{,}6\,\text{kWh}$, $17{,}4\,\text{h}$),
lt-1…lt-6, Tutki (400/350/150/140 MW, $\eta_2 = 42{,}86\,\%$, mistakes 37,5/35/57,14, product 0,350), the theory chain
example (0,3969; 198 MW; bands 50/248/4/198 MW summing to 500), the new `lataus` (5,0 h / 1,0 h) and heat-pump item
($3{,}5 - 1{,}0 = 2{,}5\,\text{kW}$ from outdoor air), sauna 43,2 MJ, EV chain 50,76 kW, pellets 3,737 t, lift 8,371 kW
with all mistake values, Tarkista (1500/900 MW; 67,5 kJ), the exit ticket (69,4 kWh; 7 mm, 30 %), s1–s6 (s3 least
squares $k = -4{,}893$, $b = 92{,}79$, 204 W/K, 229,8 kWh, balance 16,51 °C; s6 245,25 MWh, 35,97 MW, 288,5 MWh, 74,8 %,
loss 72,7 MWh) and the teacher's −8 °C extra (132 kWh, 4,1 MWh, 3,7 MWh). All agree with answers.py, tasks.json and
the solutions; `practice.py check` OK (6 tasks, 90 points). The Tutki bars drawn by `tehot()` match the data and the
pasted SVG equals the figures.py output. No `.katex-error`, raw `$` or console errors at 390 and 1280.

## Blocking
None.

## Round 1 Polish, verified
1. s1 a) now $1{,}54 \cdot 3{,}6\,\text{MJ} \approx 5{,}5\,\text{MJ}$: correct.
2. s5 b): the late reading lowers the result, the nameplate power and the scale can shift it either way: correct.
3. s5 b) `error_sources` detail now asks for and gives directions: matches the task.
4. s3 b) Järkevyys: $36{,}5\,\text{K} \cdot 0{,}204\,\text{kW/K} \approx 7{,}5\,\text{kW} = (191 - 12)\,\text{kWh} : 24\,\text{h}$: consistent with d).
5. s3 b) range 192–216 W/K in rubric and Hyväksytään = the 6 % tolerance (191,8–216,2).
6. `lataus` states constant power and that real charging slows near full.

## New or changed items checked
- Heat-pump item (`yhteistuotanto`): exactly one correct option; the energy balance and "lämpökerroin ei ole
  hyötysuhde" agree with *Kaasun tekemä työ ja lämpövoimakone*, so it stays within FY3. Distractor feedback is right.
- Hook answer at the end of Ydinajatus and the teacher plan quote the same numbers.
- $E = Hm$ now states complete combustion and the fuel's actual moisture.
- Ketju (Sankey) is to scale as the text says; the kartta's laws match the formula section.

## Polish
1. **Consistency (unchanged text).** `solutions.md`, s2 c) Järkevyys: "$1 - 42 : 59{,}4 \approx 0{,}29$ eli noin
   kolmanneksen": 0,29 is nearer 30 %; write "lähes kolmanneksen" or "noin $30\,\%$".

## Checked
Definitions, conditions (mean power, power ratio at steady running, steady lift, $Q = cm\Delta T$ without a change of
state, extrapolation distance 9 K), causality (condenser heat, CHP value of heat vs electricity, heat pump moving heat,
pumped storage storing energy, wind's lifecycle emissions), significant figures with reasons, units, and that every
rubric criterion asks only what its part gives.
