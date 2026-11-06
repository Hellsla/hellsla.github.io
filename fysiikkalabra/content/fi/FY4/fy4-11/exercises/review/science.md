VERDICT: PASS
CONTENT-HASH: 3a2e90bccdbd2345

## Blocking

## Polish
- exercises.json:249 (L2-08) — test A's 0,030 s for a belted dummy is short: it gives 0,10 m of ride-down and about 17 kN at 25 km/h. This may stay. The values are labelled esimerkkiarvot, the answer depends only on the ratio, and a realistic A (≥ 0,05 s) with B four times longer would push B to an unrealistic 0,2 s. If the text is touched again, "vanha auto ilman turvatyynyä" makes the short time plausible without changing any number.
- solutions.md:176 (L2-08) — "törmäyksen keskimääräinen voima [riippuu] nopeudesta suoraan" holds at the same stopping time. The sentence before states that condition, so this is clear in context; "samalla pysähtymisajalla" would make the sentence stand alone.

## Checked
- Round 2: the round-1 blocker is resolved. solutions.md:176 now limits the comparison to "näissä esimerkkikokeissa" and adds the same-car rule (doubling the speed doubles F_ka when Δt stays the same). Both are correct and match the lesson's F_ka = mΔv/Δt.
- "muuttuu kertoimella 2 : 4 = 0,50" (exercises.json, the correct feedback; solutions.md:174) is correct and doesn't reveal a reason.
- The commit diff touches only those two strings in this chapter. The numbers and options are unchanged, and the round-1 recomputation still holds: the ratio is 0,50, with 17,4 kN and 8,7 kN for 75 kg.
- The distractors (×8, ×2, unchanged, ¼) still each follow from their stated error. They catch the chapter's warned mistakes (v² as in braking; the belt changing Δp).
- B (50 km/h, 0,12 s) is consistent with the existing task at exercises.json:138 (0,100 s) and with the lesson.
- Exactly one option is correct, and none can be picked out by form. I checked from the text only; I did no render.
- Hash 3a2e90bccdbd2345 is the same at the start and at the end (packet regenerated, mode full).
