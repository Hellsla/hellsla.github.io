VERDICT: PASS
CONTENT-HASH: fcb065ab0c26d6d6

## Blocking

## Polish
- lessons/FY6/fy6-7/lesson-answers.py:777 — the comment says "885 W" for 230 V : 0,26 A, but that quotient is a resistance (885 Ω), as the option's feedback says. Change the comment's unit.

## Checked
- Round-3 Blocking fixed: the ennuste-2 standby feedback now says $365 \cdot 21\,\text{h} = 7665\,\text{h}$, and $0{,}0030\,\text{kW} \cdot 7665\,\text{h} = 23{,}0\,\text{kWh}$. This matches the `saastot` table and the solution. "Kaksituhatkertainen" is right: 6000 W : 3 W = 2000.
- Round-3 Polish taken: lesson-answers.py has `save-kettle-kWh` = 121,7 kWh and no charger saving. The kettle feedback now reads "kolme kertaa keittimen teho".
- Kettle feedback: 365 · 10 min = 60,8 h ≈ 61 h, against 52 · 1,5 h = 78 h. The energies are ≈ 120 kWh and 468 kWh, and their ratio 3,85 = 3 (power) × 1,28 (time), so "pääosin tehosta" holds.
- ennuste-2 has exactly one correct option (sauna 468 kWh). The others are 191,6, 121,7 and 23,0 kWh, so the order in the `saastot` solution and the johtopäätös model is right.
- One script recomputed every lesson-answers.py value from the task text, and all agree. The values: 0,20 kWh (both figure areas); 3,6 MJ; 8,7 A; 8,76 kWh; 9,0 kWh = TV 90 h; 187,5 h, 150 kWh, 27 €, 5,0 kWh a day; 59,8 W and 885 Ω; the day table 0,40/0,80/0,30/0,20/0,010 kWh; the saving mistakes 38,3 and 219; 30 000 W·min and 0,50 kWh; 227 kWh, 49,86 € (mistakes 40,86 and 36,24); 9,0 kWh (5,4 and 9000); exit 7,2 MJ and 1,0 kWh.
- The reasonableness checks are real checks: 230 kWh · 0,2 €/kWh + 9 € ≈ 55 €; 7,6 kWh a day; the hair dryer costs ≈ 1,6 €; the water heater uses 6 kWh against the TV's 0,3 kWh.
- E = Pt keeps its constant-power condition. P = UI with the 230 V effective value is limited to heating devices.
- Electrical energy becomes the resistor's internal energy and transfers as heat. The glossary, the theory and tarkistus-3 say the same.
- The power–time figure is to scale (0,1 h ≈ 15,5 px, 2 kW = 189 px; 2 h = 307 px, 0,1 kW = 9,5 px), and both areas are 0,20 kWh.
- The hash is fcb065ab0c26d6d6 at the start and at the end.
