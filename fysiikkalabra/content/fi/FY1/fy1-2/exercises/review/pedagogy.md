VERDICT: PASS
CONTENT-HASH: e66a67c219672d7e

Delta review over the audit's PASS (4157a622aabadf49): one exercise replaced by a figure task, LaTeX units.

## Blocking
- none
## Polish
- exercises.json fy1-2-L1-04 is a two-step (difference of readings plus cm to mm) at L1; acceptable, but nearer L2. L3-02 still has plain '30,07 AU' and '1920 px'.
- Ruler at 360 px: millimetre ticks are about 2 px apart, so 13,6 cm needs counting from the long tick at 13; the 3 % tolerance (+-3 mm) forgives a 1-2 mm slip.
## Checked
- Figure needed: the text gives no lengths; 2,0 cm and 13,6 cm come from the ruler. Rod does not start at zero, which tests the key idea (difference of readings).
- (13,6-2,0) cm = 11,6 cm = 116 mm correct; answers.py and solutions.md agree; **Kuvaajan lukeminen:** present.
- Description lists the ends only in the aria-label, not in the task text; ruler labelled 0-15 with LaTeX numbers.
