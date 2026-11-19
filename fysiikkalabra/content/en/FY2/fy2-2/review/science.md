VERDICT: PASS
CONTENT-HASH: f51b02a1c1936183

## Blocking
(none)

## Polish
- lesson.md:90 (hero) — the hero shows grain → bread → cyclist, while the text, hook and chain figure follow oats → porridge; same physics, but one food throughout would keep the story consistent.
- assets/sims/fy2/fy2-2/sim.js:1191 — `tx()` always writes a decimal comma, so the English canvas and readout show "6,2 · 10^20 J" next to English text that uses "6.2" (formatting, not physics).
- inquiry.json tarkistus-1 — the correct option says "almost entirely into thermal energy", but its feedback says "in the end everything ends up as heat"; using one wording in both would be more consistent.
- inquiry.json check-c2 — the 2.2 MJ chocolate bar is half the simulation's 200 g bar (4.4 MJ). This is not a contradiction: "a 100 g bar" would make it explicit.

## Checked
- One script recomputed all of lesson-answers.py with my own formulas: 340 kJ, 3.2, Sun to Earth 1361 W/m² · πR² · 3600 s = 6.25·10^20 J (= 620 EJ in 2023), thousand years ↔ 41 days ("about 40"), 600 kJ, 1800 kJ, 66 MJ, 51 GJ, 100, 2500 J; check-c2 7.3; exit ticket 9 kJ. All agree.
- The worked example is solved symbolically first, the conversion 0.45 MJ = 450 kJ is right, the rounding is justified and the sum check is real.
- Figures: the Sankey widths are to scale (96 = 24 + 72 px ↔ 800 = 200 + 600 kJ). On the log ladder 1 J, 1 kJ, 10 MJ, 1.6 GJ and 140 TJ sit within 0.3 px of log positions at 33.2 px per decade.
- Simulation values recomputed from their stated sources: photon 3.6·10^-19 J, AA 1.35·10^4 J, banana 4.6·10^5 J, petrol 32 MJ/L, LPG 5.1·10^8 J, flight 2·10^12 J, U-235 8.2·10^13 J, OL3 1.38·10^14 J, Finnish electricity 2.87·10^17 J/yr and 7.9·10^14 J/day, Finland 1.32·10^18 J, M9 2·10^18 J (USGS), Sun 3.83·10^26 W. Estimates are labelled as estimates.
- Experiments: the initial values match the FI option keys, simState gives E_MJ and E_EJ, and varying the item is the only manipulation, so the setup is sound.
- Predictions 1 and 2, kertaus, virhe, tarkistus-1 and check-c2 each have exactly one correct option, and every distractor's feedback is right.
- Numeric tasks (ketju, siirto, tarkistus-2): the mistakes (60, 34, 51000, 351, 0.1, 0.01) are diagnosed correctly, and the significant-figure reasons hold.
- Scope: FY2 energy forms, conservation, joule and prefixes; no E_k or E_p expressions, no W = Fs, no Q = cmΔT. "Thermal energy … transferred as heat" fits the FY2 guardrail.
- The conclusion's model answer and the explain model answer match the theory, and the sim's values are called rounded orders of magnitude.
