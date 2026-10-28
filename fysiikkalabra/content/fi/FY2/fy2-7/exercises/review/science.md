VERDICT: PASS
CONTENT-HASH: 95d069fcaa4bb4ac

## Blocking

## Polish
- solutions.md:108 (L3-02) — The answer "$13{,}0\,\text{MWh}$, kolme merkitsevää numeroa" is overstated. The difference of 455 and 442 MWh is known only to about 1 MWh, because 500 and 520 MWh limit the precision. — Use "$13\,\text{MWh}$, kaksi merkitsevää numeroa, koska erotus on pienten lukujen erotus". The answer field 13.0 can stay.
- solutions.md:96 (L3-01) — "$91{,}0\,\% = 0{,}910$" skips the substitution step "$91{,}0 : 100$" that every other solution shows. — Add it for both η.
- solutions.md:77 (L2-03) — "$96\,000\,\text{MWh} : 8760\,\text{h} = 10{,}96\,\text{MW}$" uses the unit step MWh/h = MW without stating it. — In Muunnokset, add "$1\,\text{MWh} : 1\,\text{h} = 1\,\text{MW}$".

## Checked
- I recomputed all 12 answers independently in one script. All match answers.py and exercises.json within tolerance: L2-03 gives 10,96 → 11, L3-01 21,04 → 21 and L3-03 65,7 → 66.
- Round 1 is fixed. All task texts are in LaTeX. L3-03 converts kWh to MWh by substitution. The L2-03 Kaava is symbolic, with $p$ as the loss share. The answer and the solution agree in every task.
- The wrong-base misconception (taking the share of the delivered energy) now falls outside tolerance in L1-01 (496), L2-01 (120), L2-02 (1440), L2-04 (1152) and L3-01 (18).
- L2-02 converts GWh to MWh by substitution, and L2-03 converts TWh to MWh by substitution.
- Each principle fits its task: the loss share is taken of the energy (or power) sent; steady power times time gives energy; L3-02 compares the delivered energies.
- The magnitudes are realistic: house heating 20 MWh a year, battery and network losses 4–20 %, and an 11 MW mean loss power for 2,4 TWh.
- The reasonableness checks are real: sums back to the input, estimates, and the 25 % ratio in L2-04.
- No FY3 content and no chain-efficiency product. There is no ×, and written division uses a colon; the solutions keep their fractions only in formulas and substitutions.
