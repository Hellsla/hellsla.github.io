VERDICT: PASS
CONTENT-HASH: 0ec9c5c89c784dc6

## Blocking
None.

## Previous polish, now applied
1. **Sensor type.** Suunnittele has a step that all modes see: read the sensor with the hose open to room air. About $100\,\text{kPa}$ means total pressure, and near zero means overpressure. The step names a barometer or a weather station for the air pressure, with a sea-level caveat. It does **not** take a decision away from mode I. It is a check of the equipment, and the theory already tells every mode to use total pressure. It leaves the setups, axes, models, ranges and uncertainty method open. teacher.md now says that groups find out the type themselves and that the teacher checks it beforehand. In OO, the new diagnostic of the intercept sign (a negative intercept of about $-p_\text{ilma}$ for overpressure, a positive one for $V_0$) gives a second chance to catch the error. It is correct, and it sits in `tuki OO`.
2. **"Päätät itse" for OO** now says that the page gives the setups, the models and the axes. It names what the student decides: ranges, points, waiting time and how to keep the constant quantity and the amount of gas constant. This matches the OO blocks.
3. **"paine–lämpötila-sarjan"** replaces "lasiastiasarjan" outside the blocks. "Lasiastiasarja" remains only inside `tuki OO`, where the setup is given.
4. **teacher.md Ajankäyttö:** OO fits one long lesson if the baths are ready. I probably needs a second session. This is realistic.
5. **teacher.md explains why these two series:** a V–T series at constant pressure is inaccurate because of piston friction, and the extension combines all three quantities.
6. **Ennusta Q3** is open now ("Millainen riippuvuus … mielestäsi on").

## Polish
- teacher.md Valmistelu still says only "kerro raja ryhmille". That is consistent with groups finding out the type themselves, which Eriyttäminen now states, so no change is needed.

## Checked
- **Mode I leaves real decisions.** The procedure, tables, axes, models and uncertainty methods stay in `tuki OO` blocks. The `tuki I` line makes the extension compulsory.
- **"Päätät itse" holds in both modes.**
- **Ennusta comes before the theory.**
- **The hero does not answer Ennusta.** The displays and the screen are blank.
- **The three learn goals are practised.**
- **The new OO paragraph on the direction of the p–T error** is in `tuki OO`, which is an acceptable place for it. The physics is right: dead volume at room temperature puts the extrapolated zero below 0 K.
