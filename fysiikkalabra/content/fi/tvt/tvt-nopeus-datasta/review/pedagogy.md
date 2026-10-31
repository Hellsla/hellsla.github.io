VERDICT: PASS
CONTENT-HASH: 805d1699396c2a38

## Blocking

None.

## Polish

- The lead says the columns are `t`, `x`, `v`, `a` "tässä ohjeessa", but sensor runs (motion detector, phone CSV) arrive with the program's or app's own column names. Add one sentence: use the names exactly as your table shows them, or rename the columns in **Column Options** first. Otherwise `integral("a","t")` fails on real hissi data.
- Step 8 writes the offset as $\delta a$; NOTES §1 says a measurement error is $\Delta x$. Here Δ already means change, so δ is defensible, but say in one clause that $\delta a$ is a constant reading error (science reviewer to confirm the notation).
- Mistake "Siirtymä ja matka on sekoitettu" has a symptom but no fix; add e.g. "Laske matka osissa ja laske osien itseisarvot yhteen."
- Graph naming varies inside the guide: "$(t, x)$-kuvaaja", "nopeus–aika-kuvaaja" (goal 2), "paikka–aika-kuvaaja"; pick one form across the 9 guides.
- Valoportti: $b$ for flag width clashes with intercept $b$ elsewhere (see tvt-mittausohjelma).
- Opening sentence "Mittausdata on taulukko lukemia tasaisin tai epätasaisin väliajoin" is slightly elliptical; "taulukko lukemista, jotka on otettu…" reads better.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Functions (firstDerivative with n = 3, 5, 7…, integral, Pro) and tools (Tangent under Graph Tools, View Integral, View Statistics, Speed Through Gate) match the verified facts; it correctly avoids two-point successive differences.
- Order follows the data type (position → photogate → velocity → acceleration), each with what to click and why (noise amplified by small Δt, offset growing as t and t²).
- Goals match the four parts; checklist checks average vs instantaneous, area units ($\text{m}$, $\text{m/s}$) and v returning to zero.
- Formulas displayed once with symbols named; photogate example converts 1,0 cm to 0,010 m before dividing. Strips figure shows Δs ≈ v·Δt, no numbers.
- Mistakes are real ones (successive differences, fit over non-uniform part, mm not converted, offset not corrected).
- Cross-links to taulukkolaskenta, suoran-sovitus, mittausohjelma sensible; investigation titles exist. No spreadsheet/Tracker leftovers.
