VERDICT: FAIL
CONTENT-HASH: 93a0c0e73bae09d1

## Blocking
- exercises.json:14, solutions.md:11–19 (L1-02) — A filament lamp is said to turn 3,0 J of 60,0 J (5 %) into *säteilyenergia*. This is false: most of a filament lamp's input leaves as infrared radiation, and only the visible light is about 5 %. It teaches that radiation = visible light. — Write *näkyväksi valoksi* / $E_\text{valo}$ instead of säteilyenergia in the text and the solution.
- exercises.json:90, solutions.md:101–109 (L3-02) — $E_0 \cdot 0{,}80 \cdot 0{,}80$ is a product of stage retention factors, the chain-efficiency product the teacher's FY2 scope excludes (fy3-15). — Give the mechanical energy after each bounce (e.g. 5,0 J, 4,0 J, 3,2 J) and ask the student to reason with them. Or ask about one bounce only.

## Polish
- solutions.md:29 (L1-03) — "noin 15 %, mikä on tavallinen määrä aurinkopaneelille": today's panels are about 20 %. — Write "hieman tavallista pienempi", or use 160 J in the data.
- exercises.json:62 (L2-03) — The question asks for the thermal energy of the ball and the floor, but the solution's system also includes air. — Ask for "lämpöenergia yhteensä", or drop the air from the system.

## Checked
- I recomputed all 12 answers independently and compared them with answers.py; all match within tolerance (L3-01 130 J via mechanical energy 880 → 750 J).
- The rounding and significant-figure justifications are right (L2-04 29 kJ from 0,001 MJ precision; L3-01 to 10 J).
- Every solution states the system and why it is isolated, solves symbolically first, converts by substituting the prefix (kJ, MJ, GJ, mJ, %), and checks by adding back.
- The magnitudes are realistic: kettle 92 %, nuclear plant one third to electricity, cyclist braking, toy car.
- There is no FY3/FY4 content apart from L3-02 above. \cdot and colon division are used throughout, with no ×.
- No exercise data claims a named source.
