VERDICT: DONE

Changed (solutions only, no answers or numbers altered):
- solutions.md: all 17 blocks now have Periaate (principle and why it applies: constant pressure, energy conservation, cyclic engine, same useful powers) and Muunnokset (each conversion, or why none is needed); Kaava ends in the solved unknown; Vastaus gives value, unit and why that many figures; Järkevyys has real checks (estimates, energy balance recomputed, limiting cases). Numeric errors found: none. One unsupported claim fixed in L3-03 (electric car 17 kWh now derived as 15 kWh / 0,90); L3-02 answer written 9,60 MWh (three figures like the data).
- lesson.md Esimerkki: restructured into the seven stages (the old "Pelkkä sähkö" and "Yhteistuotanto" stages merged into one Sijoitus; added Periaate, Yksikkömuunnokset, Tulos); problem text and figures untouched.
- inquiry.json: added solutions to exp-1 question, suunnittele question, siirto (replaced, completed) and check-2 (new, with Kuvaajan lukeminen).

## Rounding pass
- exercises.json (text only), zeros so the stored answers are supported: L1-01 480 -> 480,0 kPa; L1-03 4300/1600 MW -> 4,30 * 10³ / 1,60 * 10³ MW (Vastaus 37 % -> 37,2 %); L1-05 2,6/12 kWh -> 2,60/12,0 kWh (Vastaus 22 % -> 21,7 %); L2-03 700 J -> 700,0 J; L2-04 40 % -> 40,0 %; L3-01 40 % and 90 % -> 40,0 % and 90,0 %; L3-03 6,0 l, 80 km/h, 0,75 kg/l, 43 MJ/kg, 28 % -> 6,00, 80,0, 0,750, 43,0, 28,0 (Vastaus 12 kW -> 12,0 kW). 100 km is the defining length of the consumption unit. No value, answer, tolerance or answers.py changed.
- solutions.md: L2-03 old reason ("sadan joulen tarkkuudella kuten lämmössä 700 J") would have made 500 J one figure; replaced by the work W = 200 J. L3-02: 16,0 - 6,40 = 9,6 (decimals of 16,0), so Vastaus 9,60 -> 9,6 MWh (stored 9.6 unchanged). L1-04: reason names the tens precision of 840/670 kJ. Other Vastaus reasons name the limiting data.
- inquiry.json: exp-1 (p = 200 kPa is the simulation's set value), design task (0,40/0,45 limit; 300/500 MW and ε are design values read as two figures; ε written 3,0), siirto 9,0 MW/3,5 -> 9,00 MW/3,50 (the old reason "last digit kept so that rounding does not distort" was not a precision argument), check-2 (dV = 3,0 l).
- lesson.md Esimerkki Tulos: whole-MW data, differences known to the MW.
