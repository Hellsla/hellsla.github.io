VERDICT: PASS
CONTENT-HASH: bdd5130b947d2f62

## Blocking
(none)

## Polish
- lesson.md photo caption: "veden potentiaalienergia muuttuu turbiinissa liike-energiaksi" skips a step. The water first gains kinetic energy as it falls, and the turbine then takes that energy as rotational kinetic energy. This is acceptable at this level (C). For a more exact wording: "muuttuu veden liike-energiaksi, turbiini ja generaattori muuttavat sen sähköenergiaksi".
- lesson.md hero SVG: the arcs end at a ball-centre height of y = 420, but the floor line is at y = 440 and the ball's radius is 32, so the ball would overlap the floor where it hits it. The ball resting at the end is also partly below the floor line. This is drawing only, for the visual reviewer.

## Checked
- Hero figure: the bounce heights above the contact level are 370, 240, 150, 90, 50 and 24 px. Each bounce is about 0,5–0,65 of the one before, a roughly constant fraction, which fits a restitution model. The arc widths follow sqrt(h): 270, 210, 160, 120 and 84 px against the predicted 217, 166, 124 and 89. The ghost balls sit at the arc apexes (control points recomputed). The heat marks are at every impact point and nowhere else. The figure does not say it is to scale, and it leaves no wrong picture.
- Energy-forms table: the definitions match the glossary and the earlier text. The lämpöenergia row and the paragraph after it keep "riippuu aineen määrästä, ei sama kuin lämpötila" and the net-transfer wording for lämpö (as the guardrails require). Every example belongs to its form. E_mek = E_p + E_k is unchanged. Nothing physical was lost in the move from list to table.
- Hydropower photo: the image matches its alt text. The caption's energy chain (potential energy, then kinetic, then electrical) is correct.
- sim.js diff: only the y-axis tick labels are placed differently, and the tick mark is skipped when the label is narrow. It uses p.textSize/textWidth only, with no change to the model, simState, adapter or controls. The 390 px capture shows the "1 000" label and the gridline correctly.
- inquiry.json exercises text: only the sentence about levels was removed. No physics changed.
- Content hash bdd5130b947d2f62 at the start and the end.
