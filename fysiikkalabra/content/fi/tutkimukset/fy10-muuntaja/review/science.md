VERDICT: PASS
CONTENT-HASH: b2a47a0e93d5bdb5

## Blocking
None.

## Polish
- Setup figure: the raster already draws a ∼ inside the source circle, and the `$\sim$` foreignObject at (50…70, 180…210) sits on it, so the symbol is drawn twice in about the same place. This is a visual matter, not physics.

## Checked
- I opened `assets/pics/fy10/fy10-muuntaja-setup.webp` (1564×1006) with an image viewer. It is a transformer circuit diagram. A closed grey iron core has a copper coil on each vertical limb: the left one has about 7 turns and the right one about 11. On the left are an AC source (∼), an unlabelled meter circle in series in the top lead, and a meter circle across the primary coil between two junction dots. On the right are a meter circle across the secondary coil between junction dots, then a meter circle in series and a load resistor. There is no spring and no weight. The earlier FAIL ("spring with hanging weight") was wrong.
- Labels and image: the image is mapped to 600×386.2 (scale 0.384) and I checked each label position. A (100…120, 127…153) is at the left series meter (≈114, 144) with $I_1$ above it. V (≈170, 195) is at the left parallel meter (≈173, 198), with $U_1$ to its left. V (≈430, 195) is at the right parallel meter (≈427, 198), with $U_2$ to its right. A (≈490, 140) is at the right series meter (≈485, 144), with $I_2$ above it. $R$ is right of the resistor (533…555). "rautasydän" is above the core (top edge at y ≈ 93). $N_1$, $N_2$, "ensiökäämi" and "toisiokäämi" are under the left and right coils (x ≈ 203…250 and 350…397). The aria-label (ammeters in series with the source and the load, voltmeters across the coil terminals) matches the wiring. It also matches the text rule "Virtamittari sarjaan … jännitemittari rinnan".
- Hero raster: a closed iron core with two coils, an AC supply, four meters, a load resistor, two spare coils and a notebook. This matches its aria-label.
- teacher.md diff vs HEAD: "lämpönä" → ”lämpönä” only, with no change in meaning.
- Physics (full read of investigation.md, investigation.json and teacher.md):
  - $U_2/U_1=N_2/N_1$ is derived from equal flux per turn and zero winding resistance, with the ideal model's conditions stated.
  - The $U_2/U_1$ against $N_2/N_1$ plot is a line through the origin with slope 1, and the model figure is to scale (1 ↔ 92 px on both axes).
  - $P=UI$ with RMS values. $U_1I_1 \ge$ the real input power because of the magnetising current, so $\eta$ is a lower bound. This needs true-RMS meters, and teacher.md says so.
  - Error propagation for a quotient or product by summing relative uncertainties is correct.
  - The loss mechanisms (winding resistance, eddy currents, hysteresis, leakage flux) are correct.
  - The DC remark and the safety items are physically correct.
