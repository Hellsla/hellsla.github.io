VERDICT: PASS
CONTENT-HASH: 3b1b29439e94b105

Round 2, educator. A 17-year-old with FY1 and FY2 can follow the lesson. Linear model, suoraan verrannollisuus, kulmakerroin and liike-energia are all in FY1/FY2. Levels are 5/4/3 and match the rubric. No exercise reuses the worked example outright. Numbers re-checked: all answers lie inside tolerance of the unrounded values. All findings below are polish and non-blocking.

1. exercises.json:62, fy3-3-L2-03: same procedure (two points, line, zero pressure) and nearly the same answer (about -270 °C) as the worked example. It is not a copy, since p0 is not given and the points are not at 0 °C, so one extra step is needed. Still, a student can follow the example step by step, and the answer shows nothing new. Suggestion: ask for something the example does not, for example the pressure at -50 °C by extrapolation, or the temperature at which p = 50 kPa.
   Finnish: "Suljetussa jäykässä astiassa kaasun paine on 80 kPa lämpötilassa 20 °C ja 91 kPa lämpötilassa 60 °C. Oleta paineen riippuvan lämpötilasta lineaarisesti. Mikä paine astiassa olisi lämpötilassa −50 °C? Piirrä tarvittaessa (θ, p)-kuvaaja."

2. exercises.json:80 and :88, fy3-3-L3-01 and L3-02: they are the same template (convert to K, scale by the ratio, convert back), only inverted. L3-02 is now level 3 by the rubric (conversion plus proportionality plus rearrangement), but the two together test one idea. L3-01 is also exactly the motivating question. Suggestion: make L3-02 a reasoning task that needs the judgement "volume constant, so p ∝ T".
   Finnish: "Suljettu paineastia kestää enintään 600 kPa:n paineen. Siinä on ilmaa, jonka paine on 100 kPa lämpötilassa 20 °C. Astia joutuu tulipaloon. Paine on suoraan verrannollinen kelvinlämpötilaan. Missä celsiuslämpötilassa astia pettää? Miksi tulos ei ole 120 °C?" (answer 1,5·10³ °C, about 1465 °C. Check tolerance and sanity before use.)

3. lesson.md:6: the first Ydinajatus paragraph introduces system, environment, closed system, four state variables, pressure and kPa in one block. It is heavier than fy3-1 and fy3-2. Suggestion: split it in two.
   Finnish: insert a break after "systeemi on suljettu." and start the new paragraph "Systeemin tilaa kuvataan tilanmuuttujilla, joita ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. ..."

4. lesson.md:8: the volume case ends without a conclusion. The reader is told the particles hit the wall more often but not what happens to the pressure, whereas the temperature case ends with "paine kasvaa".
   Finnish: "...mutta yksittäinen törmäys ei muutu kovemmaksi. Törmäyksiä seinän pinta-alaa kohti tulee enemmän, joten paine kasvaa."

5. lesson.md:10: "kaasun paine on suoraan verrannollinen kelvinlämpötilaan" is stated before the example, and then the example seems to find it out. The example plots p against °C and extrapolates, so the order is slightly circular. Also the ratio form p₂/p₁ = T₂/T₁, which L3-01 and L3-02 need, is never written out. The misconception paragraph only shows a ratio of temperatures.
   Finnish: "Kokeet osoittavat, että kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan eli $p_2/p_1 = T_2/T_1$. Myös hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan, joten lämpötilojen suhteita verrataan kelvineinä."

6. lesson.md:70-73 (Tiivistelmä): it does not mention direct proportionality of p and T or the extrapolation to absolute zero, the main results of the example.
   Finnish: "- Vakiotilavuudessa kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Mittaustulosten suoran ekstrapolointi nollapaineeseen antaa absoluuttisen nollapisteen, noin −273 °C."

7. lesson.md:45 (SVG): the "p = 0" label sits above the left end of the dashed line and is detached from the open circle at (107,250). Cosmetic only: move it next to the circle, for example at x=107, y=232, text-anchor="middle".

Checked and fine:
- The line equation p = p₀ + kθ and the zero point θ = −p₀/k are derived in explicit steps, and the figure explains why the y-axis is at about -300 °C.
- Exit ticket has 3 questions, including the micro-model question, and its numbers (283 K to 293 K, about 3,5 %) agree with the lesson.
- Structure, tone and length (73 lines) are in line with fy3-1 (57) and fy3-2 (62), though a little denser.
