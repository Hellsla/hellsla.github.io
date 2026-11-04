VERDICT: FAIL
CONTENT-HASH: 76d62114ae966053

## Blocking
- exercises/exercises.json:146 + solutions.md:106 (fy5-11-L2-05) — A: the new offset mechanism does not produce the offset. The clap and its echo are on the same recording and t is read from the waveform between them, so a start delay of the recording ("äänityksen aloitusviive", Järkevyys) cancels in every single t; it cannot make each t 0,040 s too long. The data (t₀ ≈ +0,040 s) then have no physical cause, and the explanation of the data error does not give its direction. — Use a mechanism that really adds a constant positive delay, e.g. the phone itself emits a beep and its app times from the beep command to the detected echo; the phone's audio output latency (unknown but constant, tens of ms) makes every t too long by the same amount. Rewrite the task's second paragraph and the solution's Annettu/Periaate/Järkevyys to that cause ("puhelimen äänen ulostulon viive t₀").

## Polish
- solutions.md L2-06 c) — "voimakkaasti, kun b/λ on enintään noin 2" fits the table, but the lesson says strong bending when b is about λ or smaller; consider "noin 1–2 tai pienempi".
- Long inline formulas in solutions render as empty boxes in the 1280 px captures in old and new tasks alike (site-wide, other thread).

## Checked
- Changes since round 1 diffed (exercises.json, solutions.md); answers.py and all task data unchanged; every new answer recomputed again in one script: L1-08 48 ms, L2-05 342,9 m/s (residuals ≤ 0,3 ms), L2-06 8,0, L2-07 32°, L3-04 35,1°, L3-05 200; all agree.
- L2-06 c): ratios 0,5; 1,0; 2,0; 4,0; 8,0 match the five observations; rule monotone and right.
- L3-04 c): the nearest-point note is right (first echo from the nearest bottom point → vertical model underestimates the depth there); it qualifies, not contradicts, the stated vertical-pulse assumption, which still holds for a)–b).
- L1-07: only distractor wording changed; one correct option, feedbacks right.
- L1-08 Järkevyys: 1500/343 = 4,4, right.
- Typographic quotes in L2-07 only; no physics change.
