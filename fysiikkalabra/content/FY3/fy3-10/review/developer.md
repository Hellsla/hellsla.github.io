VERDICT: DONE

Teacher items only; no exercise, answer, formula or prose changed.

- lesson.md: both inline SVGs redrawn (viewBox 600×300, currentColor with opacity tints). Ydinajatus: two shaded glass balloons, the same 12 particle positions in each, motion arrows (helium arrows longer); labels n = 0,21 mol, m = 0,83 g / 6,0 g and "sama p, T" in KaTeX foreignObjects, "helium"/"ilma" as text. Kaava: four shaded cylinders with pistons, particles with arrows (2N twice as many, 2T longer arrows); N, T, V / 2N / 2T / V/2 and p / 2p in LaTeX. aria-labels updated.
- sim.js: select "Nopeus" (hidas 0,25×, normaali 0,5× default, nopea 1×) after the sliders; physics advances dt·speed, the 2 s average runs on simulated time; `speed` in simState. Kept "Nollaa mittaus" first in .controls (the DOM-order assertion and NOTES §4 want the main button first). Long note moved into details.note "Lisätietoja"; "asteikko mukautuu" removed from the canvas; readout cut to three lines (state line dropped, it is in the slider labels).
- tests/sims/fy3-10.json: select options/default, speed values, details, three-line readout, ratio at 0,25× after 4 s real time (tol 0,15), pace check; readout assertions retargeted to the new text, none loosened.
