VERDICT: FAIL
CONTENT-HASH: 9c6ecf76a631b766

Reviewer: educator. Lesson fy3-3 "Termodynaaminen systeemi, tilanmuuttujat ja lämpötila". The lesson text can be followed by a 17-year-old (see the notes at the end). The FAIL is for the exercise set only: findings 1 and 2 break the rubric rule "no exercise repeats the worked example with new numbers" and the level-3 definition. Findings 3-12 are non-blocking.

## Blocking

1. exercises.json:90 (fy3-3-L3-02) repeats the worked example and is not level 3. The worked example (lesson.md:48-58) computes the slope of a (θ, p) line and extrapolates it to p = 0. L3-02 asks for exactly that: slope from the first and last of four points, then θ = θ₁ − p₁/k. The four points are exactly linear (19 kPa per 20 °C), so there is no fitting and no judgement involved. It is also the same task as L2-03 (exercises.json:64), only with more points. Level 3 needs reasoning, two ideas combined, or an unfamiliar context, and none of those is present. Replace it with a task that combines the proportionality p ∝ T (the lesson's misconception section) with a conversion and a rearrangement, for example:
   "Suljetussa jäykässä kaasupullossa paine on 150 kPa lämpötilassa 27 °C. Pulloa lämmitetään, kunnes paine on 200 kPa. Paine on suoraan verrannollinen kelvinlämpötilaan. Mikä on loppulämpötila celsiusasteina?"
   Answer 127 °C (T₂ = 300,15 K · 200/150 = 400,2 K, θ₂ = 127,05 °C), tolerance 0,02. It differs from L3-01, where the pressure is the unknown and the temperatures are given. A short-text alternative is: "Oppilas piirtää saman kokeen kuvaajan kelvineinä, (T, p). Minkä muotoinen kuvaaja on ja missä kohdassa se leikkaa p-akselin? Perustele mikromallilla."

2. exercises.json:56 (fy3-3-L2-02) reuses the worked example's own data. It gives 100 kPa at 0 °C and 137 kPa at 100 °C, which are the example's table values, and the slope 0,37 kPa/°C is already computed in lesson.md:50. The student only substitutes into the finished line, so this counts as the example with a different question and the same numbers. Use new data, for example:
   "Suljetussa jäykässä astiassa kaasun paine on 90 kPa lämpötilassa 0 °C ja 123 kPa lämpötilassa 100 °C. Oleta, että paine riippuu lämpötilasta lineaarisesti. Mikä on paine lämpötilassa 35 °C?"
   Answer 101,55, so 102 kPa. Update solutions.md:49-55 to match (k = 0,33 kPa/°C).

## Non-blocking (polish)

3. exercises.json:48 (fy3-3-L2-01) is level 1 in disguise. The only step is converting 303 K to °C, which is the same as L1-02. The 288 K is just a distractor. Rewrite so the student adds a temperature difference and then converts:
   "Kaasu lämmitetään 288 K:n lämpötilasta lämpötilaan, joka on 45 K korkeampi. Mikä on loppulämpötila celsiusasteina?"
   Answer 59,85, so 60 °C. Update solutions.md:41-47.

4. lesson.md:10, lesson.md:61 and exit-ticket.json:8. The lesson never says why the kelvin scale is the right one for comparisons. The misconception section and exit ticket Q2 say "liike-energia ei kaksinkertaistu", and L3-03 gives "suoraan verrannollinen kelvinlämpötilaan" as a hint, but the lesson's core idea does not state the link. A student can accept the claim without understanding it. Add to lesson.md:10 after "ja eikä kylmempää voi olla":
   "Keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan: kun T kaksinkertaistuu, myös liike-energia kaksinkertaistuu. Siksi lämpötilojen suhteita verrataan kelvineinä."
   Also change the Q2 answer from "riippuu kelvinlämpötilasta" to "on suoraan verrannollinen kelvinlämpötilaan".

5. exit-ticket.json:3 (Q1). The ticket is mostly recall. Q1 lists state variables, Q2 tests the misconception and Q3 tests absolute zero, but nothing tests the core explanation from the motivating question, which is the micro model: temperature, particle speed, collisions and pressure. Replace or extend Q1 with:
   q: "Miksi suljetun, jäykän astian kaasun paine kasvaa, kun kaasu lämpenee? Selitä mikromallilla."
   a: "Lämpötilan noustessa hiukkasten keskimääräinen liike-energia kasvaa. Hiukkaset osuvat seinään useammin ja kovempaa, joten paine kasvaa."
   The state-variables check can stay as a second sentence: "Mitkä tilanmuuttujat pysyvät tässä samoina?" with the answer "tilavuus ja aineen määrä".

6. lesson.md:53. "ekstrapoloimalla" is not explained, and the equation of the line is skipped (lesson.md:53-56). The step from the slope to θ = −p₀/k is a rearrangement the student must do alone, and L2-03 needs the harder version θ = θ₁ − p₁/k. Suggested text:
   "Jatketaan suoraa vasemmalle mittausalueen ulkopuolelle eli ekstrapoloidaan. Suoran yhtälö on p = 100 kPa + k·θ. Nollapaineessa 0 = 100 kPa + k·θ, joten"
   Then keep the existing display formula, which is the same rearrangement. Add one sentence for the general case, which L2-03 needs: "Jos tunnetaan vain piste (θ₁, p₁), nollakohta on θ = θ₁ − p₁/k."

7. lesson.md:22-26. Pressure and kPa are used without any definition. The pressure lesson is fy3-4, which lists fy3-3 as a prerequisite, so this is a forward use. A student who does not remember kPa from lower secondary school can still read the table, but one sentence helps. Add after line 22:
   "Paine kertoo, kuinka voimakkaasti kaasu työntää astian seinää; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. Paineeseen paneudutaan tarkemmin myöhemmin."

8. lesson.md:28-46, the figure. The vertical axis is drawn at about −300 °C (x = 70), not at θ = 0, and only −270, 0 and 100 are marked. Students expect the p axis at θ = 0 and may misread the picture. Add a caption under the figure:
   "Pystyakseli on piirretty kuvassa kohtaan −300 °C, jotta suoran jatke mahtuu näkyviin. Yhtenäinen suora on mittausalue, katkoviiva ekstrapolointi."
   Also mark 20, 40, 60 and 80 °C on the x-axis, or drop the unlabelled points from the claim "Pisteet asettuvat suoralle".

9. lesson.md:58. The example ends with "Näin absoluuttinen nollapiste voidaan määrittää kokeellisesti". Add a short honesty note so bright students are not confused: "Todelliset kaasut nesteytyvät ennen tätä lämpötilaa, mutta suoran jatke osoittaa rajan, johon mikromalli on kuvattu." Optional, kept to one sentence.

10. lesson.md:10 and lesson.md:17. Line 10 says "Asteikkojen yksi aste on yhtä suuri", and line 17 says kelvinille ei sanota "aste". Use consistent wording: "Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina."

11. exercises.json:72 (fy3-3-L2-04) is thin for level 2. It is L1-04 (ΔT = Δθ) with a negative number. The Moon context is good, but add a step so it is a real level-2 task:
   "Kuun yöpuolen lämpötila on −173 °C ja päivänpuolen 127 °C. Anna lämpötilat kelvineinä ja laske lämpötilaero kelvineinä."
   Keep the answer 300 K, or make the task ask for the day-side temperature in K (400 K). Optional.

12. lesson.md:61, the misconception wording. "Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee 10 °C:sta 20 °C:een" is clear. Make the ratio explicit so it connects to L3-03: "Kelvineinä lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin 3,5 %."

## Checks that passed

- Hash: `python scripts/gate.py --hash fy3-3` gave 9c6ecf76a631b766 at the start and at the end, so no redo was needed.
- Level counts: 5 / 4 / 3, as the rubric requires.
- Tolerances: 0,02 is fine for every answer, including the 273 vs 273,15 variants.
- Numbers: all answers re-checked and correct: 294, 77, −196, 25, −270, 30, 119, −270 (−270,9), 300, 321, −273 (−273,2), −127.
- Motivating question: the summer tyre with no extra air pumped is natural, and lesson.md:8 answers it with the micro model.
- Micro model (lesson.md:8): particles move, so they collide with the wall. Temperature is the average kinetic energy. Hotter at fixed volume means more frequent and harder hits, so higher pressure. The steps are in order, with one idea per sentence. "Liike-energia" without a formula is fine after FY2.
- Kelvin and absolute zero (lesson.md:10, 17-19): the offset, the same step size, no word "aste" for kelvin, and the fact that celsius can be negative but kelvin cannot are all clear.
- Extrapolation example: a student can follow table, then line, then slope 0,37 kPa/°C, then zero point −270 °C, then the comparison with −273 °C. The only gaps are findings 6 and 8.
- Structure and tone: matches fy3-2 (Miksi, Ydinajatus, formula, Esimerkki, Yleinen virhekäsitys, Tiivistelmä). Length is 67 lines against 62. The register is the same and the summary has four bullets in both.
- fy3-3 does not repeat the worked example in L1 or in L3-01 and L3-03. L3-01 and L3-03 are good level-3 tasks, combining a conversion with proportional reasoning and building on the misconception.
