VERDICT: FAIL
CONTENT-HASH: 5fb1d833ae7bc6f3

## Blocking
- content/fi/FY7/fy7-15/exercises/solutions.md:188 (L3-04 Järkevyys) — A: "Lukemat jäävät hieman laskettua pienemmiksi, koska todellinen kalvo absorboi…" is false for the given data (15°: 32 > 30; 60°: 93 > 90 W/m²) and contradicts the task's "ihanteellista polarisaattoria". The check is not a real check. — Fix: "Lukemat poikkeavat lasketuista muutaman W/m² molempiin suuntiin, mikä on mittausepävarmuutta; suurin lukema 114 W/m² on lähellä laskettua 120 W/m²."

## Polish
- solutions.md:189 (L3-04 Mallivastaus c) — "Polarisaattori … kääntää sen polarisaatiosuunnan" suggests a lossless rotation; an ideal polariser passes only the projection. Write "läpi tulleen valon polarisaatiosuunta on aina polarisaattorin läpäisysuunta, ja osa valosta absorboituu."
- solutions.md:198 (L3-05 Vastaus) — the limiting datum is I₀ = 40 W/m² (two significant figures), not the angle 25,0°: give 7,1 W/m² with that reason (the answer box tolerance already accepts it).
- solutions.md:187 (L3-04 Vastaus) — "kolme merkitsevää numeroa kuten kulma 45°": 1/8 follows exactly from the ideal model; say so instead of citing a two-figure angle.
- solutions.md:~176 (L2-07) — the student's 36,3° is also the Brewster angle for light coming from inside the ethanol (the plan's "aineen sisältä katsottuna"); one sentence would close the loop with L3-02.

## Checked
- One script recomputed all 19 numeric answers with my own formulas: new ones 98,70 W/m²; 55,59°; slope 313,9 lx (intercept 6,9 lx); 50,77° (raw-point interpolation 51,6°, inside tolerance); 53,67° (student 36,33° = 90° − α_B); 12,5 % (I₃ = ⅛I₀ sin²2θ, table values 0/30/90/120/90/30/0); α_B 53,06°, Sun altitude 36,94°, 7,144 W/m², crossover 56,8°/33,2°. All match exercises.json and answers.py (ran it).
- L1-06 MC: exactly one correct option; each distractor's feedback states the right physics (horizontal polarisation of glare, transmission axis ≠ propagation direction, uniform tint).
- L2-05: background-plus-Malus model stated in the task; slope read from two points on the fitted line; guardrail fit sentence present; accepted range 305–323 lx fits tolerance 0.03.
- L3-05: Brewster-reflected glare horizontal, θ = 90° − 25°, sun altitude = 90° − α_B: correct geometry.
- New tasks stay inside Malus/Brewster as taught; levels 8/7/5 fit the plan; no duplicates (L3-04 generalises L3-01 as the plan asks).
- Rendering of the new L3 solutions at 1280 px checked: no overflow.
