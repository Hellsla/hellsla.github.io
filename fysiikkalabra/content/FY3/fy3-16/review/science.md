VERDICT: FAIL
CONTENT-HASH: e6f18de4897f4105

## Blocking
- lesson.md:19,30,31,33,36,82–92,100,101,130 and inquiry.json:94 (the `kayra` figure). The figure labels are plain SVG `<text>`: the bar values 334, 42 and 335, "jää", "sulaa", the axis tick numbers, "jää sulaa", "vesi lämpenee", "moottori" and "jäähdytin". In the captures they sit in a sans font beside the serif KaTeX labels. The teacher's standing rule puts every figure label in LaTeX. Fix: move each one into a `foreignObject` `fig-tex` box, for example `$334$`, `$\text{jää}$` or `$5$`.
- lesson.md:198, solutions.md:40, solutions.md:171 and inquiry.json:173,177. These calculations are written as plain text: "41 900 J / 334 000 J = 13 %", "27 W … noin 97 kJ tunnissa", "4,3 h lyhenee 2,9 h:ksi, yhteensä 1,4 h", "100 % − 12,9 %" and "452 kJ / 67 kJ". The teacher's rule requires calculations in solutions to be in LaTeX. Fix: write each one as LaTeX, for example `$\dfrac{41\,900\,\text{J}}{334\,000\,\text{J}} \approx 0{,}13$`.

## Polish
- inquiry.json:14: "puolen tunnin kuluttua juomat ovat haaleita". The lesson's own model gives about 9 °C after 0,5 h (≈19–22 K/h at first, falling). Fix: say "parin tunnin kuluttua", or "eivät enää ole kylmiä".
- lesson.md:131 (figure 4): the heat arrow comes from outside into the engine, which suggests an outside source. Fix: draw P from the engine into the coolant, or mark the combustion inside the engine.
- inquiry.json:67: "sulattaa sitä eikä jäähdytä sitä". This should read "eikä muuta sen lämpötilaa".
- inquiry.json:290: "teho pysyy samana" holds only at first, because $UA\Delta T$ falls as the inside temperature rises. Fix: say "teho on aluksi sama".
- answers.py:33 comment says "-> 330 kJ" but the stored answer is 333. lesson.md:67 and inquiry.json:94 aria-labels use decimal points ("2.4", "3.7"). solutions.md:139 "kivien lämmönjohtuminen" is vague; say "kiuas lämmittää kiviä koko ajan".

## Checked
- All 16 answers recomputed independently; they match answers.py and the stored values, and each is within tolerance at the data's significant figures (largest gap: check-2, 210 against 213, 1,4 %).
- Worked example: t = 292 100 J / 33,6 W = 8,69·10³ s ≈ 2,4 h; checks 2,8 h, 13 % and 19 K/h. Solved symbolically first.
- Lesson graph: t₀ = 2,41 h → x = 257,9; exponential with τ = 6285/1,2 s; T(6 h) = 25,6 °C, matching the drawn point.
- Inquiry graph: t₀ = 3,68 h → x = 282,8; T(8 h) = 27,0 °C. The numeric answer of 333 kJ (tolerance 4 %) is consistent with this.
- Bar figure drawn to scale (21,3 px and 170,1 px against 169,5 px); 334 kJ ≈ 335 kJ at 80 K.
- Table t = sm/(UAΔT): all five rows are correct. pred-2's 2,9 h is correct.
- Löyly: 67 / 452 / 519 kJ and 87 %. siirto 64,9 s, with mistake values 8,4 and 56,5. virhe: 63 kJ, 267 kJ, 0,19 kg melted, 0,61 kg left.
- L3-02 checks first that all the ice melts (251 kJ > 167 kJ) and gets 8,06 °C. Misconception 3: 126 kJ < 334 kJ, so the mixture stays at 0 °C.
- Formulas: Pt = ΣQ, cmΔT, sm, rm, UAΔT and P = c(m/t)ΔT, each with its conditions. All fall within FY3's central contents and its prerequisites.
- No lesson ids appear in student text. Every correct option and every feedback reviewed.
