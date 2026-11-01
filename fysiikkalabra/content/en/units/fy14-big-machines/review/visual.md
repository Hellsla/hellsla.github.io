VERDICT: FAIL
CONTENT-HASH: bcda2c2ef93d38ea

## Blocking
1. [Major] `lessons/units/fy14-big-machines/figures.py` `heating()` (about lines 75–80), figure `heating`, at 390 and 1280. The neutral-beam dots start at the box (x = 455) and run to x = 335, with an arrow to 300. The plasma band ends at x ≈ 438, so five of the six dots and the arrowhead lie in the empty central hole of the torus. The figure shows the beam passing through the plasma and stopping where there is no plasma. That contradicts the text ("Inside the plasma the fast atoms are ionised, trapped…") and the figure's own `aria-label` ("straight into the plasma"). Also, the injector box (x 470–590) sits on top of the ring's outer edge (x ≈ 502), and the "neutral beam" label overlaps the orange band. Fix: move the box outside the ring (for example x 515–590). End the dots inside the band (about x 500, 482, 465, 450, with no arrow into the hole). Better still, inject tangentially along the band, as PLT, TFTR and JET did. Then place the label above the box, clear of the band.

## Polish
1. [Minor] `inquiry.json` `beam-speed` **Reasonableness**: at 390, "$1.958 \cdot 10^{6} : 3.00\,\cdot$ / $10^{8}$" breaks inside a number. Fix: brace each number.
2. [Minor] Data table "Data: the big machines" at 390: "JT-60" breaks as "JT-" / "60", and the centred headers "Built by" and "Place" do not line up with the left-aligned cells. Fix: use a non-breaking hyphen (U+2011) in JT‑60, T‑7 and T‑15, and left-align the headers (shared table style, see below).
3. [Minor] `unit.md`: the same scale is written as "million kelvin" (100, 20–30) and "million degrees" (PLT's 60). Fix: use "million kelvin" throughout, or say once that at this size kelvin and degrees Celsius are the same.
4. [Minor] Figure `budget`: the title says "million dollars a year", but the values are then-year dollars (the `aria-label` says so). Fix: "US fusion budget, million dollars a year (dollars of the time)".

## Checked
- Captures regenerated for this hash: contact-1 and -2; intro-390, stage-tutki-390-4 (table), stage-sovella-390-2 (`beam-speed` solution open), the theory summary (#14) and the French corner (#22–#23).
- Own Playwright captures of `hero`, `heating` and `budget` at 390 and 1280. Smallest label 15.5 px at 390. The bars are to scale (332 : 40 ≈ 8.3). Coordinates read in `figures.py` to confirm the beam defect. No `.katex-error`, no raw `$`, no console errors, no horizontal scroll.
- Components `fx-bm-order` and `fx-bm-french` at 390 and 1280. Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English 4 · accessibility 4
