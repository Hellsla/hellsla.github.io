VERDICT: FAIL
CONTENT-HASH: 1f6cfeb92c19a88f

Pedagogy review of fy14-iron-curtain (2026-11-01). I built the page, tested it in Playwright at 390 px and looked at the captures. Both predictions lock when the student commits. `pred-verify` opens at `theory-d` and `pred-thomson` at `theory-thomson`. Model answers stay closed until the student writes. No console errors.

## Blocking
1. **`inquiry.json` `learn` gives away `pred-verify`.** The goals stand at the top of the page (capture #1/#2), before the prediction. They say "explain how laser Thomson scattering measures …" and "argue why independent verification made the T-3 result trusted". The student reads that an independent laser measurement settled it, then is asked which way would settle it. Fix: change them to, for example, "explain how a plasma's electron temperature can be measured with laser light" and "evaluate how the T-3 result of 1968 came to be accepted, and convert a plasma temperature from keV to kelvins."

## Polish
2. **Engagement, `theory-thomson`.** `pred-thomson` is revealed by text and a static figure. Let the student act on the evidence: either an `interpret` with two measured spectra and their widths ("which one is about 1 keV?"), or a small width-versus-$T_\text{e}$ slider. Then the physics of the measurement is investigated, not only read.
3. **Order of `doubt`.** In the pair split, partner A reads Sources A and C only, but `doubt` asks about A and B and comes straight after `theory-b`. Move it after the pair exchange, or say "after your partner has explained Source B".
4. **`pred-thomson` prompt.** The prompt already explains the Doppler spreading. Cut it to the setup ("electrons move in all directions; the scattered light is spread over a range of wavelengths") so that the student must reason out the link with speed.
5. **Workload.** The unit has three written tasks in class (`why-invite`, `report`, `check-write`) plus the role-play. `teacher.md` already makes the report homework if needed: say so in the `report` prompt as well.

## Checked against the brief (*Science Across the Iron Curtain*)
- **Why they cooperated:** `why-invite` and the role-play, with four roles, a word bank and starters.
- **Evidence and circumstances:** the sorting, `doubt`, `find-error` and check 3.
- **Why independent verification matters:** the Key idea, the misconception about repeating and verifying, the report and the transfer task.

The source labels and the teacher's note that the texts were written for the course support source criticism. The French tips compare with Finnish *y*.

## Shared issues
The `pair` note is rendered after the textarea (`scripts/inquiry.py`; see fy14-secret-fusion).
