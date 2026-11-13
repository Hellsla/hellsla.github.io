VERDICT: FAIL
CONTENT-HASH: a34be413af2946f5

## Blocking
- fy1-2/exercises/solutions.md (fy1-2-L1-10, Vastaus) — the new sentence says the answer has three significant figures "koska molemmissa tiedoissa on neljä merkitsevää numeroa". That contradicts the lesson rule (as many significant figures as the least accurate factor, i.e. four), and the answer 1,28 s has three; a student learns a wrong rule. Fix: either state `1,282 s` (four s.f.) or justify three honestly, e.g. `Etäisyys 384 400 km on taulukkoarvo, jonka tarkkuus on vain kolme numeroa (3,84·10^8 m), joten tulos annetaan kolmella merkitsevällä numerolla: 1,28 s.`

## Polish
- none

## Checked
- exercises.json fy1-2-L1-10: hint now precedes the question, which is its own last sentence; `t = \tfrac{s}{c}` matches the lesson notation. Previous polish fixed.
- Arithmetic 3,844e8 / 2,998e8 = 1,282 s; tolerance 4 % still consistent.
- Delta scope: only this diff judged.
