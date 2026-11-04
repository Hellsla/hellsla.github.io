VERDICT: PASS
CONTENT-HASH: 1471eeec4778a473

## Blocking
(none)

## Polish
- inquiry.json ennuste-2 prompt — "Sen rinnalle kytketään toinen samanlainen uusi paristo" can be read as "the resistor's parallel", since the sentence before names the kuormitusvastus — "Pariston rinnalle kytketään toinen samanlainen uusi paristo".
- inquiry.json ennuste-2 choices — the correct option is the only one that names "sisäiset resistanssit", a term the student meets first in the sim's Käyttöohje, so vocabulary singles it out — word all four options without the term, or give each a reason in the same register.
- inquiry.json pohdi (optional) — the opening question (why the headlights dim) is answered explicitly only in the theory paragraph "Auton akku käynnistettäessä" and in the optional reflect; siirto computes the voltage but never asks "miksi valot himmenevät" — add the question to siirto's prompt, or make one sentence of johtopaatos' model answer return to the car.
- lesson.md Esimerkki — the example gives Rs = 0,36 Ω for a "new AA" while the Ydinajatus and the sim use 0,20 Ω for a new AA — say "AA-paristo" without "uuden", or add that individual cells differ.

## Checked
- Path: hook, retrieval, two predictions, sim, two experiments (third optional), conclusion, theory, example (7 single-step stages), error item, transfer, exercises, checks, exit ticket: one hour's work, slot goals only.
- Ennuste-1 and ennuste-2 are refuted or supported by koe-1 and koe-2 tables; numbers in feedback (1,333 / 1,455 / 2,286 V; 0,20 Ω) match the model and the table.
- Wrong options carry the misconception (fixed marking voltage, parallel doubles voltage) and their feedback repairs it.
- Figures (model, potential, ui-graph, connections) read at 390 px; the model circuit and the connections diagram carry labels in LaTeX; colour is never the only carrier.
- tarkistus-2 figure is needed to answer; its description gives the data without Rs; the theory ui-graph uses different numbers.
- Tarkistus-1 distractors (varaus loppunut, mittari virhe, vain E pienempi) are real misconceptions; tarkistus-3 criteria are observable.
- Phone: sim, controls and table fit at 390 px; at 1280 px the sim sits beside the experiments.
- Finnish and glossary terms (lähdejännite, napajännite, sisäinen resistanssi, oikosulku) consistent; case endings after number+unit correct.
- Exit ticket tests the core idea (napajännite, oikosulkuvirta and why dangerous).
