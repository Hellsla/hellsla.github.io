VERDICT: FAIL
CONTENT-HASH: 389bd4a1d84db983

## Blocking
- lesson.md:622 — **Major, A.** The worked example's *Tulos* stage gives a wrong reason for rounding: "Kokonaisluku $480\,\text{kg}$ tulkitaan tarkaksi arvoksi, joten se ei rajoita tarkkuutta." A measured or rated mass is not exact just because it is an integer. Under NOTES §2 / P7 its trailing zero is significant, so 480 kg has three significant figures (480 kW: three). The answer $1{,}02\,\text{m/s}^2$ (three figures) is still right, but the stage teaches students a wrong rule. — Fix: "Siinä on kolme merkitsevää numeroa kuten lähtötiedoissa $480\,\text{kg}$, $5{,}20\,\text{kN}$ ja $9{,}81\,\text{m/s}^2$." and delete the sentence about an exact value.

## Polish
- lesson.md:595 — **Minor.** The *Kaava ratkaistuna* stage starts from the combined form $T - mg = ma$. The read-through rule (2026-11-13) says to start from the basic principle: $\Sigma\overline{F} = m\overline{a}$ → $T - G = ma$ → $G = mg$.
- inquiry.json:516 (check-3 model) — **Minor.** $N \approx 11{,}8\,\text{N}$ comes from $m = 1{,}2\,\text{kg}$, which has two figures, so it should be $12\,\text{N}$ (the same model correctly rounds $a$ to $1{,}7$).
- inquiry.json:423 (siirto solution) — **Minor, B (harmless).** The force diagram leaves out air resistance and rolling resistance without saying so. The answer is not affected, since the task asks for $\Sigma F = ma$. Add "ilmanvastus ja vierimisvastus jätetään huomiotta".
- inquiry.json:18 (hook) — **Minor.** "molemmat kuljettajat kiihdyttävät yhtä voimakkaasti", read literally, says the two trucks have equal acceleration, which contradicts the next sentence. Suggest "painavat kaasua yhtä paljon" / "moottorit vetävät yhtä voimakkaasti".
- figures.py valitse_d — **Minor.** The extra arrow $\overline{F}$ (36 px) makes the drawn sum $1{,}3G - G - F$ point down. That is a second, implicit error, while the task says "yksi virhe". Make $\overline{F}$ shorter than $0{,}3G$, or have the feedback stop at "Voimalla $\overline{F}$ ei ole aiheuttajaa".

## Checked
- One script recomputed all 23 lesson-answers.py values with my own formulas: example 4708,8 N / 491,2 N / 1,023 m/s², siirto 7000 N and its mistakes 25 200 / 5,0 / 13 734, check-2 1,0 and its mistakes 1,67 / 2,33, check-3 1,67 m/s². All agree.
- The figures are to scale: kokonaisvoima $G/T$ 1,307 against 1,308 in the physics, $F_\mu = T/3$, $\Sigma F = 2T/3$; esimerkki $T/G$ 1,102 against 1,104; kuvaaja points; nosturi four cases.
- sim.js implements $a = \pm F/m$ with no friction, and the fitted slope equals the model. No setting ends a run before 0,5 s. Exp-3 pulling left reverses at 0,75 s, and its final $v_x = -0{,}5\,\text{m/s}$ matches pred-3's correct option.
- simState carries sumFx, a, v and m. Each experiment locks everything except the varied key.
- Predictions: exactly one correct option each, and every distractor's feedback is right (pred-2's weight ≈ 10 N for 1,0 kg).
- valitse a–d, check-1 and exp-3's question have one correct option. The exit-ticket hissi answer ($T<G$) is right.
- Theory, summary, misconception box, model box and calc box are consistent, and net force always points along $\overline{a}$.
- Within FY4 scope.

## Scores
- 1 Physics and mathematical correctness: **3**. Every number, figure and model is right, but the worked example teaches a wrong significant-figure rule (Major).
- 6 (physics: models and uncertainty): **4**. The sim's model, its assumptions and its controlled variables are sound and labelled as model values. Uncertainty is not discussed, which suits a simulated, noise-free fit.
