VERDICT: PASS
CONTENT-HASH: b7748c0fe5fbff15

## Blocking

## Polish
- lesson.md "Todellinen kantaverkko on kolmivaiheinen" (and Tiivistelmä last bullet) — the section is dense for selkeä suomi and goes beyond the slot's goals; "pääjännite", "pätöteho", "tehokerroin", "vaihejohdin", "nollajohdin", "kuorma", "resistiivinen", "tasasuuntaa" are not explained at first use (NOTES.md §12) — explain each in half a sentence or move the section into a closed extra box.
- lesson.md "Yleinen virhekäsitys" — "Siirtojännite on johtimien ja maan tai johtimien keskinäinen jännite" is too abstract for this reader; say: "$U$ on koko siirtojohdon jännite, mutta johdon resistanssin yli on vain pieni osa siitä, $R I$."
- inquiry.json "ennuste-dc" — the DC-versus-AC prediction is answered by theory only, with no simulation or table to refute it. Acceptable for one lesson, but a line in the feedback ("Jännitepulssi näkyy vain kytkentähetkellä") could be turned into a demonstration later.
- inquiry.json "simulaatio" `model` — the Finnish is correct but "Todellinen kantaverkko on kolmivaiheinen, mutta häviön riippuvuus virrasta on sama" repeats the lesson. Shorten it.
- inquiry.json "tarkistus-3" is optional, so the only required explanation is the conclusion. That fits the workload, but the exit ticket asks no question about the DC idea. Consider one.

## Checked
- Learning path: prior (induction, AC) -> hook -> two predictions -> sim -> theory -> staged example -> error-spotting item -> transfer task -> checks; the opening question is answered in the conclusion's model answer only after the student acts.
- Predictions can be refuted: koe-1 locks P and l, varies U, and its table shows I, P_h and share; each wrong option has its own repairing feedback (the P = U^2/R error is addressed twice).
- Workload is one lesson; optional items are marked.
- Example is staged in seven stages with a check on power conservation.
- Captures lab-1280 and theory-1280: the sim sits beside the experiment, text sits behind the Käyttöohje, Mallin oletukset and Laskennan selitys boxes, figures stand beside their paragraphs, the formula table is legible.
- Hero, transformer, grid and loss-graph figures have descriptions that carry the same data without the answer.
- Finnish: case after number+unit is correct, terms match the glossary, and the model-value wording is consistent.
