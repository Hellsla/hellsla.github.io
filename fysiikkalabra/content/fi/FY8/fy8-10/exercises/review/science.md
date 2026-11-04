VERDICT: FAIL
CONTENT-HASH: b4b0be010b9da758

## Blocking
- exercises.json:235, 240, 245 and solutions.md:134 fy8-10-L2-07 — **A**: "Rauta-56:n sidosenergia nukleonia kohti on suurin kaikista ytimistä" and "Raudalla nukleonit ovat tiiviimmin sidottuja kuin muilla" are wrong. Ni-62 is higher: 8,7946 MeV vs Fe-56 8,7904 MeV. The set shows this itself, since L2-05 (answer: Ni-62 is the most tightly bound) and L2-01 (Fe-56 8,790 MeV) prove it, and the lesson and L1-08 say "rauta-56 ja nikkeli-62". Fix: "Rauta-56 on sidosenergiakäyrän huipulla nikkeli-62:n kanssa (noin 8,8 MeV nukleonia kohti)", and in the correct option and the model answer "Raudalla nukleonit ovat lähes yhtä tiiviisti sidottuja kuin huipun tiiviimmin sidotuilla ytimillä …".
- same task — **B**: "ei saada energiaa … ei yhdistämällä" holds only for joining iron nuclei to each other or splitting them. Fe-56 + He-4 → Ni-60 releases Q = +6,3 MeV. Fix: say "yhdistämällä rautaytimiä toisiinsa tai halkaisemalla niitä" in the stem, and in solutions.md:134 change "yhdistettäisiin toiseen ytimeen" to "toiseen rautaytimeen".

## Polish
- exercises.json:85 fy8-10-L1-08 — the last distractor's feedback states the same sentence twice and does not answer "kevyimpiä mahdollisia ytimiä". Replace the second sentence with a correction of that claim.
- solutions.md:166 fy8-10-L3-04 — the rounding argument "noin sadasosiin" understates it: ±0,0005 MeV × (141 + 92 + 235) gives up to about 0,2 MeV. Say "enintään noin 0,2 MeV"; the actual difference is 0,01 MeV.
- fy8-10-L3-04 / plan — the plan asks for Q three ways (masses, binding energies, read from the graph), and for a `fy8-10/kayra-points` graph-reading task at level 2; neither the graph reading nor the graph task is in the set.
- solutions.md:176 fy8-10-L3-05 d) — only the core hydrogen fuses, so "3,5 % of all hydrogen" overstates the margin. Add "oletetaan, että koko vety on käytettävissä" or note the core limit.
- exercises.json fy8-10-L2-07 vs L1-08 — two distractors (massavaje pienin, koko E_B suurin) repeat L1-08 almost word for word; vary one.

## Checked
- All 18 numeric answers recomputed independently in one script: all match within tolerance.
- L2-05 all eight Δm, E_B, E_B/A and the order match; AME2020 masses right.
- L2-06 student's 30,46 MeV reproduced; gap = 3 m_e = 1,53 MeV.
- L3-04 Q 173,29 (masses) / 173,28 MeV (table, consistent with its masses); 7,11·10¹⁰ J; coal check right.
- L3-05 3,51·10¹⁸ kg/a, f 0,712 %, 4,93·10²⁰ kg/a, 3,5 %; atomic masses valid for 4 ¹H → ⁴He, neutrinos stated.
- L1-06, L1-07 correct.
