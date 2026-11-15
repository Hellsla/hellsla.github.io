VERDICT: PASS
CONTENT-HASH: f6ad08df6e7380d7
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- A `sovella/tasks.json` s7 c, criterion 4: "Lämmitykseen ja häviöihin kuluva energia on siksi poissa ajamisesta" still uses the budget wording the solution's closing sentence dropped. Not wrong, but the criterion could mirror the new sentence: "Siksi jokainen kilometri vaatii akusta enemmän energiaa, ja toimintamatka lyhenee."
- B Outside this delta (untouched text, not judged in the verdict): `sovella/solutions.md` line 223 (s4), the inline formula $T = \dfrac{E_\text{muu} - E_0}{k} = \dots = 16{,}5\,^\circ\text{C}$ reaches 466 px on a 360 px screen when the solution box is open. Break it into an `aligned` display.
- C s7 d: "jäi suhteellisesti eniten ilmoitetusta" is elliptical for plain language; "jäi prosentteina eniten ilmoitetusta toimintamatkasta" is easier.

## Checked
- s7 c closing sentence (round-1 Blocking of the science review): now says each kilometre takes more energy from the battery and, separately, that a cold battery gives less; agrees with the question (consumption per km), with b's caveat and with the three bullets above it. Fixed.
- s7 c criteria: the combustion-car remark is gone from the criterion and stays in the model answer as extra; the electricity criterion now accepts either of two points, each observable; sum still 4.
- s7 d prompt: situation first, question last; matches the criteria and the solution. s7 e prompt now asks for the three factors its first criterion rewards.
- s7 b Järkevyys: the new two sentences replace the opaque one and read clearly.
- `unit.md`: the gloss of sisäenergia is correct and sits at the term's first use (line 291).
- Preview at 360 px, all boxes open: s7 has no clipped element and no raw TeX.
