VERDICT: FAIL
CONTENT-HASH: 3b99abb0c4aac723

## Blocking
- inquiry.json:433 (check-2), lesson.md:103 — A filament lamp is said to turn only 0,12 kJ of 2,5 kJ (about 5 %) into *säteilyenergia*, and lesson.md writes "säteilyksi eli valoksi". This is false: most of a filament lamp's input leaves as (infrared) radiation, and only the visible light is about 5 %. — In check-2 (prompt, hints, solution) say *näkyväksi valoksi* / $E_\text{valo}$ instead of säteilyenergia. In lesson.md:103 write "valoksi ja lämmöksi" without "säteilyksi eli".
- inquiry.json:135–143, 204–212 (exp-1, exp-2 names/units) — The setup box and status line show "kitka = 1 (pieni kitka)" / "kitka = 0", a code that reads as a friction value of 1, and "alkukorkeus h₀" / "h₀ = 2 m" in plain Unicode (teacher's rule: everything in LaTeX). — Show the option's name (*pieni kitka*), not the index. Write the name as `alkukorkeus $h_0$` and the value as $2{,}0\,\text{m}$. If the shared experiment template cannot do that, fix it there.

## Polish
- inquiry.json:114, 116 — "lähtee levosta half-pipen reunalta", but the experiments start at $h_0 = 2{,}0\,\text{m}$ and the rims are $3{,}0\,\text{m}$ high. — Write "lähtee levosta korkeudelta $h_0$ half-pipen seinältä" (sim-spec.md likewise).
- inquiry.json:116 — "Kitka vastustaa liikettä aina yhtä suurella voimalla" brings in force, which is outside FY2's scope. — Write "kitka muuttaa jokaisella liukumetrillä yhtä paljon liikkeen energiaa lämpöenergiaksi".

## Checked
- Recomputed in one script: worked example 120 J, data 0,29 J, transfer 320 kJ, check-2 2380 J → 2,4·10³ J, exit ticket 3,8 kJ, $mgh_0 = 981\,\text{J}$.
- The sim's equation of motion (bead on a parabola, Lagrange with tangential friction μmg) is correct. Thermal energy is integrated independently, and the sum stays at 981 J.
- The model-answer values for exp-1 (63/918, 862/119, 424/557 J) and exp-2 (mechanical energy 981 → 469 → 143 J, thermal 0 → 512 → 838 J) match the simulation run. Each experiment varies only t, with h0 and friction locked, and the simState keys exist.
- Correct options and feedback right in pred-1/2, exp-1/2, virhe, check-1, check-3.
- Figure 3 is to scale (0,16 px/J, each bar 800 J), and the middle skater's height matches 300 J.
- No E_k/E_p expressions, no work, no Q = cmΔT, no chain-efficiency products. \cdot, colon division and conversion by substitution are used. The canvas and readout are LaTeX (sim-1280 shot).
- No named-source data (the table is marked simulated); the worked example is symbolic first, rounded to 10 J correctly.
