VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

Educator review, fy3-1, round 3. Hash checked at start and at end of the review: 8fb367b0d6fd83e0 both times.

Summary: a 17-year-old with FY1 and FY2 can follow the lesson. The hook is natural. Mass versus weight is clear and repeated (core idea, misconception, summary, exit ticket). The spring-scale idea (direct proportionality, line through the origin, identical-weight calibration, doubling) is reachable from FY1's linear model and the direct proportionality of s = vt and m = rho V. The softened g convention (N/kg, same number as FY1's m/s², reason deferred to FY4) is stated in three plain sentences. Exercise counts (5/4/3) and levels match the rubric, no exercise repeats the worked example, and every answer in exercises.json and the exit ticket was recomputed from the data and fits its tolerance. Tone, length (669 words against 703 in fy3-2) and structure match fy3-2. No blocking findings. All findings below are non-blocking polish.

## Findings (all non-blocking)

1. lesson.md:12 and :17, circular calibration logic. Line 12 defines "two bodies = 2 N" by calibration. Line 17 then uses "two identical bodies stretch twice as much" as the proof that G is proportional to m. A careful student may ask how we know two bodies pull twice as hard. Add one sentence saying that each identical body pulls the spring equally hard. Suggestion for line 12, after "ripustamalla jouseen samanlaisia pieniä kappaleita":
   "Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla."
   Then line 17 can start: "Koska kaksi samanlaista kappaletta vetää jousta kaksi kertaa niin voimakkaasti kuin yksi, paino on suoraan verrannollinen massaan:"

2. lesson.md:10, make the FY1 link concrete. "kuten FY1:n lineaarisessa mallissa silloin, kun vakiotermi on nolla" is correct but abstract. Students know s = vt and m = rho V as direct proportionality. Suggestion:
   "Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, aivan kuten FY1:n suoraan verrannollisissa malleissa $s = vt$ ja $m = \rho V$ (lineaarinen malli, kun vakiotermi on nolla)."
   Also consider one line saying why the proportionality is believable ("kokeessa kaksinkertainen kuorma venyttää jousta kaksinkertaisesti"). Line 10 currently asserts it without evidence.

3. lesson.md:12, the "1 N" of the calibration weights comes from nowhere. Line 6 says 1 N is about the weight of a 100 g apple, but line 12 only says "joiden paino on kunkin noin 1 N". Suggestion:
   "Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden massa on kunkin noin 100 g eli joiden paino on noin 1 N."

4. lesson.md:14, the hook is never answered in terms of why. The text says the Moon's interaction is weaker but not why. A curious student will ask. Suggestion, append to line 14:
   "Kuu on pienempi ja sen massa on pienempi kuin Maan, joten se vetää astronauttia heikommin."

5. lesson.md:21, this paragraph carries five ideas (meaning of g, unit, equality with FY1 m/s², course convention, other bodies). It is readable but dense. Suggestion: split it after "…joten 1 kg:n massan paino on 9,81 N." and start a new paragraph at "Luku 9,81 on sama kuin FY1:n putoamiskiihtyvyys…".

6. lesson.md:21 against content/FY3/fy3-2/lesson.md:25 (published lesson, outside this review's edit scope). fy3-1 says "Tällä kurssilla g:lle käytetään yksikköä N/kg", but fy3-2 writes "g = 9,81 m/s²" in the very next lesson, which cites G = mg from fy3-1. The student sees the unit change. Either align fy3-2 (suggestion: "g = 9,81 N/kg") when it is next revised, or soften fy3-1 to "Tässä oppitunnissa g:lle käytetään yksikköä N/kg, ja syy lukujen yhtäsuuruuteen selviää FY4:ssä." The second option needs no change in fy3-2 but still leaves the unit switch unexplained there. Note that CLAUDE.md names m/s² as the house convention, so the human should decide.

7. exercises.json (fy3-1-L1-02 and fy3-1-L1-04), L1 level and variety. Both are the same spring rule-of-three task, and the lesson shows no formula for it, only the worked sentence "5,0 N → 2,0 cm; 10 N → 4,0 cm; 2,5 N → 1,0 cm". The ratio is 3 in L1-02 and 0,5 in L1-04. It is still one idea with values given, so L1 holds, but three G = mg tasks plus two near-identical spring tasks is thin. Suggestion for L1-04, a different kind of task: "Kappaleen massa on 0,50 kg. Mikä on sen paino Maassa?" (answer 4,9 N). Or keep the spring task, but turn it around: "Jousi venyy 2,0 cm, kun siihen vaikuttaa 5,0 N:n voima. Kuinka suuri voima venyttää sitä 3,0 cm?" (7,5 N).

8. exercises.json (fy3-1-L1-02, L1-04), wording of "paino". "ripustetaan 4,0 N:n paino" and "12 N:n painolla" use "paino" for the hanging object, which blurs the mass versus weight distinction the lesson teaches. Suggestion for L1-02: "Voimamittarin jousi venyy 2,0 cm, kun siihen ripustetaan kappale, jonka paino on 4,0 N. Kuinka monta senttimetriä jousi venyy, kun ripustetaan kappale, jonka paino on 12 N?" Same fix for L1-04.

9. exercises.json (fy3-1-L3-03) with lesson.md:52. The misconception paragraph already explains the bathroom-scale idea almost completely, ending with "vaaka näyttäisi vain noin kuudesosan massasta". The task is therefore mostly recall plus one calculation, on the low edge of L3 (an unfamiliar context). It is still acceptable because the student must compute 9,72 N / 9,81 N/kg. If you want more reasoning, drop the last sentence of line 52 or change the task to "Mikä massa tämä Kuussa toimiva vaaka näyttää, kun siihen ripustetaan 12 kg:n kappale?" No change is needed to pass.

10. exit-ticket.json (question 3). It re-asks the lesson's misconception paragraph almost word for word ("painan 70 kiloa", 690 N), so it tests recall of the wording. Questions 1 and 2 test the core ideas well (mass stays and weight drops, G = mg in a new place, spring proportionality). Suggestion for question 3, a transfer item: "Kauppias sanoo: ’Tämä kananmuna painaa 60 grammaa.’ Mikä suure ja yksikkö on oikeasti kyseessä, ja mikä on munan paino Maassa?" (massa 60 g; paino noin 0,59 N). Note that this is the answer of exercise L2-02, so a different item may be better, for example a 1,5 l water bottle (massa 1,5 kg, paino noin 15 N).
