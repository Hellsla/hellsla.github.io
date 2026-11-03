VERDICT: PASS
CONTENT-HASH: 4bbed523e6b8dec9

## Blocking

## Polish
- exercises.json L2-03 — Rovaniemi: WMM2025 gives Z 52.4 µT, F 53.8 µT and I 77.1° (pygeomag WMM_2025.COF, epoch 2025.9; IGRF-14 agrees). The task's B_v = 51 µT gives B = 52 µT, about 3 % low. Fix: B_v = 52 µT gives B = 53.4 µT; then update answers.py and solutions.md.
- exercises.json L3-03 — the task cites WMM2025 for Helsinki 52 µT and 74°, but the model gives 52.6 µT (53) and 73.7°. For Longyearbyen it gives 55.2 µT and 82.5°, so H is 14.8 µT : 7.2 µT, a ratio of 2.1, not 1.87. The physics point stands. Fix: either give the values as "noin" without claiming they are the model's rounded values, or use 53 µT, 74°, 55 µT, 82.5°, which give a ratio of 2.0.
- solutions.md L3-02 — "Punahehkuisessa teräksessä … raudalla tämä tapahtuu noin 770 °C": red heat starts at about 550–600 °C, below the Curie point, and a lighter flame may not reach 770 °C. Fix: "kun liitin kuumennetaan riittävän kuumaksi (raudan Curie-lämpötila on noin 770 °C), lämpöliike sekoittaa järjestyksen". The demagnetisation happens anyway, so this is not an error in the outcome.
- answers.py L3-02 comment — "or knocks" is not in the task or solution; harmless.

## Checked
- Recomputed all nine numeric answers in one script with my own formulas: 6,0·10⁴; 13,7; 50,0; 60,8°; 49,7; 52,3; 9,82; 11; 1,87. All agree with answers.py and the solutions.
- Kuopio 53 µT, 75° matches WMM2025 (53.3 µT, 75.3°).
- L3-01: beside the middle of the magnet with N to the north, the field points south. 25 − 14 = 11 µT south, and the needle reverses. Correct.
- L2-02: the phone's z axis points up, so B_z < 0 in Finland is consistent.
- L2-04: the perpendicularity condition is stated, so B_h cancels; ratio tan 60° / tan 10°.
- L1-04/L1-05 word answers: correct poles and directions.
- Rounding: every answer is justified by two-figure data; units are consistent.
