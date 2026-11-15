VERDICT: PASS
CONTENT-HASH: 1232992c95174de7

## Blocking
(none)

## Polish
- lesson.md:401 — the reversed-battery sentence "kahden pariston lähdejännitteen verran pienempi" is right for identical cells, which is what the flashlight example means (3 · 1,5 V → 1,5 V). With unequal cells it reads ambiguously. Fix: "väärin päin olevan pariston lähdejännitteen kaksinkertaisen verran pienempi" (or add "kun paristot ovat samanlaisia").
- inquiry.json tarkistus-3 model — "Kumpaankin sisäiseen resistanssiin jää siksi vain puolet jännitteestä" is half *compared with one cell carrying the same total current*. Say so ("puolet siitä, mitä yhteen paristoon jäisi samalla virralla") so it is not read as half of the source voltage.
- exit-ticket.json:2 — "paristo voi vuotaa tai syttyä palamaan" for a generic 9 V battery. The theory says that only a lithium battery may catch fire. Use the same wording ("kuumeta vaarallisesti; litiumparisto voi syttyä").

## Checked
- One Python script recomputed every lesson-answers.py value from the task data with my own formulas (load I = E/(R+R_s), the series and parallel groups, all of koe 1–3, ennuste feedback, virhe, siirto with its lamp-power ratio of 0,69 and I_k = 1050 A, the worked example 0,36 Ω / 4,4 A, the check-2 least-squares fit −2,00 V/A and 9,00 V, the exit ticket 5,0 A). All of them agree.
- The reversed battery (the proofreading fix): it subtracts its E and still adds its R_s. The fix is physically correct: three cells of 1,5 V give 1,5 V, which is 3,0 V (= 2E₁) less.
- Worked example: solved symbolically first. Two significant figures are justified by the difference 0,13 V. The reasonableness check is real (back-substitution).
- ui-graph figure, to scale: the pixel coordinates give E = 1,50 V, I_k = 5,00 A and a triangle from 1,2 V to 0,6 V over 1–3 A. check-graph: the line (0; 9,0)–(1,5; 6,0) matches the least-squares fit of the five points.
- Model and connection figures: the source symbol is the right way round (long plate +), and the current arrows run − → + inside the battery and + → − outside. In the series stack, − connects to the next cell's +. The parallel figure joins + to + and − to −.
- sim.js implements I = E/(R+R_s) and U = E − R_s I, and the groups 2E, 2R_s and E, R_s/2. The glow per cell uses I/2 in parallel. simState carries I and U. The adapter exposes paristo, kennot, kytkin and R. Every experiment's R values (1–8 Ω) are within the slider's range.
- The experiments isolate the varied parameter: koe-1 locks the battery, the connection and the switch; koe-2 locks the battery, the switch and R; koe-3 leaves the switch free on purpose.
- Every choice item has exactly one correct option, and each distractor's feedback is right. The numeric tolerances accept the answers as rounded (0,20 Ω, 10,4 V, 2,0 Ω).
- Magnitudes: AA R_s 0,2 Ω and I_k 8 A, car battery R_s about 0,01 Ω, the starter at 180 A, the 21700 and 18650 sizes. All are realistic.
- Scope: battery, terminal voltage, short circuit and connections are inside FY6 "akut" and the slot's täsmennys. The source-voltage definition (J/C) matches the glossary.
