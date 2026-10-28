VERDICT: FAIL
CONTENT-HASH: b6bb4eadf0fe7919

## Blocking
- lesson.md:53, :130; inquiry.json:67, :105 — Problem: no source has a year (the scope note requires one), and some values do not match the named source. Tilastokeskus *Polttoaineluokitus 2024/2025, määritelmät* gives jyrsinturve 9–11 GJ/t at 40–50 % moisture (lesson.md:101 says 40 %) and polttopuu 13–15 GJ/t at 20–25 % moisture, so the "kuiva" puu is air-dry (fully dry wood is about 19 MJ/kg). Tilastokeskus gives maakaasu per m³n, not 49 MJ/kg (IPCC 2006: 48,0). Kivihiili 26, bensiini, diesel, pelletti and the Fineli values could not be checked (the sources were unreachable). — Fix: cite each value's table and year, use "ilmakuiva (kosteus 20–25 %)", peat moisture 40–50 % and maakaasu 48 (IPCC), and name the Fineli items ("peruna, keitetty") and the year.
- lesson.md:3 — Problem: the Miksi premise contradicts the lesson's own efficiency point. Useful energy per kg is about equal: 43 · 0,25 ≈ 11 MJ for a car and 15 · 0,75 ≈ 11 MJ for a stove. — Fix: ask why one kilogram of petrol *releases* almost three times as much energy as one kilogram of wood.
- lesson.md:1, :30, :101, :106, :133, :172, :183; inquiry.json hook, :62–67, :137, the siirto and tarkistus-2 prompts; exit-ticket.json q2–q3 — Problem: quantities and symbols are plain text ("43 MJ/kg", "6,0 kg", "40 %", "E = Hm", "0,230 kg", "1500 kJ"). The teacher's rule is everything in LaTeX. — Fix: put each one in `$…$`.
- lesson.md:152, :164; inquiry.json:338, :343, :350 — Problem: the kWh conversion is a rule ("jakamalla … 3,6"). — Fix: substitute: $90\,\text{MJ} = 90 \cdot (1 : 3{,}6)\,\text{kWh} = 25\,\text{kWh}$.

## Polish
- lesson.md:39 — Problem: 129 MJ from two-figure data. — Fix: 130 MJ.
- lesson.md:104 — Problem: a label's energy is metabolisable energy, not combustion heat. — Fix: say "vastaa lämpöarvoa".
- inquiry.json:359 — Problem: "$17 \cdot 10\,\text{MJ}$" drops units. — Fix: substitute with units.

## Checked
- All lesson and inquiry numbers were recomputed in one script, and all match.
- Figure 2's bars are to scale (68 px per 10 MJ/kg). Figures 1 and 3 are right.
- Each prediction's correct option, the feedbacks, the error-spotting item and the siirto mistakes are right.
- Scope: E = Hm, one efficiency, kWh. There is no work, no Q = cmΔT and no chain efficiency. No × appears, and division uses a colon.
- The worked example is staged, solved symbolically first, and its check is real.
