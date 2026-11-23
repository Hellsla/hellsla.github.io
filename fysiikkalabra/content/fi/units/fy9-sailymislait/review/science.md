VERDICT: PASS
CONTENT-HASH: 12b570ae6be478bd
SCOPE: delta (fi): commit 693d2f77fa against the version I failed (ac36248617b265a1): unit.md pysahdy 2 (one line) and teacher.md (two lines). The rest was judged in full last round and is unchanged.

## Blocking
- (none)

## Polish
- Still open from last round, none of them blocking: pysahdy 3 could add "lyhyen törmäyksen aikana"; s7 d "kuluttaa liike-energiaa" would be more exact as "menettää kitkaan enemmän energiaa"; s8 b "47 km/h" against the unrounded value of about 45 km/h; s7 d's closing remark on air resistance.

## Checked
- Pysahdy 2 now says: "Kitkan työ on negatiivinen, $W < 0$, koska kitkavoima on liikkeen suuntaa vastaan. Siksi se pienentää mekaanista energiaa, joka muuttuu sisäenergiaksi." The cause is now the direction of the force ($W = F_\parallel s$, $F_\parallel < 0$), and the drop in mechanical energy follows from it. This matches the theory paragraph above it, s7 b ("koska kitka on liikettä vastaan") and the Virheet entry. The A finding is fixed.
- teacher.md, Arviointi: "muut seitsemän Osa II:n tyyppisiä (kuusi 15 ja yksi 14 pistettä), yhteensä 124 pistettä". 20 + 6·15 + 14 = 124, which matches `practice.py check` (8 tasks, 124 points). In the 65–75 min row, "muut seitsemän tehtävää" (8 tasks minus the one started in class) is right. "viisi" no longer appears in any language's teacher.md. The A finding is fixed.
- Nothing else changed: the parent commit's tree hashes to ac36248617b265a1, the version I failed, and `git diff 693d2f77fa~1 HEAD` touches only those three lines in fi. The same three lines changed in en and fi-easy, with the same meaning. tasks.json, solutions.md, answers.py, inquiry.json and figures are untouched, so last round's recomputation still holds.
- `practice.py check` OK. Hash 12b570ae6be478bd at start and end.
