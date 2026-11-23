VERDICT: FAIL
CONTENT-HASH: 7c3de62e349e40a5
SCOPE: full, new ```pysahdy boxes judged first; unit.md, inquiry.json, teacher.md, Sovella tasks s1–s8, solutions and answers.py judged again.

## Blocking
- **B: unit.md, third pysahdy box (Lämpötasapaino).** The box asks about water and ice in general ("Vettä ja jäätä sekoitetaan …") and answers "Jäätä jää jäljelle, ja lämpötila on tasan $0\,{}^\circ\text{C}$." That holds only while some liquid water is left. Very cold ice can freeze all the water and still end below $0\,{}^\circ\text{C}$, and the paragraph just above the box says so ("Hyvin kylmä jää voi myös jäädyttää … kaiken veden"). So the box, read on its own, contradicts the text next to it. Fix with one phrase in either place, e.g. "Vettä ja $0\,{}^\circ\text{C}$:n jäätä sekoitetaan …", or an answer like "Kun astiassa on sekä jäätä että vettä, lämpötila on tasan $0\,{}^\circ\text{C}$."

## Polish
- s3 d: the rubric criterion says the single-measurement result is "noin $12\,\%$" too large, but the solution says $13\,\%$. Recomputed: $2{,}54/2{,}256 = 1{,}127$ (or $600/530 = 1{,}13$), so $13\,\%$. Both are written as approximate, so a student loses no points either way.
- First box: "sitä on vain siirtymisen aikana" is correct. "Lämpö on siirtyvää energiaa, ei kappaleen ominaisuus" would avoid suggesting that heat is a stored thing that appears for a while.
- Carried over: s8 b, d call $333\,\text{kJ/kg}$ "the table value", while the rest of the set uses $334\,\text{kJ/kg}$.

## Checked
- Box 1 (kahvikuppi): correct definition of heat as energy transferred because of a temperature difference. It agrees with Ydinajatus, lt-2 and Yleisiä virheitä.
- Box 2 (jää sulaa): the mechanism (energy goes into interaction energy, not into the particles' kinetic energy) agrees with the formula section, tarkistus-1 and virhe-sulaminen. The pure-substance and constant-pressure condition is stated just before it.
- inquiry.json tarkistus-3: the change only splits paragraphs; the numbers ($17\,\text{kJ}$, about $80\,\text{K}$) are unchanged and correct.
- One script recomputed every number with my own formulas:
  - unit text: $21$, $334$, $419\,\text{kJ}$
  - lt-3 to lt-5 feedback
  - the aineisto answer $2083$ and its three distractors
  - amme $13{,}79$, juhlajäät $2{,}027$, masto $180\,\text{mm}$, katko $0{,}886\,\text{K}$, tarkistus-2 $3{,}88\,\text{kg}$, and every listed mistake value
  - s1: $54\,000\,\text{kg}$, $21{,}88\,\text{GJ}$, $17{,}37\,\text{h}$, shares $82/16/2\,\%$, times $2{,}7$ and $14\,\text{h}$
  - s2: $81{,}6\,\text{K}$, $1{,}667\,\text{kW}$, $35{,}8\,\%$
  - s3: least-squares fit $k = 0{,}1326\,\text{g/W}$, $r = 2{,}26\,\text{MJ/kg}$, $P_0 = 69\,\text{W}$; two-point reading $2{,}256$ and $69{,}9$
  - s5: $370{,}8$ and $333{,}0\,\text{kJ/kg}$
  - s6: $31{,}5$, $133{,}7\,\text{K}$, $40{,}2\,\%$
  - s7: $0{,}222$, $900$, $360$
  - s8: $2083$, $333$, $270{,}2$, $0{,}300$

  All agree within the tolerances.
- Every choice item has exactly one correct option, and its distractor feedback is right. Rubric points add up and the criteria ask only what each task gives. Models and conditions are stated: $Q = cm\Delta T$ without a change of state, expansion up to about $100\,\text{K}$, $P = UA\Delta T$ at constant temperatures.
- FY3 scope is kept, with FY2 and FY4 in s2 and s6 as the module intends. No "lämmöksi".
- Unit hash is the same at the start and the end.
