VERDICT: FAIL
CONTENT-HASH: 0847076788133655

## Blocking
- fy2-7/exercises/solutions.md:149, 281, 284 and exercises.json:67, 233 — "internal energy" is still used; FY2 leaves it to FY3 (packet scope), and my previous report asked for it to be removed (the round 2 fixes did not touch it) — fix: say "thermal energy" (e.g. "converted into thermal energy of the conductors").

## Polish
(none)

## Checked
- Previous Blocking fixed: `perille` is gone; Substitution uses E_arrived throughout.
- Formula lines start from eta, E = Pt or E_sent = E_arrived + E_loss and combine correctly (E_loss = 600/0.80 - 600, dE = (p_dh - p_el) E_in, N = P t / E_house); numbers unchanged (150 MWh, 1200 kWh, 21.0 MWh, 13.0 MWh, 65.7, 12.5 MWh).
- Split paragraphs: values (9 %, 91 %) still stated.
