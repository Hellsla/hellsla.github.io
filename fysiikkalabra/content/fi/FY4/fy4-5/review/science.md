VERDICT: PASS
CONTENT-HASH: 9b2ff7780f6a3d07

## Blocking

## Polish
- sim.js:139 (`dashed`) — in push mode at about 40°, the F_x label still touches F's arrowhead at the sled's top-left corner (rendered). — Offset it downward or to the left in push mode.
- review/shots predate 2d2daf3b (captions say "pisteenä"), and site/sims/fy4/fy4-5/sim.js is still the old point-model build. — Regenerate the shots and rebuild the site before publishing.

## Checked
- Delta 000c8ad0. `suunnat` now pairs a pictorial situation picture with a rectangle-only diagram in every panel (PNG viewed).
  - lattia: N = G (88 px), N from the bottom face.
  - rinne: tilted rectangle (25°). N leaves the bottom face perpendicular to it (Δ −34/−72,5, so N = G cos 25° = 80 px). F_μ starts at the up-slope bottom corner, along the slope (37 px = G sin 25°). G is vertical.
  - lamppu: T from the top face, T = G (77 px).
  - heliumpallo unchanged: N pushes down and ends on the top surface, and F_noste = G + N.
  - The aria-label matches the arrows.
- Sim: N is now left of G at the bottom face, and the F_y label is clear in pull mode (rendered at 30° with components on). The physics is unchanged: N = 146,2 N (pull 30°), 260,5 N (push 40°), and a = F cos α / m. tests/sims/fy4-5.json has its on-load defaults assertion back, without `malli`.
- inquiry.json:60: "kaksi voimaa ja narun voiman pystykomponentti" now agrees with step 7.
- check-3 criteria match `malli-tyonto`: the push "alkaa tai päättyy" at the handle, and components are optional.
- lesson.md:60 step 3 now has the push exception, which agrees with `suunnat`, `malli-tyonto` and line 278. The friction sentence matches the rule: it starts at a corner of the contact surface and is never drawn along a side from its middle.
- Unchanged from my full review this round: the four drawing rules in every other figure, the lift options (exactly one error each), esimerkki (to scale, 2,96 m/s², 71,8 N), virhe, and every recomputed inquiry number. No text mentions a point model.
