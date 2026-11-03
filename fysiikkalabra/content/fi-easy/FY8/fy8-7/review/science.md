VERDICT: PASS
CONTENT-HASH: 2bd317b00068550c

## Blocking

## Polish
- meta.json:26 — key concept "stimuloitu emissio" omits the condition that the incoming photon's energy equals the level difference $E_2 - E_1$ (the lesson and glossary state it) — add "jonka energia on tasojen erotus" after "Saapuva fotoni".

## Checked
- Numbers and JSON structure (correct flags, answers, tolerances, mistakes, initial/locked/vary/values) identical to the passed Finnish source in lesson.md, inquiry.json, exit-ticket.json; only wording differs.
- Recomputed in one script: 1 mW photon rates 2,04 / 2,68 / 3,27e15 s⁻¹; He–Ne example 3,18e15 s⁻¹ and 633 nm; ruby 694 nm ↔ 1,79 eV; CdSe bulk 713 nm; quantum-dot energies 2,58…2,00 eV; misconception 1,91 / 3,06 eV; kertaus 1,89 eV.
- Sim model (sim.js = lesson-answers.py): threshold 1,22 W; P_out 12,5 / 35 / 80 / 125 / 170 mW; two-level N₂ 33,3 / 40,0 / 45,5 %; no mirrors: inversion (66,7 %) without beam — matches every prediction feedback and the conclusion model answer.
- Ennuste 1 and 2, kvanttipisteet, Etsi virhe (1,34e16 s⁻¹; 1,3e25 s⁻¹ ↔ ≈ 5 MW), tarkistus-1: exactly one correct option, distractor feedback correct.
- siirto 96,3 W (mistakes 87,9 W, 1096 W), tarkistus-2 532 nm (mistakes 397, 228 nm) recomputed.
- Mechanisms in simplified wording stay right: stimulated photon copies energy, direction and phase; incoming photon not absorbed (energy from the atom); two-level limit ½; three levels with metastable E₂ (ms vs 10⁻⁸ s); mirrors select the axis; threshold = gain covers losses.
- Quantum structures: smaller confinement → larger gap → shorter λ; energy approaches the bulk gap, not ∝ 1/d.
- Tunnelling: probability decays in the barrier, non-zero behind a thin one; 2023 chemistry and 2025 physics Nobel statements correct.
- meta.json key concepts populaatioinversio, laser, kvanttipiste, tunneloituminen: correct.
