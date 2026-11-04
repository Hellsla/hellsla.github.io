VERDICT: PASS
CONTENT-HASH: 25581fe1b566f1d2

## Blocking

## Polish
- exercises/review/packet-science.md (tooling) — the "Exercise brief" block is empty for the English lesson: the packet generator looks for the Finnish section names (Kaava, Esimerkki ...) in an English lesson.md. Not a content issue; notation was checked against the solutions and the Finnish original instead.

## Checked
- Delta round 2: the diff since the passed version is empty (hash unchanged); a fresh scripted comparison again finds every number of exercises.json and solutions.md equal to the Finnish source.
- Every number in exercises.json and solutions.md equals the Finnish original; answers, units and tolerances unchanged.
- Recomputed in one script with my own formulas: L1-01 18,90 %; L1-02 1,615·10⁵; L1-03 6,0 mm; L1-04 7,67 %; L1-05 98,41 nm; L2-01 6,60 1/s; L2-02 0,811 %; L2-03 5,338 mm; L2-04 70,9 mm; L3-01 482; L3-02 d½ 5,55 mm, d 34,99 mm; L3-03 1,243·10⁶. All match the keys.
- Background subtracted before the attenuation law (L2-03, L3-02) and both stated in the text; L3-02 target is the source's net rate 30 /min, as the task says.
- Narrow-beam assumption stated in every attenuation task; L3-01 states even ion-pair production along the track.
- Solutions solve symbolically first, conversions right (min → s, cm → mm, MeV → eV, GHz → Hz), rounding justified, reasonableness checks are real (half-value bracketing, 1240 eV·nm check).
- L3-03 explanation correct: single-photon energy decides, power does not; microwaves heat.
- Translation keeps the physics terms (net pulse count, half-value thickness, ion pair) consistent with the lesson.
