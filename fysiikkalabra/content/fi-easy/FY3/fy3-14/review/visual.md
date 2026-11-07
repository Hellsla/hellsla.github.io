VERDICT: PASS
CONTENT-HASH: 92b90e4e2adadf7b

## Blocking
- none

## Polish
- [Minor] energy-bar figure aria-label (untouched) — decimal points in Finnish: "25.1 kJ", "2.1 kJ", "33.4 kJ", "35.5 kJ" — "25,1 kJ" etc.

## Checked
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry.json: every $c m T$ heat term now $c m \Delta T$, the limit step defines $\Delta T$ = $T$ − 0 °C and ends $T = 0\,{}^\circ\text{C} + 26{,}57\,\text{K} = 26{,}57\,{}^\circ\text{C}$; the tea step names $\Delta T = 70\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 70\,\text{K}$. Source-checked; the supplied fy3-14-fi-easy-l2sol captures show Koe 1, not these steps, so the rendering of the inserted \Delta was not seen (a one-glyph change in formulas that passed earlier; the aligned block in the error task gains only that glyph).
- delta review 2026-11-07 (teacher's proofread replacement texts): the new intro sentence, the Kaava split into $Q_\text{v}$, $Q_\text{j,läm}$, $Q_\text{j}$ displays with $\Delta T_\text{v}$, the numbered four-case list, "Tapauksessa 3/4" paragraph and $\Delta T_\text{v}$ in example and summary; opened fy3-14-fi-easy-kaava-390/-1280 and fy3-14-fi-easy-tapaukset-390/-1280 (subscripts incl. "läm"/"warm" render upright, inequalities fit at 390 px, list numbering and energy-balance display intact).
- batch delta review: "Luvun tärkeät käsitteet" panel captured from preview/fi-easy/fy3-14.html at 390 and 1280 px (the review/shots set has no capture of it) and opened — between the opening and stage 1, term bold over its explanation at 390 px, two-column at 1280 px, no clipping, no horizontal overflow, no KaTeX error; top-390 opened in a montage (read-aloud "Kuuntele" button under the title, layout intact).
