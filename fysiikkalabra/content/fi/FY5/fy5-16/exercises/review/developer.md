VERDICT: DONE

Queue 19, round 1; no proofreading fixes listed.

**New task:** `fy5-16-L2-10` (teacher's label FY5-A5, Työterveyslaitos – Melu), kind data + reasoning, parts a)–d) in the teacher's order. Answer box: part c), $1{,}0\,\text{h}$ (`answer` 1.0, unit h, tolerance 0.03; answers.py: 8 h : 10^0,9 = 1,007 h). In fi, en and fi-easy; solved from $I_1 t_1 = I_2 t_2$, the 3 dB rule as the check.

**Tarkennukset**
- "raja-arvoihin" → "viitearvoihin (toiminta-arvot ja raja-arvo)": on the page 85 dB(A) is the upper action value, the limit value is 87 dB(A).
- c) says that 85 dB is the upper action value of the source's table and asks what follows from it and where 94 dB lies against the limit value, so the source is needed; the intensity ratio by part b)'s method.
- d) adds "Perustele laskuillasi ja aineiston viitearvoilla."
- Overlap: the chapter's formula section itself gives "94 dB, n = 3, 8 h : 8 = 1 h", and L2-02 of this set uses 94 dB with 85 dB / 8 h (dose 150 %). Teacher's numbers kept; the teacher decides whether to change them.
- English: the three values cannot be printed as numbers (check_i18n requires the same formulas as the Finnish text, which must not print them); they are given in words relative to 85 dB ("five decibels below", "two decibels above").

**Notes**
- Lint warning: the solution has 537 words (four parts); kept complete.
- Checks: lint 0 errors, check_solutions ok, check_i18n clean for fy5-16.
