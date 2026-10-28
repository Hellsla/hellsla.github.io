VERDICT: FAIL
CONTENT-HASH: 5e17e209235f27bb

## Blocking
1. inquiry.json activity `sahko` (table) — at 390 px the third column is clipped in the capture (fy2-7-stage-tutki-390-1.png: "noi", "4 %" cut at the edge, "9,2" without its %); teacher's rule: tables fit 360 px, and the student cannot read the Osuus column that the question is about — drop "noin" from the cells (say "noin"/rounded in the text above, which already says luvut pyöristetty), shorten headers ("Lähtö (TWh)", "Häviö (TWh)", "Osuus") and write the shares as "4" and "9,2" with "Osuus (%)" in the header.

## Polish
1. inquiry.json `sahko` + lesson.md Siirtohäviö — the 83 TWh is the consumption ("kulutus"), yet the table column says "Verkkoon" (fed in) and the Sankey calls 4 % a share of the outgoing energy; the student is asked to compute shares of the outgoing energy. Say once that 4 % is of the consumption (or use "noin 86 TWh" fed in), so the table, text and Sankey agree.
2. lesson.md figure "grid" — the label "muuntaja" touches the first pylon's wires at 390 and 1280 px; move it left or above the box. The 20 kV label floats between the station and the poles; place it above the poles.
3. inquiry.json `jannite` text — "Päättele ... kuinka monta prosenttia ... häviää" but the question is a choice; the percentages (8 %, 0,26 %, 0,020 %) appear only in feedback. Add a "Osuus" column or reword to "Vertaa häviötä".
4. inquiry.json `siirto` solution — the reasonableness check "samaa suuruusluokkaa kuin kaukolämpöverkon häviö" compares 15 % with 9 %; better: "suurempi kuin verkon häviö, koska energia muunnetaan kahdesti".
5. lesson.md Ydinajatus — "Hyvässä muuntajassa häviö on hyvin pieni" is unsupported by a number; give "alle 1 %" with source or drop.

## Checked
- Round 1 polish items resolved: sähkö row in Tutki, "muuntaja" and "yläallas/alaallas" labels, both terms bold, kertaus repeats η, ennuste-1 feedback repairs.
- Path: hook, retrieval, two predictions before data, three data items, conclusion, theory, example, error item, transfer, 3 checks, exit: one lesson; opening question answered; slot goals only.
- Ennuste-2 refutable by the voltage table (8 % to 0,020 %); options shuffled; no answer disclosed before commitment.
- Figures 1-4 legible at 390 px; Sankey to scale (4 %/9 %); figures sit after their paragraphs; 1280 px beside text fine.
- Worked example: seven stages, symbols before numbers, sig figs justified, differs from transfer items.
- No paragraph over 120 words; chapter names not ids; Finnish and glossary terms correct.
- Exit ticket tests η calculation, high voltage, loss energy.
