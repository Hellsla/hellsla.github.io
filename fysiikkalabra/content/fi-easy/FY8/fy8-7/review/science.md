VERDICT: PASS
CONTENT-HASH: 6462de917d30bb56
Mode: full, round 1

## Blocking
(none)

## Polish
- assets/sims/fy8/fy8-7/sim.js (readout, `tx(S.Pout, 0)`) — at $P_\text{p} = 1{,}5\,\text{W}$ the readout shows 12 mW while simState, the feedback of ennuste-1 and the johtopaatos model say 12,5 mW — show one decimal in the readout.
- inquiry.json ennuste-1, first distractor's feedback — "Valo vahvistuu vasta, kun ylätasolla on tarpeeksi enemmän atomeja" blurs gain (any $N_2 > N_1$, as the theory says) with the threshold (gain covers the losses) — say "Säde syntyy vasta, kun vahvistuminen korvaa häviöt".
- inquiry.json johtopaatos model — "1,0 W ja sen alle ... eikä inversiota ole" skips the model's range 1,1–1,2 W where there is an inversion (52,4 %, 54,5 %) but no beam; one clause would tie it to the threshold 1,22 W and to criterion 2.
- inquiry.json siirto — `answer` 96.3 against the solution's two-figure 96 W; inside the tolerance, harmless.

## Checked
- Own recomputation (h, c, e as given): graph 2,04 / 2,68 / 3,27 · 10^15 1/s; example 3,1399e-19 J, 3,1848e15 1/s, 632,65 nm; 1,91 and 3,06 eV; CdSe 1,74 eV → 713 nm; dots 2,58 / 2,34 / 2,18 / 2,07 / 2,00 eV; hydrogen 3→2 1,89 eV. All agree with the text and lesson-answers.py.
- Sim model recomputed and driven in the preview: three levels 50 % / 0 mW at 1,0 W, 55 % and 12,5 / 35 / 80 / 125 / 170 mW at 1,5–5,0 W, threshold 0,55/0,45 = 1,22 W; two levels 33,3 / 40,0 / 45,5 %; no mirrors 66,7 / 83,3 %, inversion yes, no beam. simState gives n2, inv, Pout at every experiment's initial state.
- Experiments: levels and mirrors locked, only P varied; each isolates its parameter.
- Predictions, kertaus, kvanttipisteet, virhe, tarkistus-1: exactly one correct option; every distractor wrong and its feedback right (1,3e25 · 3,7e-19 J ≈ 5 MW; 1,3e16 1/s corrected).
- siirto 96,31 W, mistakes 87,85 and 1096 W; tarkistus-2 532,19 nm, mistakes 397 and 228 nm; solutions symbolic first, rounding by the limiting datum.
- Stimulated emission (incoming photon not absorbed, energy from the atom), two-level limit of one half stated for resonant pumping, thermal equilibrium never inverted, ruby ms lifetime vs 1e-8 s: correct; semiconductor laser kept apart from atomic levels.
- Scope: laser, quantum structures through applications, tunnelling optional and qualitative; no de Broglie, no Schrödinger; dot-size calculation said to be extra.
- Laser safety statement exact (power in a narrow beam, not photon energy); Nobel 2023 and 2025 claims correct.
- Sim limits stated in Mallin oletukset (steady state, model values, heating ignored).
