VERDICT: FAIL
CONTENT-HASH: 843688caee54bb50

## Blocking
- solutions.md:183 (fy5-6-L3-04 Vastaus, part c) — **A.** The mechanism is wrong. The text says "havainnoissa on voinut jäädä väliin joka toinen ohitus tähden edestä, jolloin kahden havaitun ohituksen väli on kaksi kertaa liian lyhyt". A missed transit makes the interval between observed transits LONGER, a multiple of the true period, never shorter. The listed 7,82 d is half the true 15,7 d. — Use a cause that halves the period, for example: "Jokaisella kierroksella on tulkittu kaksi kirkkauden heikkenemistä ohitukseksi (esimerkiksi myös hetki, jolloin planeetta kulkee tähden taakse), tai kahden eri planeetan ohitukset on sekoitettu, jolloin havaittu väli on puolet todellisesta kiertoajasta."

## Polish
- Duplicate across chapters: the new fy5-5-L3-05 b) repeats this chapter's existing L3-03 (weightless at the equator, 84,4 min). — The fix belongs in fy5-5 (see that report). Keep L3-03 here.
- exercises.json:131 (L2-05) — the answer is stored as 1.9, but the solution gives 1,90 with three significant figures. — Store 1.90.
- solutions.md:183 (L3-04 Vastaus) — "kolme merkitsevää numeroa kuten taulukon arvoissa", but r_b = 6,0 has two significant figures. — Say that three figures are justified by the period data and the averaging, or change the row to 6.00.
- exercises.json:197 (L2-06 row C) — the computed value is 3,9551 km/s, which rounds to 3,96, not the listed 3,95. — Change the row to 3.96 so that only row B is wrong.
- solutions.md:187 (L3-05 Annettu) — "satelliittien massa vaikutus" → "massan vaikutus". Plan: L1-08 (v = 2πr/T) repeats the method of L1-04, and L1-07 repeats the method of L1-01 and L1-05. The plan's level-1 "jaksonaika" item, and its level-3 "perustelu ISS:n painottomuudesta", are covered only by L1-06. Optional.

## Checked
- The hash is the same at the start and the end (843688caee54bb50).
- I recomputed all 19 numeric answers in one script with my own formulas, and all of them match. The new ones are 17,33 km/s, 29,786 km/s, 1,898·10²⁷ kg, 7,254 km/s, 7,454 km/s, 1,588·10³⁰ kg and 12,88 h.
- L2-05: the Galilean-moon data are real. r³/T² = 3,206–3,211·10¹⁵ (spread under 0,2 %), which gives M = 1,898·10²⁷ kg.
- L2-06: rows A, C and D agree with GM/(R+h). Row B, 7,52, is the swapped digits of 7,25.
- L2-07: F = 3874 N and 15 496 N (ratio 4), and the mass cancels. The explanation of the error is right.
- L3-04: r³/T² values of 2,673 / 2,706 / 10,76 / 2,674·10¹⁸ make d the outlier. T_d = 15,66 d. Leaving d out follows the outlier guardrail: it is justified, and the text asks for a re-measurement.
- L3-05: T_A = 92,43 min and T_B = 104,99 min. t = T_A T_B/(T_B − T_A) is the right condition for "one lap ahead".
- L1-06: exactly one correct option. The 88 % in the feedback is right, and the centrifugal-force distractor is refuted correctly.
- Scope: everything stays within the circular-orbit model. T² ∝ r³ is derived from it in the task text, not taught as Kepler's law.
- Every new solution solves symbolically before substituting, and each has a real reasonableness check.
