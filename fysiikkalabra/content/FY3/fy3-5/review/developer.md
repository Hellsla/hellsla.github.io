VERDICT: DONE

Lesson-form retrofit (lint: 2 errors -> 0).

lesson.md
- Ydinajatus: new inline SVG after the paragraph on the two ways to change internal energy (viewBox 0 0 600 300, currentColor, 24 px, aria-label, marked schematic). Left: piston pushed into a cylinder, arrow with $W \gt 0$ (fig-tex foreignObject), faster particles, "ilma kuumenee". Right: hot and cold blocks in contact, arrow with $Q$ from hot to cold, "kuumasta kylmään".
- Esimerkki: staged into 4 stages with `<!-- vaihe -->`: Tunnetut ja kysytty (W = +150 J, Q = −40 J), Kaava (ΔU = Q + W), Sijoitus (aligned display, symbolic first row, = 110 J), Tulos ja järkevyys (unchanged text). Numbers and physics unchanged.

solutions.md, inquiry.json, other files: unchanged (no findings; section titles unchanged).

Checks: check_lesson.py all ok; test_inquiry.py 12 passed; screenshot 390 px shows the new figure without clipping or overlap.

Not changed (out of this pass's scope, not flagged by lint): the existing Kaava figure still writes "ΔU = Q + W" and "Q < 0 tai W < 0" as plain <text> at 22 px rather than fig-tex at 24 px.
