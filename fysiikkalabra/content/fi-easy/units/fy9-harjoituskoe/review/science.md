VERDICT: PASS
CONTENT-HASH: 060191698eb68ae9
Delta review (rule for extra answers, 2026-11-14) of the version passed at 889350cdbeb1cd52.

## Blocking
None.

## Polish
None.

## Checked
- The one changed paragraph: when more answers are given in Part II or III than allowed, the real exam counts the allowed number of answers with the lowest combined score, and the student is told to assess the practice exam the same way. This matches YTL Reaaliaineiden kokeiden määräykset 2.5 (fetched 2026-11-14): "katsotaan kokeen kyseisen osan kokonaispistemäärän muodostuvan siitä sallitusta määrästä vastauksia, joiden pistesumma on pienin", and the English page ("only the permitted number of answers with the lowest combined score are counted"). The rule is stated per part, as in the regulation. The second-stage rule (7 answers for the whole exam) is left out, which is fine: Parts I to III have fixed counts that add up to 7.
- The old rule (count the ones chosen before opening the model answers) is gone in all three languages; no other place in the unit states a rule for extra answers (grep).
- "The page does not add up the points for you": the developer log says no scoring code exists and no code was changed; the sentence matches that.
- 120 p maximum unchanged. fi, en and fi-easy say the same thing.
- Hash checked at the start and the end with `python3 scripts/units.py hash fy9-harjoituskoe --lang fi-easy`.
