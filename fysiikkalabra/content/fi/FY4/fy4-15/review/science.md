VERDICT: FAIL
CONTENT-HASH: 0c5b2caec3779ecf

## Blocking
- inquiry.json:146 (vesi-data), also :265 (siirto, Järkevyys) — **B**: the table gives the plants' *maximum* powers beside the Vuoksi's *mean* flow 600 m³/s, and the text implies that this is the flow behind those powers. Combining them gives η ≈ 1,36, above 100 %. The ratio P/h ≈ 8 MW/m matches because both plants' largest turbine flows are about the same (≈ 900 m³/s at η 0,90, lesson-answers.py). The text never says so, and siirto's check then uses "suurimmasta virtaamasta 900 m³/s", which the student has never seen. — Fix: say in vesi-data that the largest power is reached at the turbines' largest flow, about 900 m³/s, which is more than the mean of about 600 m³/s, and label the 900 as calculated (η ≈ 0,90). Or drop the 600 and reword siirto's check.

## Polish
- inquiry.json:330 (check-3) — "keskimäärin 6 / 8 m/s": the v³ ratio is exact for a steady wind. For mean speeds it also needs the same wind distribution and no hours at rated power. Fix: "tuuli puhaltaa tasaisesti …" and "suuremman tehon".
- exit-ticket.json:11 — "yli noin 13 m/s" is the rated speed of the V82 only. Fix: "tehokäyrän voimalan teho".
- inquiry.json:112 — give the archive's full path, `turbine_models/data/Onshore/…`.
- lesson.md:185 — PE → KE in the pipe → the jet pushes the blades: this is the impulse-turbine picture. Imatra's turbines run mostly on pressure. C at FY4 level.

## Checked
- Recomputed every number of lesson.md, inquiry.json and the exit ticket in one script, mistakes included. All agree.
- Worked example: A = 11 310 m², P = 2,32 MW, wind power 5,15 MW, V82 area scaling 2,18 MW. Correct, solved symbolically, 2 s.f. justified.
- Real data: the V82 curve (3–20 m/s) matches the NREL file exactly. Fortum gives Imatra 192 MW / 24 m and Tainionkoski 62 MW / 7,8 m. The 29.4.2026 release (STT Info) gives a mean flow of about 600 m³/s.
- The 8,9-fold rise explained by η 0,35 → 0,39 (ρ 1,25) is correct. Betz 59 %, "alle puolet" (archive Cp ≤ 0,461) and rated power 1650 kW from 13 m/s are correct.
- Derivations of ρQgh and ½ρAv³, their units and conditions, and the efficiency wording (guardrails) are correct.
- Each choice item has exactly one correct option, and every distractor's feedback is correct.
- Power-curve figure: the points are to scale, and the dashed model with η = 0,45 meets 1650 kW at 10,4 m/s.
