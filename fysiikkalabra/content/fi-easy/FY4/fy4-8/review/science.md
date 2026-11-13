VERDICT: PASS
CONTENT-HASH: 5516d2430f384ce9

## Blocking
None.

## Polish
1. lesson.md, Tiivistelmä bullets 2 and 3: W is the total work in one and the other forces' work in the next; each says so in words, but adding "(kokonaistyö)" / "(muiden voimien kuin painon työ)" after the formulas would make it unmissable.
2. lesson.md, Esimerkki: the data keep v_1 = 0, v_2 = 7,6 m/s beside E_k0/E_k (as the brief allows); one clause "loppunopeus v_2 on lopputilan nopeus" would tie the indices together.
3. Not student-facing: assets/sims/fy4/fy4-8/sim.js comments (lines 8, 11, 154) and lessons/FY4/fy4-8/answers.py, lesson-answers.py comments still say W_muut, W_kok, E_mek,1; content/en/FY4/fy4-8/figures.json keeps an unused "muut": "other" entry.
4. kortit/fy4.json fy4-energiaperiaate: the definition says "ei-konservatiivisten voimien työ", the lesson "muiden voimien kuin painon"; same thing in FY4 (weight is the only conservative force) but the card could use the lesson's words.

## Checked
- Formula tables: W = Fs (F the component along the motion, constant force, one direction, stated), E_k0 + W = E_k (W total work), E_p0 + E_k0 + W = E_p + E_k (W other forces' work, the switch is said explicitly), conservation law with W = 0: all equal MAFY with conditions; symbols and units defined where they first appear.
- Worked example, inquiry feedback (mgh + W = E_k, ΔE_mek = W), sim labels (lang sims.fy4-8: W, E_mek0), figures (palkit, palkit-asteikko), exit ticket, kortit: same symbols; no leftover F_∥, W_kok, W_muut, E_k,1, E_mek,1 in student-facing text.
- Numbers recomputed (own script): −645 J, 9,9 m/s, 41 %, 27 N, 314 N; lesson-answers.py unchanged; lint has no physics warnings; fi, fi-easy and en say the same.
