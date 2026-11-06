VERDICT: PASS
CONTENT-HASH: 2d22792f6d7cc426

## Blocking
(none)

## Polish
- exercises.json:260 (fy2-3-L2-08) — two problems with realism. The stove's powers (2,0 kW and 4,0 kW) are well below the lesson table's sähkökiuas 8 kW. Also, a resistance stove with fixed elements cannot double its own power. This is a C-level idealisation, not wrong physics — fix it by comparing two stoves ("kiuas A … kiuas B"), or use values in the stove range, e.g. 12 kWh in 2,0 h vs 1,0 h (6,0 kW vs 12 kW is still high). Two stoves is the cleaner fix.
- exercises.json:284 (fy2-3-L2-08, the "nelinkertaiseksi" feedback) — "riippuu ajasta suoraan käänteisesti" is awkward wording — write "on kääntäen verrannollinen aikaan, kun energia pysyy samana".
- solutions.md:135 (fy2-3-L1-08, carried over) — "Moottori muuntaa energiaa tasaisesti" is not needed for a keskiteho — write "Keskiteho on muuntunut energia jaettuna ajalla".
- solutions.md:187 (fy2-3-L3-04, carried over) — "satoja megawatteja" for hydro: most Finnish hydro plants are tens of MW and the largest is about 190 MW — write "kymmenistä megawateista noin 200 megawattiin".
- docs/exercise-bank/FY2.md:24 (carried over) — the plan's stair-climb task needs mgh (FY4). Update the plan to match the set.

## Checked
- New task L2-08, recomputed: P1 = 6,0 kWh : 3,0 h = 2,0 kW and P2 = 6,0 kWh : 1,5 h = 4,0 kW, so the ratio is 2,0. Exactly one option is correct ("kaksinkertaiseksi"). Each distractor (puolittuu, sama, nelinkertainen) is really wrong, and its feedback names the right reason: at fixed E, P is inversely proportional to t.
- L2-08 solution: P = E : t is stated before substitution, the units (kWh : h = kW) are consistent, and it agrees with the lesson's notation. "Tasaisella teholla" is stated in the task.
- L2-08 scope: only P = ΔE/Δt, with no work, force or FY4 content. The kind "concept, reasoning" fits.
- answers.py: the L2-08 line is a comment (multiple choice, no number), which is correct. All 21 lines run, and every numeric answer agrees with exercises.json within tolerance (L2-04 78,84 → 79, L3-01 15,18 → 15, L3-02 342 → 340, L3-03 102 → 100, L3-05 43,2 → 43).
- The rest of the set is unchanged since the previous PASS (82920b17): the earlier recomputation of L2-05, L2-07, L3-04 and L3-05 still holds.
- The hash was 2d22792f6d7cc426 at the start and at the end.
