VERDICT: FAIL
CONTENT-HASH: e4fe071f5de168b6

## Blocking
- content/fi/FY3/sovella/tasks.json:355 (fy3-s3 c) — (B, guardrail "State the model's assumptions in the task", which names exactly this case: "the air at the same temperature from the tank to the lungs") the task text does not state that the air is assumed to be at the same temperature in the tank and in the lungs. The criterion at :363 instead awards a point for the student making that assumption, and the solution and d-part rely on it. — Add to the task text "Oleta, että ilma on yhtä lämmintä säiliössä ja keuhkoissa." and reword the criterion at :363 to "Käyttää annettua oletusta: kun lämpötila on sama, ilmamäärä on verrannollinen paineen ja tilavuuden tuloon (Boylen laki)." d can still ask the student to judge this assumption; the model answer's third bullet (about 10 % longer) stays right.

## Polish
- solutions.md:95 — "$P = UA\Delta T$" brings in a U-value that the course never introduces; the sentence works without the formula ("sitä suuremmalla teholla, mitä suurempi lämpötilaero").
- tasks.json (fy3-s3 a) / solutions.md:170 — the bubble is taken to have the water temperature already at the bottom; exhaled air starts near 37 °C. Saying in the task "kun kupla on jäähtynyt veden lämpöiseksi, sen tilavuus on 4,0 cm³" removes the ambiguity.

## Checked
- One Python run recomputed every number: s1 237 W (tangent 0,85 K/min), 229 W and 223 W from the 5 and 10 min chords (inside the accepted 220–250 W and the tolerances), η = 0,594, late rate 0,425 K/min, loss 119 W, levelling near 80 °C; s2 181 kPa → 117,0 °C by interpolation, 288 kJ → 0,127 kg (0,130 kg with r = 2,21 MJ/kg), 3,15 % flashing, about 43 g ≈ 70 l of steam; s3 248,15 kPa, bubble 10,3 cm³, lungs 14,7 l, 725 l → 36 min, 89 min at the surface, 310/279 ≈ 1,11.
- The collector data follow a Newton-type warming curve (T∞ ≈ 80 °C), are labelled as model-made, and the boiling table matches handbook values for water.
- Guardrails: heating linear only while losses are small (b's reason), net heat transfer to the air, efficiency ≤ 1 with the useful power defined; the pressure cooker task states only steam under the lid and potatoes at the pot's temperature, and the solution says the cooker is opened only after the pressure has fallen; the diving safety sentence is the agreed wording.
- Gauge vs absolute pressures handled correctly (s2 a, s3 c), with the reason why the gauge difference equals the absolute difference.
- Rubrics: every criterion matches its part; points add up to 15 per task; other correct methods accepted (r at 117 °C, 116–118 °C carried into d).
- Scope inside FY3 (pV = nRT, Q = cmΔT, Q = rm, hydrostatic pressure).
- Hash identical at start and end.
