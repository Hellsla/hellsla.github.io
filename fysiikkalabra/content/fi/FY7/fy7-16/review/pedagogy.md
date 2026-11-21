VERDICT: PASS
CONTENT-HASH: ccfeb4615c07a746

Delta, round 3. Scope (teacher 2026-11-20): only the three ```pysahdy blocks and old content that stops them working.

## Blocking
(none)

## Polish
- lesson.md:156-160 (hob block, now at 215-219) — still only recalls the sentence above and the caption. Optional: ask what the pot's bottom must be made of for eddy currents to form. Carried over from round 2.
- lesson.md:289 (attenuation block) — needs a calculator for $10^{0{,}90}$ right after a conceptual section; accept, or use a rounder case.

## Checked
- Attenuation answer (line 291) now shows the inversion: $\lg(P_0:P)=A:10\,\text{dB}=0{,}90$, $P_0:P=10^{0{,}90}\approx 7{,}9$, so $P/P_0\approx 0{,}13$ (1/7,94 = 0,126). Correct; the round-2 Polish on the missing step is resolved.
- The answer follows the glossary definition $A = 10\,\text{dB}\cdot\lg(P_0:P)$ and the house style (colon for division, number with unit in LaTeX).
- Change is one answer line; the question, the other two blocks and their placement are unchanged; no prediction is given away.
- Charger and hob blocks as approved in round 2.
- No old content stops the blocks working.

## Vanhan sisällön löydökset
- Section "Kaava: Vaimennus desibeleinä" still does not display the inverse $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$, although the transfer item and worked example use it. Put it in the formula block (not fixed in this PR).
