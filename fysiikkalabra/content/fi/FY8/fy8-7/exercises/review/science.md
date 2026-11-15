VERDICT: PASS
CONTENT-HASH: e49afa1dac9166f6

## Blocking

## Polish
- exercises/exercises.json:319 (L3-02) — the task asks for photons per second but `unit` is "kpl"; L1-07 uses "1/s" for the same quantity — set "1/s".
- exercises/exercises.json:237 (L2-06) — "fotonivuo" is used for N/t without being introduced; the lesson says "fotonien määrä sekunnissa" (flux is strictly per area) — say "fotonien määrä sekunnissa (fotonivuo)" at first use or drop the word.
- exercises/solutions.md:237 (L2-05 b) — "muutos hidastuu, joten ei suoraan verrannollinen" gives the weaker reason; the decisive one is that the gap decreases as the size grows, so E/d is not constant (2,55 eV / 2,0 nm against 2,01 eV / 6,0 nm) — add that sentence.
- exercises/solutions.md:33 (L1-02) — "kolme merkitsevää numeroa kuten vakioissa": the constants have four; the limiting datum is the wavelength 1550 nm — justify by it.
- exercises/solutions.md:292 (L3-05) — the example slope 0,40 is read from two raw data points (30; 2,1) and (70; 18,1); guardrails: read a slope from two points on the fitted line — take the points from the line (for example 30 → 2,08 and 70 → 18,0).

## Checked
- All 17 numeric answers recomputed with own formulas in one script: each agrees with answers.py and with the box within 0,9 % (tolerances 2–6 %).
- Solutions are symbolic before substitution with real reasonableness checks; answers.py computes each answer from the task's own data (photon energy hc/λ, P = (N/t)·hf, ratios with hc cancelled, least-squares fit of the five points above threshold: 0,398, −9,86 mW, threshold 24,8 mW).
- Rounded shown answers (1,3 · 10^16, 2,0 · 10^18, 9,2 · 10^4, 0,52) stay inside the check (tolerance or half of the last digit).
- Multiple choice L1-06, L1-08, L2-07: exactly one correct option, each distractor false and its feedback names the right reason.
- L1-09: truth values 1 false, 2 true, 3 false, 4 false, 5 true are right; 650 nm photon 1,91 eV.
- Models and assumptions stated in the task: L3-01 (no decay during pumping, lasing ends in ground state, more than N/2), L3-02 (upper bounds, 0,76 W green below 1,0 W pump), L3-04 (all pump light absorbed, rest becomes internal energy).
- L3-05 d: threshold explained as gain against losses, four-level inversion at low pumping; consistent with the lesson.
- Scope and data: inside FY8 contents; quantum-dot calculations marked Lisätietotehtävä; example data marked Esimerkkiaineisto; magnitudes realistic.
