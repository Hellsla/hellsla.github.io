VERDICT: FAIL
CONTENT-HASH: 94e15a47fe5d26e5

Round 2 (fy7-5-L1-09, ordering)

## Blocking
- exercises.json:98 — with C flux now 0,080 mWb the task no longer catches the chapter's warned mistake "large flux means large voltage": a student using e = N·Φ gets 0,04 V for C, still below D (0,60 V), so C stays first and the order is the same as the correct one — restore a flux for C that makes the wrong rule put C clearly high (e.g. 8,0 mWb as before gives 4,0 V, above B), and fix the C sentence in solutions.md:196 if the number changes again.

## Polish
- exercises.json:92 — five calculations is heavy for level 1; consider four situations (round 1, unchanged).
- exercises.json:98 — "yhden kierroksen vuo tarkoittaa käämin yhden kierroksen läpi kulkevaa magneettivuota" is circular; say "Vuo on yhden kierroksen läpi kulkeva vuo."
- solutions.md:196 — "tilanteelle C tulee virheellisesti nollaa suurempi jännite" no longer shows why the order would go wrong; after the fix above name the wrong position.

## Checked
- Values recomputed: A 1,2 V, B 3,0 V, C 0, D 0,60 V, E 2,0 V; order C, D, A, E, B; direction stated in the prompt.
- Round-1 Polish on the solution paragraph applied (wrong-order causes on separate lines).
- The forgotten-N mistake is still caught (A, B fall below D).
- Checked from text only (no renders; pedagogy role); inline formulas fit (measured earlier, at most 227 px at 390 px).
