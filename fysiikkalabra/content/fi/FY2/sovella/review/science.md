VERDICT: PASS
CONTENT-HASH: 9550d44a916340b5

## Blocking
None.

## Polish
- Part b asks for three emissions, but the machine-checked `answer` holds only the natural-gas value (186 200 t); the unit/field gives no hint which of the three it is. Consider asking for one value in the answer field or naming it in the part text. Not scientific.
- `### Hyväksytään myös` says full marks need a recommendation that covers the winter peak, yet the nuclear example leaves 20 MW (60 < 80 MW) uncovered and is accepted when that is discussed. The rubric's `conclusion` detail should say "covers or explicitly assesses the gap".
- Solution a: "Keskiteho on vakio koko vuoden" reads as if power were constant; "keskiteho kerrottuna ajalla antaa energian" is exact.
- Solution d calls gas the highest-emission option "vaihtoehdoista"; the coal row (820) is the plant being closed, so "uusista vaihtoehdoista" is clearer.

## Checked
- Hash at start and end: 9550d44a916340b5 (unchanged).
- Recomputed in one own script, all agree with answers.py and the solutions: E1 = 14,016 GWh, N = 27,11 -> 28 (27 gives 378,4 GWh < 380); emissions 3,116e5 / 1,862e5 / 4,18e3 t, cuts 40,2 % / 98,7 %; winter P wind 58,1 MW, city 54,5 MW, calm 7,0 MW (4,5 MW for 18 turbines); solar 9,636 GWh each, 40 parks 385 GWh, winter 15,4 GWh = 7,1 MW; mix 252,3 + 87,6 + 40,1 GWh, biomass k = 0,11, 1,41e4 t, -95,5 %; peak local 64,5 MW, import 15,5 MW (55,5 MW without biomass); nuclear 473 GWh, 4,56e3 t; two biomass plants k = 0,54, 8,74e4 t, -72 %; fuel ratio 0,16; biomass share 11 %.
- Season shares each sum to 100 %; winter = 31+31+28 = 90 d = 2160 h.
- Rubric points: a 3, b 3, c 4, d 3, e 5 (criteria sum equal to each part total). Every criterion asks only what the task gives.
- IPCC AR5 WGIII Annex III medians (820, 490, 230, 11, 48, 12, 24) correct; invented data labelled as example in source_note.
- Scope: no FY3 physics (no W, Q = cm dT, chain efficiencies, Carnot); capacity factor defined in the task. Significant figures (2 s.f.) and rounding reason stated. No source is called emission-free; biomass biogenic-CO2 convention and slow re-uptake stated. Alternative methods accepted (nuclear, wind + gas, two biomass, wind + grid).
