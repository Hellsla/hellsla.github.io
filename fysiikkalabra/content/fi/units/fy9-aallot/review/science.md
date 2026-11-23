VERDICT: PASS
CONTENT-HASH: e1e86d735a997e1d
SCOPE: delta (re-review after my FAIL at 7ea980554d63e713; the only content change is teacher.md, commit 693d2f77fa). Language: fi.

## Blocking
- None.

## Polish
- These are carried from the previous report and are still open. None is blocking.
  - Source speed symbol: $v_\text{s}$ (lt-6 feedback, juna) and $v_\text{l}$ (s2 c) differ from the formula section's $v_\text{L}$.
  - jousitus, Periaate: write $m_\text{kori} + m$ in $T = 2\pi\sqrt{m/k}$.
  - pysahdy 3: "nimittäjä $v - v_\text{L}$ on pienempi kuin osoittaja $v$" would be clearer.

## Checked
- Previous Blocking item (teacher.md, task count and points) is fixed:
  - Arviointi now says s3 is 20 points and "muut seitsemän" are Osa II type tasks: five at 15 points, one at 12 and one at 13, 120 points in total.
  - The 65-75 min plan says "muut seitsemän tehtävää".
  - I recomputed the part points from tasks.json:
    - s1: 4+4+4+3 = 15
    - s2: 3+4+5+3 = 15
    - s3: 4+5+6+5 = 20
    - s4: 5+5+5 = 15
    - s5: 4+5+6 = 15
    - s6: 3+5+4+3 = 15
    - s7: 4+2+3+3 = 12
    - s8: 3+3+4+3 = 13
  - Total 120, which matches the new text.
- Nothing else changed. Since the reviewed version, `git log` on content/fi/units/fy9-aallot and lessons/units/fy9-aallot shows two commits:
  - e5a3f7ab3a touched only review/science.md.
  - 693d2f77fa changed only teacher.md: two lines, the plan line and the Arviointi paragraph.
  - The working tree has no uncommitted changes to the unit's content. Lesson, inquiry, task set, solutions and answers.py are as I passed them, so the full-review numbers in my previous report still hold.
- The rest of the teacher.md I read in the packet is consistent with the unit:
  - The Pohdinta answer is 0,12 m and 0,50 m at 3,0 kHz.
  - Pipes give about 343 m/s.
  - The 10 dB lg 2 ≈ 3 dB remark is right.
  - The Moon pendulum is about 0,16 m.
- practice.py check: OK. Unit hash e1e86d735a997e1d at start and end.
