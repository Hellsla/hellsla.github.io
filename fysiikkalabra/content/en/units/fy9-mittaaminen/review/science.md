VERDICT: PASS
CONTENT-HASH: 4425c0d198ddfcc1

Full science review of the English translation of fy9-mittaaminen against the Finnish source (all three source reviews PASS at dd56370e666f1ba6).

## Blocking

None.

## Polish

1. inquiry.json, Starting point 6, choice 2: "The extension of the line is only an estimate" can be misread as the spring's extension. Fix: "Extending the line gives only an estimate, since forces above $10\,\text{N}$ were not measured."
2. sovella/solutions.md, s2 a) Conversions: "$1\,\text{mm} = 1000\,\mu\text{m}$" is stated twice in one sentence. This is inherited from the Finnish source (fix there first, then re-extract), not a translation fault.

## Checked

- `python3 scripts/check_i18n.py`: en 0 errors; `practice.py check`: en/units/fy9-mittaaminen 6 tasks, 89 points (same as fi).
- Every number in unit.md, teacher.md, inquiry.json, exit-ticket.json, sovella/tasks.json and sovella/solutions.md compared with the Finnish file (comma to point): the multisets of numbers are identical in all six files. No `{,}` remains.
- Every answer, tolerance, correct flag and mistake value is unchanged (check_i18n plus a field-by-field walk of the JSON files: only text fields differ).
- Recomputed in one Python call: 2.705 g/cm³ → 2.7; Δρ = 28 kg/m³; ε = 2.70 %; k = 79.0 N/m; a = 1.24 m/s²; t = 10.0 min; θ0 = −271.7 °C; s1 v = 7.294 m/s, 26.26 km/h, Δv = 0.123 m/s; s2 79.85 g/m², 782.8 kg/m³; s3 k = 0.919, 1378 g; s4 750 g; s6 n = 1.064·10⁻³ mol, pV 2269 → 2454 (+8.2 %); s5 v = 0.477 m/s. All agree with the English text.
- Physics wording: Boyle's law, ideal gas law, systematic / random / gross error, resolution vs uncertainty, extrapolation caveats and the interpretation of slope and constant term are rendered correctly in standard English physics terms; no claim was strengthened or weakened (e.g. "does not, however, prove that the times are equal", "only a prediction of the model").
- Figure texts (figures.json): numbers, units and aria descriptions match the drawn data, with decimal points.

## Shared issues

None.
