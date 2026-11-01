VERDICT: FAIL
CONTENT-HASH: d34eff70d761834f

Science, fact and French-accuracy review of fy14-fr-nombres, 2026-11-01.

## Blocking
1. **A. Broken maths shows wrong sums to the student.** `inquiry.json`, eight feedback strings in `fx-match-numbers` (*quatre-vingt-quatre*, *quatre-vingt-un*), `fx-match-heardB` (A3, A4), `fx-match-heardA` (B2, B3) and `fx-gap-receipt` (4,95 € and 9,90 € lines) have misplaced delimiters such as `$4 \cdot $20 = 80$$`. In the browser (checked with Playwright) they render as "4⋅4⋅20 = 80$$", "80 + 80+1 = 81$$" and "90=4⋅20 + 10$$". Fix each one as a single span: `$4 \cdot 20 = 80$`, `$80 + 1 = 81$`, `$60 + 15 = 75$`, `$4 \cdot 20 + 10 = 90$` (twice), `$60 + 10 = 70$`, `$95 = 4 \cdot 20 + 15$`, `$90 = 4 \cdot 20 + 10$`. The developer's "no raw `$`" check missed these because they appear only after *Check*.
2. **A. "Old English".** `inquiry.json`, `explain` in *Think about it*: "Old English also counted in twenties: *four score and seven* was 87." Old English (before about 1150) did not use *score* for numbers. The word comes from Old Norse and the phrase is Lincoln's (1863). Write "Older English also counted in twenties: *four score and seven* (Lincoln, 1863) was 87". The lower-case "the old English *four score*" in `unit.md` is fine.

## Polish
3. `fx-match-heardA` checks only B1–B4, but table B has five lines. Add an item for line B5 with the answer "84 €". The option is already in the list.
4. `unit.md`, *Sounds* point 2: "In 22–29 the *t* of *vingt* is heard". It is also heard in 21 (*vẽ-te-Ẽ*, as in your own list), so write "21–29".
5. Extension phone numbers: *06 12 34 56 78* and *04 91 21 77 99* may belong to real people. ARCEP reserves ranges for fiction, for example 01 99 00 xx xx and 06 39 98 xx xx. Use one of those or say that real numbers must not be dialled.
6. Check 4 model: *j'ai acheté … Le jus d'orange coûte …*. Write *a coûté*, or keep the present but drop the past tense.

## Checked
I recomputed every number in Python: all twelve number words in the match tasks, all ten heard prices, the receipt (1,80 + 1,20 + 3,70 + 4,95 + 9,90 = 21,55 €), the market total (6,10 €) and the check 4 total (8,65 €). All are right. French rules match fr.wikipedia *Nombres en français* (*et* only in 21–71; *quatre-vingts* with *s* only at the end; septante, nonante and huitante in Vaud, Valais and Fribourg). Also checked: the decimal comma, € after the number, *centime*, phone pairs and 06/07 for mobiles, and that Aix is 35 km south of ITER. The respellings follow the pilot's style throughout: Finnish letters, capitals for stress, õ/ã/ẽ, *y* for French *u*, *J* for /j/, *ö* for *eu* and schwa. The liaisons (*dö-zö-RO*, *ẽ-nö-RO*, *vẽ-tö-RO*, *di-se-tö-RO*), *SIS/DIS/si krwa-SÃ* and *ka-trö-vẽ-Ẽ* are correct. Every prediction and check has exactly one correct option, and the distractors are really wrong. I could not verify the content of the two videos.

## Shared issues
None new. I agree with the developer's three notes.
