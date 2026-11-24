VERDICT: PASS
CONTENT-HASH: af372740ea1dad74
## Blocking
(none)

## Polish
- inquiry.json (activities `exp-1`, `pred-1`) and lesson.md "Esimerkki" — the same atom/proton calculation (1,1·10^-10 m : 1,7·10^-15 m, five steps) appears in pred-1, exp-1, the ladder figure, the worked example and exp-1's solution. The example therefore adds nothing the experiment has not already shown. Fix: base the worked example on another pair, for example Sun and neutron star, or Earth and Sun. Check-2 uses that pair, so use Moon and Earth or a virus and a hair instead.
- inquiry.json `hook` vs `reflect` — the hook asks about the range from "pienimmän" to "suurimman" size and names the proton. The reflect model answer then gives 42 orders (the proton) and 62 (Planck). Fix: name the smallest object in the hook, or say in reflect which of the two the hook meant.
- inquiry.json `simulaatio.text` — "kuinka pitkä kymmenen potenssi metrejä on" is hard to read for an S2 student. Fix: "Palkki näyttää, kuinka pitkä $10^{k}\,\text{m}$ on tällä mittakaavalla." The `model` box is one 250-word block of jargon (kosmologinen malli, sirontakoe, tapahtumahorisontti). It is closed and optional, but break it into a short list or cut it to what the table needs.
- lesson.md "Maailmankaikkeuden rakenteet" / "Perusvuorovaikutukset" — fi-easy words not explained at first use: "fuusioreaktioissa", "superjoukko", "antineutriino", "paralaksi" (in `menetelmat`). Fix: add a short gloss in brackets or cut the word.
- inquiry.json `exp-2.question` — the only task of the experiment is a choice whose correct option is the longest and most detailed. Prediction 2 (eight orders) is tested only through the table. Fix: add a numeric part, "Montako suuruusluokkaa Neptunuksen radasta Linnunrataan?", or shorten the correct option so its length does not give it away.

## Checked
- The packet hash equals `reviews.py hash fy1-1 --lang fi-easy` at the start; I re-ran it at the end.
- The opening question is answered by the theory sections. Predictions 1 and 2 are committed before the evidence. Each wrong option's feedback repairs a named misconception (size shown in drawings, ratio against orders of magnitude).
- Experiments 1 and 2 can refute their predictions. The simulation's table gives n = -10 and n = -15, and 13 and 21. The simulation shows the objects at true scale, so a student who guessed "one order" sees the contradiction.
- The slot's two goals are covered: experiment, model and measurement (`menetelmat`) for the scientific method, and the scale, matter and interaction sections for scale. The core path is compact: retrieval, `virhe`, `siirto`, exp-3, `menetelmat` and check-3 are optional, so the workload is about one lesson.
- Figures 1 to 9 (contact sheet 1): recognisable, uncluttered, labels legible at 390 px, "ei mittakaavassa" marked where it applies. The atom-stadium figure marks the pea as drawn too large. Descriptions give the same data as the figures without extra answers.
- The worked example has 7 stages, one step each, symbols first, with a unit check and a reasonableness check. The simulation at 390 px shows picture, controls and key values, and the text sits in closed boxes. The experiment layout shows Alkutila, Vakiona and Muutetaan.
- Tarkista checks: the concept and calculation checks use real misconception distractors (coefficient read as an exponent, exponents added or divided). The explain criteria are observable. The exit ticket tests the strong interaction and why models are tested.
- The transfer and `tunnista` tasks have progressive hints and common-mistake feedback. The exercise set was not judged here, as the packet says.
- Finnish: no case or term errors found. The glossary terms are used consistently, and numbers with units are LaTeX.
