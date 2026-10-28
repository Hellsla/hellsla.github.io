VERDICT: PASS
CONTENT-HASH: b6e1d96d15ea188c

## Blocking

## Polish
1. inquiry.json ennuste-1 — the sähköverkko 4 % is never met as evidence: the Tutki stage has kaukolämpö data and the voltage table only, so the prediction is settled by the feedback text and the reflect step has nothing to compare with — add the Sähkövuosi 2024 figures (consumption about 83 TWh, loss about 3 TWh) as a row or a short interpret item.
2. inquiry.json ennuste-1 feedback — "Näin suuri häviö olisi mahdoton kantaa" and "ei ole puolikasta sääntöä" restate rather than repair; say instead what a 25 % loss would mean (a quarter of the power plants' output heated the lines), and that the prompt's "alueverkko" never appears in the lesson (drop it or add it to the figure).
3. lesson.md figure "grid" — the transformer by the power plant is drawn but unlabelled although the text names it; add the label "muuntaja". Figure "storage": the pumped-storage drawing (brown block, thin pipe) is hard to read at 390 px; add "ylä-/ala-allas" labels.
4. lesson.md Ydinajatus — "**sähköenergiana** ... ja lämpöenergiana" bolds only one of the two terms; bold both or drop the bold. "Kuuma vesi on ympäristöä lämpimämpää, siksi kaukolämmön häviö on suurempi" is the only reason given for 9 % vs 4 %; consider "isompi lämpötilaero ympäristöön".
5. inquiry.json kertaus — the retrieval checks only P and E, while the lesson calculation rests on hyötysuhde (a prior); make the optional item (or the first hint of the example) recall η = E_hyöty : E_käytetty. Also jannite text asks to "laske prosentti" but the question is a choice; the calculation is not checked.

## Checked
- Path: hook, retrieval, two predictions, data, conclusion, theory, example, error item, transfer, 3 checks, exit: one lesson's worth; the opening question is answered.
- Slot goals met (electricity and heat transmission, qualitative high voltage); no FY3 content (no I²R, no chain of efficiencies).
- Predictions before evidence; ennuste-2 is refutable by the voltage table; options shuffled, feedback names the misconception.
- Worked example: seven stages, symbols first, 223 / 22,1 MWh rounded and justified; example differs from the transfer items.
- Figures (390 px captures): sankey legible, scale correct (4 % and 9 %); grid and district figures sit right after their paragraphs; 1280 px figure beside text fine.
- Tables fit 390 px; no paragraph over 120 words; Finnish and glossary terms correct; chapter names, no ids.
- Exit ticket tests the core idea (η calculation, why high voltage, loss energy).
