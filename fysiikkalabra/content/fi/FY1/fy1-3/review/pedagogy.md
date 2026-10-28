VERDICT: FAIL
CONTENT-HASH: b32be6c0168d0282

## Blocking
- inquiry.json check-2 (id "check-2", answer 2.1, tolerance 0.05) and its solution — the solution's own answer is "$2\,\%$, yksi merkitsevä numero kuten virhearviossa $0{,}05\,\text{s}$ (laskimen arvo 2,08 %)", but the answer check accepts only 2,05–2,15, so a student who rounds as the solution and the lesson rule teach ("tulos samaan tarkkuuteen kuin virhe-arvio") types 2 and is marked wrong. Fix: answer 2, tolerance 0.15 (accepts 2,0–2,15), or change the solution to "$2{,}1\,\%$, kaksi numeroa" and drop the one-digit claim. The exit ticket's third item ("$\approx 2\,\%$") shows the same rounding, so pick one rule for both.

## Polish
- lesson.md Kaava — "Keskiarvon epävarmuus on yleensä sitä pienempi, ja sitä pienempi, mitä enemmän mittauksia on" is garbled. Write: "Keskiarvon epävarmuus on yleensä pienempi kuin yksittäisen tuloksen, ja sitä pienempi, mitä enemmän mittauksia on."
- lesson.md — $\Delta x$ means the error ($x - x_\text{oikea}$) in Ydinajatus and the uncertainty (range half) in Kaava, and the text itself says they differ. Use another symbol for one (e.g. $u$ or $\delta x$ for the uncertainty), or a sentence at the Kaava saying the symbol is reused.
- inquiry.json exp-3 (optional) — answer 6.2 with tolerance 0.03 is narrow for a ratio read from three-digit table values; 6,17 to 6,23 is fine, but 6 (the ratio of the settings) is already the mistake. Widen to 0.06 or ask for the ratio to the nearest whole number.
- inquiry.json exp-1 question — the correct option is two lines long and discloses the plateau value; shorten to "Keskiarvon ero pienenee mutta vaihteluvälin puolikas ei" and keep the number in the feedback.
- pred-2 prompt states the 0,30 s systematic error and its option set offers "noin 0,30 s" — students can answer by reading the prompt. Acceptable as a model-comprehension check, but a prompt without the number (only "kello näyttää liikaa") would leave the prediction open.

## Checked
- Hand-checked numbers: example mean 3,1817 s, half-range 0,12 s, ε 3,8 %; karkea virhe feedback (+0,2 s, 0,09 s to 0,62 s); siirto 5,44 g; exp-2 0,30 s.
- Example has seven stages, symbolic first, Järkevyys states the 3,31 s outlier honestly.
- Predictions precede evidence, are revealed by experiments with min 3, and each wrong option repairs its misconception; both experiments can refute the predictions.
- Choice items have exactly one correct option (karkea, virhe, check-1, data, pr-numerot).
- Glossary terms match (karkea virhe, satunnaisvirhe, systemaattinen virhe, toistettavuus); case after number+unit correct.
- Workload one lesson: exp-3, Etsi virhe and the third check are optional.
- Opening question is answered in the reflect stage and conclusion.
- Page captures were not present (review/shots missing), so figure legibility and 390 px sim fit were not judged visually.
- Hash unchanged at the end.
