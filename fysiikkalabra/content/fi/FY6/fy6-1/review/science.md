VERDICT: PASS
CONTENT-HASH: a9b345687bfb82fb

## Blocking

## Polish
- inquiry.json:111 (sim `model`): "todellisen hehkulampun virta kasvaa jännitteen mukana hieman hitaammin" understates it: a filament's resistance grows strongly as it heats (roughly I ∝ U^0,5–0,6 near the operating point), so two real lamps in series carry clearly more than half of one lamp's current. The 2,00 → 1,00 C halving is already called a model value. "selvästi hitaammin" would be closer. C-level, not blocking.
- inquiry.json:388 (check-2 Järkevyys): 1500 mAh is "noin puolet tavallisen puhelimen akun varauksesta". Current phones hold about 4000–5000 mAh, so "noin kolmasosa" fits better.

## Checked
- Recomputed everything in one script: the worked example (180 C, 1,12·10²¹ e⁻), 1/e = 6,24·10¹⁸, a dot (0,05 C ≈ 3,1·10¹⁷ e⁻), exp-1 0,200 A with the mistakes 20 and 5, exp-2 0,100 A, siirto 432 kJ (mistakes 7,2 and 12 000; 0,12 kWh; estimate 450 kJ), check-2 5400 C (mistakes 90 and 1350; 1,5 Ah), exit ticket 6,0 J.
- sim.js: I = 1,5 V·n/(lamps·15 Ω). The counted dots give Q = 1,00/2,00/3,00 C (one lamp) and 0,50/1,00/1,50 C (two lamps), matching every feedback. The time is clamped at exactly 10,0 s. Dots move against the conventional path. A is before the lamps and B on the return wire. An open switch makes I = 0 everywhere. The model box now states that Q_A = Q_B is built into the model (the round 1 polish).
- exp-1 and exp-2: the varied parameter is isolated, the others are locked, and QA and QB are in simState.
- pred-1, pred-2, the exp-2 question, kertaus, check-1, Etsi virhe and check-3 each have exactly one correct option, and the distractor feedback is physically right. Electrons pass B before the lamp, as pred-1's last feedback says.
- Figures: in virhe-kaavio both lamp leads go to the + node and − is open. In check-3, (a) is a series loop, (b) uses resistor symbols and (c) puts the switch on a dead-end branch. The I arrows in piiri, kaavio, johdin and virta run + → − outside the cell, with electrons opposite. In jannite, + is at the top and the return arrow points to the battery. The IEC cell symbol is the same everywhere.
- Jännite now states the condition "kun johtojen ja pariston oma vastus jätetään huomiotta" (the round 1 polish).
- Definitions I = Q/t, U = E/Q and Q = Ne, conductor and insulator, and the same current through one loop agree across the glossary, theory, summary and exit ticket.
- Magnitudes are plausible: the drift speed is below 1 mm/s, the signal travels near c, and the typical-values table is right.
- Scope: DC circuit basics only, with nothing beyond FY6.
