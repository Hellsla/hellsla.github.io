VERDICT: DONE

Fix round 1 for the fy7-15 exercises.

## Blocking
- pedagogy, fy7-15-L1-04 — the lesson works air to water (53,1°), so the task now uses acrylic instead: "Auringonvalo heijastuu akryylilevyn pinnasta. Akryylin taitekerroin on $1{,}49$ ja ilman $1{,}00$." The answer is 56.1328 (α_B = tan⁻¹ 1,49 = 56,13° → 56,1°), and the 0,02 tolerance is unchanged. The solutions.md L1-04 Annettu, Periaate, Sijoitus, Vastaus and the Järkevyys check are updated: taitekulma 33,87°, and 1,00 · sin 56,13° = 0,830 = 1,49 · sin 33,87°. lessons/FY7/fy7-15/answers.py now computes atan(1.49).
- The L1-05 Järkevyys compared with "veden 53,1°". It now compares with "akryylin 56,1°".

## Polish applied
- science, answers.py:14 — the comment now reads "67,548° -> 67,5°".

## Not done (optional)
- L2-01 variation, adding a qualitative item, the L1-03 rewrite, the L2-02 wording, the L3-01 full stop.

`python3 scripts/check_lesson.py fy7-15`: all ok.
