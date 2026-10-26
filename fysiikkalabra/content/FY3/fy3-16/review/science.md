VERDICT: PASS
CONTENT-HASH: 7b642f39b87c6795

## Blocking

## Polish
- inquiry.json:718,723,725 (check-3): the prompt gives only 25 kg of stones, but the model answer uses 0,20 kg of water at 20 °C (67 kJ and 452 kJ), and criterion 4 asks for "noin 13 %", which comes from those same figures. A student cannot get these numbers from the prompt. Fix: add "0,20 kg 20-asteista vettä" to the prompt, or drop the numbers from criterion 4.
- solutions.md:1018 (L3-03 Järkevyys): the sum "Seinä tuo 486 kJ ja juomat 50 kJ, yhteensä noin 536 kJ" is written in prose. The same holds for "565 kJ eli noin 87 %" (solutions.md:941), "452 kJ eli 87 %" (solutions.md:985) and "339 kJ eli 87 %" (inquiry.json siirto solution). Fix: write them as LaTeX, for example `$486\,\text{kJ} + 50\,\text{kJ} \approx 536\,\text{kJ}$` and `$\tfrac{565}{649} \approx 87\,\%$`.
- inquiry.json:443 (pred-1) puts "jääpussi ja juomia" in the bag, but the `kayra` model curve has only 1,0 kg of ice ($\tau = 4190 \cdot 1{,}0 / 0{,}90$ s). This is qualitatively harmless. Fix: drop "ja juomia" so the prediction and the graph describe the same bag.
- lesson.md:369: `$4190 \cdot 1{,}5 = 6285\,\text{J/K}$` carries no units on its factors, unlike the rest of the example. Fix: add the units to the factors.

## Checked
- Hash 7b642f39b87c6795 at start and end. All 18 answers.py values were recomputed independently and match. Each stored answer lies within its tolerance at the data's significant figures (check-2: 210 against 213, 1,4 %).
- Round-1 blockers are resolved. No SVG `<text>` remains in lesson.md or inquiry.json, and every label is a `fig-tex` foreignObject. The flagged plain-text calculations (example 13 %, L1-03 97 kJ, löyly 14,3 %, mistake 6,0) are now in LaTeX.
- Round-1 polish items are done: the hook says "parin tunnin kuluttua", Dan's feedback says "eikä muuta sen lämpötilaa", check-1 says "teho on aluksi sama", and the coolant figure's heat arrow starts inside the engine.
- Worked example: solved symbolically first. t = 2,41 h; the cross-check gives 2,8 h, 13 % and 19,2 K/h.
- Lesson graph: t₀ = 2,41 h, which puts x = 257,9; τ = 6285/1,2 s; T(6 h) = 25,6 °C. Inquiry graph: t₀ = 3,68 h, which puts x = 282,8; T(8 h) = 27,0 °C. Both are drawn as computed.
- Bar figure is to scale (0,508 px/kJ). Table rows t = sm/(UAΔT) are all correct. pred-2's 2,9 h and its distractor 2,2 h are correct.
- Löyly 85,7 %, with mistake values 14,3 and 6,0. siirto 64,9 s, with mistake values 8,4 and 56,5. virhe: 63 kJ, 267 kJ, 0,19 kg melted. The weighted average comes out the same in K and °C.
- L3-02 checks first that all the ice melts (251 kJ > 167 kJ). Misconception 3: 126 kJ < 334 kJ. Exit ticket: 175,5 kJ and 335 kJ.
- Formulas Pt = ΣQ, cmΔT, sm, rm, UAΔT and P = c(m/t)ΔT each come with their conditions, and all lie inside FY3's contents and prerequisites.
- No lesson ids appear in student text. Every correct option and every feedback was reviewed.
