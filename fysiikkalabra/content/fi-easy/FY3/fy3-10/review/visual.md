VERDICT: PASS
CONTENT-HASH: 1f48965343916086

## Blocking
- none

## Polish
- [Minor] fy3-10 sim canvas, settling state: the bar still shows a (noisy) height and the gauge needle moves while the number is hidden; acceptable as the readout says the value is settling, optionally lighten the bar until settled.
- [Minor] lesson.md, new kaasuvakio passage — "Silloin tulon $pV$ yksikön pitää olla joule. … kuutiometreiksi. Silloin" repeats "Silloin" — second one e.g. "Näin saadaan".

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): opened fi-easy-fy3-10 settling captures (360 and 1280 px; en and fi-easy included in the set): readout 'mittaus tasaantuu…' with KaTeX '0,1 s' and upright unit, wraps cleanly at 360 px, number label above the bar hidden and axis unchanged, no clipping or overlap; settled captures consistent. Decimal comma on canvas is allowed.
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry.json "Etsi virhe" feedback for the pressure and volume rows: no longer calls the pascal the only correct unit; Pa with m³ or kPa with l, $1\,\text{kPa}\cdot\textsf{l} = 1\,\text{J}$, litre now \textsf{l} as elsewhere. Text-only (no capture of these feedbacks); KaTeX and wording checked in source, sentences consistent with the unchanged lesson text.
- delta re-review 2026-11-07 (ml fix): verified in the inquiry.json diff that the Boyle recall prompt now writes $60\,\text{ml}$ and $30\,\text{ml}$ (thin space, upright unit, matching the feedback); nothing else changed. The earlier Major finding is resolved.
- delta review 2026-11-07 (teacher's proofread replacement texts): the rewritten "missä"-paragraph, the new displays ($R$, $1\,\text{Pa}\cdot\text{m}^3 = … = 1\,\text{J}$, $1\,\text{kPa}\cdot\textsf{l} = 1\,\text{J}$) and the typeset kPa/mol values in inquiry and exit ticket; opened fy3-10-fi-easy-a-390 and -1280 (displays fit at 390 px, decimal separators right; the capture starts just below the $R$ display, which was read from source).
- batch delta review: "Luvun tärkeät käsitteet" panel captured from preview/fi-easy/fy3-10.html at 390 and 1280 px (the review/shots set has no capture of it) and opened — between the opening and stage 1, term bold over its explanation at 390 px, two-column at 1280 px, no clipping, no horizontal overflow, no KaTeX error; the edited lesson.md/inquiry.json sentences read in their diff (prose only, no new maths); top-390 opened in a montage (read-aloud "Kuuntele" button under the title, layout intact).
