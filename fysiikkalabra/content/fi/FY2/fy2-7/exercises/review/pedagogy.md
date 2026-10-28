VERDICT: PASS
CONTENT-HASH: 95d069fcaa4bb4ac

## Blocking

## Polish
1. exercises.json fy2-7-L1-01 — same data and answer as the inquiry item "Etsi virhe" ($500\,\text{MWh}$, $4\,\%$, $480\,\text{MWh}$), whose feedback states the answer; a student who did that item just copies. Change to e.g. $640\,\text{MWh}$ and $3{,}0\,\%$ (answer $620{,}8 \approx 621\,\text{MWh}$; update answers.py), and keep the structure.
2. solutions.md fy2-7-L1-02, Vastaus — "koska molemmat energiat on annettu täysinä megawattitunteina ja epätarkin tieto rajoittaa" is muddled; write: "kaksi merkitsevää numeroa, koska erotus $360 - 327$ päättyy kymmenien kohdalle (yksiköt)". Simpler: "erotuksen tarkkuus on kokonaiset MWh".
3. solutions.md fy2-7-L1-05, Järkevyys — the estimate $3 \cdot 24 = 72$ against $60$ is $20\,\%$ off and does not convince; use $2{,}5 \cdot 24 = 2 \cdot 24 + 0{,}5 \cdot 24 = 48 + 12 = 60$ or the estimate $2{,}5\,\text{kW} \cdot 24\,\text{h}$ "neljäsosa tuhannesta".
4. L3-02 — the question has two parts (which network, how many MWh) but the answer field takes only the difference; add "Anna vastaukseksi erotus" (present) and name the network in the solution only; fine, but consider asking just "kuinka monta MWh enemmän verkko A tuo".
5. L2-03 text — "Alueen" and "esimerkkitilanne" fine; add the unit hint "1 TWh = 10^6 MWh" is in the solution only; acceptable for L2 (conversion is the skill), no change needed unless levels need relief.

## Checked
- Levels per rubric: 5 / 4 / 3; L1 one formula, L2 conversion or two steps (GWh, TWh, power to energy), L3 comparison and reasoning.
- No exercise repeats the worked example (245 MWh, 9,0 %) except L1-01 overlapping the error item.
- Answers verified by hand: 480, 33, 96,0, 120, 60, 150, 1500, 11, 1200, 21, 13,0, 66; tolerances 0,02 suit the rounding.
- Solutions follow the seven steps with symbols before numbers, conversions stated, reasonableness checks present.
- Finnish and case forms after number+unit correct; LaTeX everywhere, colon for division.
- Data marked as examples where invented.
