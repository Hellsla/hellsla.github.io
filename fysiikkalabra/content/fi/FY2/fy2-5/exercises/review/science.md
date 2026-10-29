VERDICT: PASS
CONTENT-HASH: 4f4044aba1139dc3

## Blocking

## Polish
- exercises.json L1-03 — "12 000 kg" has an ambiguous number of significant figures, and the solution rounds to 310 000 MJ by the lämpöarvo; fine, but "12 t" would be clear. C-level.
- exercises.json L3-01 — the prompt asks for both masses, the difference and an explanation, but only the difference (5,2 kg) is the checked answer; say "Anna lopuksi erotus kilogrammoina".

## Checked
- Recomputed all 12 answers in one script: 86, 96, 312 000 (→ 310 000), 4000, 0,96, 480 kJ, 41,86 (→ 42), 578 (→ 580), 4,465 (→ 4,5), 5,21 (→ 5,2), 3,6, 35 MW. All agree with answers.py and exercises.json; every value is inside its tolerance.
- Figure fy2-5/lampoarvot gives maakaasu 48 at the bar, which is to scale; the alt text matches.
- Models: E = Hm, m = E : H, η = E_hyöty : E_sisään and P = E : t are correct; the conditions are met and the units are consistent (GJ, t, kJ/100 g, 1 MJ/s = 1 MW).
- Magnitudes are realistic: 4,5 kg of petrol per 100 km is about 6 l; 100 MW of fuel power and 35 MW electrical for the peat plant; 18 MJ/kg for trail food.
- Food tasks are marked as example values and call the energy content the body can use, not a heating value (guardrail wording).
- Solutions are complete and symbolic first; the reasonableness checks are real checks.
- Scope: no chain efficiencies or FY3 content.
