VERDICT: PASS
CONTENT-HASH: 0e35175c4902c240

Science re-review, 2026-11-01, of commit c6532e4f. Earlier findings 1–3 are all fixed:
- §Why now gives 1987 for the agreement and 1988 for the conceptual design, matching `order-story`.
- §Challenges now says the assembly was halted and the next sector module went into the pit only in April 2025 (NEI, April 2025; ITER PR of 29 July 2026: "Sector module installation began in April 2025").
- `pred-why` now uses KSTAR.
The re-ordered site paragraph (Nov 2003 EU choice, Dec 2003 Canadian withdrawal and deadlock) matches the sources. The schedule table, the shares and the Members are unchanged and still match the 2024 baseline PDF and iter.org.

## Blocking
None.

## Polish
None in the unit files.

## Shared issues
1. `assets/units/fy14/data/timeline.json`, card `iter-first-module-2025`, which this unit's timeline task now shows. The card says "Assembly had been stopped for about two years". That is the claim this unit dropped: module #6 was in the pit from May 2022 and came out 14 months later, and the next module went in in April 2025. The card also calls the bevel non-conformities "welding defects". Fix: "…after repairs to defects at the welding edges of its sectors. Assembly of the vessel had been halted since 2022…".
