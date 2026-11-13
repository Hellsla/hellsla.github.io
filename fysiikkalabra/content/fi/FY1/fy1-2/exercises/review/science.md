VERDICT: PASS
CONTENT-HASH: a34be413af2946f5
SCOPE: delta added-exercise from bfb2af3a6b840af5 base 81db4a6fd727

## Blocking
- none

## Polish
- content/fi/FY1/fy1-2/exercises/solutions.md:204 — "kolmella merkitsevällä numerolla, koska molemmissa tiedoissa ... on neljä" reads as if four figures in the data gave three. The rule allows four (1,282 s), and three is the house default. Optional: "kolme merkitsevää numeroa riittää; lähtöarvoissa on neljä, joten tarkkuus ei rajoita".

## Checked
- fy1-2-L1-10 only (delta, added exercise; round 2). The hash was the same at the start and the end.
- I recomputed the answer myself: t = s/c = 3,844·10⁸ m / 2,998·10⁸ m/s = 1,2822 s (1,2822 s with the exact c). answers.py gives 1.282188 and the key is 1.28: right.
- Round 1 Blocking fixed: the answer is now 1,28 s with a significant-figure reason. It is no longer an unexplained 1,3 s.
- The MAFY Moon mean distance (384 400 km) and the hint's table (Aurinkokunta) are right. The km → m conversion is right, and t = s/c is solved before substitution.
- Physics: the radio signal travels at c (category C, fine at this level). The reasonableness check is a real one. The tolerance of 0,04 is fine.
