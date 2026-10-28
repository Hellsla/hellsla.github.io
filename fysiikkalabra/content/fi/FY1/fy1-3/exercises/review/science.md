VERDICT: FAIL
CONTENT-HASH: 3f0dfa7324a244fc

## Blocking
- exercises/exercises.json fy1-3-L2-01 (tolerance 0.02) — the lesson rounds Δt to one figure (0,09 s) and ε to the figures of Δt, giving 5 %, which is 3,6 % off 4.83 and rejected — raise tolerance to 0.04 and in solutions.md:58 state 5 % as the strictly rounded answer (4,8 % unrounded) instead of "kaksi merkitsevää numeroa".

## Polish
- solutions.md:68 (L2-02) — "kolmen lukeman keskiarvo kantaa yhden numeron lisää" is not a sound rule; justify 10,7 mm by the millimetre readings, or give 11 mm.
- solutions.md L1-05 Järkevyys — "Virhe-arvio ei voi olla asteikkoväliä suurempi" is too absolute (a hard-to-read scale can need more); say "on tavallisesti enintään".

## Checked
- All 12 answers recomputed independently; all match answers.py within tolerance.
- No × or ÷; products in \cdot; divisions as \frac; error symbols Δx, Δt_sys, ΔL_sys.
- L3-01 signs (late start shortens, late stop lengthens; −0,06 s); L3-02 2,0 µm and the 100 µm paper check; L3-03 0,26 cm with 0,025 cm scatter.
- Every solution has the seven parts, symbolic before numbers, conversions stated (L2-02, L2-03, L3-02).
