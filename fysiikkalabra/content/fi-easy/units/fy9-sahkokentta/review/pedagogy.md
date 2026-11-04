VERDICT: PASS
CONTENT-HASH: b3d2c2bde898a57e

Pedagogy review of the Selkeä suomi (S2) translation of fy9-sahkokentta against NOTES.md §12.

Same physics and structure as the passed source: the 6 diagnostic questions, Tutki, the 4 multiple-choice and 4 calculation
tasks, the three Tarkista tasks, the exit ticket, six exam-style tasks (95 points, rubrics unchanged) and the 75-minute plan.
Every text is translated, including figure descriptions (figures.json, 32 entries), hints, mistake feedback, worked
solutions, model answers, rubric criteria, Yleisiä virheitä / Hyväksytään myös and teacher.md.

Language: sentences are short and connected, one idea per sentence, natural rather than robotic. Physics terms are kept
and explained at first use inside the sentence (kohdistaa eli vaikuttaa, kaksinkertaistetaan eli tehdään kaksi kertaa
suuremmaksi, homogeeninen eli samanlainen joka kohdassa, mitätön eli niin pieni…, systemaattinen virhe eli…, alaraja eli
pienin mahdollinen arvo, diagnostinen testi eli…). Instructions are explicit and ordered (Tutki text, Sovella intro, task
intro "Piirrä… Kirjoita… Arvioi…"). Chapter links are names, not ids. `key_concepts`: 5 central terms (sähkökenttä,
homogeeninen sähkökenttä, potentiaali, kapasitanssi, läpilyöntilujuus), each 1–2 plain sentences under 25 words, rendered
as *Luvun tärkeät käsitteet* with the fixed lead and no note fields.

## Blocking
None.

## Polish
1. inquiry.json, Tutki (activities[7]) hint 2: "Sano myös, miksi energiaksi potentiaalienergian väheneminen muuttuu."
   *miksi* reads first as "why". Fix: "Sano myös, millaiseksi energiaksi potentiaalienergia muuttuu, kun se pienenee."
2. inquiry.json, Lähtötaso 4 (activities[4]): adding "samana" made the correct option the longest (70 vs 65/66 characters;
   in the source it was the shortest). Fix: "Kaksinkertaistuu, koska varaus ei muutu ja kapasitanssi puolittuu." or
   begin it "Jännite kaksinkertaistuu…" like the other two options and shorten the reason.
3. unit.json `key_concepts`: *potentiaali* and *kapasitanssi* start with a subjectless "Kertoo…". Write "Potentiaali
   kertoo…", "Kapasitanssi kertoo…" so each explanation is a whole sentence (§12.5).
4. sovella/tasks.json `source_note` of s1, s2, s5, s6: "… ja sen luvut ovat keksitty esimerkki" (number disagreement,
   inherited from the source). In S2 write "… on keksitty esimerkki." or "… ovat keksittyjä esimerkkejä."
5. teacher.md, Arviointi: "Osa III:n tyyppinen" / "Osa II:n tyyppisiä" → "kokeen osan III kaltainen" / "osan II kaltaisia".
