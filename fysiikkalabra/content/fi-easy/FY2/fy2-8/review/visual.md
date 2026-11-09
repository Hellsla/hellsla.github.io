VERDICT: PASS
CONTENT-HASH: 322b65f689539151
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only
Round: 2

## Blocking
- none

## Polish
- [Minor] inquiry.json, line 154, correct-option feedback — the sentence now begins with a numeral ("2020-luvun alun pitoisuudella …"), which Finnish style usually avoids; optionally reorder: "Maapallo on 2020-luvun alun pitoisuudella noin $+15\,{}^\circ\text{C}$ ja lämpenee yhä kohti noin $+16\,{}^\circ\text{C}$:ta."

## Checked
- git show b01e11571: one-line change in content/fi-easy/FY2/fy2-8/inquiry.json, feedback "Nykyisellä" -> "2020-luvun alun"; round-1 blocking item resolved.
- fi-easy now agrees with fi and en in all four changed passages (sim model, koe intro, values.co2.420, feedback); no "Nykyisellä pitoisuudella" left.
- Round-1 checks still hold: changed sentences short and clear (NOTES §12); rendered preview/fi-easy/fy2-8.html at 390 px showed "2020-luvun alun määrä" without clipping or overflow.
- Content hash recomputed: 322b65f689539151 (matches coordinator).
