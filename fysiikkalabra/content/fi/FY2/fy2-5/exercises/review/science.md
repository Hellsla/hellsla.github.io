VERDICT: PASS
CONTENT-HASH: e9677835c145266c

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/solutions.md:89 — L2-04 uses petrol density 0,74 kg/l, while the chapter on energy units uses 0,75 kg/l (32 MJ per litre); use one value across chapters (no effect on the answer).
- content/fi/FY2/fy2-5/exercises/solutions.md (L1-04) — "kaksi merkitsevää numeroa kuten lämpöarvossa 10 MJ/kg": 10 and 400 do not show their figures; say the answer is given to the precision of the data, 4,0·10³ MJ.

## Checked
- All 12 answers recomputed independently in one script: 86, 96, 312 000 → 310 000, 4000, 0,96 MJ; 480 kJ; 41,9 → 42 kg; 578 → 580 MJ; 4,47 → 4,5 kg; 5,21 → 5,2 kg; 3,6; 35 MW. All agree with answers.py and exercises.json, and each rounded answer is inside its 2 % tolerance.
- Heating values match the lesson table; L3-01's light fuel oil value (43 MJ/kg) is given in the task.
- Food tasks (L1-05, L2-01, L3-02) use the energy content e and say it is not a heating value (food and fuel guardrail); example values are marked as examples.
- Efficiency tasks (L2-03, L2-04, L3-03) separate released energy from useful energy and use one device's η only (FY2 scope); 35 % electrical efficiency for a peat plant and 85 % for a pellet boiler are realistic.
- L3-03 converts t → kg and h → s correctly, with 1 MJ/s = 1 MW.
- Solutions complete in seven parts, symbolic first, conversions explicit, checks real (L2-04: about 6 l per 100 km).
- Notation (E = Hm, e, η, E_sisään, E_hyöty) the same as in the lesson.
