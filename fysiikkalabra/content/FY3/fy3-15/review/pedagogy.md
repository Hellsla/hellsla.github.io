VERDICT: FAIL
CONTENT-HASH: fa37d70a3cebe951

## Blocking
- inquiry.json `ketju` (tutki) and `hook`, `pred-1` — the question "Kuinka suuri on sähköteho?" has the answer 200 MW, which the hook ("sähköverkkoon lähtee vain 200 MW") and pred-1 ("sähköteho 200 MW") already state; the student can type it without computing, and the pred-1 question (which stage loses most) is never answered by anything the student does. Ask instead for the loss in the höyrykierto stage (248 MW) or P2 (212 MW), and say in the text that the table is where the prediction is tested.
- inquiry.json `ketju`, `kaukolampo`, `tyypit` (390 px captures tutki-1/-2) — the markdown tables are clipped at the right edge: the Hyötysuhde column (the data the tasks use) and half of "polttoaine → höyry" are not visible, with no scroll cue. The question "yli kaksi kertaa" cannot be answered from what shows. Make the tables fit at 360 px (short headings, drop the Tapahtuma column, or smaller type) or wrap them in a visible scroll container.
- solutions.md (all 12 solutions) — calculations and symbols are plain Unicode (`η = 0,920 · 0,980 = 0,9016`, `P₃`), not LaTeX; the teacher's rule is LaTeX for every calculation in solutions. Rewrite Kaava and Sijoitus lines in `$...$` as in the example and the `siirto` solution.

## Polish
- lesson.md "Kuvassa pylväs lyhenee vaiheesta toiseen kertoimella $\eta_k$" — $\eta_k$ is undefined and the figure shows η1, η2, η3: "kertoimella η₁, η₂ ja η₃".
- inquiry `kaukolampo` asks the student to compute hukkalämpö and η_kok for both states "ennen kuin vastaat", but nothing checks it; either add a numeric item (hukkalämpö 48 MW at full CHP) or drop the sentence. The pred-2 refutation then rests on a read-off.
- Figure 3 (waterfall): only the P2 loss bar is labelled "häviö"; label the P1 and P3 ones too, or add 248 MW and 12 MW, so the biggest loss is read from the figure.
- Example stage "Järkevyys" packs three claims (306 MW, 54 MW and 12 MW, where to improve) into one paragraph; split into two sentences-groups or move the improvement remark to the misconception.
- Pred-1 option "Höyrykierrossa" uses a term first met in the theory; "turbiinissa ja lauhduttimessa" suffices.

## Checked
- Path: prerequisite (fy3-11 Q2 = Q1 − W) is retrieved, then built into the chain; slot goals (energiaketjut, hyötysuhteet, lauhde, yhteistuotanto) covered, no excess.
- No simulation is justified (sim-spec); table/graph investigation fits, one hour of work.
- Pred-2 is refutable by the kaukolämpö table (160 to 120 MW) and each wrong option repairs its misconception; speakers not predictable.
- Figures 1-4 (captures, 390 and 1280 px): Sankey to scale and consistent (500 = 200+40+248+12), stacked chart, waterfall and condenser legible, colour not alone, LaTeX labels.
- Example: five staged steps, symbolic first, arithmetic correct (0,38038; 228 MW; 372 MW), not repeated in exercises.
- Exercises 5/4/3, original; L3 asks for reasoning; exit ticket tests product rule, η_kok and the heat-engine reason.
- No lesson-id references in student text (chapter names used); Finnish reads correctly.
- Layout at 1280 px: figure beside paragraph, two-column hook; Ennusta box and Tehtävät last are fine at 390 px.
- Not opened: 768 px (no capture).
