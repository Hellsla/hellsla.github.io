VERDICT: FAIL
CONTENT-HASH: 3d657337f41168ea

## Blocking
- inquiry.json:40 (kertaus, $1{,}3\,\text{J}$ feedback): "Silloin saisit tehon muutosnopeuden" is wrong physics. $P : t$ is not the rate of change of power, which is zero at constant power. — Fix: "Silloin yksikkö olisi $\text{W} : \text{s}$ eikä joule, joten tulos ei ole energiaa." Or drop the clause.
- lesson.md:141, 145 (worked example, Tulos and Järkevyys): the substitution ends at $36\,000\,\text{J}$, but the answer jumps to $36\,\text{kJ}$ (and $360\,000\,\text{J}$ to $360\,\text{kJ}$) without showing the conversion. This breaks the teacher's standing rule that unit conversions are done by substitution. — Fix: in Tulos, write $36\,000\,\text{J} = 36 \cdot 1000\,\text{J} = 36\,\text{kJ}$ before the sentence (and the same once for $360\,000\,\text{J} = 360\,\text{kJ}$). Or keep the check in joules.

## Polish
- lesson.md:33, 153: "aina alle $100\,\%$, koska osa energiasta muuttuu aina lämmöksi". A resistance heater, whose useful output is heat, is a counterexample (η ≈ 100 %). — Add "kun hyöty on muuta kuin lämpöä, ja lämmittimessäkin osa lämmöstä karkaa hyödyttömään paikkaan", or a similar qualifier.
- lessons/FY2/fy2-4/lesson-answers.py:39 — `inq-tulkinta-eta` (6,0 cm / 1,5 cm) belongs to no activity any more. The lesson's own numbers are missing: the Sankey cm example $4{,}0 : 5{,}0 = 80\,\%$ (lesson.md Kahden lampun vertailu) and the $100\,\text{W} \to 5\,\text{W}$ misconception example. — Fix: replace the stale line with these.
- inquiry.json ennuste-1: the koe-1 evidence is the model's preset 25 %, so the experiment cannot refute an engine prediction. The feedback now labels the value honestly ("simulaation mallin arvo"), which is acceptable. A sentence in koe-1's question feedback saying the 25 % is a typical measured value fed into the model, not a result of the sim, would close the loop.

## Checked
- One Python run recomputed every key of lesson-answers.py and all the inquiry and exit-ticket numbers, and all match. The values are 36 kJ, 1200 J (distractors 70, 1,3, 0,75), 25 % and 600/150/450 kJ, 15/45 kW, 24 kW, 2,0 W, 250 W (mistakes 1250 and 15 000), 80 % (20 and 125), 30 %/333 %, 70 %/150 J and 50/150 W.
- The previous blocking item is resolved. The model box, koe-1 intro, the conclusion ("mallissa … todellisen moottorin hyötysuhde riippuu kuormasta"), Tiivistelmä and lesson.md:44 now separate the model's constant η from real load dependence. Ennuste-2 states that the argument is the calculation, not the sim.
- The formulas η = E_a/E_o = P_a/P_o (steady power stated, t cancels shown), E_o = E_a + E_h, and P_o = P_a + P_h are correct and within FY2 scope. There is no W = Fs, Q = cmΔT, chain product or Carnot.
- The figures are to scale. Figure 1 splits 120 px into 6 and 114 (5 %/95 %). In figure 2, 96 px gives 4,8 + 91,2 and 16 px gives 4,8 + 11,2, so the LED input is 1/6 of the filament lamp's and the useful bands are equal.
- The sim implements the model (100, η·100 and (1−η)·100 px, E = Pt), and its limits are stated in the model and calc boxes. The canvas and readout are rendered LaTeX in the captures.
- Koe 1 and koe 2 each isolate t, with laite and P_o locked. The adapter sets laite before P_o, so setRange does not override 40 W. The values are in slider range, and simState has Eo, Ea and Eh.
- The worked example is symbolic first, with kW, min and % converted by substitution. It gives 2 s.f. with a justification and a real check.
- Siirto, koe-1 and tarkistus-2 solutions have all seven parts, and their numbers are correct.
- Typical-value table labelled as rounded typical values, not measurements; data honest.
- There is no ×, written division uses a colon, and numbers with units are in LaTeX throughout.
