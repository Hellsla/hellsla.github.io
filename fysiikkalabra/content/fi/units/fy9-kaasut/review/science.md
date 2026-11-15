VERDICT: FAIL
CONTENT-HASH: 9d91dfe6c6c1bab9
Review of the recognition chart (queue 9c) and the term change against the version passed at 380511676da95b96; full on the chart, delta on the rest.

## Blocking
- B (row 7 and ARIA_KARTTA): "kaasu laajenee tai puristuu → kaasun työ, W = pΔV". W = pΔV holds only at constant pressure; in general the work is the area under the (V, p) curve. The unit's Kaava section states the condition ("Vakiopaineessa laajeneva kaasu tekee työn …; työ on (V, p)-kuvaajan alle jäävä pinta-ala"), the chart drops it, so a student would apply pΔV to an isothermal or adiabatic change. Fix: "kaasu laajenee vakiopaineessa" (or add "vakiopaine" to the choice) in the chart and the aria-label.

## Polish
- C: "sisäenergia muuttuu → ΔU = Q + W": the sign convention (W work done on the gas) is in the Kaava section; fine for a chart.
- C: "syvyys nesteessä → p = ρgh" is the overpressure in a fluid at rest; the Kaava says so, and the next row gives p = p_0 + ρgh, so the pair is right.

## Checked
- Rows against the Kaava section: force over an area → p = F/A; depth → p = ρgh; depth and air pressure → p = p_0 + ρgh (p_0 the pressure at the surface, usually air pressure: aria says so); amount of substance known → pV = nRT; state changes, amount does not → p_1V_1/T_1 = p_2V_2/T_2; Celsius → T = θ + 273,15 K (θ the numerical value, as the Kaava defines); gas expands or is compressed → W = pΔV (above); internal energy → first law; engine takes heat and does work → η = W/Q_1.
- Names agree with kaavanimet.tsv; the Johda itse result W = Q_1 − Q_2 is kept out, as decided 2026-11-12; nothing outside FY9.
- ARIA_KARTTA: same nine rows, same order and physics.
- teacher.md: only the term "tunnistuskaavio". unit.md: only the figure.
