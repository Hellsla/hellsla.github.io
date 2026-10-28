VERDICT: PASS
CONTENT-HASH: 3bcebf10ec3465fe

## Blocking

## Polish
- inquiry.json:pred-1 — "Päättele: kaksi palloa" sits in Tutki after punnitus-vertailu, whose correct-answer feedback already states "samassa paineessa, tilavuudessa ja lämpötilassa kaikissa näissä kaasuissa on yhtä monta moolia"; the item restates the answer, and reflect lists it as a prediction — move it before punnitus (a real prediction, "yhtä monta?") or rename it a conclusion and drop it from reflect.predictions.
- inquiry.json:tutki workload — eleven activities (punnitus, vertailu, päättele, sim, two experiments, taulukko, laske-r) before theory, then example, virhe, siirto, 12 exercises, three checks, exit ticket: more than an hour for a 16-year-old on a phone; cut `taulukko` (exp-1/exp-2 already show p ∝ N and p ∝ T) or `siirto`.
- simulation phone, first frame (fy3-10-sim-390.png) — before the first measurement the bar value "0,00" is drawn outside the canvas at the top left over the gauge; in a running sim at 390 px (checked) all labels are clean, and at ≥10 px (ts(11–13) × 0,54). Skip drawing the bar value when the average is empty, or draw it after KaTeX has loaded.
- inquiry.json:exp-1/exp-2 table headings — the "Mittaukset" header mixes monospace Finnish words with italic KaTeX ($N$, $p/p_\text{ref}$ mitattu), which looks unfinished at 1280 px; use KaTeX for the whole heading ($\text{osumia seiniin (1/s)}$, $p/p_\text{ref}$) in the page's body font.
- solutions.md:fy3-10-L2-01 Järkevyys — "tulos on arvio (tehtävä pyysi ideaalikaasun arvoa, joten vastaus 180 bar pätee)" is confusing; write: "Todellisessa pullossa paine on hieman pienempi, mutta tehtävässä oletetaan ideaalikaasu, joten vastaus on 180 bar."

## Checked
- Learning path: kertaus (Boyle) → prediction (N) → weighing table → simulation → R from data → theory → example; opening balloon question is answered only after the student has acted (reflect, check-3).
- Slot goals covered (pV = nRT, solving for a quantity, gas laws as special cases via combined law); nothing beyond FY3.
- pred-n is refutable: exp-1 locks T and V, varies N, min 2 rows; exp-2 is a challenge the student can only solve from exp-1 data.
- Wrong-option feedback repairs the misconception (collisions, "in the way", no change); no answer disclosed before commitment.
- Simulation at 390 px and 1280 px: gauge, bar, legend, V arrow and readout legible and not overlapping; canvas text ≥10 px on a phone (measured label boxes × canvas scale 0,54); controls and the three closed boxes (Käyttöohje, Mallin oletukset, Laskennan selitys) reachable; visible lead 25 words.
- Figures 1–3 legible at 390 px, LaTeX labels, colour with meaning (helium blue, air grey), speed arrows labelled in the caption.
- Worked example has five single-step stages, symbolic before numeric; numbers re-computed (0,2073 mol, 0,83 g); the example repeats the opening balloon data (acceptable as a bridge).
- Exercises 5/4/3 with right levels, no repeat of the example; mistake values (°C, litres, kPa) match common errors; exit ticket tests the core idea (n independent of gas, p ∝ T).
- Finnish and glossary terms (moolinen kaasuvakio, ainemäärä, moolimassa) correct; table values p·V/(N·T) recomputed correctly.
