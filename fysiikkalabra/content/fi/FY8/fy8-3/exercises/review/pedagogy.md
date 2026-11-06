VERDICT: PASS
CONTENT-HASH: aa7434ae1159c8f8

## Blocking
(none)

## Polish
- exercises.json fy8-3-L2-08, options — the correct option is the only one that says "pienenee"; the other three say "kasvaa" or "ei muutu", and "1,7-kertaiseksi" is the reciprocal of "0,58". A student can pick it by elimination. Fix: make one distractor a shrinking one, e.g. "Aallonpituus pienenee noin 0,44-kertaiseksi" (0,378 eV : 0,85 eV, the single-level mistake with the direction right), and drop the reciprocal pair.
- solutions.md fy8-3-L2-08 — "Paschenin sarjan" is named only in the solution; the brief's table has Paschen, so it is fine. Give the series' name already in the stem or leave it out.
- exercises.json fy8-3-L2-08 stem — "Miten fotonin aallonpituus muuttuu" has no stated reference direction. Say "Miten siirtymän 6 -> 3 fotonin aallonpituus on verrattuna siirtymän 4 -> 3 fotonin aallonpituuteen?"

## Checked
- New task fy8-3-L2-08 (prediction of change, type 6): the situation and then one question; E4-E3 = 0,661 eV, E6-E3 = 1,133 eV, ratio 0,583 all verified.
- Distractors match the chapter's warned mistake (photon energy from one level, |E4| = 0,85 eV -> 0,38 eV gives 2,25) and the inverse reading (1,7). Feedback names each error.
- The correct feedback gives the energies and the ratio but no extra reasoning stage. The ratio route (h and c cancel) is explained step by step in the solution.
- Within the chapter: E_n and lambda = hc/dE only.
Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders were opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
