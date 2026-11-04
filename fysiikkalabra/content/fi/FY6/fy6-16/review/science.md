VERDICT: PASS
CONTENT-HASH: 8e3accc8a97e1b21

## Blocking

## Polish
- lesson.md:265–267 — optional, C-level: SFS 6000-7-722 also requires DC fault-current protection (an RCD of type B, or type A with 6 mA DC detection). "Oma vikavirtasuoja" is a fair simplification.

## Checked
- Round 2, judged from the diff HEAD~1..HEAD: lesson.md, inquiry.json, the figures.py labels; everything else as in round 1.
- Round-1 blocking item (lesson.md:309) is resolved. The text now says the main fuse "ei pala heti pienestä ylikuormasta, mutta jos ylikuorma on riittävän suuri ja jatkuu pitkään, se voi palaa". This matches gG behaviour and inquiry.json ("voi palaa").
- lesson.md:265 now gives the real mechanism: a load near the rating for hours, socket contacts heating, and other loads interrupting the charge.
- Efficiency: "tyypillisesti noin 80–95 %, ja se jää aina alle 100 %" is right for charging, because the charger, cables and battery always have losses. The summary now gives that reason ("koska latauksessa on aina häviöitä"). The tavat table (85 %, 90 %), the worked example (90 %) and Lukuarvojen lähteet ("80–95 % on arvio") all fall inside the new range.
- inquiry.json:71: the distractor "noin 1,7 kertaa … 400 V eikä 230 V" is still wrong, its feedback still explains why (3UI with 230 V phase to neutral), and exactly one option remains correct.
- The kayra labels "varaus 20/90/99 %" are re-anchored at the right points: centres at t = 4,53 h and 6,01 h.
- Unit-only edits (€/kWh, units in brackets) change no number. I re-ran the round-1 recomputation; all lesson numbers are unchanged and correct.
