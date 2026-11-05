VERDICT: PASS
CONTENT-HASH: 6f2205f3d7a0348d

Round 1 (new YO-skill task L2-08, type 10 Mittausdata, added 2026-11-05; the rest of the set was PASS in round 2 and is unchanged).

## Blocking

## Polish
- exercises.json:311 and :319, solutions.md:204 (L2-08) — the difference of two values is compared with one value's uncertainty, 10 kt. Each value carries ±10 kt, so the guardrail's test is whether the intervals overlap (difference < 2Δm = 20 kt). The conclusions do not change (5 kt overlaps; 100 kt does not; no pair falls between 10 and 20 kt), so C, but say it the guardrail way: "välit 520 ± 10 kt ja 515 ± 10 kt menevät päällekkäin, joten eroa ei voi osoittaa" and "ero 100 kt on selvästi suurempi kuin yhteenlaskettu epävarmuus 20 kt" (drop "kymmenkertainen").
- exercises.json L2-08 stem — "elinkaaren … päästö" for one plant's single year is an odd quantity (lifecycle emissions include construction, not a yearly figure). Say "vuosittainen hiilidioksidiekvivalenttipäästö" or keep it as invented example data; either is fine.
- lessons/FY2/fy2-8/answers.py:28 — the comment lists the multiple-choice tasks L1-06, L1-07 and L2-07; add L2-08.
- solutions.md:200–201 — the new heading follows the previous paragraph with no blank line; add one.

## Checked
- L2-08 recomputed: 520 − 420 = 100 kt; 520 − 515 = 5 kt; the straight-line 2034 value 420 − 25 · 10 = 170 kt (least squares gives 182 kt, same point); emission per energy 520 → 420 g/kWh, realistic for a fossil plant and consistent with the lesson's table (gas 490).
- Exactly one correct choice; answer equals its text. Each distractor is really wrong and its feedback names the right reason: overlap within uncertainty, cause not in the data, extrapolation 10 years past a 5-year set, wrong column.
- "todennäköisesti todellista" matches the guardrail (never "varmasti"); "ei voi osoittaa" rather than "ovat samat" is right.
- Data marked "esimerkkiaineisto, ei tilasto", as the FY2 data rule asks. Scope: m = e·E idea only; no FY3 content.
- Recomputed every numeric answer by running answers.py and comparing with exercises.json in one script: all 17 within tolerance; unchanged since round 2.
- Round-2 report stands for the other tasks; the diff touches only L2-08.
- The hash was unchanged at the start and at the end.
