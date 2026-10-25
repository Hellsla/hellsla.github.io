VERDICT: PASS
CONTENT-HASH: fc5375c46d696bd5

# Educator review, fy3-1, round 2

Method: lesson read as a 17-year-old who has FY1 (linear model, s = vt, v = gt, graphs) and FY2 (energy, no work). Hash checked at start and at end: fc5375c46d696bd5, unchanged. Compared with content/FY3/fy3-2/lesson.md (content/_gold/lesson.md is only a skeleton, so tone and structure come from fy3-2 and the CLAUDE.md rules).

Summary: a student can follow the lesson. The chain spring stretch -> force -> weight proportional to mass -> G = mg is reachable from FY1, and the mass versus weight distinction is clear and tested three ways (lesson, exercises, exit ticket). The levels fit the rubric (5/4/3, L2 each has one conversion, rearrangement or second step, L3 each need reasoning). Nothing below blocks a student. The findings are ordered by value.

## Findings

1. lesson.md:21 (g convention, medium). "yksiköt N/kg ja m/s² ovat sama yksikkö" is stated as a fact with no reason. A student who knows FY1's g as an acceleration will ask why a weight per kilogram is an acceleration, and nothing in FY1 or FY2 answers it (1 N = 1 kg·m/s² is FY4). The definition of g in the sentence before ("yhden kilogramman massan paino") is clear and good; the identity just needs to be marked as accepted for now so it does not read as a gap. Suggested rewrite of the sentence:
   "Sama luku 9,81 tuli vastaan FY1:ssä putoamiskiihtyvyytenä (m/s²). Yksiköt N/kg ja m/s² ovat sama yksikkö, ja miksi näin on, selviää vasta FY4:ssä. Tällä kurssilla käytämme g:tä yksikössä N/kg, koska silloin laskun yksiköt kertovat, mitä g tarkoittaa: newtonia kilogrammaa kohti."

2. lesson.md:12 (calibration, medium-low). "ripustamalla jouseen tunnettuja painoja" is circular for a first-time reader: how is the force of a "known weight" known, when G = mg comes only after? Also the doubling idea is the natural calibration trick and is not used. Suggested rewrite:
   "Asteikko kalibroidaan ripustamalla jouseen samanlaisia punnuksia, joista yhden paino on tunnettu, esimerkiksi noin 1 N. Kaksi punnusta venyttää jousta kaksi kertaa niin paljon kuin yksi, joten jokaiselle venymälle voi merkitä asteikkoon voiman. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina."
   This also sets up the first sentence of the Kaava section (line 17) without repeating it.

3. lesson.md:10 (FY1 anchor and axes, low). "kuten FY1:n lineaarisessa mallissa silloin, kun vakiotermi on nolla" is correct but abstract. The students' concrete memory is s = vt (fy1-5, "suoraan verrannollisuus"). Also "(voima, venymä)" does not say which quantity is on which axis, and FY1 uses the (x, y) order. Suggested rewrite:
   "Kuvaaja, jossa voima on vaaka-akselilla ja venymä pystyakselilla, on siis suora, joka kulkee origon kautta. Näin kävi myös FY1:n tasaisessa liikkeessä s = vt: kun kuljettu aika kaksinkertaistuu, myös matka kaksinkertaistuu."
   Optional: show the three example pairs as a small table (voima 2,5 / 5,0 / 10 N; venymä 1,0 / 2,0 / 4,0 cm) so the doubling is seen, not only read.

4. lesson.md:6-14 (pacing, low). The motivating question is about the Moon, but the answer arrives only in the fifth paragraph of Ydinajatus, after four paragraphs on force and spring scales. fy3-2 has three paragraphs there. A student may lose the thread. Cheapest fix is a bridge sentence at the start of line 8 (no need to cut text):
   "Jotta voimaa voi vertailla Maassa ja Kuussa, tarvitaan väline, jolla sitä mitataan: voimamittari."
   And at the start of line 14: "Nyt voimme vastata alun kysymykseen."

5. lesson.md:14 (cause left open, low). The lesson says the Moon's interaction is weaker but not why, and a curious student will ask. One honest sentence prevents a dead end without bringing in gravitation law: 
   "Syy on Kuun pienempi koko ja massa; painovoiman tarkempi laki kuuluu myöhempään kurssiin."

6. lesson.md:52 (misconception paragraph, low). Four ideas in one paragraph (everyday "painan 70 kiloa", mass does not change, force meter reads force, bathroom scale). The bathroom-scale sentence is the key to L3-03 and deserves its own paragraph. Suggested split, with the last part as a new paragraph:
   "Kylpyhuonevaaka näyttää kilogrammoja, vaikka se mittaa voimaa: sen asteikko on tehty Maassa jakamalla voima luvulla 9,81 N/kg. Kuussa sama vaaka näyttäisi noin kuudesosan oikeasta massasta."

7. exercises.json L1 set (rubric, low; not a violation by itself). Four of five L1 tasks are the same m -> G calculation and L1-01 is structurally identical to the worked example (lesson.md:45, "paino Maassa" from a given mass). L1-02 and L1-03 are near duplicates (both the Moon, one with g given, one with g from the table). The rubric allows L1 to be direct use of the formula, but "no exercise repeats the worked example with new numbers" is only weakly met. Smallest change: replace L1-02 (exercises.json:12-18) with a second spring task so the proportionality idea gets two L1 items:
   "Voimamittarin jousi venyy 2,0 cm, kun siihen ripustetaan 4,0 N:n paino. Kuinka monta senttimetriä jousi venyy 12 N:n painolla?" Answer 6.0 cm, tolerance 0.02 (unit cm). Check: 2,0 cm · 12/4,0 = 6,0 cm.
   If L1-02 is replaced, the solutions.md entry for L1-02 must follow (x = 2,0 cm · 12 N / 4,0 N = 6,0 cm; sanity: voima kolminkertaistuu). Any change here changes the hash, so decide whether this is worth another round; it is not required for PASS.

8. exit-ticket.json:7-8 (recall instead of check, low-medium). Question 2 reuses the lesson's own numbers (lesson.md:10: 5,0 N venyttää 2,0 cm; 10 N venyttää 4,0 cm) and ends with the same kind of whole-number multiple, so a student can answer by remembering the lesson. Use new numbers with a non-trivial ratio:
   q: "Voimamittarin jousi venyy 3,0 cm, kun siihen vaikuttaa 8,0 N:n voima. Kuinka paljon jousi venyy 20 N:n voimalla?"
   a: "7,5 cm. Venymä on suoraan verrannollinen voimaan, ja 20 N on 2,5-kertainen 8,0 N:oon verrattuna."
   Check: 3,0 cm · 20/8,0 = 7,5 cm.
   Questions 1 and 3 test the core idea well (mass stays, weight changes; kg versus N). Numbers check: 3,0 kg · 9,81 = 29,4 N, 3,0 · 1,62 = 4,86 N, 70 kg -> 687 N ≈ 690 N.

9. lesson.md:55-57 (summary, low). The summary does not say that g has the unit N/kg and means the weight of one kilogram, which is the one new convention of the lesson. Suggested third bullet:
   "- Maassa $g = 9{,}81\,\text{N/kg}$: yhden kilogramman massan paino on 9,81 N. Kuussa $g = 1{,}62\,\text{N/kg}$ ja Marsissa $3{,}71\,\text{N/kg}$."

## Checked and fine (no action)
- Motivating question (lesson.md:3) is natural and is answered in the lesson and in exit-ticket Q1.
- Mass versus weight (lesson.md:14, 52, exercises L2-01, L3-01, L3-03, exit ticket 1 and 3) is clear and consistently uses "paino" for the force and "massa" for kg. No "painaa 70 kiloa" slips elsewhere; the question's "painaa Kuussa kuudesosan" uses weight correctly.
- Line 17 links the spring scale to G = mg in one clear step (two equal bodies stretch twice as much -> weight proportional to mass). This is the pedagogic centre of the lesson and it works.
- Scope: force as a magnitude, no Newton's laws or motion, as the curriculum asks. g in N/kg here and m/s² in fy3-2 are bridged by the line-21 sentence (see finding 1); fy3-2 refers back to "edellinen oppitunti", consistent.
- Levels: L2-01 rearrangement, L2-02 g -> kg conversion, L2-03 two weights and a difference, L2-04 two steps (G = mg, then proportionality; borderline L3 but acceptable). L3-01 mass constant, L3-02 same force on the Moon (premise stated in the task itself), L3-03 scale calibrated on Earth used on the Moon; all are reasoning or unfamiliar context. 5/4/3 as required. Answers and tolerances recompute correctly (39, 8,1, 49, 1,5, 62; 5,0, 0,59, 1190, 5,9; 6,8, 133, 0,99). A student rounding sensibly stays within 0,02 (for example L3-03: 1,0 kg is 0,9 % off).
- Tone, length and structure match fy3-2 (same headings, one example with SVG, one misconception, bulleted summary); the lesson is shorter than fy3-2, appropriate for a first lesson.
- Finnish usage follows NOTES.md (units inflected as "12 N:n paino", no "80 N voimalla").
