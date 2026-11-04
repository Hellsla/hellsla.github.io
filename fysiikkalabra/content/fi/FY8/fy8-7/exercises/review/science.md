VERDICT: FAIL
CONTENT-HASH: 9c0963421a85829d
## Blocking
- exercises/solutions.md:181 and :185 (fy8-7-L3-05, Periaate and d) — A, causality: "Kynnyksen alapuolella inversiota ei ole … Kynnyksellä inversio syntyy." The task's neodymium laser (808 → 1064 nm) is the standard four-level laser: its lower laser level empties at once, so inversion exists at any pumping. The threshold is where the gain from stimulated emission grows large enough to cover the losses per round trip (output mirror, scattering, absorption). — Fix: Periaate "Kynnyksen alapuolella inversio on liian pieni: valo ei vahvistu enempää kuin sitä häviää peilin läpi ja muualle"; d) below threshold gain < losses, no laser oscillation builds up, only weak spontaneous light in all directions (P_L ≈ 0); at threshold gain = losses, above it extra pumping goes into laser light. Keep inversion as the necessary condition, not as the threshold.

## Polish
- exercises/solutions.md:160 (fy8-7-L2-06) — "kolme merkitsevää numeroa kuten tehojen … arvoissa": the powers 6,0; 5,0; 4,0 mW (and 10 mW) carry two, so the answer is 1,3 (which is also the key) — say two figures.
- exercises/exercises.json:229ff (fy8-7-L2-07, option 2 feedback) — "tuleva energia on enintään pumpatun energian suuruinen" — write "laserista ulos tuleva energia".
- exercises/exercises.json fy8-7-L1-07 — the key holds 1,34·10¹⁶ while the Vastaus gives 1,3·10¹⁶ (2 s.f. from 5,0 mW); both lie inside 2 % — consider 1.3e16.
- exercises/exercises.json:298 (fy8-7-L3-05 d) — "pumppausteholla" → "pumppaustehoilla".
- exercises/solutions.md:186 (fy8-7-L3-05) — "kaksi merkitsevää numeroa kuten tehoissa": most P_L values have three; justify the two figures by the fit's spread (tolerance 6 %) instead.

## Checked
- All 17 numeric answers recomputed in one script with my own formulas; all agree with answers.py and the keys (L1-07 1,339·10¹⁶; L2-05 0,5417 eV; L2-06 1,298; L3-04 82,22 %; L3-05 slope 0,398, threshold 24,8 mW, 0,524).
- L2-05: photon energies 2,551/2,344/2,164/2,063/2,010 eV, shrinking steps; consistent with the existing L2-03 (3,0 nm ↔ 529–530 nm).
- L2-06: fluxes A 2,039, B 1,571, C 1,636, D 1,973 ·10¹⁶ s⁻¹; order A, D, C, B and its explanation right.
- L3-04: heat 5,0 W, quantum-defect part 15,0 W·(1070/976 − 1) = 1,44 W (29 %); η_E = η_q·λ_p/λ_L = 0,750 correct.
- L1-06, L1-08, L2-07: exactly one correct option, every distractor wrong and its feedback right; energy conservation in stimulated emission stated correctly.
- New tasks follow the plan in docs/exercise-bank/FY8.md (data tasks at level 2, error analysis, level-3 modelling and graph/threshold task); no duplicate of an existing task.
- Hash identical at start and end.
