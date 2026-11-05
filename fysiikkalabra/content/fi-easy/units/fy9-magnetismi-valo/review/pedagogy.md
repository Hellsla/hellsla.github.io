VERDICT: PASS
CONTENT-HASH: b053cd2d9ea1dacc

Pedagogy review of the Selkeä suomi (S2) translation of fy9-magnetismi-valo against NOTES.md §12 and the reviewed Finnish source.

Checked: §12.1 is met. The physics, steps, hints, feedback per misconception, rubrics (95 points), task order, the 75-minute plan and the chapter links are all the source's, and no step is dropped. §12.2 is met: the terms stay (homogeeninen, keskeisvoima, ferromagneettinen, polarisoitunut, linearisointi, sopusoinnussa, ääriarvot, häviöteho) and each is explained the first time it is used, usually inside the sentence with "eli". §12.5 and §12.6: long Finnish sentences with "joten" and "ja" are split into short ones that still connect (Siksi, Silloin, kuitenkin). Multi-step prompts are split into one question per sentence: s2 b, s2 d, s4 a–c, s3 d and the inquiry tasks. The text does not sound childish or padded. All Vastaus lines now use full sentences ("Vastauksessa on kaksi merkitsevää numeroa, kuten …"). §12.7 and §12.8: there are 5 `key_concepts` (magneettikenttä, magneettivuo, induktio, muuntaja, taitekerroin), all central to the unit. Each explanation has at most 2 sentences and at most 25 words. They render after the opening with the fixed lead and the "Vapaaehtoinen" tag, and the page has no note fields. teacher.md is translated and adds the usual "Suomi toisena kielenä" item, as in the other fi-easy FY9 units. Exit ticket, hints, mistakes, criteria and the model answers are all in plain Finnish.

## Blocking
None.

## Polish
1. unit.md, Ydinajatus: "…kohdistaa voiman vain liikkuvaan varaukseen ja virtajohtimeen. Kohdistaa tarkoittaa, että voima vaikuttaa niihin." This sentence explains the word from the outside and is clumsy. §12.3 asks for the explanation inside the sentence. Fix: "…kohdistaa voiman eli vaikuttaa voimalla vain liikkuvaan varaukseen ja virtajohtimeen."
2. Figure words that S2 readers may not know: "sm-aalto" in the kartta figure (figures.json) is an unexplained abbreviation. Use "valo = aalto" or "sähkömagn. aalto". "loivenee" in the s3-B figure is explained only in the aria-label. Use "laskee yhä hitaammin" or "pienenee hitaammin", which matches the model answer's wording.
3. sovella/solutions.md: two sentences start with "Tai", which reads like a fragment. In s4 Yleisiä virheitä b: "Tai unohdetaan, että heijastus kääntää aallon." In s5 b Mallivastaus: "Tai se on niin himmeä, ettei sitä huomattu." Join each to the sentence before it ("…ulkopuolella, tai se on niin himmeä…"), or write "Toinen virhe on unohtaa, että…".
4. unit.json `description` is a list of about 20 nouns in one long sentence, the same as the source. It is acceptable as a catalogue line, but for S2 readers it could be split into two sentences: magnetism and induction first, then light.
5. key_concepts: "magneettivuo" should keep the perpendicular condition (science finding 1). "taitekerroin" could say "kuinka monta kertaa hitaammin".
