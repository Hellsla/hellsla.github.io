VERDICT: PASS
CONTENT-HASH: f02ac19e6d16a8fe

## Blocking

## Polish
- exercises/solutions.md:9 (L1-01 Järkevyys): "tavallinen esimerkiksi auton ajovalossa" is not a typical value. A 55 W headlamp at 12 V draws about 4,6 A. Use instead e.g. "auton jarruvalossa (21 W, noin 1,8 A)" or "pienessä polkupyörän valossa".
- exercises/solutions.md:19 (L1-02 Järkevyys): "1,2·10²⁰ elektronia ... tavallinen suuruusluokka pienen moottorin virralle" mixes a count of electrons with a current. Either drop the clause or say "0,50 A on tavallinen pienen moottorin virta".

## Checked
- Recomputed every answer from the task text with my own formulas, and all agree with exercises.json and answers.py: L1 1,5 A, 20 C, 9,0 V, 1800 J, 30 s; L2 108 C, 9,99·10¹⁷, 39,96 kJ, 11 C; L3 8,0 h, ratio 1,2.
- L2-04 graph (figures.py virta_kuvaaja): 0,40 A for 0–20 s, 0,10 A for 20–50 s, 0 after that. These match the solution's readings, and the answer is the area 8,0 + 3,0 = 11 C.
- L2-03 conversion: 3000 mAh = 10 800 C. The reasonableness check (40 kg lifted 100 m ≈ 39 kJ) is correct.
- L3-02: 9,0 V·0,50 Ah vs 1,5 V·2,5 Ah gives 16 200 J : 13 500 J = 1,2. The capacities are realistic.
- L3-03 model figure (kaavio_malli): two cells in series with + up and the upper cell's − on the lower cell's +; switch, lamp and ammeter in one loop; the I arrow runs + → around the loop. This agrees with the answer text and the model solution.
- Every solution solves symbolically first, converts units before substituting, and justifies significant figures by the limiting datum.
- Physics: I = Q/t, U = E/Q, Q = Ne and Ah as a unit of charge are used correctly. There is no content beyond FY6 scope.
