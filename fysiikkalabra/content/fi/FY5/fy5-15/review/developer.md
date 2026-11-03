VERDICT: DONE

Draft, round 1 (fy5-15 Äänen voimakkuus). check_lesson.py: every line ok; check_layout 345 px ok; test_sims 33 assertions + sweep pass.

- `lesson.md`: Ydinajatus (intensity I = P/A, point source and inverse-square law, hearing threshold I0 and pain threshold, decibel scale, perceived loudness and dB(A) qualitatively, forward reference to *Ääni ympäristössämme*); Kaava: Intensiteettitaso (I = P/(4πr²), L = 10 dB · lg(I/I0), solving I from L step by step, level differences +3/+10/−6 dB, adding independent sources); seven-stage example (96 dB at 10 m → I, P); misconceptions; summary.
- `figures.py`: hero (open-air concert), kartio (r², 4A, 9A), asteikko (dB ladder with I), kuvaaja (L(r), −6 dB per doubling), summa (intensities add, 80+80 → 83 dB).
- `inquiry.json`: hook, optional retrieval, two predictions (doubling r; second speaker), sim + two experiments, conclusion, theory, reflect, example, error spotting (log not undone), transfer (two speakers at 2 m and 4 m), checks (threshold choice, 50→70 dB ratio, optional explain), exit.
- Exercises 5/4/3 with `answers.py` and complete solutions (L3-03 a word task on negative dB); `lesson-answers.py`; exit ticket (2).
- New sim `assets/sims/fy5/fy5-15/` (P, N speakers, r, speed; I, L readout, L(r) graph), `tests/sims/fy5-15.json`, `lang/fi.json` sims.fy5-15, four glossary terms.
