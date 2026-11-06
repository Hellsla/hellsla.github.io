VERDICT: PASS
CONTENT-HASH: 94e15a47fe5d26e5

## Blocking
- (none)

## Polish
- (none)

## Checked
- Round 2. The only round-1 item is fixed: in situation C the flux per turn is now 0,080 mWb (exercises.json:98, solutions.md), a realistic value for a bar magnet inside a school coil. The order and e_C = 0 are unchanged.
- The reworded solution is right. The "forget N" check gives A 6,0 mV and B 60 mV, which then sit straight after C, as the solution says. The "flux, not its change" mistake now says C would get a non-zero voltage, which no longer claims C becomes the largest (the old text said it would, which no longer held with the smaller flux). Järkevyys is now its own field: E has the fastest change, 2,0 Wb/s, but B's 50 turns give it the largest voltage.
- Recomputed: A 1,2 V, B 3,0 V, C 0, D 0,60 V, E 2,0 V. The order C, D, A, E, B matches `order`, `answer` and the answers.py comment. The rest of the chapter's numeric answers are unchanged in answers.py and within tolerance.
- Conditions stated: each change is uniform, "yhden kierroksen vuo" is defined, and the rod, v and B are mutually perpendicular. Notation matches the brief.
- Text only, not rendered: the inline chains are short (estimated under 250 px).
- The hash was identical at the start and at the end.
