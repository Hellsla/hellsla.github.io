VERDICT: PASS
CONTENT-HASH: da9ba5eb24ac7a54

# Educator review, fy3-1 (Voima vuorovaikutuksen mittana ja paino G = mg)

No blocking findings. A 17-year-old who has done FY1 and FY2 can follow the lesson, the levels match the rubric (5/4/3), and the exit ticket tests the core idea. The findings below are improvements, ordered by value. Findings 1 to 4 are the ones I would fix if a fixer round happens anyway.

## What works
- The motivating question is one a student would really ask. The lesson answers it directly in the third paragraph of Ydinajatus (lesson.md:10) and again in the worked example.
- Mass versus weight is clear: mass is the amount of matter in kg and the same everywhere, weight is a force in N and depends on place (lesson.md:10). The worked example (lesson.md:47) and the misconception section (lesson.md:50) repeat the point from two sides.
- The structure matches `_gold` (Miksi, Ydinajatus, Kaava, Esimerkki, Yleinen virhekäsitys, Tiivistelmä). The length (540 words) is between gold (a stub) and the published fy3-2 (703 words). The tone is the same as in fy3-2.
- Scope is respected: no Newton's laws, no vectors, force only as a measure of interaction.
- All numbers recomputed: 39,24 / 8,1 / 92,75 / 62,0 / 4,995 / 0,5886 / 1187,55 / 5,886 / 6,807 / 133,2 / 0,991 are correct, and the answers and tolerances are consistent with the data's significant figures. The exit-ticket values (29 N, 4,9 N, 690 N) are correct.

## Exercise level audit
- L1 (5): four are G = mg with one given g (01 uses g = 9,81 from the lesson). L1-04 is a proportion with no formula, but the ratio is exactly one half, so it stays at L1 (see finding 1: the lesson never teaches it).
- L2 (4): 01 rearrangement, 02 g to kg conversion, 03 two weights and a difference, 04 weight plus proportion. All fit the rubric.
- L3 (3): 01 constant mass, new place; 02 same force, different g; 03 scale calibrated on Earth, read on the Moon. All are reasoning or unfamiliar-context tasks. Good.
- Repetition rule: L1-03 comes close to repeating the worked example (finding 8). None of the others do.

## Findings

1. **lesson.md:8 (spring scale paragraph carries three ideas, and the proportion calculation is never shown).** The paragraph packs together the spring scale, direct proportionality, the link to FY1's linear model and calibration. "Kalibroitu" is not explained. The proportion step (new stretch = old stretch times force ratio) is needed by L1-04, L2-04 and exit-ticket question 2, but neither the text nor the worked example shows it. Also, FY1's linear model is y = kx + b in general, and the lesson does not say that proportional means b = 0, so the link is reachable but not quite spelled out. Suggested rewrite:
   > Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa. Venymä on suoraan verrannollinen voimaan: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan ja kolminkertainen voima kolminkertaisen. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta. Se on FY1:n lineaarinen malli tapauksessa, jossa vakiotermi on nolla. Jos tiedät yhden parin, esimerkiksi 5,0 N venyttää jousta 2,0 cm, voit laskea muut: 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm.
   >
   > Asteikko kalibroidaan ripustamalla jouseen tunnettuja painoja ja merkitsemällä, kuinka pitkälle jousi kullakin venyy. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.

2. **lesson.md:6 (the first paragraph is abstract, and "paino" is used before it is defined).** "Vuorovaikutus" and "voima" are defined in terms of each other, and no concrete interaction is named. The apple example uses "paino" one paragraph before the term is introduced. Suggested rewrite:
   > Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa, ja magneetti vetää rautanaulaa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N). Noin 1 N on voima, jolla Maa vetää sadan gramman omenaa, eli omenan paino.

3. **lesson.md:13 (the two halves of the lesson are not connected: why is weight proportional to mass?).** G = mg is stated as a fact. The spring scale is the obvious bridge, because two identical objects stretch the spring twice as much as one. A student who has just learned "venymä verrannollinen voimaan" can then see "voima verrannollinen massaan" for themselves. Suggested rewrite of the first line under Kaava:
   > Kaksi samanlaista kappaletta venyttää voimamittarin jousta kaksi kertaa niin paljon kuin yksi, joten paino on suoraan verrannollinen massaan:

4. **lesson.md:17 (the definition of g is abstract, and "mittaamasi" assumes the student measured g in FY1).** "Painovoiman voimakkuus massayksikköä kohti" is hard to read. A curious student also asks why N/kg and m/s² are the same number; the lesson only says it is the same number, which is fine at FY3 level if it is said openly. Note that fy3-2 line 25 uses g = 9,81 m/s², so the bridge sentence also helps there. Suggested rewrite:
   > missä G on paino (N), m massa (kg) ja g painovoiman voimakkuus (N/kg). Se kertoo, kuinka suuri on yhden kilogramman painon voima. Maan pinnalla g = 9,81 N/kg. Se on sama luku kuin FY1:ssä käsitelty putoamiskiihtyvyys 9,81 m/s². Yksiköiden yhteyden selvittäminen kuuluu FY4:ään, joten tässä riittää tietää, että luku on sama. Muualla g on erilainen:

5. **lesson.md:26 (meta sentence, and "only magnitude" sits next to an arrow that shows direction).** The sentence repeats the weight definition and then says force has "vain suuruus" while the arrow in the figure shows a direction. A student reads this as a contradiction. Suggested rewrite:
   > Tässä vaiheessa meitä kiinnostaa vain voiman suuruus. Kuvissa nuoli näyttää, mihin suuntaan voima osoittaa. Suuntien käsittely kuuluu FY4:ään.

6. **lesson.md:43 and :31 (significant figures, unneeded kN, figure placement).** 120 kg is given with 2 to 3 significant figures, so "1177 N" (4 sf) is over-precise, and the "1,2 kN" rounding introduces an extra unit. CLAUDE.md asks for three significant figures. The figure of the spring scale also appears inside the robot example, while the spring scale is introduced in Ydinajatus, so the figure comes after the first mention of the spring scale and the body text. Suggested rewrite:
   > Maassa: $G = m g = 120\ \text{kg} \cdot 9{,}81\ \text{N/kg} = 1180\ \text{N}$.
   >
   > Marsissa: $G = 120\ \text{kg} \cdot 3{,}71\ \text{N/kg} = 445\ \text{N}$.
   >
   Optionally move the SVG to directly after the spring paragraph (line 8) and add a caption: "Voimamittarissa jousi venyy sitä enemmän, mitä suurempi on ripustetun kappaleen paino G."

7. **lesson.md:50 (a question every student has is left unanswered).** The text says "jousivaaka mittaa voimaa, ei massaa". But the student's own bathroom scale shows kilograms, and he or she will ask why. The answer is only found in L3-03. One sentence in the misconception section closes it. Suggested rewrite of the last sentence:
   > Huomaa myös, että jousivaaka mittaa voimaa, ei massaa: sen lukema muuttuisi, jos se vietäisiin toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska sen asteikko on laskettu Maassa jakamalla voima luvulla 9,81 N/kg. Kuussa sellainen vaaka näyttäisi noin kuudesosan oikeasta massasta.

8. **exercises.json:22 (L1-03 is the worked example's Mars half with new numbers).** The worked example is "tutkimusrobotti, paino Maassa ja Marsissa"; L1-03 is "Mars-kulkija, paino Marsissa". The rule "no exercise repeats the worked example" is nearly broken. L1-02, 03 and 05 are also the same task with a different planet. Suggested rewrite of L1-03 as a table lookup (answer 49 N, since 30 kg · 1,62 N/kg = 48,6 N):
   > "Kuun pinnalle jätetyn mittalaitteen massa on 30 kg. Mikä on sen paino Kuussa? Katso g:n arvo oppitunnin taulukosta."

   with `"answer": 49`, `"unit": "N"`, `"tolerance": 0.02`. The matching text in solutions.md would change accordingly (30 kg · 1,62 N/kg = 48,6 N; "Maassa sama laite painaisi noin 294 N, joten Kuussa paino on noin kuudesosa").

9. **exercises.json:72 and :98 (wording).** "ripustetaan ... 0,20 kg:n massa" mixes up the object and its mass. L3-03's sentence is hard to parse on the first read. Suggested rewrites:
   - L2-04: "Voimamittarin jousi venyy 1,5 cm, kun siihen ripustetaan Maassa 0,20 kg:n kappale. Kuinka suuri voima venyttää jousta 4,5 cm?"
   - L3-03: "Jousivaaka on kalibroitu Maassa niin, että sen lukema kilogrammoina on voima jaettuna luvulla 9,81 N/kg. Vaa'alle asetetaan Kuussa (g = 1,62 N/kg) kappale, jonka massa on 6,0 kg. Mitä lukemaa vaaka näyttää kilogrammoina?"

10. **exercises.json:82 (L3-01 hint gives away the method, low priority).** "Vihje: mikä pysyy samana?" turns the reasoning step into a prompt. It is acceptable for a first lesson, but if the fixer wants L3-01 to differ from the level 2 tasks, a student could try it without the hint first. Suggested rewrite: remove the hint from the text and move it to solutions.md as "Ajatus: massa pysyy samana".

11. **exit-ticket.json (fine, with one optional improvement).** The three questions test the core idea (mass constant and weight changes, spring proportion, kg versus N). Questions 1 and 3 both test the same misconception from two sides, and question 1 needs g for the Moon from memory. Optional: give the values in the question, "(g = 1,62 N/kg Kuussa)", so the question tests the idea and not the memory of a table:
    > "Kappaleen massa on 3,0 kg. Mitä sen massalle ja painolle tapahtuu, kun se viedään Maasta Kuuhun (g = 1,62 N/kg)?"
