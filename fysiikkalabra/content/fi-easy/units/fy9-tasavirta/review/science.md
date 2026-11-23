VERDICT: PASS
CONTENT-HASH: 74609c45aabfe90e
SCOPE: full, new content first: three ```pysahdy boxes in unit.md; three figures (hero, mokki, piiri) are now the shared webp line art under unchanged LaTeX labels; one inquiry model answer split into paragraphs. Previous PASS: 683e4a80b5d04cff.

## Blocking
(none)

## Polish
(none)

## Checked
- Pysähdy 1 (after the mokki figure): the devices are in parallel, so each has the source voltage 12 V. This matches fi line 104; the only change is that one sentence became two.
- Pysähdy 2 (after Teho ja energia): in series the larger resistance gets the larger power, because I is the same and P = RI². This matches fi line 142 and the theory paragraph above it ("Sarjaankytkennässä suurempi resistanssi saa suuremman tehon"). The condition (series, same current, Ohmic resistor) is stated.
- Pysähdy 3 (Paristo ja akku): U = E − R_s I, with the drop across the internal resistance. This is the same formula and wording as fi line 179, and it agrees with the johda derivation and the Virheet item. "Kuluu" is the unit's own level-appropriate wording (C).
- All three boxes sit at the same places as in fi.
- Figures: in mokki, the + terminal (long plate) is on top, current leaves it, and 4,5 A splits into 0,50 A and 4,0 A at the junction and rejoins. The LED and the cool box are in parallel, and the labels are unchanged. In piiri, E and R_s are in series inside the dashed battery, the U arrow runs between the terminals, and the current I flows + → R → −. These are the same images as fi, which passed.
- Inquiry model answer: only the paragraph breaks changed. Recomputed: R = 1322 Ω and 529 Ω, I ≈ 0,124 A, P ≈ 20 W and 8,2 W. The 40 W lamp is brighter.
- Unit text: 0,50 A + 4,0 A = 4,5 A; 100 Ah lasts 200 h on the LEDs alone and about 22 h on both devices. The formulas and their conditions (Ohm's law for a metal at constant temperature, the P = RI² and U²/R forms only for a resistor, constant E and R_s, terminal voltage while charging) are unchanged and correct.
- Sovella s1–s8: the task set is unchanged since the PASS. I recomputed one independent script against answers.py, and every headline value agrees: s1 11,25 Ω, 162 W, 9,78 µm, 146 W, 136 W; s2 374 Wh, 27,7 km, 2,5 A, 35,5 V, 85,7 %; s3 R_s 0,733 Ω, I_k 6,31 A, 4,11 W; s4 68 W, 1,62 mV; s5 96,2 Ω; s6 6,40 h, 66,7 W, 2,74 kW, 2,33 kWh; s7 9,52 Ω, 4,0 Ω, 75 %; s8 0,30 A, 0,10 A, 1,8 W, 3,6 W, 1,35 W. practice.py check: OK.
- The hash was the same at the start and the end (74609c45aabfe90e).
