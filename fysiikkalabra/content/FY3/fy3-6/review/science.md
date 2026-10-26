VERDICT: PASS
CONTENT-HASH: a38128ef6919c113

## Blocking

## Polish
- inquiry.json (tarkistus-3 criterion 1) — "noin viisinkertainen hiekkaan tai maahan verrattuna": the factor 5 holds for dry sand (800); moist soil has c ≈ 1000–2000 J/(kg·K) — say "kuivaan hiekkaan" (carried over from round 1).
- inquiry.json koe-1/koe-2 tables — the varied column's header shows "aine, c" and "kuuman veden massa" without the unit (J/(kg·K), kg) that `units` gives, while the measured columns carry theirs — show the unit in the varied column too.

## Checked
- Round 2 diff (exercises L1-04, exit ticket 1, inquiry prior, siirto mistake 21,3, tarkistus-2 mistake 768): text-to-LaTeX only; every number, sign and unit identical to the previous wording (−35 MJ, 419 000 J ≈ 420 kJ, 60 − 30 vs 60 − 38 = 22 K, 98,0 − 18,0 vs 69,0 K).
- All 12 exercise answers recomputed independently: match answers.py and exercises.json (0,63 MJ, 210 kJ, 720 kJ, −35 MJ, 19 kJ, 78 °C, 210 s, 54 °C, 27 °C, 12 kg, 3,6 K, 3,3 m³).
- solutions.md: symbolic before substitution; all side checks correct.
- Worked example: 5656,5 J, 374,6 J/(kg·K), sensitivity 383 at 24,6 °C, copper equilibrium 24,6 °C, 1257 and 75 J/K correct.
- Formula section and misconception (35 °C, ≈ 9× water vs iron) correct, inside FY3 "aineen lämpeneminen ja jäähtyminen".
- Figures: water-sand ΔT bars 20 vs 105 px (5,25 ≈ 4190/800, to scale as stated); c-bars to scale within 0,3 %; calorimeter numbers match the worked example.
- ennuste-1/koe-1: 26,8 / 44,0 °C, 8,5 / 30 kJ, C = 160 / 838 J/K; ennuste-2/koe-2: 40,0 / 55,0 / 63,1 °C; each experiment varies one parameter, Teq and CB are in simState; screenshots show 8,52 kJ and 41,9 kJ on both sides.
- virhe 6,6 °C vs 30,0 °C and the Kelvin-shift argument; siirto 29,1 kg (mistakes 220, 21,3); tarkistus-1 4500 vs 838 J/K; tarkistus-2 891 (mistakes 768, 501); exit ticket 419 kJ, ≈ 9×, 50 / 65 °C — all verified.
- Speed control: scales only the animation clock (clamp 0,1 s × speed), not in inputKey, so it never resets a run; Teq, Q and T(t) as a function of the clock are speed-independent, as the new howto sentence says.
- sim.js implements the lossless equilibrium model with no phase change; the exponential approach (τ = 1,5 s) is labelled illustration in code and the "model" box.
