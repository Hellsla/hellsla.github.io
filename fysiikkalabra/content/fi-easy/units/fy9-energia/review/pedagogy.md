VERDICT: PASS
CONTENT-HASH: 2c058d99010374be

Pedagogy review of the Selkeä suomi translation (NOTES.md §12). Every student and teacher text is translated:
unit.json, unit.md, inquiry.json (prompts, options, feedback, hints, mistakes, solutions, criteria, model answer),
exit-ticket.json, sovella/tasks.json (texts, parts, rubric criteria and details), sovella/solutions.md and
teacher.md. The language is natural Selkeä suomi: long source sentences are split into short connected ones, terms
are kept and explained in the sentence ("hajaantuu eli leviää", "katetaan eli saadaan kokonaan", "ekstrapolointi",
"lomitse eli niiden välistä", "harhaanjohtava eli se antaa väärän kuvan"), multi-step instructions are numbered
(aineisto: "Toimi näin: 1) … 2) … 3)") and compound questions are split into one question per sentence. The tone
is neither childish nor padded. key_concepts: five central terms (energian säilyminen, teho, kilowattitunti,
hyötysuhde, lämpöarvo), each with a short, correct explanation; rendered after the opening with the fixed lead,
no note fields. teacher.md adds a sensible S2 note (go through the concepts before Ennusta). Option lengths,
feedback per misconception, points (90), the 75-minute plan and the chapter links are unchanged from the source.

## Blocking
None.

## Polish
1. `inquiry.json` lt-6 prompt adds "Nimellisteho on suurin teho, jolla voimala toimii." This explains the term
   (§12.3) but also rules out the distractor "yli 44 GWh, koska kovalla tuulella teho kasvaa", which the source
   leaves for the student to judge; the diagnostic becomes a little easier than the Finnish one (§12.1). Fix:
   explain without the ceiling, e.g. "Nimellisteho on voimalan valmistajan ilmoittama teho." or leave the
   definition to the feedback, where it already is.
2. `unit.json` key_concepts "hyötysuhde": the formula uses $E_\text{a}$ and $E_\text{o}$ without naming them.
   Fix (17 words): "Kertoo, kuinka suuri osa otetusta energiasta $E_\text{o}$ tulee hyödyksi eli on annettua
   hyötyenergiaa $E_\text{a}$: $\eta = \frac{E_\text{a}}{E_\text{o}}$." Keep the chain sentence if it fits in 25 words.
3. `inquiry.json` lataus prompt: "Sähköpyörän akkuun mahtuu $0{,}60\,\text{kWh}$:n energia" is unidiomatic; write
   "Sähköpyörän akkuun mahtuu $0{,}60\,\text{kWh}$ energiaa." (as in tarkistus-2 "akkuun mahtuu 15 Wh energiaa").
4. `sovella/solutions.md` fy9-energia-s3 d): "Siksi lämmittimiä tarvitaan vain loppuun." is unclear for an S2
   reader. Fix: "Siksi lämmittimien täytyy tuottaa vain se lämpö, joka vielä puuttuu."

## Shared issues
None.
