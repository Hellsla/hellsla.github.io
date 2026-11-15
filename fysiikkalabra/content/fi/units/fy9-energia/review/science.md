VERDICT: FAIL
CONTENT-HASH: b9b329ae41043878
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- A (internal consistency) `sovella/solutions.md`, fy9-energia-s7 c, closing paragraph: "Ajamiseen jää siksi vähemmän energiaa kilometriä kohti kuin leudolla säällä, ja toimintamatka lyhenee." The task asks why the energy used per kilometre grows, and the mechanics bullet just above says the work against the resistive forces per kilometre is larger; the sentence states the opposite (less energy per kilometre for driving). Corrected: "Jokainen kilometri vaatii siksi akusta enemmän energiaa kuin leudolla säällä, ja kylmästä akusta energiaa saadaan vähemmän, joten toimintamatka lyhenee."

## Polish
- A: s7 b reasonableness: the measured 21,2 and 21,6 kWh/100 km are from long-range cars; one clause saying the model car's mild-weather 17 kWh is itself an assumption would keep the comparison honest.
- B: `site/` is not rebuilt on this branch (built pages still show "lämmöksi" and the one-line derivation), so the changed aligned block in `unit.md` was judged from source only.

## Checked
- Every item 18 hunk (inquiry.json feedbacks and solution, solutions.md s1, s4 d, s6 c–d, tasks.json s4 criterion, unit.md, figures.py aria): sisäenergia / "siirtyy lämpönä ympäristöön" used correctly; fridge share 1,08/1,54 = 70 %.
- s7 recomputed in one script: -28,9 / -42,9 / -45,8 %, mean 39,2 %, wrong 41 %; 16,67 and 26,88 kWh/100 km, 279 km, factor 1,61, 600 N, wrong 23 kWh; 27 K, 52 K, 15 kWh = 1/5, density +15,8 %. All agree with tasks.json, solutions.md and answers.py; `practice.py check` OK (7 tasks, 105 points; s7 3+4+4+2+2).
- Rubrics ask only what the parts ask; b's assumption criticism and d–e reasoning are sound. The claim that the longest-driving car lost the largest share holds for the table (Lucid); the other 21 cars could not be checked offline.
