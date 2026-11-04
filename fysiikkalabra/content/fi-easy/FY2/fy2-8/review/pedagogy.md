VERDICT: PASS
CONTENT-HASH: 0820bc39ae57687e

## Blocking
(none; the item below is resolved, see Follow-up)

## Earlier blocking (resolved)
- inquiry.json ennuste-1 (feedback of the correct option), simulaatio `model`, koe-1 feedback: the new Ydinajatus now explains *säteilytasapainomalli* and *efektiivinen säteilylämpötila* well, but Ydinajatus is in the Selitä stage. The student meets both terms earlier, in Ennusta/Tutki: in the simulation's model note, in the ennuste-1 feedback (changed in this commit) and in the koe-1 feedback. So NOTES §12 rule 3 ("the first time") is still not met. The earlier report's assumption that Ydinajatus comes first was wrong. Fix the ennuste-1 feedback sentence: "Maan yksinkertainen säteilytasapainomalli olettaa, että Maa lähettää avaruuteen yhtä paljon energiaa kuin se saa Auringolta. Mallin antama lämpötila on efektiivinen säteilylämpötila, noin $-18\,{}^\circ\text{C}$." Also fix the simulation model note's parenthesis: "(yksinkertaisen säteilytasapainomallin efektiivinen säteilylämpötila eli lämpötila, jonka malli antaa, kun Maa lähettää avaruuteen yhtä paljon energiaa kuin se saa Auringolta; ei tarkka ennuste)". After these, koe-1 and the later mentions may use the terms as they are.

## Polish
- The Europe-at-night caption does not say what it teaches (energy use leads to emissions). Add one sentence.
- The same terminology note applies to the fi and en versions, as polish there.

## Checked
Follow-up delta (2c31ff041, NOTES §12): the Ydinajatus sentence now explains both terms in the sentence, in plain short clauses and in bold, and the physics is unchanged. The ennuste-1 feedback and the tarkistus-3 criterion use the hedged wording in short sentences ("Maanpinnan keskilämpötila on kuitenkin…"). tarkistus-3 comes after Ydinajatus, so its use of the term is fine. Activity order checked from inquiry.json: ennuste-1 → simulaatio → koe-1 → teoria-osa. Earlier: the −18 °C hedge is consistent across the page, and the map caption is clear.

## Follow-up (uncommitted edit, hash 0820bc39ae57687e, NOTES §12)
- The Blocking item above is resolved: both fix sentences were applied word for word. ennuste-1 feedback (inquiry.json:63) is now the first place a student meets the two terms (activity order hook → kertaus → ennuste-1 → … → simulaatio → koe-1 → teoria-osa; grep: no earlier mention). Each term is explained inside the sentence where it first appears (§12 rule 3), and the glossary terms stay (rule 2). koe-1 (:154) and the later mentions can now use them as they are.
- Natural Finnish (rule 5): short, connected sentences, no childish tone.
- Polish: "Mallin antama lämpötila" uses an agent participle; "Lämpötila, jonka malli antaa, on efektiivinen säteilylämpötila" is easier for S2 readers. The simulaatio parenthesis is long, with a semicolon inside, but it does not break understanding. Split it into sentences as visual.md suggests.
- Blocking: none.
