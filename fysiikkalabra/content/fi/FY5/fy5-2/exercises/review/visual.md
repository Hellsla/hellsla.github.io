VERDICT: PASS
CONTENT-HASH: 37db2f4776a48d36

## Blocking
(none) Round 3: the round-2 Major is fixed. The L1-01 answer box now shows "N" next to the task asking for a force, and the shown answer is $960\,\text{N}$.

## Polish
- [Minor] fy5-2-L1-01 text — "vaakasuunnassa" appears twice in one sentence pair ("on vaakasuunnassa ... päässä naulasta ... vaakasuunnassa ... päässä tukipisteestä"); one "vaakasuunnassa" for both distances would read lighter, for example "Raudan tukipiste ja käden vaikutuspiste ovat vaakasuunnassa ...". Optional.
- [Minor] solutions.md L2-03 Kaava — a single 100-word paragraph with four "koska/joten" steps; split it into the construction and the tangent step. Carried over from round 2.
- [Minor] `hylly` figure — $\tfrac{d}{2}$ is dimensioned on the floor, while the leg it names runs along the tilted base. Carried over from round 2.

## Checked
- Round 3 delta (exercises hash 37db2f4776a48d36). The captures were stale, so I regenerated them (`screenshot.py fy5-2 --if-stale`), then opened open-exercises-1280-1: L1-01 with the new text and unit, and its Annettu, Periaate, Kaava, Sijoitus and Vastaus blocks. The layout survived, rows align at "=", and units are upright.
- The diff since round 2 (`git diff HEAD~1` on exercises) touches only the L1-01 text and unit; no other exercise, solution or figure changed. The round-2 reviews of `hylly` and `kyltti` still stand.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
