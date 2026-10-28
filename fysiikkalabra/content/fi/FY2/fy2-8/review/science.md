VERDICT: PASS
CONTENT-HASH: b2efb99bdf33c286

## Blocking

## Polish
- inquiry.json:301 — virhe, distractor "päästökerroin on nolla": feedback says "Laskun periaate (m = e · E) on silti oikea; virhe on laskutoimituksessa", but the student used m = E : e, a wrong formula, not an arithmetic slip. Say "Oikea kaava on m = e · E; opiskelija jakoi kertomisen sijaan."
- lesson.md:101 — the figure's aria-label contains literal "$70$"; a screen reader reads the dollar signs. Write "noin 70 kertaa".
- lesson.md (Kaava) — the symbol e (päästökerroin, g/kWh) is the same letter the chapter *Polttoaineet ja lämpöarvo* uses for ruoan energiasisältö (MJ/kg). Not wrong inside this chapter; a one-line note or a different symbol would avoid a cross-chapter clash.

## Checked
- IPCC AR5 WG III Annex III medians correct (coal 820, gas 490, dedicated biomass 230, PV 41–48 rooftop/utility, hydro 24, nuclear 12, wind 11–12 onshore/offshore); the biomass caveat (combustion CO₂ counted as zero, regrowth takes decades) is stated.
- Emissions bar chart to scale (0,44 px per g/kWh, every bar within 0,3 px); 820 : 12 ≈ 68 → "noin 70" agrees in text, caption and exit ticket.
- Worked example recomputed: 490 · 4800 = 2 352 000 g = 2,4 t; wind 57,6 kg ≈ 58 kg, ratio 41; staged, symbolic first.
- Inquiry numerics: 820 kg (mistake 820 000), 43,2 kg in virhe, 49 000 t (mistakes 0,049 and 4,9·10¹⁰), 1200 t in the model answer, trip 7,2 l · 32 MJ/l · 69 g/MJ = 15,9 → 16 kg (mistakes 13,2 and 15 900); 32 MJ/l agrees with 43 MJ/kg · 0,74 kg/l from the fuels chapter.
- Greenhouse effect qualitative and correct: solar radiation mostly passes, thermal radiation absorbed and re-emitted in all directions, −18 → +15 °C, N₂/O₂ hardly absorb, water vapour the largest; CO₂ 280 → 420 ppm (NOAA 2023), < 0,5 ‰.
- Simulation: levels −18 / +14 / +16 / +17 °C match 14 + 3·log₂(c/280) (ECS 3 °C, AR6), starts at measured +15 °C; the lag τ = 3 s gives the stated half-time ≈ 2 s; the Mallin oletukset box says it is an illustration, not a model, and names what it leaves out.
- koe-1 varies only the gas level; Teq exists in simState for every level; the 0 ppm level removes water vapour, as the intro says.
- Every choice item has exactly one correct option, distractor feedback right (ozone, "estää auringon säteilyn", gases "produce heat", coal vs biomass carbon, truck distance).
- Carbon guardrail kept: CO₂ from carbon-containing fuels, hydrogen burns to water; wind/nuclear "pienipäästöisiä, eivät päästöttömiä" consistent throughout.
- No radiative-balance model (left to FY3, named by chapter); hash identical at start and end.
