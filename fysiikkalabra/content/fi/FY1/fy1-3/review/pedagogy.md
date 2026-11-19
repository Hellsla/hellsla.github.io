VERDICT: PASS
CONTENT-HASH: 2e675a488ebf4890

## Blocking
(none)

## Polish
- inquiry.json:320-329 (pred-1) — "satunnaisvirhe" is used in the prompt before Teoria and without a gloss; pred-2 glosses "systemaattinen virhe" through its situation ("näyttää joka kerta 0,30 s liikaa"), pred-1 does not. Fix: "jokaisessa mittauksessa on satunnaisvirhe eli kerta kerralta vaihteleva heitto, välillä ylös ja välillä alas". The same holds for "toistettavuus" in the feedback of the `data` item.
- inquiry.json:739-818 — four checks (check-1, check-c2, check-2, check-3) all non-optional, plus the exit ticket; the core-path rule is 1–2 checks and the slot's goals do not ask for resolution. Mark check-c2 `optional: true` or fold it into check-1; the lesson is already heavy (two predictions, three experiments, data, conclusion, six formulas, relative uncertainty, rounding, correction formula).
- lesson.md:147 — the LIGO photo follows Toistettavuus ja oikeellisuus but explains nothing in it and the text never refers to it ("no figure after a block it does not explain"). Tie it to the resolution/uncertainty paragraph (kaava section) or drop it.
- inquiry.json:435 (exp-1 correct option) — it is by far the longest option and carries the hedge in parentheses, so it can be picked by length. Shorten: "Keskiarvon ero oikeaan aikaan pienenee, mutta vaihteluvälin puolikas pysyy noin $0{,}25\,\text{s}$:ssa." Move the n = 1 remark into the feedback. Same pattern in `karkea` (inquiry.json:657).
- inquiry.json:558-562 (exp-3) — the answer 6 (the expected proportionality) is filed as a "mistake" with feedback that treats it as nearly wrong. Reword to credit the idea ("suhde on lähes sama kuin satunnaisvirheiden suhde; kysyttiin taulukon lukuja") so the student does not unlearn the proportionality.

## Checked
- Learning path: the opening question (ten different times, same clock) is answered by the reflect item and the exit ticket; the "is the clock wrong for everyone" half by the thermometer data and exp-2.
- Predictions: both can be refuted by the sim; every wrong option's feedback repairs a named misconception, the right ones cite experiment values; wording still makes sense when reopened.
- Experiments set initial state, lock sat/sys, vary one thing, record measured quantities, `min` 3; model values are labelled as such, including in the conclusion's model answer.
- Worked example: seven stages, numbers verified (sum 19,09 s, mean 3,18 s, Δt 0,12 s, ε 3,8 %), rounding rule applied and explained, reasonableness check honest about 3,31 s outside the interval.
- `karkea` task: figures check (mean shift about 0,2 s, Δt 0,09 s to 0,62 s); feedback matches the theory on tarkistus and kirjattu poisto.
- `siirto` (5,44 g) matches the sums and mistake values 5,6, 27,2, 4,8, 28; hints go from error type to procedure to numbers.
- Exit ticket tests the core idea (systematic vs random, why averaging helps one only, relative uncertainty); solutions complete and symbolic first.
- Finnish: glossary terms match glossary.json; no case or grammar errors found; paragraphs stay under about 110 words by count.
- Phone usability not re-opened beyond the packet's passed layout checks; no capture was needed for the judgments above.
