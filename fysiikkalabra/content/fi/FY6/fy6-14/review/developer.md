VERDICT: DONE

I drafted *Puolijohteet, diodi, LED ja aurinkokenno*. `check_lesson.py` passes every check, and `check_layout` at 345 px is ok.

- `lesson.md`: the Miksi question is about the LED's polarity and its series resistor. Ydinajatus covers semiconductors briefly as components, the diode's forward and reverse direction (anode and cathode), the threshold voltage and the (U, I) characteristic, the LED, why an LED needs a series resistor, and the solar cell as a DC source (I_k, U_t). `## Kaava: Etuvastus ja aurinkokennon teho` gives R = (U − U_D)/I, P = UI with the maximum power point, and η = P/(GA). Then the staged bicycle-LED example, three misconceptions and the summary.
- `figures.py`: hero, suunnat, ominaiskayra, kenno, etuvastus, teho, and the task figures ex-led and ex-kenno (both safe).
- `inquiry.json`: a retrieval item, two predictions (the LED's voltage; the load for maximum power), the sim, five experiments (2 optional), a conclusion, Etsi virhe, a transfer task (panel on a battery vs the MPP), three checks. `exit-ticket.json` has two questions.
- Exercises 5/4/3 with `answers.py` and complete solutions; `lesson-answers.py`.
- New sim `assets/sims/fy6/fy6-14` (LED circuit with a Shockley model; solar panel with its load and the light), `sim-spec.md`, `tests/sims/fy6-14.json` (77 assertions), and `lang/fi.json` sims.fy6-14. Ten glossary terms added.
