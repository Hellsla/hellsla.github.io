VERDICT: PASS
CONTENT-HASH: 307c0dfc144588a5

Educator re-review of fy3-1 after the g change from N/kg to m/s². A student with FY1 and FY2 can follow the new g paragraph (lesson.md:21): g is the FY1 free-fall acceleration, G = mg gives newtons, and 1 N = 1 kg·m/s² is deferred to FY4. Mass versus weight is still clear (lines 14, 52). The spring-scale idea is reachable (lines 8-12, calibration by equal small weights). Levels follow the rubric (5/4/3). Answers recomputed: all correct. Length (680 words vs 703 in fy3-2), tone and structure match fy3-2. Nothing blocks. Finding 1 is a unit error and should be fixed in the next edit round; the others are polish.

1. lesson.md:57 (should fix, non-blocking). The summary says "g = 9,81 m/s²: yhden kilogramman massan paino Maassa". The weight of 1 kg is 9,81 N, not m/s², so the line mixes up the unit with the new g definition. Suggested rewrite:
   - $g = 9{,}81\,\text{m/s}^2$ on Maan pinnalla sama suure kuin FY1:n putoamiskiihtyvyys, ja yhden kilogramman massan paino Maassa on 9,81 N. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.

2. lesson.md:21 (polish). "painovoiman voimakkuus (m/s²)" followed at once by "putoamiskiihtyvyys" may make a student ask why a force-like quantity is an acceleration. One bridging sentence would help. Suggested rewrite of the middle of the paragraph:
   missä G on paino (N), m massa (kg) ja g paikallinen putoamiskiihtyvyys (m/s²), joka kertoo, kuinka voimakas painovoima paikassa on. Luku g on sama suure kuin FY1:n putoamiskiihtyvyys: Maan pinnalla g = 9,81 m/s².

3. lesson.md:21 (polish). "ei ole syy minkään liikkeen tai putoamisen alkamiseen" reads stiffly and may confuse a student who knows that a dropped body falls. Suggested rewrite:
   Tässä vaiheessa paino on vain vuorovaikutuksen voimakkuuden mitta. Sitä, miten voima vaikuttaa liikkeeseen, tutkitaan vasta FY4:ssä.

4. lesson.md:49 (polish). The Mars explanation repeats the Earth explanation and does not connect to g. Suggested rewrite:
   Marsissa paino on pienempi, koska Marsin g on pienempi: Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin. Robotin massa on molemmissa paikoissa 120 kg.

5. exercises.json fy3-1-L2-03 (polish). "Kuinka paljon pienempi hänen painonsa on Kuussa kuin Maassa?" is correct and needs two steps. Add the Earth value of g so the student does not need to remember it. The text already gives the Moon value, so the two are given the same way. Suggested rewrite:
   Astronautin massa varusteineen on 145 kg. Kuinka paljon pienempi hänen painonsa on Kuussa (g = 1,62 m/s²) kuin Maassa (g = 9,81 m/s²)?

6. exercises.json fy3-1-L3-03 (polish). The calibration rule is given in the task, which is good for an unfamiliar context. "Mitä lukemaa mittari näyttää" is clumsy. Suggested rewrite:
   ... Minkä lukeman mittari näyttää kilogrammoina?
