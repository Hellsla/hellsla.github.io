VERDICT: FAIL
CONTENT-HASH: 31ee974b6c4747a0

## Blocking
- [Major] lesson.md figure `luistelijat` (fig-4-390, theory-1280-1) — the scene is broken in two places. Adult A's head and cap go past the top of the viewBox: the circle is at cy 15 with r 17,8, the cap path reaches y −7, and the cap shows cut flat at every width. Child B's torso (`M339.5,124 Q354,65.5 337.5,75.5 …`) draws as a thin red wedge, separate from the legs — why it matters: this is the only picture for the third law, it breaks the print-quality rule (nothing clipped, 12 px margin), and the deformed child pulls the eye away from the force pair — fix: move the upper scene down about 25 px, or scale it to about 0,9 with the ice at the same place, so the top of the cap sits at y ≥ 12. Redraw B's torso as a closed body shape like A's, from the shoulders to the hips.

## Polish
- [Minor] Esimerkki, Yksikkömuunnokset — the step says no conversion is needed and then converts anyway ("joten tulos saadaan suoraan kilonewtoneina: 48 kN = 48 000 N") — fix: "Voimat ovat kilonewtoneina, joten muunnoksia ei tarvita, ja tulos saadaan suoraan kilonewtoneina."
- [Minor] lesson.md Arkikokemus and Yleinen virhekäsitys — the text uses straight quotes ("liikkeen voima", "kuluu loppuun") — fix: use Finnish ”…” quotes, as inquiry.json already does.
- [Minor] lesson.md Kaava — the symbols' units are plain in parentheses ("(N)", "(m/s)", "(kg)"), but Ydinajatus writes "($\text{N}$)" — fix: write them as $\text{N}$, $\text{m/s}$ and $\text{kg}$.
- [Minor] figure `kone`, scene panel — the two grey engine circles under a downward-slanting wing look like landing-gear wheels, so the plane seems to cruise with its gear down — fix: draw the engines as pods under the wing, level with it.
- [Minor] exp-1 Alkutila line and simulation (lab-1280-1) — the Alkutila line shows "$3\,\text{m/s}$" where the intro says $3{,}0\,\text{m/s}$, and the canvas tick and panel labels are about 9 px at 1280 px — fix: give the initial value as 3,0; enlarge the canvas label font.

## Checked
- top-390, intro-1280 and the opening illustration (fig-1-390)
- fig-2 (anturit), fig-3 (curling), fig-4 (luistelijat, zoomed; SVG lines 410–461), fig-5 (auto; arrow lengths checked in the source)
- example-390-1 and -2, with the `kone` figure (SVG 535–569: thrusts 38,5 px each, drag 77 px, lift = weight)
- sim-390, sim-1280, lab-1280-1 and -2
- theory-1280-1, -2 and -3
- open-ennusta-1280-1, open-tarkista-1280-1 and -2
- the malli-lamppu model figure: rendered myself from preview/fy4-3.html at 390 and 1280 px, because no capture opens it
- contact sheets 1, 2, 4, 5 and 6 (the stages at 390 px)

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 4
