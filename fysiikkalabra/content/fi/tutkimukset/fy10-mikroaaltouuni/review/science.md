VERDICT: PASS
CONTENT-HASH: 20924171d6882045

## Blocking
None.

## Polish
- Mode O, frequency step: the page says to use the manufacturer's tolerance when the manual gives one, and that the last-digit estimate is too small. It does not say what to do when no tolerance is given. Suggest one clause: then Δf is left out of the number but named as a source of error in Luotettavuus (Δd usually dominates anyway). Give no value.
- Mallin rajat (student text) still says only "voi poiketa". The direction (spacing ≥ λ/2 along a line, c tends to come out high) is now in teacher.md, and teacher.md deliberately lets students reach it themselves. This is acceptable as it stands.

## Checked (re-check of hash 20924171d6882045)
- The previous polish was applied correctly:
  - The intro no longer gives the scale ("aallonpituuden voi selvittää juustoraasteen avulla"), so Ennusta Q3 stays open.
  - teacher.md states the 3D systematic correctly. In a cavity mode the spacing along a straight line is π/k_x ≥ λ/2, so c tends to come out too high.
  - The mode O Δf step uses the manufacturer's tolerance and no longer the plate's last digit. teacher.md gives the same rule.
  - Raportoi: "alusta ei pyöri: poistettu käyttöohjeen mukaan". This is no longer ambiguous.
  - Mode O heating uses the teacher's power setting and interval. teacher.md tells the teacher to give both to the O groups and to test them first.
- Physics unchanged and correct: the antinode and node spacing is λ/2, λ = 2d, c = fλ = 2fd; the 1D model and its 3D limits; heat conduction; the neglected effect of cheese, plate and cup; "sopusoinnussa" rather than proof.
- Uncertainty: ΔL = Δx₁ + Δx₂, Δd = ΔL/n against the row spread (the larger is taken), relative errors added for c = 2fd, the exact factor 2, rounding, and the extension's slope standard error. All correct.
- No invented numbers. There is no oven frequency or tolerance anywhere in investigation.md, investigation.json, teacher.md or figures.py (no GHz, MHz, 2450 or 2,45). The only numbers are 7.5 laps of the Earth per second (3.00·10⁸ / 4.0·10⁷ ≈ 7.5) and c = 2.998·10⁸ m/s, and both are correct.
- Safety intact on the page, in the json and in teacher.md: door and interlock never bypassed, damaged oven not used, turntable disabled only as the manual allows and by the teacher, water cup in the oven the whole time, no metal (ruler included), the superheating warning with fresh cool water, burns, stop if it smokes, no eating, milk allergy.
- Figures: the generated output matches the embedded SVGs (`investigations.py` figures check is up to date). The standing wave has nodes at the walls and λ/2 between adjacent antinodes. The spots figure shows 4 spots and 3 gaps. The model graph has no points. The hero shows the cheese unmelted. No fabricated data.
