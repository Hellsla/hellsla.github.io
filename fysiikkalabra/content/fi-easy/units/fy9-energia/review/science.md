VERDICT: FAIL
CONTENT-HASH: 0d6428d22f2ec290
Review of the recognition chart (queue 9c) and the term change against the version passed at db991bf31ee21542; full on the chart, delta on the rest.

## Blocking
- A (term, contradicts the unit's Kaava and glossary): the first row "suljettu järjestelmä → energia säilyy, $E_\text{alussa} = E_\text{lopussa}$" (aria: "Suljettu järjestelmä: energia säilyy"). A closed (suljettu) system can still exchange energy as heat and work; the Kaava section (fi-easy unit.md 285) and glossary.json ("eristetty systeemi": "Suljettuun systeemiin energiaa voi vielä siirtyä…") use **eristetty systeemi**. Fix in figures.py rows and ARIA_KARTTA (fi) and in figures.json (fi-easy key and value): "eristetty systeemi" (or "ei energiaa sisään eikä ulos").

## Polish
- C: "voima siirtää matkan → W = Fs" holds for a constant force along the displacement; the sign implies it.

## Checked
Rows: P = ΔE/Δt, E = Pt (steady power), 1 kWh = 1000 W · 3600 s = 3,6 MJ (recomputed), η = W_a/W_o (MAFY symbols, matches Kaava 306), η = η1η2η3 for devices in series, Q = Hm, W = Fs. fi-easy aria-label matches the chart row for row; "hyötyenergia jaettuna otetulla energialla" is right. teacher.md: teacher.md: käsitekartta -> tunnistuskaavio only, no physics changed.
