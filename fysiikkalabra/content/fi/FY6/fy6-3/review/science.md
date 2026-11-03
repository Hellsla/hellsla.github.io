VERDICT: PASS
CONTENT-HASH: 4ad54aac3ad98100

## Blocking

## Polish
- inquiry.json:117 (simulaatio.calc) — "Kaava on kokeellisiin mittauksiin sovitettu malli" claims a fit to measurements that the lesson does not source; the parameters (1,0 Ω, 12,0 Ω, exponent 0,6) are chosen to imitate a 3 V lamp — write "todellisen lampun käyttäytymistä jäljittelevä malli, ei fysiikan laki".
- lesson.md:392 — "muuttuu lämpötilan mukana hyvin vähän, joten niistä tehdään vastuksia ja lämmityslankoja": small temperature dependence is the reason for precision resistors; for heating wires the reason is the high resistivity (and heat/oxidation resistance), which the next paragraph gives — consider "...vastuksia; suuren resistiivisyytensä vuoksi kromnikkelistä tehdään lämmityslankoja".

## Checked
- Definitions R = U : I, ohmi, Ohmin laki (metal, constant temperature), ominaiskäyrä, resistiivisyys agree with glossary, summary and checks.
- Microscopic cause (ion vibration, collisions, R grows with T for metals) correct at level; micro figure: electrons left, I right.
- Measure-circuit figure and sim: ammeter in series, voltmeter across, conventional current + to −, long plate +.
- Curves figure to scale: resistor through (0,30 A; 3,0 V) = 10 Ω, lamp (0,25 A; 3,0 V) = 12 Ω, dashed chord; lamp curve shape correct.
- Recomputed in one script: lamp model 8,26 Ω / 0,182 A at 1,5 V, 12,0 Ω / 0,250 A at 3,0 V, ratio 1,38; wire 2,50 / 5,00 Ω, 0,600 / 0,300 A; koe 4 5,00 / 2,50 / 1,25 Ω; example 4,8 m; siirto 0,408 Ω (mistakes 0,204, 4,08·10⁻⁴); tarkistus-2 least-squares slope 22,0 Ω; exit ticket 150 Ω and ¼.
- Etsi virhe: tangent dU/dI at 3,0 V = 26,7 Ω ≈ 27 Ω, chord 12 Ω; exactly one correct option, distractor feedback right.
- Predictions 1–2: one correct option each, feedback numbers match the model.
- Experiments isolate the varied parameter (comp/U/A or comp/U/L locked); simState gives I; slider steps reach 1,00/2,00 m and 0,10/0,20/0,40 mm².
- sim.js implements R = 10 Ω, the stated lamp model and ρl/A; model box states ideal meters and constant temperature; values called model values.
- Hook/table: nichrome/copper ratio ≈ 65 ("yli 60-kertainen") correct; table values within textbook ranges.
