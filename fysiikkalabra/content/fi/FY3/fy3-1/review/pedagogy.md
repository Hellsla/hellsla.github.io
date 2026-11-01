VERDICT: PASS
CONTENT-HASH: 62daa651fbd9a7eb

## Blocking
- none

## Polish
- content/fi/FY3/fy3-1/lesson.md:214 — "sillä $1\,\text{N}$ = $1\,\text{kg}\cdot\text{m/s}^2$" splits one equation into two maths spans with a plain "=" between — "sillä $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$".
- content/fi/FY3/fy3-1/inquiry.json:222,226,230 — the calibration feedback divides with "/" while the lesson now writes "1{,}62 : 9{,}81"; one notation would read more consistently.

## Checked
- Finnish case endings after re-set maths are right: $1\,\text{N}$:ksi, $2\,\text{N}$:ksi, $8{,}0\,\text{N}$:n voima, $20\,\text{N}$:n voimalla, $1{,}6\,\text{cm}$:n venymää, $5{,}6\,\text{cm}$:iin, $98{,}1\,\text{N}$:sta $294\,\text{N}$:iin, $1180\,\text{N}$:sta, $12\,\text{N}$:n lukemaa; punctuation stays after the closing $.
- Ratio "($1{,}62 : 9{,}81 \approx 0{,}17 \approx 1 : 6$)" reads naturally as "noin kuudesosa"; same for Mars 0,38.
- No change of meaning, task wording, options, feedback logic or order anywhere in the diff; predictions still gated, experiments unchanged.
- Forcemeter figure (capture fig-2): red G/2G arrows match the sim's red weight arrow, pointer and bars — colour now carries one meaning across figure and sim; labels G, 2G keep it from relying on colour alone.
- Simulation (capture sim-390): gridlines 50…200 N reach close to the 248 N full-scale line, so the Jupiter bar is readable; caption "kaavion asteikko 0–248 N" no longer reads as the spring ruler's scale (0–2500 N), and the readout sentence explains it.
- Learning path, staged example (one step per stage), opening question answered in "Kaava: Paino", workload one lesson — unchanged since the PASS at ee6b2ec.
- Exit ticket still tests the core proportionality idea; answer $7{,}5\,\text{cm}$ correct.
