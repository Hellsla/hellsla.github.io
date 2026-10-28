VERDICT: DONE

Fix round 1; `check_lesson.py fy2-4` all ok. Exercise set untouched.

- `inquiry.json`: Koe 1 now locks the petrol engine at $P_o = 60$ kW and varies $t$ (E_o, E_a, E_h measured, η = E_a : E_o = 25 %), so it no longer reads the constant-η assumption back as a load result; intro says why P_o is locked; `values` names the device in words. Conclusion `after` koe-1 only; its prompt, model and criteria are about time (aika supistuu) and say plainly that load-independence is the model's assumption. Sim `model` box: real η depends on load (strongly for an engine, little for a motor near its rated power). Ennuste-1 feedback: "tyypillinen arvo noin 25 % (mallin arvo)" instead of "malli kumoaa/tukee", plus a hint to the hot lamp. Ennuste-2 and Koe 2 optional; their feedback gives E = P · t as the reason. "1 = 100 %" → "kerrotaan luvulla 100 %"; hook and learn values in LaTeX.
- `lesson.md`: table header "tyypillinen η", values in LaTeX, note that they are typical values (engine: steady road driving, lower at light load); % conversion explained via 1 % = 0,01; summary qualified; prose values in LaTeX.
- `exit-ticket.json`: 0,70 · 100 % = 70 %.
- `sim.js`: canvas labels ≥ 20 canvas px (14·k); η and P_a labels repositioned.
- `lesson-answers.py`, `sim-spec.md`: new Koe 1 numbers and wording.
