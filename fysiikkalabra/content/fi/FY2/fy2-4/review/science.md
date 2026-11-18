VERDICT: PASS
CONTENT-HASH: 12d8ba386bbe77ca

## Blocking

## Polish
- inquiry.json:396 — the feedback says the heating of "johdot" is useful. That is true only for the cord inside the room. Losses in the supply line lie outside the boundary set at the socket, so this is a fair simplification (C). — optional: "patterin ja sen johdon lämpeneminen huoneessa".

## Checked
- koe-1 intro (inquiry.json:117): removing the stated 25 % changes no physics. It still says the efficiency is a model input, not measured. The intro still locks P_o = 60 kW and varies only t. The typical 25 % stays in the prediction feedback (lines 62–75) and the sim's model box (line 113), so the text stays consistent.
- koe-1 conclusion (inquiry.json:257–258): recomputed in my own script. 60 kW · 10 s = 600 kJ, E_a = 150 kJ. 60 kW · 20 s = 1200 kJ, E_a = 300 kJ. P_a = 15 kW and the losses are 75 %. All agree with the model answer.
- Removing the run-time question and its criterion is sound. The model's efficiency is constant by assumption, so "does not depend on run time" would be circular as a conclusion from the experiment. The remaining "aika supistuu" reasoning and the model-assumption caveat are correct.
- The remaining criteria (inquiry.json:259–262) ask only what the new prompt asks.
- check-patteri, new 50 % distractor (inquiry.json:395–396): it is really wrong, and its feedback names the right mechanism (the heat is the useful output, about 100 %). The guardrail says a resistance heater is practically 100 %. Exactly one option is correct (line 386). The other distractors' feedback is unchanged and right.
- The content hash was the same at the start and the end (12d8ba386bbe77ca).
