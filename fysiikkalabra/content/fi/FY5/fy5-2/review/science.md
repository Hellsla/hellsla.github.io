VERDICT: PASS
CONTENT-HASH: a2c4fdc9e0e64166

## Blocking

## Polish
- lessons/FY5/fy5-2/figures.py:260 (keinu-voimat): the figure shows no board mass, and only the text alternative says that G's length (15 kg) was chosen. A sighted student sees a figure drawn to scale and could think N's length is determined. Fix: add a short visible note in the figure, e.g. "G:n pituus valittu (massaa ei annettu)", or draw G with a broken or undimensioned style.

## Checked
- The diff since the round-3 PASS (git diff HEAD) is limited to the two solution embeds in inquiry.json and the new seesaw_fbd in figures.py. The rest of the lesson is unchanged.
- keinu-voimat, rendered and measured: scale 0,26 px/N. F_l is 61 px, F is 76,5 px (= 1,25 · F_l), G is 38,5 px (15 kg) and N is 176 px, which equals F_l + F + G. ΣF = 0 holds as drawn.
- keinu-voimat points of application: F_l and F push the top surface down, with the child at the left end and the adult's hand at X(1,2 m) on the other side. G starts at the CoM at the pivot. N ends on the bottom surface 16 px beside the pivot, and the text alternative states this offset. The dimension lines read 1,50 m and 1,20 m. The turn arrow is clockwise, which matches "aikuisen voiman kiertosuunta positiiviseksi" and F r₂ − mg r₁ = 0.
- Drawing G is correct. The prompt says the board's own weight acts but does not turn it, so a complete diagram must include the Earth's pull on the board. G acts at the pivot, so it has no moment and the answer does not depend on it. The text alternative is honest: it says G's length was chosen because the mass is not given.
- The solution text for tarkistus-2 lists the same four forces in the same places as the figure.
- lauta-voimat (siirto), measured at 0,08 px/N: F_p is 86,5 px from the rear end, pointing down. N is 157 px at 1,50 m, equal to F_p + G + F_h. G is 23,5 px at the centre and F_h is 47 px at the front end on the top surface. The turn arrow is anticlockwise, which matches "Vastapäivään … positiivinen" in the solution text.
- I recomputed every number with my own moment points: worked example N_B = 392,4 N and N_A = 196,2 N; koe-1 and koe-2 N₁ (from moments about support 2) and the tipping limit x_k = 3,5 m; siirto 1079 N and its distractors 1962 N, 981 N and 883 N; tarkistus-2 294 N and its distractors 188 N and 235 N; Etsi virhe 78,48 N; tan 30° = 0,577. All agree with lesson-answers.py and inquiry.json.
- No other activity, the theory, the simulation or the earlier figures changed, so the round 1–3 checks still hold.
