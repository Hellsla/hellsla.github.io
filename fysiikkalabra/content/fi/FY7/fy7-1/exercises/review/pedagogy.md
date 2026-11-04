VERDICT: PASS
CONTENT-HASH: aca1e5e86a2b06fb

## Blocking

## Polish
- exercises.json:fy7-1-L3-03 — Helsinki is 53 µT here but 52 µT in the lesson table and example; "82,5°" suggests false precision for a "noin" value. Fix: use 52 µT and 82° with answer 1,87 as before, or say "kurssin arvo 52 µT" in the lesson.
- exercises.json:fy7-1-L3-01 — answer is now -11 µT; the sign convention is stated, but a student may enter 11. Fix: add "(vastaus voi olla negatiivinen)" or accept the sign as the graded part in the solution note.
- exercises.json:fy7-1-L2-01 — still repeats the worked example with unknown and given swapped (earlier Polish, unchanged).
- exercises.json:fy7-1-L2-02 — three-component Pythagoras not in the lesson (earlier Polish, unchanged).

## Checked
- L1-05: "Maan kenttä jätetään huomiotta" removes the earlier ambiguity; the answer (away from the magnet) is now unambiguous.
- L2-03: 52/sin 77° = 53,4 µT recomputed; 53,4 cos 77° = 12,0 µT, so the sanity check is true.
- L3-01: the north-positive sign convention makes the key insight (needle flips) part of the checked value; solution explains how the sign gives the direction.
- L3-02: "riittävän kuumaksi" replaces "punahehkuinen", which is more accurate; the model answer names the Curie temperature and random re-formation of domains.
- L3-03: 53 cos 74° / (55 cos 82,5°) = 14,61 / 7,179 = 2,03 recomputed; the "miksi" part now has a model answer with a criterion (horizontal component, not total field).
- answers.py agrees with exercises.json and solutions.md for all changed tasks.
- Finnish: "$53\,\mu\text{T}$", "$770\,{}^\circ\text{C}$" formatting and cases correct.
