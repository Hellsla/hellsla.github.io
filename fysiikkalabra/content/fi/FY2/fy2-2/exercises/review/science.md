VERDICT: PASS
CONTENT-HASH: d15c8d91aa20aab0
Mode: delta
Round: 3

## Blocking
(none)

## Polish
- content/fi/FY2/fy2-2/exercises/exercises.json (L1-09 text) — "Pellettikattilan lämpöenergia on 1 MJ" gives a boiler a stored "lämpöenergia" value, which has no clear meaning (heat is energy in transfer). Write e.g. "Pellettikattila luovuttaa veteen lämpönä 1 MJ energiaa."
- solutions.md L1-09 Muunnokset — "1 000 000 : 1000 kJ" mixes a pure number with the unit; "1 000 000 J = (1 000 000 : 1000) kJ" is clearer.

## Checked
- Hash d15c8d91aa20aab0 at start and end; the delta packet and the diff from round 2 (9fd1b2088) to HEAD show one changed line, in solutions.md L1-09.
- That line only changes the label "**Vastaus:**" to "**Mallivastaus:**". Its text is the same: correct option 1000 kJ; 1000 J = 1 kJ; 1 000 000 kJ = 1 GJ; 1000 GJ is 10^6 times too large. All are still correct.
- exercises.json, answers.py and the other solution steps are unchanged, so the round-2 checks still hold: exactly one correct option, every distractor's feedback names its real value, and the task stays within J/kJ/MJ/GJ.
