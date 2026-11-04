VERDICT: FAIL
CONTENT-HASH: 797d0da97ee26e59

## Blocking
- exercises.json:170 (fy7-9-L2-07) — B: this is the only Wien task that does not state the black-body assumption. A tungsten filament is not a black body, but the task and its solution (solutions.md:170, "tulo on vakio b kaikissa lämpötiloissa") compare the data with b as if it were. — Fix: add to the task "Lanka oletetaan mustaksi kappaleeksi." and to the Periaate "mustalle kappaleelle".

## Polish
- solutions.md:184 (L3-04) — "3,2 kertaa; kolme merkitsevää numeroa" contradicts itself. — Give 3,19 (three figures), or say two figures and why.
- solutions.md:154 (L2-05) — Every temperature is rounded to two figures "kuten aallonpituuksista osassa", but 1,62 and 1,08 µm have three. — Round each result by its own datum: 2,68·10³ K, 1,79·10³ K, 5,8·10³ K.
- solutions.md:165 (L2-06) — "lähellä näkyvän valon rajaa 750 nm": 1,63 µm is more than twice 750 nm. — Write "infrapuna-alueella, lähempänä näkyvää valoa kuin holvin 4,0 µm".
- exercises.json L2-04, L2-05 (Aurinko 0,50 µm) and L3-04 (tähti B 500 nm) — the same 500 nm → 5796 K step appears three times. — Change L3-04's star B to, for example, 480 nm.
- Plan drift for pedagogy: the planned thermal-camera and emissivity experiment was replaced by L2-07, and the planned two spectrum graphs by L3-04's table.

## Checked
- One script (python3 -I) recomputed all 20 answers with my own formulas. All agree with exercises.json/answers.py to within 0,1 %: new 67,33 ms; 8,571 cm; 2683 K; 1,634 µm; 2,897; 3,192; 17,48 min.
- L1-06: exactly one option is correct, and each distractor's feedback is right.
- L2-06: the student's 1,932 µm comes from b/1500. The correct value uses 1773,15 K.
- L2-07: the mean of the products is 2,897, and the deviations of −2,3 %/+2,4 % match the solution.
- L3-04 c): the colour is explained from the visible part of the spectrum on the correct side of the peak for both C (UV peak) and A (IR peak).
- L3-05: T = 1610/1414/1233/1054 K, interval rates 49,1/45,1/44,8 K/min. The mean is 46,3 K/min. Glow ends at 17,5 min, and the real time is longer, which is correctly argued. 800 K → 3,6 µm agrees with the lesson.
- The new tasks solve symbolically first and stay in scope (no photon, no Stefan–Boltzmann).
- The L2-05 table renders cleanly at 1280 px.
- The hash was the same at the start and at the end.
