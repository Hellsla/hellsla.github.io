VERDICT: PASS
CONTENT-HASH: d88ebf005f47e7f8

## Blocking

## Polish
- solutions.md:104 (L3-02 Periaate) — the sum of atomic numbers is not conserved (4 → 2). One clause would say why atomic masses still work: two positrons annihilate with two electrons. The task says to use atomic masses, so this is not blocking.
- answers.py:30 — the comment says "8,95e37", but the computed value is 8,944·10^37 (exercises.json 8.94). Correct the comment.
- answers.py:28 — the comment "4,53 kg" agrees with the computed 4,526 kg, and the stored answer 4.5 lies within tolerance (0,6 %). Storing 4.53 would give a tighter answer.

## Checked
- Round-1 blocker fixed: exercises.json:82 (L3-01) now says "Oleta, että kaikki lämpöteho syntyy uraani-235:n fissioista". The solution's Periaate states the same assumption and notes the Pu-239 share in a real reactor.
- L3-01 recomputed: 4300 MW · 86 400 s / (200 MeV) = 1,160·10^25 fissions, × 3,903·10^-25 kg = 4,526 kg, which rounds to 4,5 kg. The cross-check (82 GJ/g) is a real check.
- All twelve answers recomputed with my own formulas: 4,783; 178,4; 348,7; 3,269; 939,57; 1,509 kg; 3,374·10^14 J/kg; 184,7 MeV (x = 2); 4,106 %; 4,526 kg; 8,944·10^37 1/s; 2,402·10^5 a. All are within 0,6 % of exercises.json.
- Round-1 polish applied: L1-05 now says "massan pienenemistä" instead of "muuttuu energiaksi", and L1-04 says "yksi syy".
- The stated conditions are right: the charge-number sum is conserved, the plant runs at full power for 365 d, and all the Sun's energy is radiated.
- Hash d88ebf005f47e7f8 at the start and at the end.
