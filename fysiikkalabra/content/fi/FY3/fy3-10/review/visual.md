VERDICT: PASS
CONTENT-HASH: 5e3d91121ea79e92

## Blocking
(none)

## Polish
- [Minor] fy3-10-sim-390, fy3-10-exp-exp-1-390-1 — the readout breaks as "keskiarvo 0,3 s / :n ajalta", so the case ending lands at the start of the next line — keep the ending with the unit (non-breaking join of "s" and ":n" in the readout string).
- [Minor] fy3-10-sim-390 — the canvas labels (hidas/nopea, osumia/s, axis ticks, "osumia seinään") shrink to about 8 px on a phone; the values are repeated as text below the canvas, so nothing essential is lost — enlarge the canvas text at narrow widths if the sim template allows.
- [Minor] fy3-10-lab-1280-1 and fy3-10-sim-1280 — the sticky simulation card cuts the "Laskennan selitys" row in half at its lower edge; probably an internal scroll in a 900 px viewport, please check it is reachable.
- [Minor] fig-4 (paine-ja-tekijat, fy3-10-fig-4-390) — in the "N, 2T, V" cylinder the doubled speed is barely visible, because the arrows are only slightly longer than in the first cylinder; lengthen them (about 1.4x) so that the temperature difference is seen, not only read from the label.
- [Minor] fy3-10-example-390-1/2 — each unit-conversion bullet is followed by a boxed one-line chain, which splits the list into fragments on a phone; this follows the build's rule, so accept it or shorten the bullets. Also "Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä" appears in three places (Ydinajatus, Järkevyys, the inquiry feedback); the last repetition could go.

## Checked
- Opened at readable size: fig-1..5 (390), top-390, sim-390, sim-1280, intro-1280, theory-1280-1..3, example-390-1/2, stage-tutki-390-1/3, exp-exp-1-390-1, lab-1280-1/2, open-ennusta-1280, open-tarkista-1280-1, open-exit-1280, open-exercises-1280-1, sovella-390-1.
- Contact sheets 5 and 6 (exercises L1 to L3, every solution open) were triaged. The exercises are already PASS-reviewed, so I opened none of them at full size beyond L1-1.
- Counted the particles in the SVG source: 12 and 12 in helium-ilma, 8 in each vessel in mole-masses, and the bar lengths follow 4:29:44.
- Not opened separately: stage-herata/ennusta/selita/tarkista-390, exp-2, lab-1280-3, open-tarkista-2/3 (the contact sheets showed nothing abnormal).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
