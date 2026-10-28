VERDICT: FAIL
CONTENT-HASH: 150f1def688a5bf2

## Blocking
- lesson.md:105 — the price 20 snt/kWh is labelled "Energiavirasto, 2025", but it is unverifiable (Energiavirasto's site refused access). The published statistic is Tilastokeskus, *Sähkön hinta kuluttajatyypeittäin* (13rb): a household's total price (energy + transfer + taxes) averaged 17,6 snt/kWh in 2025, for 5 000–15 000 kWh/a. — Cite that source and value: "Tilastokeskus 2025: noin 18 snt/kWh kokonaishintana". Keep 20 snt/kWh only as an explicitly labelled round example price (esimerkkihinta).
- lesson.md:130 and inquiry.json:224 (siirto solution) — "$80\,\text{W} = 80 : 1000\,\text{kW}$" and "$2{,}5 : 1000\,\text{kW}$" are dimensionally wrong as written: 80 : (1000 kW) has the unit 1/kW. They are also not conversions by substitution (teacher rule). — Write $80\,\text{W} = 80 \cdot 10^{-3}\,\text{kW} = 0{,}080\,\text{kW}$ (substituting $1\,\text{W} = 10^{-3}\,\text{kW}$).
- lesson.md:8, 95–101, 103, 155; exit-ticket.json:12; inquiry.json prompts (e.g. ennuste-1, virhe) — quantities with units appear as plain text (2000 J, 1800 W, 0,15 kWh, the table's powers, "8760 tuntia", 43,8 kWh partly). The teacher's rule is that everything is in LaTeX. — Put every number-with-unit in $…$ (e.g. $1800\,\text{W}$:n).

## Polish
- lesson.md:103 — "pari wattia laitetta kohti" is high for current devices. EU ecodesign caps standby at 0,5–1 W; older devices draw a few watts. — Write "alle wattista muutamaan wattiin".
- lesson.md bar figure — the television is 100 W in both figures but 80 W in the table and the worked example. — Name it "esimerkkilaite" or align the values.
- inquiry.json:3 — "kilowattitunti on teho kertaa aika" — Write "energia (kWh) on teho kertaa aika": the kilowatt-hour is a unit.
- inquiry.json:18 — "sähkömittari pyörii" describes an old electromechanical meter; current meters are digital. — Write "mittarin lukema kasvaa".
- exit-ticket.json:7 — "joulina" → "jouleina". In answer 3, round 43,8 and 36,5 kWh to two significant figures (44 and 37 kWh), matching 5,0 W and 3,0 min.

## Checked
- Recomputed every lesson, inquiry and exit-ticket number (tables, predictions, siirto 21,9 kWh, check 2 800 W, mistake values, example 1,92 €): all correct.
- Both figures to scale; graph slopes match 2000, 1000 and 100 W.
- P = ΔE/Δt and its conditions (steady conversion → E = Pt) are stated. 1 kWh = 3,6 MJ is shown by substitution.
- Scope: no work, no force, no Q = cmΔT, no E_k/E_p, no chain efficiencies. No × anywhere. Written division uses a colon; formulas keep fractions.
- Worked example: seven complete stages, real check.
