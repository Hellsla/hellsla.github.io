VERDICT: FAIL
CONTENT-HASH: 4773c1d9057101b7
## Blocking
1. (B, consistency) lesson.md, Tiivistelmä/Summary first bullet (line 658): still states $a = \tfrac{\Delta v}{\Delta t}$ as the acceleration, unconditionally, while the formula section now defines $a_\text{k} = \Delta v/\Delta t$ as the average acceleration and $a = a_\text{k}$ only for constant acceleration. Fix: "Keskikiihtyvyys $a_\text{k} = \tfrac{\Delta v}{\Delta t}$ … ; kun kiihtyvyys on vakio, $a = a_\text{k}$." (same in en: average acceleration $a_\text{k}$). The concept card `fy4-kiihtyvyys` (kortit/fy4.json, kortit/en/fy4.json) has the same $a = \Delta v/\Delta t$ while `fy4-keskikiihtyvyys` has no formula: move it there as $a_\text{k}$.
## Polish

## Checked
- Formula section: $a_\text{k} = \Delta v/\Delta t$ (MAFY keskikiihtyvyys), $a = a_\text{k}$ for constant $a$, $v = v_0 + at$, $x = x_0 + v_0t + \tfrac12at^2$ with names and units; correct and as MAFY.
- Worked example and inquiry (constant $a$; $-2{,}0\,\text{m/s}^2$ feedback) remain valid with $a$; numbers unchanged (lesson-answers.py).
- fi, fi-easy, en say the same.
