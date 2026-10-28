VERDICT: PASS
CONTENT-HASH: b7c0632dd1e64252

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- content/fi/FY3/sovella/solutions.md:95 — "$P = UA\Delta T$" brings in a U-value that the course never introduces; the sentence works without the formula ("sitä suuremmalla teholla, mitä suurempi lämpötilaero").
- tasks.json (fy3-s3 a) / solutions.md:170 — the bubble is taken to have the water temperature already at the bottom, though exhaled air starts near 37 °C. Saying in the task "kun kupla on jäähtynyt veden lämpöiseksi, sen tilavuus on 4,0 cm³" removes the ambiguity.

## Checked
- Round-1 item resolved: fy3-s3 c now states in the task "Oleta, että ilma on yhtä lämmintä säiliössä ja keuhkoissa." (tasks.json:355); the criterion asks the student to use the given assumption; the solution's Periaate says "Tehtävän mukaan …". The d-part can still ask the student to judge this assumption, and its model answer (about 10 % longer, 310/279 ≈ 1,11) stays right.
- Answer 36 min (725 l at 248 kPa, 20 l/min) is unchanged; the points still add up to 15.
- The changed lines are grammatical and change no other physics.
- The rest is unchanged since my full review at e4fe071f5de168b6 (collector 237 W, η 0,59, loss 119 W; cooker 117 °C, 0,13 kg, 3 %; bubble 10 cm³, lungs 15 l).
- Hash identical at start and end.
