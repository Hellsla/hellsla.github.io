VERDICT: PASS
CONTENT-HASH: fa56f18f38e944df

## Blocking

## Polish
- inquiry.json:404 — siirto still stores 96.3 W while its solution answers "96 W, two significant figures" — align the stored value with the stated rounding (tolerance accepts both).

## Checked
- Sim axis label: sim.js:226 now draws `__('akseli_ulos')`; lang/en.json gives `$P_\text{out}\ (\text{mW})$`, the same symbol as the readout, howto and calc; the model function (τ = 1.0 ms, D = 0.10, K_OUT = 100 mW) is unchanged.
- Recomputed in one script with my own formulas: worked example 3.18e15 1/s and 632.7 nm; graph 2.04 / 2.68 / 3.27 e15 1/s; quantum dots 2.58–2.00 eV; CdSe bulk 1.74 eV → 713 nm; 650 nm 1.91 eV, 405 nm 3.06 eV; kertaus 1.89 eV ↔ 656 nm; virhe 1.34e16 vs 1.34e25 (5 MW); siirto 96.3 W, mistakes 87.9 / 1096; tarkistus-2 532 nm, mistakes 397 / 228 nm — all agree with the text and lesson-answers.py.
- Sim steady state: three-level N₂ = Wτ/(1+Wτ), clamp 55 %, P_out = 100 mW·(WτN₁ − N₂), threshold 1.22 W; koe-1 0 / 12.5 / 35 / 80 / 125 mW; koe-2 33.3 / 40.0 / 45.5 %; koe-3 66.7 / 83.3 % without beam — match every feedback and model answer.
- Physics: spontaneous vs stimulated emission (same energy, direction, phase; incoming photon not absorbed, energy from the atom), no inversion by heating, two-level limit ½, ruby three-level scheme and ms lifetime (~3·10⁵ × 10⁻⁸ s), threshold vs losses, monochromatic/directional/coherent, laser hazard from power concentration not photon energy.
- Quantum confinement raises the gap, energies approach bulk (not 1/d); tunnelling, STM, flash, 2025 Nobel (macroscopic tunnelling and quantisation in circuits) correct.
- Experiments lock levels and mirrors and vary only P; simState gives n2, inv, Pout.
- Each choice item has exactly one correct option; distractors and feedback correct.
- Model limits stated (steady state, heating ignored, model values); worked example and tarkistus-2 symbolic first with sig-fig reasons.
