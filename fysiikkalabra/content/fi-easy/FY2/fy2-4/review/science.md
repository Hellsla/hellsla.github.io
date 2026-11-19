VERDICT: PASS
CONTENT-HASH: eda4ea09580287e0

## Blocking

## Polish
- inquiry.json check-patteri, option "Noin 50 %" feedback — "patterin ja johtojen lämpeneminen on hyötyä" holds for the heater and its cord inside the room; the building's wiring outside the room is a (tiny) loss. Optional: "patterin ja sen johdon lämpeneminen huoneessa" (C level, not blocking).

## Checked
- koe-1 intro: the reworded sentence still says the 25 % efficiency is a model input, not measured; Po locked at 60 kW, only t varied, setup isolates t as before.
- koe-1 conclusion: model answer recomputed, 60 kW x 10 s = 600 kJ, x 20 s = 1200 kJ; 25 % gives 150 kJ and 300 kJ; 15 kW : 60 kW = 25 %; 75 % losses. All correct.
- Removing the "Muuttuiko se..." question and its criterion leaves prompt, model answer and the three remaining criteria consistent (the "aika supistuu" criterion still matches "laskettu energioista ja tehoista").
- Model answer still states the constant-efficiency assumption and the real engine's load dependence (condition kept).
- check-patteri: exactly one correct option (lähes 100 %); new distractor "noin 50 %" is genuinely wrong and its feedback gives the right reason (heating is the useful output, energy conservation), in line with the guardrail that a resistance heater's efficiency is practically 100 %.
- Other three options and feedback unchanged and consistent with the new one; no "minkään laitteen hyötysuhde ei voi olla 100 %" claim left in the diff.
- Hash eda4ea09580287e0 at start and end.
