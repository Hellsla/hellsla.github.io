VERDICT: PASS
CONTENT-HASH: 536cade809f2b051

Round 3. Student can follow the lesson; levels match the rubric (L1 5, L2 4, L3 3); no task repeats the example. All answers recomputed and within tolerance. Findings are polish only (non-blocking).

1. lesson.md:10 (and :73) The direct proportionality p ~ T(K) is stated without support; the lesson defers it ("tutkitaan kunnolla myöhemmin"), which is acceptable because L3-01/02/03 each restate it in the task text. Optional clearer link to the example:
   "Kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan: jos kelvinlämpötila kaksinkertaistuu, myös paine kaksinkertaistuu. Esimerkin kuvaaja kertoo saman: paine nollautuu kohdassa 0 K."

2. lesson.md:64 "kuvaa raja-arvoa" is jargon a 17-year-old may not know. Rewrite:
   "Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa, joten suoran jatke on vain malli: se kertoo, mihin suuntaan kaasu käyttäytyisi, jos se pysyisi kaasuna."

3. lesson.md:8 The micro-model paragraph is long (about 130 words, three ideas). Optional split before "Kun lämpötila nousee":
   "Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään sekä useammin että kovempaa, joten paine kasvaa. Siksi rengas tuntuu kesällä kovemmalta."
   Lesson is 829 words against 669 (fy3-1) and 703 (fy3-2), so trimming helps.

4. exercises.json L2-03 (extrapolation to -50 °C) is a different task from the example (zero pressure), but it needs the same method (slope, then p0 at 0 °C) with p0 not given. Fine for L2, but the student must find p0 first. Optional hint sentence:
   "Laske ensin suoran kulmakerroin ja paine lämpötilassa 0 °C."

5. exit-ticket.json q2 repeats the misconception paragraph's numbers (283 K and 293 K) verbatim, so it tests recall more than transfer. Optional new numbers:
   "Lämpötila nousee 0 °C:sta 100 °C:een. Kaksinkertaistuuko hiukkasten keskimääräinen liike-energia? Perustele."  (a: "Ei. 273 K -> 373 K, kasvu vain noin 37 %.")

6. exit-ticket.json q1 The micro-model question is present and answerable from the lesson. No change needed.

Checked and OK: Kelvin scale taught (:10, :13-19), unit wording "kelvin, ei aste" (:17), extrapolation defined (:55) and worked through (:50-64), figure note explains the axis (:48).
