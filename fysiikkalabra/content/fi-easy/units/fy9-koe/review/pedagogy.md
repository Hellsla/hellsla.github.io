VERDICT: PASS
CONTENT-HASH: fbf82dd8d638f8de

Pedagogy review, round 2, of the Selkeä suomi translation of fy9-koe. Structure, task counts, rubrics (61 points),
the 75-minute plan and the chapter links are the source's. The language follows NOTES.md §12: short sentences, one
action per sentence, difficult words explained in the sentence, no solution step dropped.

## Blocking
None. Round-1 Blocking 1 (correct option often the longest) is fixed. The correct options of activities 1, 3, 5,
21, 30 and 32 were shortened ("Kevyempi henkilöauto kiihtyy enemmän.", "Jännite syntyy vain, kun … magneettivuo
muuttuu." with *indusoituu eli syntyy* moved to the feedback). Now the correct option is strictly the longest in 4
of 19 choice items, by at most 5 characters (source: 3 of 19 strictly, plus one tie), and in two more items it
ties with a distractor. No item gives the answer away by length.

## Polish
1. Round-1 Polish 2–4 are done: *merkitsevä numero* is now a fifth key concept (5, within 3–5) and *sovite* is
   explained in the kulmakerroin entry ("sovitteelta eli sovitetulta suoralta"); the s4 criterion is a full sentence
   ("Esimerkiksi mitataan viisi eri vesimäärää …"); *Ylioppilastutkintolautakunta* is glossed ("eli kokeen
   järjestäjän").
2. inquiry.json `activities[1].choices[0].text` no longer says *why* the answer is incomplete ("ilman yksikköä"
   was cut for length). The prompt shows `v = 14` without a unit and the feedback says "Ilman yksikköä lukija ei
   tiedä", so the item still teaches the point; no change needed.
3. `activities[5]` "kahdesta suoran pisteestä kaukana toisistaan" is a little compressed for S2 but understandable
   and matches the key concept.
