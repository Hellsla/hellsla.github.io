VERDICT: FAIL
CONTENT-HASH: 389bd4a1d84db983

## Blocking
- lesson.md:622 — **Major, A.** The reason for rounding is wrong: "Kokonaisluku $480\,\text{kg}$ tulkitaan tarkaksi arvoksi". A measured mass is not exact because it is an integer. Under P7 (NOTES §2) 480 kg has three significant figures. The answer $1{,}02\,\text{m/s}^2$ stands, but the stage teaches a wrong rule. — Fix: "kolme merkitsevää numeroa kuten lähtötiedoissa $480\,\text{kg}$, $5{,}20\,\text{kN}$ ja $9{,}81\,\text{m/s}^2$"; delete the exact-value sentence.

## Polish
- lesson.md:595 — **Minor.** The *Kaava ratkaistuna* stage opens with the combined $T - mg = ma$. Start from $\Sigma\overline{F} = m\overline{a}$ → $T - G = ma$ → $G = mg$ (read-through rule).
- inquiry.json:516 (check-3 model) — **Minor.** $N \approx 11{,}8\,\text{N}$ should be $12\,\text{N}$: $m = 1{,}2\,\text{kg}$ has two figures.
- inquiry.json:423 (siirto solution) — **Minor, B.** Air and rolling resistance are left out unstated (the answer $\Sigma F = ma$ is unaffected). Add "ilmanvastus ja vierimisvastus jätetään huomiotta".
- inquiry.json:18 (hook) — **Minor.** "kuljettajat kiihdyttävät yhtä voimakkaasti", read literally, means equal acceleration, which contradicts the outcome. Use "painavat kaasua yhtä paljon".
- figures.py valitse_d — **Minor.** The extra $\overline{F}$ (36 px) makes the drawn sum $1{,}3G - G - F$ point down, a second implicit error against "yksi virhe". Make $\overline{F}$ shorter than $0{,}3G$.

## Checked
- One script recomputed all 23 lesson-answers.py values (example, siirto and its three mistakes, check-2 and its two mistakes, check-3, experiments). All agree.
- The figures are to scale: kokonaisvoima $G/T$ 1,307 against 1,308 in the physics, $F_\mu = T/3$; esimerkki $T/G$ 1,102 against 1,104; kuvaaja; nosturi.
- sim.js: $a = \pm F/m$ with no friction, and the fit equals the model. No run is shorter than 0,5 s. Exp-3 pulling left reverses at 0,75 s, matching pred-3.
- simState gives sumFx, a, v and m. Each experiment locks all but the varied key.
- Predictions, valitse, check-1 and exp-3's question each have one correct option, and every distractor's feedback is right.
- The exit ticket, the misconception box, the summary and the sim boxes are consistent: net force always points along $\overline{a}$.
- Within FY4 scope.

## Scores
- 1 Physics and mathematical correctness: **3**. Every number, figure and model is right; one Major reasoning error (significant figures).
- 6 (physics: models and uncertainty): **4**. The sim's model and controlled variables are sound and labelled as model values; uncertainty is not discussed, which suits a noise-free fit.
