VERDICT: PASS
CONTENT-HASH: 58242d5b3c115dce

## Blocking

## Polish
- lesson.md:366 — the simulation's piston changes V without doing work on the gas (isothermal by construction); the sim's Lisätietoja says so (sim.js:124), but the lesson paragraph does not — add "mäntä ei lämmitä kaasua: lämpötila pysyy samana, kun tilavuus muuttuu" at the point of use.
- solutions.md:23 — "18 g, mikä on tavallisen patruunan koko": adult automatic lifejackets mostly use 33 g cartridges (18–24 g in smaller ones) — say "pienen patruunan koko" or drop the claim.

## Checked
- Recomputed all 12 exercise answers independently: answers.py, exercises.json and my values agree within 0,5 % (L1-05 9,659 → 9,7; L3-02 10,96 → 11).
- Inquiry numbers: m/M He 0,2075, N₂ 0,2064, ilma 0,2076, CO₂ 0,2068; mean 0,2071 → R ≈ 8,32 (lesson "≈ 8,3"); laske-r 8,302 and its mistakes 121,7 / 8302 / 0,0083; siirto 2645 kg (n = 91 200 mol), mistakes 9869 and 2,64, outside air 3,37 t → ~700 kg difference; virhe 1,2 → 0,083 mol; check-2 3,00 (mistakes 2,25, 1,69); exp-2 N = 50; kertaus 200 kPa; table pV/(NT) 0,98/0,98/0,99 correct.
- Worked example: n = 0,2073 mol, m = 0,83 g, air 6,0 g, molar volume 24,1 l; symbolic before substitution. Exit ticket 0,601 mol.
- Solutions: every one solves symbolically first; side claims (0,32 kg, 2,7×, 23,9 l and 17 %, 2,7·10²¹ O₂, 22 g/16 g, initial 2,6 kg and "yli neljäsosa", O₂ Z < 1 at 180 bar so ideal value too high) are right.
- Figures: fig 1 12 + 12 particles, arrow length ratio 32 : 12 ≈ 2,7 = √(29/4); fig 2 bars 14 : 101,5 : 154 = 4 : 29 : 44, 8 particles each; fig 3 6/12/6/6 particles, 2T arrows √2 longer, V/2 gas column half height.
- sim.js: impulse per perimeter gives p = NkT/A exactly; P_REF from the same model; thermalize keeps ⟨vx²⟩ = ⟨vy²⟩ = kT/m; v ∝ √T; 2D model, no inter-particle collisions and fluctuation stated; prediction not shown, as the spec says.
- Experiments: exp-1 and exp-2 lock T and V and vary N only; simState gives N, T, pMeasured, hitRate, adapter adds V; N = 50 reachable (slider step 10).
- Prediction feedback: pred-n, pred-1 (He: 2,69× more hits, 2,69× less impulse each), check-1 physics correct.
- Scope: ideal gas law, mole and M within FY3 "ideaalikaasun tilanyhtälö"; kinetic picture qualitative.
- Hash 58242d5b3c115dce at start and end.
