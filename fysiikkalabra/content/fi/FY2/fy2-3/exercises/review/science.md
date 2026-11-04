VERDICT: PASS
CONTENT-HASH: 82920b176561defd

## Blocking
(none)

## Polish
- solutions.md:135 (fy2-3-L1-08) — the Periaate says "Moottori muuntaa energiaa tasaisesti", but the task asks for keskiteho, and an average power needs no constant rate — write "Keskiteho on muuntunut energia jaettuna ajalla".
- solutions.md:187 (fy2-3-L3-04) — "Vesivoimalan teho on satoja megawatteja": most Finnish hydro plants are tens of MW, and the largest (Imatra) is about 190 MW — write "kymmenistä megawateista noin 200 megawattiin".
- docs/exercise-bank/FY2.md:24 — the plan's level-3 stair-climb power model needs E_p = mgh (FY4, out of FY2 scope). The set was right to replace it with L3-05 (fridge duty cycle); update the plan to match.

## Checked
- Recomputed all 20 answers in one script with my own formulas (scratchpad sci_fy2_34.py). All agree within tolerance: new 30 kW, 1,96 kWh, 3,0 kWh, 1803 W, 2,8 GWh and 43,2 €.
- L2-05: per-device energies 800/280/300/400/180 Wh. The fridge is the largest consumer, as stated.
- L2-07: a least-squares fit through the origin gives 1,803 kW and a free fit 1,802 kW with intercept ≈ 0. 1800 W ± 5 % fits. The origin is justified physically (meter zeroed), and the slope is read from the fitted line (guardrail).
- L3-04: deficits +200/600/800/800/400 MW over 06–11. Peak consumption is 09–10 (10 600 MW), and at least 800 MW of balancing power plus import is needed. The data are marked as example data in "Fingrid-type" form. The hydro, wind and nuclear reasoning matches the course worksheet.
- L3-05: duty cycle 47/119 = 0,395, giving 39,5 W, 346 kWh/a, a saving of 43,2 €/a and a payback of 13,9 a. The model's assumptions are stated.
- L1-06 and L1-07: exactly one correct option, every distractor really wrong, and the feedback right (kW vs kWh, energy = P·t).
- L2-06: the error (min used as h, a factor of 60) is identified correctly.
- Levels fit and no new task duplicates an existing one. FY2 scope: no mgh, no work/force, no c·m·ΔT and no chained efficiencies in any task. Only P = ΔE/Δt, E = Pt, kWh and price.
- Conversions are shown, the unknown is solved symbolically first, and the significant figures follow the limiting datum.
