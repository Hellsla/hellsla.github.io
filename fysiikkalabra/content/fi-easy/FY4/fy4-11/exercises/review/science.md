VERDICT: PASS
CONTENT-HASH: 3cec58093328684c

## Blocking

## Polish
- solutions.md (L3-04 c and Järkevyys) — the impact speed at 80 km/h is $14{,}31\,\text{m/s} = 51{,}5\,\text{km/h}$; "noin 51 km/h" — "noin 51–52 km/h" would be exact.
- solutions.md (L2-10 Periaate) — "vain yksi vaakasuora voima: kitka" assumes air resistance is neglected; add "kun ilmanvastus jätetään huomiotta" (level C).
- exercises.json L2-10 — the answer field (69,4 km/h) follows the calculator's parameters read on 16.11.2026; if the calculator changes, the field and answers.py must follow.

## Checked
- Diff since the passed version (bab8736584): only solutions.md of L2-10, Vastaus split into paragraphs before "Lisäksi: a)", "b)", "d)", "e)"; whitespace-normalised text identical to the passed version; exercises.json and answers.py unchanged.
- All 22 numeric answers recomputed in one script with my own formulas (L2-05 a = 7,85; L2-06 60,0 km/h; L3-01 36,7 km/h; L3-02 11 253 N; L3-03 35,9 m; L3-04 fit t_r = 1,21 s, a = 5,10 m/s², 65,9 km/h; L3-05 18 kN): all inside tolerance and equal to answers.py.
- L2-10 b: 6,86; 15,43; 27,43; 42,87 m round to the calculator's 7, 15, 27, 43 m; 40 → 80 km/h four-fold.
- L2-10 c: 49,66 m < 50 m, margin 0,3 m not relied on (safe side); 100 km/h: v = 19,28 m/s = 69,4 km/h; rounded 28 m gives 69,8 km/h, inside 0.03.
- L2-10 d: 186,8 m on ice, six-fold braking distance, μ = 0,92 and 0,15 from ΣF = ma; e: ABS cannot raise μ, 1,25² = 1,56, calculator 27 → 43 m. No "muuttuu lämmöksi".
- Source values (1 s; 9 and 1,5 m/s²; rounding to a metre) exactly as in the coordinator's record; solution dated and called an example.
- L2-08: one correct option (2 : 4 = 0,50); L1-06, L1-07 one correct option each, feedback right.
- Figures ex-tv-jarrutus (45 m) and ex-tv-tyyny (10,5 kN) readable at grid crossings.
- Hash the same at the start and the end.
