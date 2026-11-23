VERDICT: FAIL
CONTENT-HASH: 3c6710f77b96877f

## Blocking
1. Box 2 (absoluuttinen nollapiste, "Miksi suoran jatkaminen nollapaineeseen on vain kaasumallin ennuste?") is in the wrong place. It splits a sentence: the text before it ends "Kelvinlämpötila on", and the formula `T = θ + 273,15 K` comes after the box. On a phone the reader sees a broken sentence, then a box, then a formula that completes it. Worse, the paragraph the student has just read says nothing about extending a line to zero or about condensing. The tested idea ("Absoluuttinen nollapiste saadaan ... Se on mallin ennuste: todellinen kaasu tiivistyy") comes only after the box, so the answer cannot be worked out from the text just read. Move the box to after that paragraph, following the formula and the sentence on the model's prediction. Better still, reword the question to ask for the cause, for example "Mitä todelliselle kaasulle tapahtuu ennen nollapistettä?", so it is not answered by reading the next line.

## Polish
- Box 3 (hyötysuhde < 100 %) sits before the sentence "Osa lämmöstä on aina luovutettava kylmempään..." that states its answer. The preceding paragraph does define Q_2 and W, so it is answerable, but the box then repeats the next sentence almost word for word. Put it after that sentence and ask something not yet said, for example what would have to hold for η = 100 % (Q_2 = 0).
- Box 3's answer says "työ W on pienempi kuin Q_1" without naming the energy balance W = Q_1 − Q_2. The `johda` box right after it derives that. Either link the two or leave the box out.
- Box 1 (mittarin lukema, 230 kPa) is well placed right after the worked tyre example. It is answerable from the paragraph just read and it targets the main misconception. Its answer repeats the paragraph's numbers, which is fine as a check.
- Three boxes in one unit is light. A box after the Boyle/hydrostatic text (for example, why the pressure at depth does not depend on the vessel's shape) would be natural, but this is optional.

## Checked
- Pysahdy boxes 1 to 3: placement, whether the answer is in the paragraph just read, and how they read on a phone (short question, short answer, no scrolling).
- unit.md text, the Ydinajatus, "Yleisiä virheitä" and "Kertaa" sections, the `johda` derivation (it follows the 1st law and signs correctly), and the deterministic check (practice.py check OK).
- Task set (9 tasks, the Sovella tasks.json): skimmed titles, the criteria of s1 (paineilmanostin) and the mix of contexts (korjaamo, biokaasu, laiva, ydinvoimala, kuumailmapallo). The set is varied, uses authentic situations and has multi-part tasks with rubrics tied to observable steps. Nothing new blocks since the passed version; I judged only the change in depth.
- The full task set was not re-read in detail, because the diff touches only unit.md.
