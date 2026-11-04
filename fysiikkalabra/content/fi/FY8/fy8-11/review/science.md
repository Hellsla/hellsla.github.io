VERDICT: PASS
CONTENT-HASH: 8286157c5be4079d

## Blocking

## Polish
- lessons/FY8/fy8-11/lesson-answers.py:81 — the comment still says "E_s/A"; the lesson, the figures and inquiry.json now use $E_\text{B}$. Change the comment to "E_B/A".
- lesson.md:569 — the operating licence date is confirmed only by secondary sources (GreekReporter, Credence Research: 22.10.2026; STUK statement 4.8.2026; application December 2021, licence to the end of 2070). yle.fi could not be reached from this session. The teacher should check it once against valtioneuvosto.fi.
- lesson.md:569 — "Posiva rakentaa Onkaloa" is still true, but now that the licence has been granted, "on rakentanut" would read better (taste).

## Checked
- Round-1 blocker 1 fixed: lesson.md:569 now says STUK's favourable statement came in August 2026, the government granted the operating licence in October 2026 to the end of 2070, and disposal can begin after STUK's inspection. This matches the search results. The summary (lesson.md:672, "on tarkoitus loppusijoittaa") stays consistent.
- Round-1 blocker 2 fixed: lesson.md:610 and the keskustelu model answer in inquiry.json now say "ydinaseissa käytetään noin 90 %:iin rikastettua uraania". This is correct and contrasted with 3–5 %. The criterion (rikastusaste tai hidastin) still fits.
- The symbol $E_\text{B}$ is used consistently in the lesson text (line 101), the sidosenergia figure label, the sidosenergia-luku figure (figures.py:52, 73), the kertaus feedback and the Tarkista 2 solution. No $E_\text{s}$ is left in the content.
- Polish items from round 1 were applied: the hook and the answer say 3,4 t, and "työnnetään syvemmälle".
- Recomputed with my own script: example Q = 173,28 MeV, 0,079 %; Etsi virhe −0,8226 u, −766 MeV; D–T 17,59 MeV, 3,52 vs 0,847 MeV per nucleon (×4,2); 1 g gives 2,56·10^21 nuclei, 82 GJ, 3,42 t of coal; ITER 1,773·10^20 1/s, 1,48 mg/s; hook 14 400 t/d; 1000·1,04^30 = 3243, 176 generations; decay heat 258 MW; 12/820 = 1,5 %; total 4394 MW.
- Sim numbers rerun with lesson-answers.py: 39 387 / 934 / 7 and 1000 / 1437 / 1987 / 3264. These match ennuste-1, ennuste-2, johtopäätös and sim-spec.
- Tarkista 2: 236·0,9 ≈ 210 MeV, with mistakes 0,9 and 106. This is unchanged and correct.
- Hash 8286157c5be4079d at the start and at the end.
