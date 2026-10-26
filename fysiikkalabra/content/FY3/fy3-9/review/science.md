VERDICT: PASS
CONTENT-HASH: 89861521952abfbd

## Blocking

## Polish
- sim.js:710 and the readout line — "Lämpötila T = 20 °C = 293,15 K" still uses T for a Celsius value, while exp-2 and its column header use θ — write "θ = 20 °C, T = 293,15 K". (Carried over from rounds 1 and 2.)
- solutions.md L1-03 Järkevyys — "paine jää hieman pienemmäksi": adiabatic expansion from 1,00 l to 1,50 l gives about 244 kPa, roughly 15 % lower — "selvästi pienemmäksi" is more accurate. (Carried over.)

## Checked
- Round 3 diff since 4653608f3e8638e6 (`git diff HEAD`): the only lesson-file change is the exp-1 intro in inquiry.json. The other changed files are review/pedagogy.md and review/science.md.
- exp-1 intro: "$pV$" and "$1\,\text{kPa}\cdot 1\,\text{ml} = 0{,}001\,\text{J}$". The conversion is correct: 10³ Pa · 10⁻⁶ m³ = 10⁻³ J. The text and number are unchanged, so the round-2 polish item is fixed.
- inquiry.json parses. check_latex.py on the lesson passes with 382 fragments, including the new ones.
- Round-2 checks are carried forward unchanged. All 12 answers agree with answers.py and exercises.json. The inquiry numbers (200 kPa, 5,00 J, 60,2 ml, 0,171 ml/K, syringe products, 160 kPa) agree with my recomputation. The figures, the experiment tables and their adapter keys and units, and sim.js, sim-spec.md, answers.py and figures.py were all checked in rounds 1 and 2 and have not changed since.
- The content hash was the same at the start and at the end.
