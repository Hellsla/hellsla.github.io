VERDICT: FAIL
CONTENT-HASH: 0a0473c406c167f3

## Blocking
- inquiry.json:377 (tarkistus-2 solution, Järkevyys) — "koska jäätä on vain viidesosa teen massasta" is wrong: 0,050 kg / 0,20 kg = 1/4 (ice is a fifth of the *total* 0,25 kg). The reasonableness check states a false ratio — fix: "neljäsosa".

## Polish
- inquiry.json:160, 231 (koe-1, koe-2) — `answer` 26.6 °C / 12.6 g carry three figures while each solution's Vastaus rounds to 27 °C / 13 g with two-figure data — align them or say why three figures are asked.
- inquiry.json:322 (siirto, Muunnokset) — writes "$22\,{}^\circ\text{C} - 8{,}0\,{}^\circ\text{C} = 14\,\text{K}$", but Annettu and Vastaus use 22,0 and 14,0 K (the three figures the Vastaus relies on); write 22,0 − 8,0 = 14,0 K.
- solutions.md:59 (L2-01, Järkevyys) — balance shown as 23,6 kJ vs 23,5 kJ "täsmäävät pyöristyksen tarkkuudella"; with T = 13,944 °C both are 23,55 kJ. Use 13,944 or give both as ≈ 23,5 kJ so the check visibly closes.
- solutions.md:29 (L1-03, Järkevyys) — "jäätyminen vaatii paljon enemmän energiaa kuin jäähtyminen": freezing releases energy; say "olomuodon muutos sitoo/vapauttaa paljon enemmän energiaa kuin 20 K:n jäähtyminen".
- sim-spec.md:1 — promises a readout line naming "mikä kolmesta tilanteesta toteutuu"; sim.js has four cases and no such line (howto describes four). Align the spec with the sim.

## Checked
- All 12 exercise answers recomputed independently match answers.py and exercises.json.
- Worked example: 25 140 / 17 540 / 7600 J, T = 6,05 → 6,0 °C; two-figure justification via Q_j precision correct; its check (≈19 °C, 2/3, 18,8 kJ) correct.
- Every solution states the right principle (insulated, ice warms→melts→melt water warms; limit cases at 0 °C), solves symbolically first, conversions right; rounding lines name the limiting datum (L3-02 difference to the gram, L3-03 −4410 J to hundreds → 2 figures, L2-04 21,9 K).
- inquiry.json and exit ticket: every number, correct option, feedback and mistake value recomputed (26,57 °C threshold, 12,6 g, 39,9 / 43,9 / 438 g, 40,06 / 56 / 35 °C, 12,5 g).
- koe-1/koe-2 isolate TW0 / TI0; simState carries Tf and iceLeftG.
- Figures: bar heights (6 px/kJ: 150,8, 12,6, 213), kink at 26,6 °C (152,8 px) and 40,07 °C at 80 °C, before/after masses 0,375 / 0,025 kg and cube areas to scale.
- sim.js: four-case solve and Qend, sequential stateAt reaches Tf on both sides in every case; pace stated as illustration only.
- Scope: inside FY3.
