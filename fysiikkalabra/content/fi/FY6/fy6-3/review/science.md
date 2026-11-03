VERDICT: PASS
CONTENT-HASH: 63948b0ff042a09c

## Blocking

## Polish
- inquiry.json (ennuste-1 feedbacks, johtopaatos.model) — the lamp's U : I at 1,5 V is given as 8,3 Ω (model value 8,26 Ω), but a student who divides the readouts 1,50 V : 0,182 A gets 8,24 ≈ 8,2 Ω; consider "noin 8,2 Ω" or showing the readout division so the model answer matches the student's table.

## Checked
- Definitions R = U : I, ohmi, Ohmin laki (metal, constant temperature, not lamp/diode), ominaiskäyrä, resistiivisyys agree with glossary, summary, checks and exit ticket; round-1 polish (calc "jäljittelevä malli", konstantaani vs. kromnikkeli reasons) applied.
- Mechanism: ion lattice, collisions, R grows with T for metals; micro figure electrons left, I right; "virta ei kulu" correct.
- Measure-circuit figure and sim: ammeter in series, voltmeter across, long plate +, current arrows and moving dots + to −.
- Curves figure to scale (1050 px/A, 71,5 px/V): resistor line slope 9,98 Ω, lamp point (0,250 A; 3,0 V), chord 12 Ω; lamp curve shape right.
- One script recomputed: lamp 8,26 Ω / 0,182 A at 1,5 V, 12,0 Ω / 0,250 A at 3,0 V, ratio 1,38; tangent dU/dI at 3,0 V = 26,7 ≈ 27 Ω; wire 2,50/5,00 Ω, koe 4 5,00/2,50/1,25 Ω; example 4,8 m; siirto 0,408 Ω (mistakes 0,204 and 4,08·10⁻⁴); tarkistus-2 least-squares slope through origin 22,0 Ω (points 21,5–23,5 Ω); exit ticket 150 Ω and ¼; kromnikkeli/kupari ≈ 65.
- Predictions, kertaus, virhe, tarkistus-1: exactly one correct option each, distractor feedback physically right.
- Experiments isolate the varied parameter (comp; comp/U/A; comp/U/L locked); sliders reach 0,5/1,5/3,0 V, 1,00/2,00 m, 0,10/0,20/0,40 mm²; simState gives I.
- sim.js implements 10 Ω, the stated lamp model and ρl/A; model box states ideal meters, constant temperature, model values.
- tarkistus-2: origin justified physically, guardrail fit sentence used, slope from fitted line; figure (screenshot) shows the five listed points.
- tarkistus-3 model and criteria ask only what the task gives; siirto reasonableness (≈4 V of 230 V at 10 A) correct.
