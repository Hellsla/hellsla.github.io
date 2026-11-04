VERDICT: FAIL
CONTENT-HASH: ae1673190c4f6b4e

## Blocking
- exercises/exercises.json:234 — fy5-16-L2-07 (new) is a near-duplicate across chapters. It uses the same student mistake as fy5-15-L1-07 (decibels added: 70 + 70 = 140 dB) and the fy5-15 lesson's misconception, and its calculation is the same as fy5-15-L2-02: two sources 3 dB apart give the higher level +1,76 dB. The later chapter's task must go (A). — replace it with an error-analysis task on fy5-16 content. For example: a student halves the allowed time for every 6 dB (or 10 dB), or divides t₀ by n instead of 2ⁿ, at 94 dB; the task asks for the error and the correct time (1,0 h). Change the solution and answers.py to match.
- exercises/exercises.json:192 — fy5-16-L2-06 b asks why low sound is attenuated less, "aallonpituuden avulla", and the model answer (solutions.md:166) compares λ = 2,7 m with "esteen korkeus", but the task gives no barrier size. The rubric asks for something the task does not give (B). — add the barrier height to the task text, e.g. "Este on 3,0 m korkea".

## Polish
- exercises/solutions.md:135, :154 — the heading "Kuvaajan lukeminen" is used for values from a table (L2-05, L2-06), and no graph is shown. Use "Taulukon lukeminen".
- exercises/exercises.json:316 — fy5-16-L3-05 c: say that the listener keeps the earplugs at 16 m. The solution assumes it, and without plugs the dose would be 300 %.
- fy5-16-L2-05 repeats the method of the existing L2-04 (T from a partial decay at a steady rate) twice. You could ask for T from a line fitted through all the rows.

## Checked
- Recomputed all 8 new answers in one script: L1-07 27; L2-05 T 1,51 s → 0,599 s, 60,3 %; L2-06 25,2 − 13,4 = 11,8 dB, λ 2,74 m and 0,086 m; L2-07 84,76 → 85; L3-04 D = 3,375, ΔL = 5,26 dB, with the enclosure D = 1,57 (2,0 dB); L3-05 100 dB, 1,59 h, 190 %, 47 %. All match answers.py and the solutions.
- L1-06, L1-08 MC: exactly one correct option. The distractor feedback is right (the reverberation time does not depend on the initial level; the reversed chain describes a microphone).
- Scope: noise dose, reverberation, barrier diffraction and loudspeaker principle are all in the slot. There are no figures, so no values read from figures and no "graph" kinds.
- fy5-17: no overlap.; plan 8/7/5 met.
