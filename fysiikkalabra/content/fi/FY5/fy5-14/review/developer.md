VERDICT: DONE

Round 1 draft of *Äänen ominaisuudet*.

- `lesson.md`: Ydinajatus (longitudinal pressure wave, speed of sound by medium and temperature with a table, measuring it by echo, two microphones and resonance tube, pitch and hearing range, infra- and ultrasound, timbre and the harmonic series $f_n = n f_1$, FFT spectrum); `## Kaava: Huojunta ja Dopplerin ilmiö` (beats, moving source, moving listener, sign rule and conditions); seven-stage example (train horn passing); misconception; summary. Forward references only to *Äänen voimakkuus* and later ultrasound imaging.
- `figures.py`: hero (ambulance), six theory figures, two task figures (spectrum, beats envelope).
- New sim `assets/sims/fy5/fy5-14/`: Doppler from wavefront geometry (arrival intervals, no formula), source or listeners moving, frequency line; `tests/sims/fy5-14.json` 36 assertions; `lang/fi.json` `sims.fy5-14`.
- `inquiry.json`: two predictions, two experiments, conclusion, FFT spectrum reading, hands-on FFT task (generic Graphical Analysis steps), beats graph task, error spotting, transfer (whirled buzzer), three checks.
- Exercises 5/4/3 with `answers.py` and full solutions; `lesson-answers.py`; exit ticket (2); nine glossary terms.

Checks: `check_lesson.py` all ok; layout 345 px ok. Open: `lang/en.json` lacks `sims.fy5-14` (translation step).
