VERDICT: PASS
CONTENT-HASH: afb3b91be208f94f

## Blocking
(none)

## Polish
- Previous Polish items (sim "luvun taulukon" wording, ΔE "energian muutos", glossary "teho" adding P = W/t and P = Fv, the Tilastokeskus 18 snt/kWh source) are outside this diff and still stand as before.

## Checked
- exit-ticket.json: the W → kW conversion now stands as its own sentence before the result; the order of steps and every formula and number are unchanged. 1 W = 10⁻³ kW and 5,0 W = 0,0050 kW are correct.
- Recomputed in one script: 0,0050 kW · 8760 h = 43,8 kWh ≈ 44 kWh; 3,0 min · 365 = 1095 min = 18,25 h; 2,0 kW · 18,25 h = 36,5 kWh ≈ 37 kWh (2 s.f., as the data). The conclusion (standby uses more energy) follows, and it agrees with the theory P = ΔE/Δt and E = Pt.
- lesson.md hero SVG (new in the diff, not named in the brief): a decorative picture with no numbers. Kettle clock sector ≈ 26° (short time), lamp clock sector ≈ 334° (long time), and the hands lie on the sector edges. A single meter feeds both devices. It matches the lesson's opening question (the bill depends on power and time) and draws no misleading physics; checked against the 390 px capture.
- Content hash the same at start and end (afb3b91be208f94f).
