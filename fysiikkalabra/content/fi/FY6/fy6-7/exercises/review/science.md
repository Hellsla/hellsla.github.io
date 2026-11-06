VERDICT: PASS
CONTENT-HASH: 5161df0334c5195f
Round: 1. One new YO-skill task, fy6-7-L1-09 (type 5, Suuruusluokka); the rest of the set was PASS before and is unchanged.

## Blocking

## Polish
- exercises.json:101 (fy6-7-L1-09) — the question asks for a suuruusluokka but the options carry two significant figures ("noin 0,060 kWh"). That is fine, but "noin 0,06 kWh" (and 0,001 kWh) would read more like an order of magnitude. Taste only.

## Checked
- Hash 5161df0334c5195f at start and end.
- All answers.py values rerun in one call: no mismatch with exercises.json.
- L1-09 recomputed: 1,2 kW · 0,050 h = 0,060 kWh. Distractors recomputed: 1,2 · 3,0/3600 = 0,0010; 1,2 · 3,0 = 3,6; 1200 · 0,050 = 60; 1200 · 3,0 = 3600. Each feedback names its real error.
- Neighbouring options are 17–60 times apart (type 5 asks for 10–100).
- The 3600 kWh option (watts × minutes) is the lesson's own warned unit mix (2000 W · 15 min ≠ 30 000 kWh); 60 kWh is the Wh/kWh confusion.
- 1,2 kW input power for a microwave oven is realistic.
- Not identifiable by form: five parallel "noin X kWh" options; the correct feedback adds no reason beyond the calculation.
- Notation E = Pt, kWh as in the brief's Tiivistelmä.
- Inline/display maths measured with KaTeX in Chrome at 390 px (formula widths only, not a page render): widest 171 px.
