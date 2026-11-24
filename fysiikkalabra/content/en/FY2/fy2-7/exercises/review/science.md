VERDICT: PASS
CONTENT-HASH: c490387b34b31487

## Blocking

## Polish
- content/fi/FY2/fy2-7/exercises/exercises.json:67, :233; content/fi/FY2/fy2-7/exercises/solutions.md:142, :268, :269 — the Finnish set still says "sisäenergiaksi". The FY2 scope note leaves internal energy to FY3, and the guardrails let FY2 keep "lämpöenergia", so the two languages now use different terms. This is outside this English set and does not block it — if the teacher wants the same FY2 wording in Finnish, change it to "lämpöenergiaksi, joka siirtyy lämpönä ympäristöön" in a separate change.

## Checked
- I ran the hash `--exercises --lang en` at the start and again at the end. Both times it was c490387b34b31487, the same as in the packet.
- I judged the diff in its context. There are five replacements of "internal energy" by "thermal energy": exercises.json:67 and :233, and solutions.md:149, :281 and :284. No number, symbol, option text or `correct` flag changed, so the 15 answers I recomputed in round 2 still hold and answers.py is not touched.
- `grep` finds no "internal energy" left in the English exercises.json, solutions.md or answers.py. The FY2 scope note ("no internal energy or first law") is now respected.
- Physics of the new wording: electrical energy becomes thermal energy of the conductors, which is transferred as heat to the surroundings. This keeps the P1 structure, so the energy goes to the surroundings as heat and is not "turned into heat". It uses FY2's permitted term "thermal energy" and leaves no wrong picture (C), and it does not contradict FY3.
- L1 high-voltage choice (exercises.json:67): the correct option's feedback still gives the right mechanism, a smaller current at the same power and so less heating of the conductors. Exactly one option is correct.
- L2-07 speed-of-light misconception (exercises.json:233, solutions.md:281–284): the distractor's feedback still says that the cause is the current heating the conductor, not how long the transfer takes. The feedback, the Principle line and the model answer say the same thing.
- solutions.md:149 (district heating comparison): the wording for the electricity grid and the district heating network matches the other two places. The 40 MWh and 27 MWh are unchanged.
- No guardrail break (A or B) in the changed text.
