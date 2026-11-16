VERDICT: PASS
CONTENT-HASH: 632e5672772dd3f3
SCOPE: delta added-exercise from c96bc3211eef95f8 base abdc9e095e4f

## Blocking

## Polish

## Checked
- The hash was the same at the start and at the end. Round 2, a delta review of the added exercise L2-10 only. `git diff 09d57eb5ac..HEAD` changes the task text c), the solution's Vastaus (now in paragraphs) and Järkevyys, and adds two checked lines to answers.py.
- Round-1 Blocking 1 is fixed. The task now asks for the 8-hour case ("jos melu kestää koko kahdeksan tunnin työpäivän"). The solution says that the three values are 8-hour exposure levels, which the additions confirm. For a whole day at 94 dB the level is 94 dB(A), 7 dB over 87 dB(A), so the protectors must attenuate at least 7 dB (the limit is assessed inside the protector). For 1 h with the rest of the day quiet, L_8h = 94 + 10 lg(1/8) = 84,97 dB(A), which is 85 dB(A): the upper action value (protectors compulsory) and below the limit. This is consistent, and the answers.py assert computes the same.
- Round-1 Blocking 2 is fixed. The impulsive-noise sentence is now the source's own words ("yksittäinenkin riittävän kova meluhuippu voi olla kuulolle vaarallinen").
- Round-1 Polish is settled by the additions. The 85 dB(A) row requires the areas to be marked, and the 80 dB(A) row requires informing workers about the risks, so "alueet … merkittävä" and "tiedottamisen" are supported.
- Recomputed: 10^0,9 = 7,943, so t₂ = 8 h/7,943 = 1,007 h, which is 1,0 h. answers.py prints 1.0. 10^0,3 = 1,995. The values 80–87 lie within 7 dB.
- The time is still called a reference value and not a safe time.
