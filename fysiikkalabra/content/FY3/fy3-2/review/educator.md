VERDICT: PASS

Reviewer: educator. Scope: lesson.md, exercises.json, exit-ticket.json, solutions.md read as a 17-year-old with FY1, FY2 and fy3-1 only. The student can follow the lesson from start to finish and the exercise levels are roughly right. The findings below are real weaknesses, not blockers. Findings 1-4 should be fixed before the human moves the status to reviewed.

## Overall read
- Motivating question (repun kantaminen ei ole työtä) is one a student really asks, and the first paragraph answers it.
- The flow from "work is a transfer of energy" to W = Fs to the (s,F) area to P is clear. Units are consistent and the worked example's "kaksinkertainen virhe" note is good.
- The lesson is heavier than _gold (gold: 1 formula, 2-line example, 1-line misconception, 3 summary bullets; here 4 formulas, an SVG, a two-sentence misconception, 4 bullets). It is still readable, but E_k and E_p are only recall and could be one line.

## Findings

1. **Joulen koe is missing, and W = Fs is only asserted** (lesson.md:13-17; curriculum goal "määritellään kokeeseen perustuen (Joulen koe)"). The student never learns why work is defined as F·s and not, say, F·t. This is the one goal in the slot that the lesson does not touch.
   Suggested addition after line 17:
   > Miksi työ määritellään juuri näin? James Joule antoi painon pudota ja pyörittää vedessä siipipyörää. Mitä suurempi paino ja mitä pidempi putoamismatka, sitä enemmän vesi lämpeni: lämpeneminen riippui vain tulosta voima · matka. Tämän kokeen perusteella tulo $F s$ on järkevä mitta energiasiirrolle, ja sille annettiin nimi työ.

2. **The link to fy3-1 and to E_p = mgh is never made** (lesson.md:8, 21-25; exercises L1-02, L2-03, L2-04; solutions.md:57-64). The student is never told that lifting a mass h up with force G = mg does work W = G h = mgh = ΔE_p. This is the simplest demonstration of "työ kasvattaa energiaa" and it uses the prerequisite (G = mg). L2-03 and L2-04 silently assume it. Note: force at steady speed equals weight is FY4 (Newton's laws); say "nostat hitaasti" and rely on fy3-1 voimamittari.
   Suggested addition after line 25:
   > Kun nostat kappaleen hitaasti korkeudelle $h$, nostovoima on yhtä suuri kuin kappaleen paino $G = m g$ (fy3-1). Työ on siis $W = G h = m g h$, ja se on täsmälleen potentiaalienergian kasvu $E_p = m g h$.

3. **Level violations in exercises.json.**
   - exercises.json:7, L1-05 (4,0 min -> 240 s, kW -> W, and P = W/t rearranged to W = P t). That is a unit conversion plus a rearrangement, so it is L2 by the rubric, not L1. Also L1-04 (line 6) needs kJ -> J; give it in J or accept it as a trivial prefix. Fix L1-05: "Vesipumpun teho on 1500 W. Kuinka suuren työn pumppu tekee 240 sekunnissa?" (answer 360 kJ), and move the minutes version to L2.
   - exercises.json:17, L3-02 is a direct P = Fv plus km/h -> m/s. That is L2. The "Perustele kaava" part cannot be checked by a numeric answer. Make it reasoning, for example: "Kuorma-auto vetää perävaunua tasaisella nopeudella 80 km/h. Vetovoima on 4,5 kN. Kuinka paljon työtä vetovoima tekee yhden minuutin aikana ja mikä on teho? Selitä, miksi kaksinkertainen nopeus vaatii samalla vetovoimalla kaksinkertaisen tehon."
   - exercises.json:18, L3-03 is the same structure as L2-03 (Pt = mgh, solve for one quantity) with a minutes conversion. It is not new reasoning. Suggested replacement in an unfamiliar context: "Vesivoimalan turbiinin läpi putoaa 2000 kg vettä sekunnissa 30 m korkeudelta. Kuinka suuri on enintään teho, jonka vesi voi luovuttaa, ja miksi todellinen sähköteho on pienempi?"
   - exercises.json:12, L2-03 combines two formulas and rearranges for h. It is a high L2, borderline L3, acceptable.
   After the swaps L3 would have 1 real reasoning problem (L3-01) plus two new ones. This is not enough on its own to FAIL, but it is the main rubric weakness.

4. **No exercise uses the (s,F) graph or variable force** (exercises.json, all 12 items; goal "graafinen integrointi (s,F)-koordinaatistossa"). A named goal and half of the Kaavat section are untested. The sim spec (sim-spec.md) and sim.js:60 also show only a constant-force rectangle, so the student sees the area idea only in the static example. Add one L2 and make one L3 graph-based:
   - L2: "Voima vetää kappaletta niin, että voima kasvaa tasaisesti nollasta 30 N:iin matkalla 0,50 m. Laske työ." (answer 7,5 J; this is the area of a triangle with different numbers, so change the shape, see next item).
   - L3 (does not repeat the example): "Kuvaajassa voima on 20 N matkalla 0-2,0 m ja pienenee sen jälkeen tasaisesti nollaan matkalla 2,0-5,0 m. Laske kokonaistyö." (answer 50 J, rectangle plus triangle). Needs an inline SVG or a data table of points in the text.
   The example in lesson.md:34-55 (spring 0 -> 40 N, 0,20 m) must not be reused with new numbers, so keep the new problems a different context or a different shape.

5. **Solutions use W = F s cos α, which is outside the lesson and scope** (solutions.md:4-5, "cos 0°"). The lesson defines work only for force along the motion, and CLAUDE.md scope keeps vectors/angles for FY4. The student reading the solution meets an unexplained formula.
   Suggested rewrite of solutions.md:4-5:
   > **Kaava:** W = F s (voima on liikkeen suuntainen)
   > **Sijoitus:** W = 80 N · 25 m = 2000 J

6. **Energy losses are never mentioned before L3-01** (lesson.md:8; exercises.json:16). Line 8 says "kun teet kappaleeseen työtä, sen energia kasvaa täsmälleen tehdyn työn verran" and "energia ei synny eikä katoa", but the lesson does not say that friction and air resistance turn energy into heat. L3-01 then asks how much energy "kitka ja ilmanvastus veivät". The student has to infer a concept. Also "koko kurssin kantava ajatus" is an overclaim.
   Suggested rewrite of lesson.md:8 second half:
   > Kun teet kappaleeseen työtä, sen energia kasvaa tehdyn työn verran. Energia ei synny eikä katoa, vaan se vaihtaa muotoa ja omistajaa. Osa energiasta muuttuu usein kitkassa ja ilmanvastuksessa lämmöksi, joten se ei enää ole hyödyllisessä muodossa, mutta sitä ei ole hävinnyt mihinkään.

7. **Exit ticket tests a recalled example and a FY2 detail, not the whole core idea** (exit-ticket.json:3-12).
   - Line 3-5: the question is the lesson's own opening example (reppu), so it checks memory, not transfer. Replace with a new context: "Nostat laatikon lattialta pöydälle ja kannat sen sitten vaakasuoraan pöydän toiseen päähän. Missä vaiheessa voimasi tekee työtä?" Answer: "Vain nostaessa. Vaakasuoralla kannolla voima osoittaa ylös, mutta liike on sivulle, joten työ on nolla."
   - Line 6-8: v^2 scaling is a FY2 detail never discussed in this lesson. Replace with a check of W = Fs / area: "Jousta venytetään 10 cm ja voima kasvaa tasaisesti nollasta 30 N:iin. Mikä on tehty työ?" Answer: "1,5 J (kolmion pinta-ala, ei 30 N · 0,10 m = 3 J)."
   - Line 10-12 (työ vs teho) is a good core check; keep it.
   A fourth item is not needed; _gold has one question, three is already generous.

8. **Worked example never says where the energy went** (lesson.md:34-55). It computes 4,0 J and 8,0 W, but a student asks "työ mihin?". The example also stacks three ideas (area, average force, power) in six lines.
   Suggested rewrite of lesson.md:51 ending:
   > Työ on kolmion pinta-ala: $W = \tfrac{1}{2} \cdot 40\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$. Tämä energia on nyt varastoituneena venytettyyn jouseen.
   Optionally tie to fy3-1: "Voima luetaan voimamittarista (fy3-1)" in line 34 so the force values have a source.

9. **Wording that may confuse** (lesson.md:3, 6, 62).
   - "siirtää kappaletta omaan suuntaansa" (lines 6, 58) is awkward and ambiguous (whose direction?). Suggested: "voima tekee työtä vain, kun kappale liikkuu voiman suuntaan".
   - Line 62 "nollatyötä" is not a word; suggested: "Kantaminen tasaisella alustalla ei tee fysiikassa työtä."
   - The student may ask about forces at an angle (hinaus köydellä). One line suffices: "Jos voima ja liike eivät ole samansuuntaisia, laskenta kuuluu myöhemmille kursseille; tässä käsitellään vain liikkeen suuntaista voimaa."
   - Summary (lines 61-64) omits P = Fv, which is used in L3-02. Add: "Tasaisessa liikkeessä $P = F v$."

10. **Significant figures** (exercises.json:5, L1-03). Data 85 kg and 6,0 m/s have two significant figures, answer 1530 J has three. CLAUDE.md says not more than the data has. Suggest answer 1.5 with unit "kJ" (tolerance 0.03), and update solutions.md:17-23 accordingly.

## Not issues (checked)
- Numeric answers recomputed: L1-01 2000 J, L1-02 176,6 J, L2-01 375 kJ, L2-02 16,2 MJ, L2-03 43,2 m, L2-04 760 W, L3-01 14,4 kJ, L3-02 100 kW, L3-03 45,4 min are all consistent with the solutions.
- No exercise repeats the worked example with new numbers; none uses the spring.
- Counts are correct: 5 / 4 / 3.
