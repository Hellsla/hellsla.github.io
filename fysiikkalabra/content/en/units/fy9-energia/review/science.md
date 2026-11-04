VERDICT: PASS
CONTENT-HASH: 44d6a17aa7d17ef6

Science review of the English translation of fy9-energia (source content/fi/units/fy9-energia/, already passed).

## Blocking
None.

## Checks done
- `python3 scripts/check_i18n.py`: en 0 errors (answers, units, tolerances, correct flags, formulas, sections, task set unchanged).
- Every number of unit.md, teacher.md, inquiry.json, exit-ticket.json, sovella/tasks.json and sovella/solutions.md compared with the Finnish as a multiset (decimal comma -> point): identical; the only difference is the dates of task 3 (7.1. -> 7 Jan), which is correct.
- Recomputed in one Python call: chain 0.90·0.45·0.98·500 MW = 198 MW; petrol 7.5·43 MJ = 320 MJ ≈ 90 kWh; 40 kWh : 2.3 kW ≈ 17 h; steam cycle 150/350 = 43 %; fuel to wheels 51 kW; pellets 3.7 t; lift 8.4 kW; phone 67.5 kJ; chip plant 110.8 MW, 157 MW, 59.4 t; pumped storage 245 MWh -> 36 MW, 289 MWh, 75 %; kettle 83.4 %; wind 5.3 GWh; diesel 2100 t; teacher's January extra 132 kWh/day, 4.1 MWh, 3.7 MWh. All agree with the translation.
- Law conditions survive the translation: isolated system, constant power for E = Pt, complete combustion and actual moisture for E = Hm, force along the motion for W = Fs, steady lifting for mgh, series stages for multiplied efficiencies, parallel plants in task 2c, extrapolation caveat in task 3, coefficient of performance not called efficiency for the heat pump, life-cycle emissions.
- Physics terminology is standard English: heat of combustion, rated power, condensing power plant, combined heat and power, overall/electrical efficiency, pumped-storage plant, dispatchable power, coefficient of performance.

## Polish
1. unit.md / figures.json, hero description: "steam rising from its chimney and cooling" reads as if the steam cools; the Finnish *jäähdytyksestä* is a place. Fix: "steam rising from its chimney and its cooling tower".
2. inquiry.json activity 7 solution and several principles (activities 10, 15, 19, task 2b, 5a): "the share of X in Y" is a Finnicism; physics English says "the fraction of the power entering it that comes out" / "the fraction of the energy taken from the grid that is stored in the battery". Meaning is correct.
