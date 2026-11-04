VERDICT: FAIL
CONTENT-HASH: b32f7a442b2e29c4

Pedagogy review of the Selkeä suomi translation of fy9-koe. The structure, task counts, rubrics (61 points), the
75-minute plan and the chapter links are the source's; teacher.md is unchanged except for a useful S2 note in
"Eriyttäminen". The language follows NOTES.md §12 well: short sentences, one action per sentence in the
instructions (kertaustesti, Sovella tasks), difficult words explained in the sentence ("johto eli päättely",
"vakioina eli samoina", "luovuttaa eli antaa", "hidastuvuus on kiihtyvyyden itseisarvo"), and no step of any
solution is dropped. Four key_concepts, each 1–2 short sentences.

## Blocking
1. **inquiry.json: the correct option has become the longest option far more often (developer-brief: "the
   correct option is not the longest").** In the source the correct option is the longest in 2 of 19 choice items;
   in fi-easy in 8 of 19 (activities 1, 3, 4, 5, 21, 30, 32, 35). A test-wise student now gains a lot by
   picking the longest answer, and the Ennusta items are a diagnostic. Worst cases (characters, correct vs. longest
   distractor): 32 "Ultraviolettifotonin energia on suurempi kuin sinkin irrotustyö. Punaisen fotonin energia ei
   ole." 97 vs 87 (shortest 70, beyond ±30 %); 1 "Vastaus on puutteellinen: …" 94 vs 85; 21 "Ne ovat yhtä suuret ja
   vastakkaiset. Henkilöauto kiihtyy enemmän, koska sen massa on pienempi." 94 vs 82; 35 92 vs 82; 5 92 vs 81;
   3 92 vs 86; 30 89 vs 84. Fix by trimming the correct options (e.g. 32 "UV-fotonilla on energiaa enemmän kuin
   sinkin irrotustyö, punaisella fotonilla vähemmän."; 21 "Yhtä suuret ja vastakkaiset. Kevyempi henkilöauto
   kiihtyy enemmän."; 5 "Sovitetun suoran kulmakertoimesta, kahdesta kaukaisesta suoran pisteestä."; 30 "Jännite
   syntyy vain, kun käämin läpi kulkeva magneettivuo muuttuu." with "indusoituu eli syntyy" moved to the feedback)
   or by giving distractors the same "Vastaus on …"/"Kiihtyvyys osoittaa …" length, until no correct option is
   clearly the longest.

## Polish
2. key_concepts: *sovite* and *merkitsevä numero* are central to this lesson (Ennusta 3–5, the Tutki rubric, every
   solution's Vastaus line) but are not among the concepts, while "kulmakerroin" uses *sovite* unexplained. Consider
   replacing "suure" or adding a fifth: "merkitsevä numero — numero, joka kertoo mittauksen tarkkuuden; lopputulokseen
   yhtä monta kuin epätarkimmassa lähtöarvossa."
3. sovella/tasks.json `tasks[3].parts[0].criteria[0].text`: the second sentence is a fragment ("Esimerkiksi viisi
   eri vesimäärää …"). Write "Esimerkiksi mitataan viisi eri vesimäärää …".
4. unit.md "Sähköinen koe": *Ylioppilastutkintolautakunta* is a long unexplained word for S2; add "eli kokeen
   järjestäjä".
