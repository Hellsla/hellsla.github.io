VERDICT: FAIL
CONTENT-HASH: c33e72bc943a0fcc

## Blocking
- content/fi/FY5/fy5-16/exercises/exercises.json:301 — "Lukema 85 dB on epävarmuuden vuoksi välillä 84–86 dB" says the reading itself lies in a range and states the range as certain. The reading is 85 dB; only the true level is uncertain, and only *todennäköisesti* inside the interval (guardrails, Measurement and data: "never for certain") — fix: "Epävarmuuden vuoksi todellinen taso voi olla 84–86 dB, joten ylempi toiminta-arvo voi ylittyä." (solutions.md:97 already says "voi todellisuudessa olla 86 dB"; make the two match.)

## Polish
- content/fi/FY5/fy5-16/exercises/exercises.json:297 — the feedback says the uncertainty of a difference "on 2ΔL", but solutions.md:88 says "enintään 2ΔL" — use the same words in both (e.g. "on enintään").
- content/fi/FY5/fy5-16/exercises/exercises.json:291 — the correct option is the only one with a hedge ("noin"), a mild form cue (FY2 lesson) — add "noin" to a distractor too, or drop it here (6, 6 and 5 dB are given).

## Checked
- New task L2-08 (type 10, Mittausdata), checked against the text only, not renders: drops of 6, 6 and 5 dB per doubling of distance; expected 10·lg 4 = 6,02 dB. The largest deviation, 1 dB, is less than the 2 dB uncertainty of a difference, so the correct option follows from the data. Exactly one option is correct.
- Distractors: halving of the level (the log scale read linearly), a "slower attenuation" claim from a difference within the uncertainty (type 10's intended trap), and a safety conclusion from a borderline reading. The last one's feedback correctly adds that the allowed-time formula is an estimate, not a guarantee, matching the lesson.
- Point source, open field and ΔL = 1 dB are stated in the task; the data are realistic for a compressor. The 6 dB rule comes from the brief and the prerequisite fy5-15.
- The data use decimal points, as the rest of the set does. The caption is short.
- answers.py ran, and its 16 numeric answers are unchanged. L2-08 has a text answer and no entry. The rest of the set was PASS before and is unchanged.
