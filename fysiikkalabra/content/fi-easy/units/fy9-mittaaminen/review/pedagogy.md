VERDICT: PASS
CONTENT-HASH: 167a7e1ffcb6d0db

Pedagogy review of the fi-easy (Selkeä suomi) translation of fy9-mittaaminen (NOTES.md §12).

## Blocking
None.

## Polish
1. [Minor] "kääntäen verrannollinen" is never explained (inquiry.json activities/5 choice 3 feedback, activities/10 choice 3 feedback, sovella/tasks.json s6 a, teacher.md). §12.3 asks for the explanation inside the sentence the first time it appears. Fix (first time, activities/5 choice 3): "…kun $ on kääntäen verrannollinen $:ään eli $ pienenee samassa suhteessa kuin $ kasvaa, kuten Boylen laissa."
2. [Minor] Also "suoraan verrannollinen" (inquiry.json prior/2, the first place it appears) could get a short explanation: "eli kun tilavuus kaksinkertaistuu, myös massa kaksinkertaistuu".
3. [Minor] unit.md "Yleisiä virheitä" items 1 and 4 and solutions.md "Yleisiä virheitä" lists begin a second sentence with "Tai …", which reads as a fragment. Fix: join them with a comma ("…, tai suora pakotetaan…"), or write two whole sentences.
4. [Minor] sovella/tasks.json s4 text: "Vaa'an näyttö näyttää kokonaiset grammat" repeats the verb. Fix: "Vaaka näyttää massan kokonaisina grammoina."

## Checked
- Same physics: there are 316 JSON strings plus unit.md, teacher.md and solutions.md, and every number, formula, answer, tolerance, correct flag, point and rubric criterion is the source's. check_i18n.py gives 0 errors. No solution step was dropped; the steps are split into short sentences.
- The language is natural Selkeä suomi. Sentences are short and connected, and they use common words. Physics terms stay and are often explained: "lomaan eli niiden väliin", "kumoavat toisensa eli poistavat toistensa vaikutuksen", "lineaarisesti eli suoran mukaan", "päällekkäin eli osittain samalle alueelle", "jäykkä eli sen tilavuus ei muutu". The tone is not childish and has no padding.
- The instructions are clear: the opening question, the Tutki steps ("Sovita ensin…, Lue sitten…, Mieti lopuksi…"), the multi-part task texts and the feedback each say what to do and in which order.
- key_concepts: 5 central concepts (mittausepävarmuus, systemaattinen virhe, suoran sovitus, kulmakerroin, ekstrapolointi), each explained in 1–2 plain sentences of 25 words or fewer, with LaTeX for the symbols. The component renders after the opening, with the fixed lead and no note fields.
- teacher.md is fully translated, and it adds a short S2 note (go through the key concepts before Tutki). The plan, the timing (75 min) and the task counts are the source's.
- Rubrics: the criteria are observable and the points are the source's. The self-assessment UI texts are in Finnish.
