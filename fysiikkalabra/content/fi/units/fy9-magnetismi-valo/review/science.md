VERDICT: PASS
CONTENT-HASH: 3197e5705c13d2c3

# fy9-magnetismi-valo: science review

Round 2 (delta review of round 1 fixes; round 1 hash 26e396a49ac8db69)

## Blocking
None.

## Verified
1. **Round 1 Blocking 1 (hook: 40 kW sent vs used): fixed.** `inquiry.json` hook.text: "kaapelia pitkin siirretään mantereelta enintään 40 kW:n teho"; `unit.md` Ydinajatus answer paragraph: "Kaapelia pitkin siirretään mantereelta 40 kW:n teho". No "käyttävät … 40 kW" remains. The `siirto` figure (P = 40 kW sent; 230 V: 174 A, 15 kW = 38 % lost, "perille 25 kW"; 20 kV: 2,0 A, 2,0 W, "perille lähes 40 kW") now agrees with the text. Recomputed: I = 173,9 A, RI² = 15,1 kW (37,8 %), delivered 24,9 kW; 2,0 A, 2,0 W (0,005 %).
2. Polish 2: Malus θ defined separately from the grating θ in Kaava: Valo. Done.
3. Polish 3: "kun valo tulee lähes kohtisuoraan" added for 2nd. Done.
4. Polish 4: `sirius` 9.925 feedback now "Käytit kerrointa 10⁻⁶, joka kuuluu mikrometreille". Done.
5. Polish 5: s2 a) Vastaus and units_precision rubric. Recomputed α_r for Δn = 0,014/0,015/0,016: 82,09°/81,81°/81,54°, so about 0,3° per 0,001, as stated; rubric accepts 81,8°/8,2° or 82°/8°. s2 b) unchanged (68,6 µs, about 0,7 µs extra).
6. Polish 6: `lt-1` feedback "Tässä tilanteessa vauhtia voisi muuttaa vain sähkökenttä." Done.
7. New `lue-kuvaaja` options: 50 Hz with 8,5 V and 25 Hz with 12 V; the feedback correctly names which half is right (T = 40 ms, f = 25 Hz, U = 12 V/√2 = 8,49 V).
8. `ympyra` redrawn with inline r = mv/(qB): directions still correct (positive charge, B into page, F = qv × B toward the centre, counterclockwise).
9. Build: 0 .katex-error, 0 raw $, 0 console errors with all details open at 390 and 1280.

## Polish
None new. The numbers and physics checked in round 1 are unchanged.
