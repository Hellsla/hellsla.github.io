VERDICT: FAIL
CONTENT-HASH: 657d9c21afc1fe02

## Blocking
- inquiry.json exp-2 question (answer 50, tolerance 0.02) — the student reads N from a noisy 2 s average (about ±6 % at N = 50, the lab capture shows 0,98 and 1,93 instead of 1,00 and 2,00), yet only 49–51 counts as right. A student who measures honestly and reports 46 or 54 is told they are wrong. Fix: tolerance about 0.12 (45–56), or ask for the ratio "puolet" as a choice. Also say in the feedback that noise is expected.

## Polish
- inquiry.json `taulukko` — the last column cannot be reproduced from the raw columns (N, T in K, V in %); it is really $(p/p_\text{ref})(V/100\,\%)/((N/100)(T/300\,\text{K}))$. State that formula in the text.
- inquiry.json Tutki stage — nine required tasks (punnitus, vertailu, pred-1, kokeile, exp-1, exp-2, taulukko, laske-r, johtopäätös) plus the prediction, two checks and the exercises is more than an hour. Make `taulukko` or `laske-r` optional. The sim never isolates V in an experiment; the table covers it, which is acceptable.
- lesson.md "Kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan" — liike-energia is an FY4 term (scope note). Fix: "Mitä korkeampi kelvinlämpötila, sitä nopeammin hiukkaset keskimäärin liikkuvat."
- lesson.md "Tilavuus 5,0 l rajoittaa ainemäärää. Massaa rajoittaa myös moolimassa" — awkward. Fix: "Tilavuudessa ja moolimassassa on kaksi numeroa, joten tulokset annetaan kahdella merkitsevällä numerolla."
- lesson.md "5,0 l : 24 l/mol" and moolimassa 4,0 / 4,00 mixed — use a fraction and one precision for helium.

## Checked
- Hook: the question is not answered before the student commits; the answer appears only in the theory.
- Predictions (pred-n, pred-1): distractors are real misconceptions (mass = amount, particle collisions, helium packs tighter); each feedback repairs its own.
- exp-1 and exp-2 lock the controlled variables, the measured pressure emerges from counted hits, and the prediction can be refuted.
- Weighing data are consistent (m/M 0,2064–0,2076) and labelled as invented example values.
- The worked example has seven stages; its principle and reasonableness check are explained.
- The transfer task (hot-air balloon) is a new context; its mistakes list real unit errors.
- The Tarkista concept checks (volume to pressure, Celsius vs Kelvin) are misconception-based.
- Exit ticket tests the core idea (n = pV/RT, units).
- The 390 and 1280 px captures of the sim and the lab are legible and uncluttered. The exercise set was not judged here.
