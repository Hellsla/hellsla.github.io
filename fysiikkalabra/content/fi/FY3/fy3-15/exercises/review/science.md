VERDICT: PASS
CONTENT-HASH: 59dbbb72338667fe
Round: 2

## Blocking
(none)

## Polish
- exercises.json:246 and solutions.md:169 (L2-08) — typo: "polttoaineteosta" should be "polttoainetehosta" (language).
- exercises.json:241 (L2-08, 50 MW option) — "kuutiometri sadaksi litraksi" is still a contrived slip; carried over, not blocking.
- lessons/FY3/fy3-15/answers.py — no comment marking L2-08 as multiple choice with no number (carried over).

## Checked
- Round-2 change (6bbde30c5): the task moved from L1-09 to L2-08 (exercises.json:224), which resolves the round-1 level note. The id is unique and nothing in answers.py refers to the old id.
- The correct option's feedback now reads "noin 42 % polttoaine[tehosta] 1200 MW, mikä sopii lauhdutinhäviöksi". That is consistent with the lesson, where the condenser heat is the largest part of the waste heat. The "= 500 MW" is now "≈ 500 MW", which is correct for 502,8 MW.
- Recomputed: q_m = 12 000 kg/s, ΔT = 10 K, P_L = 502,8 MW (41,9 % of 1200 MW). The distractors are 0,503 MW, 50,3 MW and about 14 600 MW, the last one larger than the fuel power and so impossible. Every feedback is right, and exactly one option is correct.
- The other content is unchanged from round 1.
- Renders: I measured the fresh preview at 390 px in Chromium with feedback and solution open. The widest inline formulas are 285 px and 278 px, within about 300 px. The physics is judged from the text.
- Hash identical at start and end.
