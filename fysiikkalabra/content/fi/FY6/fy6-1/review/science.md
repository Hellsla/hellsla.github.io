VERDICT: PASS
CONTENT-HASH: eeb7638a0da72ed1

## Blocking

## Polish

## Checked
- Hash eeb7638a0da72ed1 at the start and the end. The changes since round 2 (a9b345687bfb82fb, commit d1e64343) are the piiri figure's left I arrow, the + and − labels plus the moved U label in jannite, and the two round 2 polish wordings.
- piiri: the left arrow now sits at x = 30, outside the left wire (x = 60), and points down. With the + end on the right of the cell pair, all four arrows run + → switch → up the right → left across the top through the lamp → down the left → −. This agrees with kaavio (+ on the right, switch at bottom right, I up the right edge) and with the caption.
- jannite: + is now labelled at the top cell's terminal nub and − at the bottom. The top wire goes from + to the lamp and the bottom wire returns to −. The violet "sama varaus palaa paristolle" arrow points from the lamp toward the battery's − end, which is correct for conventional current. U = 1,5 V and "1,5 J / 1 C" match U = E/Q.
- Sim `model` box: "selvästi hitaammin" now states correctly that a hot filament's resistance rises with voltage (round 2 polish 1).
- check-2 Järkevyys: 1500 mAh is "noin kolmasosa" of a 4000–5000 mAh phone battery, which is right (round 2 polish 2).
- I recomputed everything in one script and every value agrees with lesson-answers.py and the texts. Worked example: 180 C and 1,12·10²¹ e⁻; 1/e = 6,24·10¹⁸; one dot is 3,1·10¹⁷ e⁻. exp-1: 0,200 A (mistakes 20 and 5). exp-2: 0,100 A. Sim Q: 1,00/2,00/3,00 C with one lamp and 0,50/1,00/1,50 C with two. siirto: 432 kJ (mistakes 7,2 and 12 000; 0,12 kWh). check-2: 5400 C (mistakes 90 and 1350; 1,5 Ah). Exit ticket: 6,0 J.
- I re-read the full packet and found no new issue. Definitions, the current direction, the drift speed against the field signal, and the options and feedback are unchanged from the round 2 PASS. sim.js and the experiment setups are unchanged.
