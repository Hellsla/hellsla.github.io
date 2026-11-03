VERDICT: PASS
CONTENT-HASH: 1a0b4ef8d49e71bc

## Blocking

## Polish
- inquiry.json:111 (sim `model`): in the sim every dot moves with one shared phase, so Q_A = Q_B is built into the model rather than discovered. The text says this only implicitly. Add one clause such as "Mallissa varaus ei synny eikä katoa missään piirin kohdassa; todellisilla virtamittareilla mitattuna tulos on sama." so that the exp-1 conclusion is not read as an independent measurement.
- lesson.md:343: "jokainen paristosta lamppuun kulkeva coulombi tuo lamppuun 1,5 J" is exact only when the cell's and wires' own resistance is ignored, which the sim states but the theory does not. FY6 later measures internal resistance, so "(kun johtojen ja pariston oma vastus jätetään huomiotta)" would avoid a later contradiction. This is a C-level simplification and is not blocking.
- lesson.md:83: "sähkökenttä syntyy koko johtoon lähes valon nopeudella". The signal speed is a large fraction of c and depends on the cable. "hyvin nopeasti, lähes valon nopeudella" is fine as written; this is optional.

## Checked
- Recomputed in one script: worked example (180 C, 1,12·10²¹ e⁻), siirto 432 kJ (7,2 and 12 000 mistakes, 0,12 kWh, 450 kJ estimate), check-2 5400 C (90, 1350, 1,5 Ah), exp-1 0,200 A (mistakes 20 and 5), exit ticket 6,0 J, 1 C ≈ 6,24·10¹⁸ e⁻, dot 0,05 C ≈ 3·10¹⁷ e⁻.
- sim.js: I = 1,5 V·n / (lamps·15 Ω). Dot counts are 20/40/60 (one lamp) and 10/20/30 (two), giving exactly the Q values the feedback quotes. Electrons move against the conventional path. A lies before the lamps, B on the return wire after them, and electrons pass B first (pred-1's last feedback is right). An open switch sets I = 0 everywhere, and brightness is √(P/Pmax).
- exp-1 and exp-2: varied parameter isolated, other parameters locked, QA and QB present in simState.
- pred-1, pred-2, exp-2 question, kertaus, check-1: exactly one correct option, and each distractor's feedback is physically right.
- Etsi virhe figure (figures.py virhe_kaavio): both lamp leads end at the + node and − is open. The key is right, and the "kytkimen paikka" and symbol distractors are correctly wrong.
- check-3 figures: (a) series loop correct, (b) resistor symbols, (c) switch on a dead-end branch. The feedback matches each drawing.
- Figures piiri, kaavio, johdin, virta: I arrows go + → − outside the cell and electrons go the opposite way. The IEC cell symbol (long thin plate +) is consistent in the text, the symbols figure and every diagram.
- Definitions I = Q/t, U = E/Q, Q = Ne and conductor/insulator agree with the glossary and summary. The current is the same everywhere in one loop, as stated in the glossary.
- Typical values table (AA 1,5 V, phone 3,7 V, car 12 V, LED 0,02 A, lamp 0,3 A, charger 2 A): plausible magnitudes. Drift speed below 1 mm/s is consistent (≈0,04 mm/s at 0,3 A in 0,5 mm² Cu).
- Scope: DC circuit basics only, with nothing beyond FY6.
