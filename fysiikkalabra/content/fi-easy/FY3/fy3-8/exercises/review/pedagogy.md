VERDICT: PASS
CONTENT-HASH: 4c5a23b8baf24e5f
## Blocking
(none)
## Polish
- solutions.md fy3-8 L3-04 Vastaus — "13,2 mm" is followed by "tulokset kelpaavat kahteen numeroon pyöristettyinä", and two figures would give 13 mm (an "at least" limit rounds up to 14 mm). Fix: "...g_min = 13,2 mm (alaraja pyöristetään ylös: 14 mm)" or say the values are kept with three figures because the check in c) needs them.
## Checked
- Delta: the "käytännössä vähintään 14 mm" clause was removed from a); the answer is now g_min = 13,2 mm, b) g_max = 18 mm unchanged.
- Mallivastaus c) uses 13,2 mm and 18 mm, so it is consistent with the shorter answer; the Järkevyys block also uses 13,2 mm and 4,8 mm.
- The earlier polish point is now only a rounding-sentence mismatch, not an error.
- Judged from the diff and the solutions file on disk. Hash unchanged at start and end.
