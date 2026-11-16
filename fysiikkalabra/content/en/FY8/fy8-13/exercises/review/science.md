VERDICT: PASS
CONTENT-HASH: 5b4cdf65b9dd2961
Mode: delta (added aineisto task fy8-13-L2-09, caption badges removed)

## Blocking
(none)

## Polish
- exercises/solutions.md:278 — "$8760\,\text{h}$, which is the exact number of hours in a year" holds for a common year (a leap year has 8784 h) — write "the task's year of $8760\,\text{h}$ is exact".

## Checked
- Recomputed: H = 0.10 µSv/h · 8760 h = 876 µSv = 0.876 mSv → 0.88 mSv; answers.py 0.876; relative tolerance 0.02 (0.862–0.898) fits; two figures from 0.10 µSv/h justified.
- Radon share 4/5.9 = 67.8 % → 68 %; 0.876/5.9 = 14.8 % ("about 15 %"); 5.9 − 0.88 = 5.0 mSv correct.
- Source facts (5.9 mSv total, radon 4 mSv and "two thirds", other natural 1.1 mSv, medical 0.76 mSv, external terrestrial 0.45 and cosmic 0.33 mSv) match the verified list; 0.45 + 0.33 = 0.78 mSv correct.
- Part a) lets the student choose the sources and gives a dated example, as required for a reading-dependent part.
- Part d) mechanism right: radon progeny's alpha radiation irradiates the lungs from inside and is not seen by an external meter; internal K-40 and medical doses are the solution's own reasoning, not attributed.
- Principle H = Ḣt with the constant-rate condition stated; symbolic before substitution.
- Caption changes "(example data)" removed: no number changed; the task texts still say the data are example data (L2-05 names STUK-A263 as basis).
- Hash 5b4cdf65b9dd2961 at start and end.
