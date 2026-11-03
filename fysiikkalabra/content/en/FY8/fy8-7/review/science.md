VERDICT: PASS
CONTENT-HASH: 5b8a1236669b6700

## Blocking

## Polish
- inquiry.json:404 — siirto stores 96.3 W while its solution answers "96 W, two significant figures" — align the stored value with the stated rounding (tolerance accepts both).

## Checked
- Recomputed in one script: worked example 3.18e15 1/s and 632.7 nm; graph points 2.04 / 2.68 / 3.27 e15 1/s; quantum-dot energies 2.58–2.00 eV; CdSe bulk 1.74 eV → 713 nm; 1.91 eV at 650 nm; kertaus 1.89 eV; virhe 1.34e16 vs 1.34e25 (≈ 5 MW); siirto 96.3 W and mistakes 87.9 / 1096; tarkistus-2 532 nm with mistakes 397 / 228 nm — all agree.
- Sim steady-state model (τ = 1.0 ms, Wτ = P/1 W, three-level N2 = Wτ/(1+Wτ), clamp at N2 = 55 %, P_out = 100 mW·(WτN1 − N2); two-level Wτ/(1+2Wτ)): threshold 1.22 W, koe-1 12.5/35/80/125 mW, koe-2 33.3/40.0/45.5 %, koe-3 66.7/83.3 % with no beam — match sim.js, lesson-answers.py and all feedback.
- Physics: spontaneous vs stimulated emission (same energy, direction, phase; incoming photon not absorbed), two-level limit ½, ruby three-level scheme and ms lifetime (~3·10⁵ × 10⁻⁸ s), threshold vs losses, monochromatic/directional/coherent, quantum confinement raising the gap, tunnelling — correct and consistent with summary, choices and model answers.
- koe setups isolate the varied parameter (levels and mirrors locked).
- Each choice item has exactly one correct option; distractors and feedback correct.
- Model limits stated (steady state, heating ignored, values from the model).
- Exercise set: reviewed separately in exercises/review/science.md (PASS).
