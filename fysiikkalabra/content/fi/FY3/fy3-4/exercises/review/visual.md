VERDICT: PASS
CONTENT-HASH: 42492e47d1fafc99
Round: 3

Round 3 checks the last commit (`git show HEAD -- content/fi/FY3`), which touches only the fy3-4 L3-05 Järkevyys line; the rest is covered by the round-2 PASS.

## Blocking
- none

## Polish
- [Minor] Data tables (L2-05, L2-06, L2-07, L3-05): header and number alignment (site-wide table style, not task content; carried over).
- [Minor] L3-05 Sijoitus c): the chain 122,6 + 367,9 + 613,1 + 858,4 = 1962 kN has no units on the terms; add kN (carried over).
- [Minor] Answer-field wording "Vastauskenttään" (fy3-4) vs "Vastauslaatikkoon" in fy3-5..7; pick one site-wide (carried over).

## Checked
- Diff HEAD read: the Järkevyys line now has three ≈ signs in valid LaTeX (`\approx`), the same notation as elsewhere; no notation or line-length problem. Plain-text quantities: none.
- No new capture was taken; the change is one symbol in a formula line.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
