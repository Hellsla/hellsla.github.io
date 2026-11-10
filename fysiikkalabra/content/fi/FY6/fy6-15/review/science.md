VERDICT: PASS
CONTENT-HASH: bd66f3fde94bfd46

## Blocking

## Polish
- content/fi/FY6/fy6-15/lesson.md:408 — the sentence says the potential difference between the feet is very small but not why. Optional: add "koska johtimen resistanssi jalkojen välillä on hyvin pieni". This is C-level and not a finding.

## Checked
- Previous blocking item (internal consistency, bird): lesson.md:408 (Suurjännitejohdot) and :570 (Yleinen virhekäsitys) now say "lähes samassa potentiaalissa / potentiaaliero hyvin pieni / vain erittäin pieni virta". This matches ennuste-2's correct option and all four of its feedbacks (inquiry.json:91–100). A grep finds no remaining "ei jännitettä / ei kulje virtaa" claim in the lesson, the inquiry, the exit ticket or the figure labels.
- ennuste-2: exactly one correct option. Each distractor is really wrong and its feedback says why (feet conduct; the current divides between parallel paths; the conductors are bare). The correct option's feedback names the wing-to-second-conductor or wing-to-pylon case correctly.
- ennuste-1, kertaus, virhe, tarkistus-1, tarkistus-2: exactly one correct option each, and the distractor feedback is right.
- Recomputed in one script with my own formulas, compared with lesson-answers.py: 2300 W and 3680 W limits; 8,70 A; kitchen 13,9 A, all devices 22,6 A; skin 1,15, 11,5 and 230 mA (ratio 200); example 19,6 A (9,57 + 4,35 + 5,65), estimate 22,5 A; virhe 12,6 A; siirto 14,8 A, 131 W, 8,87 V drop; mistakes 0,0719, 45,4 W, 88,2 kW; exit 2,56. All agree, and the rounding is justified.
- Models and conditions: P = UI with rms values for in-phase loads (power factor about 1 is stated); E_max·d only in a uniform field; the TN system is named for the fault-current path; the body-current table is tied to 50 Hz, about 1 s and IEC 60479-1; the shoes condition is given in the theory and in the iho task.
- Mechanisms: the fuse protects the cable through RI²; the RCD compares the line and neutral currents (its L–N limit is stated); the step voltage comes from the ground's potential gradient.
- Model answers (johtopaatos, tarkistus-3) and the exit ticket say what the theory says.
- Scope is within the FY6 content on electrical safety.
- Hash identical at start and end.
