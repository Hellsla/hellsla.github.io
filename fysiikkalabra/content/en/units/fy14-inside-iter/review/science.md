VERDICT: PASS
CONTENT-HASH: 46ad737ab67de926

Science re-review, 2026-11-01, of commit c6532e4f.

## Blocking 1 from the previous review: fixed
"Over 300 MW" is gone from the unit, `teacher.md`, `unit.json` and `iter.json`. The text now gives iter.org's own figures from https://www.iter.org/node/2751, read again today: at least 110 MW, up to 620 MW in 30-second peaks, cooling water and cryogenics about 80 %. It no longer says that the heating alone needs this power. The comparison is now "170 MW … far less than ITER's peak demand of 620 MW", which is correct.

## New content checked
- **The rebuilt `power` figure is to scale.** At 0.51 px/MW: 50 → 25.5, 500 → 254, α 100 → 50.5, n 400 → 203.5, 110 → 56, 620 → 315, and the 0–600 axis labels sit at the right heights.
- **New `pred-gain` (turbines turning one third of 500 MW).** "No" is correct. Turbines would give 167 MW, and only during pulses. The plant draws at least 110 MW all the time and up to 620 MW in peaks, so over a day it uses more than it makes. All four feedbacks are right.
- **Earlier recomputation still holds.** "About 400 MW" in Reasonableness is fine, and the tritium numeric (0.355 g) is unchanged.

## Blocking
None.

## Polish
None.

## Shared issues
The earlier `iter.json` points are all fixed:
- the power figures now come from iter.org, with the Power supply page cited;
- the 2034 entry now says "a more complete machine";
- the cryopump text and hint now say "lower (divertor) port", which matches iter.org.
