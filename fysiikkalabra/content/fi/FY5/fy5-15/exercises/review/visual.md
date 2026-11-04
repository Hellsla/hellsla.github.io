VERDICT: FAIL
CONTENT-HASH: beb42d2e273c0e91

## Blocking
- [Major] fy5-15 solutions.md "## fy5-15-L2-06", the line after the Kaava display block (line 191) — a stray closing code fence (a bare triple backtick after the closed latex block) renders as a visible "```" row under the formula in the open solution (capture open-exercises-L2-1280-8). Fix: delete that one stray line so only the single closing fence of the latex block remains.

## Polish
- [Minor] fy5-15-L2-06 Kaava — "L_malli = L_1 - 10 dB * lg (r_2/r_1)^2" reads as (lg x)^2 at a glance; write "\lg\left(\dfrac{r_2}{r_1}\right)^{2}" with the square inside, or "20\,\text{dB} \cdot \lg \dfrac{r_2}{r_1}".
- [Minor] fy5-15-L2-07 Sijoitus — "k = 10^{4,0/10}" drops the dB units; write 10^{4,0 dB/(10 dB)}.
- [Minor] fy5-15-L1-07 — the equal-sources dB-sum idea also appears in old fy5-16-L1-02 (two identical fans, 73 dB); acceptable because fy5-15 is the earlier chapter.

## Checked
- Numbers verified: L1-08 120 dB; L2-05 24,1 dB / 4 = 6,03 dB; L2-06 model 67,94 dB, difference 3,96 dB; L2-07 mean error 4,0 dB, k = 2,51; L3-04 powers 0,405/0,380/0,428/0,366 W, mean 0,3945 W, r = 315 m; L3-05 I = 3,11e-4 W/m2, 84,9 dB, r = 44,6 m.
- Error directions are right: reflections raise the level at 8 m (L2-06); a saturated microphone reads low at 90 dB (L2-07); air absorption lowers the real level at long range (L3-04).
- Captures: contact sheets 6-7 plus L2-1280-8 and -9 at full size: layout otherwise clean.
- Overlap judged: 15-L1-07 (70+70 dB) vs 16-L2-07 (83+80 dB): the later chapter's task (16-L2-07) is the Blocking one, see fy5-16.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
