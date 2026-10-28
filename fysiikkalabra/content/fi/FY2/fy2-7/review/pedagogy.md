VERDICT: PASS
CONTENT-HASH: 5b64360e6e9a794d

## Blocking

(none)

## Polish
1. inquiry.json `jannite` text — "Päättele taulukosta, kuinka monta prosenttia ... häviää" but the task is a choice and the percentages (8,0 %, 0,26 %, 0,020 %) appear only in feedback. Add an "Osuus (%)" column or reword to "Vertaa häviötä jännitteiden välillä" (carried from round 2).
2. lesson.md Ydinajatus — "Hyvässä muuntajassa häviö on hyvin pieni" has no number or source; give it ("alle 1 %", with source) or drop the sentence (carried).
3. inquiry.json `ennuste-1` prompt — asks for the share of "verkkoon syötetystä sähköenergiasta", while the 4 % is of consumption (the lesson text says this once, in Siirtohäviö). Write "sähkön kulutuksesta" or "verkon läpi kulkevasta" so prompt, table (83 TWh) and Sankey agree.
4. inquiry.json `siirto` solution — reasonableness line compares 15 % with grid losses ("uskottavaa varastolle, jossa energia muunnetaan kahdesti") without naming the 4 % and 9 %; add them so the check is concrete.
5. lesson.md figure "grid" — "muuntaja" label sits close to the first pylon's wires and "20 kV" floats between station and poles at 390 and 1280 px; move the label above its box and 20 kV above the poles.

## Checked
- sahko table at 390 px: all three columns and the units fit, Osuus (%) readable (round 2 blocking fixed).
- Path: hook, optional retrieval, two predictions before data, three data items, conclusion, theory, staged example, error item, transfer, three checks, exit ticket: one lesson's work; opening question answered; slot goals only (no formulas beyond the slot).
- Ennuste-2 is refutable by the voltage table (8,0 % to 0,020 %; ratio 400 verified); ennuste-1 by the Kaukolämpö/sähkö data; options shuffled; each wrong option's feedback repairs its misconception; nothing disclosed before commitment.
- Figures 1-4 legible at 390 px, after the paragraphs they explain, beside the text at 1280 px; Sankey widths match 4 %/9 %; colour not alone (labels and percentages).
- Worked example: seven stages, symbols before numbers, unit step, significant figures justified, reasonableness check; differs from transfer and checks.
- No paragraph over 120 words; chapter names not ids; "Exit ticket" and "Kaava: Siirtohäviö" naming correct; Finnish and glossary terms correct.
- Data carry source and year, invented cases marked "esimerkkitilanne", model values called model values.
- Exit ticket tests the η calculation, high voltage and loss energy (P·t); exercises not judged (own packet).
- Phone: tables, answer fields and buttons clear in the 390 px captures; 1280 px theory column readable.
