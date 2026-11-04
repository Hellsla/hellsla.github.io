VERDICT: PASS
CONTENT-HASH: 210723c3675594ef

Round 2 (delta review of the developer's Round 1 fixes; round 1 hash 23902d39dc18f729).

## Blocking

None. All three round 1 Blocking findings are fixed:
1. **Option lengths.** I measured all 19 choice items. Every option is within ±30 % of the correct one; the largest gap is +25 % (testi-15). The correct option is the longest, or tied for longest, in 4 of 19 items (pred-1, pred-4, testi-11, testi-17), which is close to chance (25 %). The length cue is gone.
2. **Seven steps against the model-answer headings.** unit.md now maps the headings to the steps right after the steps figure ("**Annettu** ja **Kysytty** ovat vaihe 1 … **Järkevyys** vaihe 7"). The Esimerkki maps its own stage names. The teacher plan tells the teacher to go through this mapping.
3. **Workload.** teacher.md: the 12 choice items are done in class in 20 min (about 1 min each), and the 12 numeric items are done at home. The minutes add up to 75 (7+10+13+12+20+13). Modules are assigned rather than picked by the students.

## Polish

1. unit.md, Esimerkki: the stages are still named *Tunnetut ja kysytty*, *Yksikkömuunnokset* and *Tulos*, while the steps figure says *Annettu ja kysytty*, *Muunnokset* and *Vastaus*. The page now has three sets of names, and the example needs its own translation sentence. Fix: rename the Esimerkki stages to the figure's names and delete the line "Esimerkin vaiheet ovat samat kuin…".
2. inquiry.json pred-1: the correct option (83 characters) is still 12 % longer than the next-longest (74). This is within the limit, but pred-1 is the first item the students see. Shorten it to about "Puutteellinen: ilman yksikköä ei tiedä, onko se m/s vai km/h."
3. teacher.md, Kotona: 12 numeric items at 3–4 min each is 36–48 min of homework in a single evening. Give a lighter option, for example "vähintään yksi laskutehtävä jokaisesta moduulista".
4. inquiry.json vastaukset, `practice`: the complete-solution steps are sent to *Aineen lämpeneminen ja jäähtyminen*. Point to this unit's Teoriatiivistelmä instead, or drop that half of the sentence.

## Checked

- Round 1 Polish items: the Tutki rubric now says "oikea vastaus", gives no point for a substitution without units, and names its items as the steps. Answer B is now a list. check-2 has a precision mistake (0,4). The s1 a) Järkevyys check is now a kettle comparison. The modules are no longer self-picked.
- The feedback on the rebalanced options still repairs the misconception and names the chapter. The task counts against the plan table are the same as in round 1 (6/1/24/3/4, 61 p).
- I looked at the captures of Tutki, the mapping paragraph and the Esimerkki at 390 and 1280. The hash is the same at the start and the end.
