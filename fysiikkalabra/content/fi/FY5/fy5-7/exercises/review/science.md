VERDICT: PASS
CONTENT-HASH: 3de6b1d57fce91b7

## Blocking

## Polish
- content/fi/FY5/fy5-7/exercises/solutions.md:178 — `(\text{pienin kokonaisluku k})` sets the symbol k upright as a word, not as the variable $k$ — write `\quad (\text{pienin kokonaisluku } k)`.

## Checked
- Delta: the Kaava steps of L1-02, L1-07, L2-02…L2-07, L3-01…L3-05 are now aligned blocks that start from the basic relation (f = 1/T, t = nT, t6 − t1 = 5T, d_max = D + A, d_min = D − A, kT1 = mT2) and end at the form the Sijoitus uses. Every rearrangement is algebraically right. The packet's diff collapsed the line breaks; I read the file on disk.
- One script recomputed every changed task from its data. L1-02 5,102 ms, L1-07 25 s, L2-02 2,005 Hz, L2-03 66,67 ms, L2-04 7,50 cm, L2-05 1,639 Hz, L2-06 1,51 s, L2-07 0,745 s / 1,342 Hz, L3-01 0,10 s, L3-02 12,14 cm, L3-03 1,80 s, L3-04 79,06 % (72,6 and 130 1/min), L3-05 44,24 cm. All of these match the Sijoitus lines and answers.py, which are unchanged.
- L3-01: the first positive root π/6 is right, and 5π/6 is correctly ruled out as the descending crossing.
- Paragraph splits in L1-06, L1-08, L2-06, L3-01 and L3-05 change no wording. The physics is as I passed it before.
- Hash 3de6b1d57fce91b7 at the start and at the end.
