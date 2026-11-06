VERDICT: FAIL
CONTENT-HASH: e803415d0d56c89b
Round: 1. One new YO-skill task, fy6-11-L2-08 (type 3, Voimakuvion valinta, four new figures); the rest of the set was PASS before and is unchanged.

## Blocking
- exercises.json:255 (fy6-11-L2-08) — the data are not realistic. A 0,10 g plastic bead has a radius of about 3 mm, and −20 nC on it gives a surface field of about kq/r² ≈ 2·10⁷ V/m. That is roughly seven times the breakdown strength of air (about 3·10⁶ V/m, which FY6 itself teaches under läpilyöntilujuus), so the bead could not keep its charge in air. — Put the plates in a vacuum ("levyt ovat tyhjiökammiossa" in place of "Ilmanvastus jätetään huomiotta"), or scale the bead down, for example a dust grain of 1,0·10⁻¹² kg with −2,0·10⁻¹⁶ C, in a vacuum. That keeps F_s : G ≈ 2 and the figures unchanged; update the solution and the feedback numbers to match.

## Polish
- exercises.json:255–290 — no distractor carries the lesson's Yleinen virhekäsitys (force growing near a plate; E depending on the test charge). A and D carry mistakes the lesson's Kaava warns about, and A repeats L1-07. Consider a sentence on the bead's height in the task, with D's feedback (or the solution) saying F_s is the same anywhere between the plates.
- lessons/FY6/fy6-11/figures.py (pick-*) — the descriptions say "suorakulmiona" but not that the forces start from the body (G from the centre, F_s from just left of it). Add "lähtevät kappaleesta" for a reader who cannot see the figure.

## Checked
- Hash e803415d0d56c89b at start and end.
- All answers.py values rerun in one call: no mismatch.
- F_s = |q|E = 2,0 mN down (negative, upward field), G = 0,98 mN; ratio 2,04, matching the figures' "kaksi kertaa" and PK_FS : PK_G in figures.py; four descriptions match the drawn arrows.
- Physics in the feedback: no force along v needed, forces change only the vertical velocity; weight is negligible for an electron, not for this bead (brief: öljypisarat, pölyhiukkaset).
- Notation \overline{F}_\text{s}, \overline{G}, \overline{v}; the force is red and v blue as FY6 requires (from code; colours not rendered).
- Not identifiable by form: "Voimakuvio A–D".
- Formulas measured with KaTeX in Chrome at 390 px (formula widths only, figures not rendered): widest inline 282 px (G = mg … in the solution), under 300 px.
