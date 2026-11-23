VERDICT: PASS
CONTENT-HASH: 202f81d31b383f25
SCOPE: full (fi), this change first: three new ```pysahdy boxes in unit.md, three figures (hero, mokki, piiri) whose SVG line art is now a webp image under the same LaTeX labels, and paragraph breaks in one inquiry model answer. The unit hash was the same at the start and the end.

## Blocking
(none)

## Polish
- Pysähdy 1 (mökki): "sama jännite kuin lähteellä" holds because the loads sit straight on the battery terminals and the wiring is ideal. Strictly, the voltage is the terminal voltage, not E (see Paristo ja akku). This is a C-level simplification that matches the 12 V of the text. "kuin akun napojen välillä" would also fit with the later section.
- Pysähdy 3: "Osa lähdejännitteestä kuluu" repeats the wording of the theory paragraph above it. A phrase like "jännitehäviö $R_\text{s}I$ pariston sisällä" would say the mechanism more exactly. Not an error.

## Checked
- Pysähdy 1: the loads are in parallel, so both have the same voltage (Kirchhoff 2 across parallel branches). This matches the figure, the Ydinajatus text and the Kaava paragraph.
- Pysähdy 2: in series the current is the same, so with P = RI² the larger R gets more power. This matches the theory sentence ("Sarjassa suurempi resistanssi saa suuremman tehon"), the Johda derivation and the inquiry 40 W / 100 W model.
- Pysähdy 3: U = E − R_sI is correct and agrees with the Johda derivation (E − R_sI − RI = 0), the U(I) graph (intercept E, slope −R_s) and the Yleisiä virheitä item. The answer is right for a discharging battery, and the box's question says "kun piirissä kulkee virta". It does not conflict with the charging sentence.
- Figures redrawn as images (checked from the webp files): mökki shows a battery with its long plate (+) on top, two parallel branches (lamp symbol and resistor) and junction dots. The arrows go out of + along the top, down through both branches and back along the bottom, which agrees with the 4,5 / 0,50 / 4,0 A labels and Kirchhoff 1. Piiri shows E and R_s in series inside the dashed battery box, with terminals on its edge and U pointing from − to +. The current I leaves + and goes through R. Both match their aria-labels and the text. Label placement is for the visual reviewer.
- Recomputed: 6,0 W / 12 V = 0,50 A; 48 W / 12 V = 4,0 A; sum 4,5 A; 100 Ah / 0,50 A = 200 h = 8,3 d ("yli kahdeksaksi vuorokaudeksi"); 100 Ah / 4,5 A = 22 h; 1 kWh = 3,6 MJ. In the inquiry model: R40 = 1322 Ω and R100 = 529 Ω, giving 1850 Ω, I = 0,124 A, P40 = 20,4 W and P100 = 8,2 W, the same as the text's "noin 20 W / 8 W". The inquiry change is only paragraph breaks; the wording and numbers are identical.
- Formulas and conditions in Kaava (Ohm's law at constant temperature, a non-ohmic filament, P = UI general and RI², U²/R only for an ohmic resistor, the E–R_s model with constant E and R_s): correct and inside FY6. MAFY names were unchanged.
- tasks.json, solutions.md and teacher.md did not change since the PASS at 9298f8fbb6e98905 (s1–s8 recomputed there and in earlier rounds), and the diff shows nothing that touches them. I did not recompute them in this round.
