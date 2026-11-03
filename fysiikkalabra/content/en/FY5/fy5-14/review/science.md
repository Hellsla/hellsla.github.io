VERDICT: PASS
CONTENT-HASH: 0f98c20c555bfd1e

## Blocking
(none)

## Polish
- Notation (C, not a finding): $f_\text{h}$, $T_\text{h}$ (beats) and $v_\text{h}$ (listener) keep the Finnish subscript, because the figures translate \text{h} through one key and use it for both meanings; the text now says once, after $T_\text{h}$, where the letter comes from. Physics unaffected.

## Checked
- lesson.md, inquiry.json, exit-ticket.json and meta.json against the Finnish PASS version: every formula identical (check_i18n: no fy5-14 lines), every number identical by script (decimal point), all steps, hints, mistakes, feedback and model answers kept.
- Recomputed: train 341.10 / 285.78 Hz, drop 55.32 Hz; model values 444 / 571 Hz (source), 440 / 520 Hz (listener), λ 0.765 / 0.595 m; moped 659 Hz; buzzer 2076.8 Hz; microphones 342.86 m/s; beats 4.0 Hz.
- Physics terms: longitudinal wave, compression, rarefaction, fundamental frequency, overtone, partial, harmonic series, beats, beat frequency, Doppler effect, wavefront; conditions (still air, motion on the line, only one moves, source slower than sound) kept.
- Each prediction keeps one correct option; feedback physics matches the Finnish.
- Fixed in translation: chapter name *Sound intensity* (was "Loudness of sound"); experiment names "situation" (was Finnish "tilanne" in the initial-state box); two ambiguous pronouns in the cyclist check; "Both hear an equally high frequency … relative speed".
- Sim labels lang/en.json sims.fy5-14 match fi; test_sims.py fy5-14 PASS.
