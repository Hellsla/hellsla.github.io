VERDICT: PASS
CONTENT-HASH: b81d92cfb4e125cd

Round 2: The round-1 blocking item is fixed. L2-07 now says "Lanka oletetaan mustaksi kappaleeksi", and the Annettu and Periaate say "mustalle kappaleelle". Four round-1 polish items are also fixed: L3-04 gives 3,19, L2-05 rounds each result by its own datum, L2-06 says "lähempänä näkyvää valoa", and star B is now 480 nm (6038 K → 6,0·10³ K, still yellow-white and Sun-like). L1-06 now has new distractor wording and its options are in a new order.

## Blocking

## Polish
- exercises.json fy7-9-L1-06 (correct option) — "kohtisuorassa toisiaan ja etenemissuuntaa vastaan, koska aalto on poikittainen": being transverse explains only why the fields are perpendicular to the direction of travel, not why E ⊥ B. — Write "..., ja kumpikin kenttä synnyttää toisen" (as the feedback and Mallivastaus say), or drop the "koska" clause.
- solutions.md fy7-9-L2-07 Vastaus — "kolme merkitsevää numeroa kuten mittausten aallonpituuksissa", but 0,89 µm has two. — Write "kolme merkitsevää numeroa, kuten useimmissa aallonpituuksissa".
- Plan drift for pedagogy (carried over): the planned thermal-camera and emissivity experiment was replaced by L2-07, and the planned two spectrum graphs by L3-04's table.

## Checked
- One script (python3 -I) recomputed all 8 new answers with my own formulas, and they agree with answers.py: 67,33 ms; 8,571 cm; 2683/1789/5796 K; 1,634 µm; 2,897; 3,192 (T_B 6038 K); 17,48 min.
- Every Vastaus value of the new tasks lies inside its answer box's tolerance.
- L1-06: exactly one option is correct, and each distractor's feedback is right.
- L3-05: the interval rates are 49,1/45,1/44,8 K/min, so the claim "real glow lasts longer" is right.
- All tasks are in scope: no photon, no Stefan–Boltzmann.
- The hash was the same at the start and at the end.
