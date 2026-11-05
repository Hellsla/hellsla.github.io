VERDICT: PASS
CONTENT-HASH: b9aec31fc4971a53

## Blocking

## Polish
- exercises/solutions.md:144 — fy5-15-L1-07 (replaced): the same concept (equal sources add 3 dB) also appears in the old fy5-16-L1-02 (70 dB fans → 73 dB). Here the setting, numbers and format are different (64 dB dishwashers, MC error analysis, 67 dB), and fy5-15 is the earlier chapter, so it is acceptable. No change is needed.

## Checked
- Round-1 Blocking resolved: the stray fence after the L2-06 Kaava block is gone (solutions.md has an even fence count, 28). Capture L2-1280-8 shows a clean formula block and no literal backticks.
- Round-1 Blocking resolved: L1-07 now uses two 64 dB dishwashers (student 128 dB, correct 67,01 dB). Exactly one option is correct. The distractors (mean 64 dB, +3 dB per machine giving 70 dB, ten-fold intensity giving 74 dB) are wrong, and their feedback is right. It no longer copies the setting or answer of fy5-16-L1-02. No other FY5 chapter has this task (grep).
- Round-1 Polish done: L1-06 feedback no longer gives 120 dB, so L1-08 stays a task. L3-04 is now 3,2·10² m with the ±0,5 dB range 297–334 m and tolerance 0,05, and its c) explanation says "pienempi tai suurempi".
- Recomputed in one script: L1-08 120 dB; L2-05 6,025 dB (steps 6,1/5,8/6,1/6,1); L2-06 model 67,94 dB, difference 3,96 dB; L2-07 mean 4,0 dB → k = 2,51; L3-04 P = 0,405/0,380/0,428/0,366 W, mean 0,3945 W, r = 315 m; L3-05 84,93 dB, 44,6 m (sources alone 84,0 and 78,0 dB). All match answers.py and the solutions.
- The error directions are right: reflections raise the level and the gap grows with distance (L2-06); the saturated microphone reads low at 90 dB (L2-07).
- The assumptions are stated in the task (point source, no reflection or absorption) and are not contradicted by the explanations.
- Scope: intensity, level, summing intensities and 1/r² are inside the slot. There are no figures, and no "graph" kind is used. The plan 8/7/5 is met and the levels fit it.
