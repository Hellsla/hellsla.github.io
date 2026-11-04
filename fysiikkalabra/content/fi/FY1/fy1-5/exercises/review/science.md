VERDICT: PASS
CONTENT-HASH: 1b1e5178b3cffb72
Round 2: full review of the exercise set after the round-1 fixes (commit c18c6114); round 1 had no Blocking items.

## Blocking
(none)
## Polish
- exercises.json:279 (L3-05) — the graded number is $v = 3{,}0\,\text{m} : 0{,}010\,\text{s}$, one division, and the two scale lengths are not graded; as level 3 it is light. Consider grading the steepness ratio (rise 3,0 cm : run 0,10 cm = 30) or asking how many times steeper the line is than a walker's line at the same scale.
- solutions.md:193 vs :198 (L3-05) — the Periaate says the quotient "ei olisi mikään luku", the Vastaus says "nopeus olisi ääretön" (carried from round 1) — one wording, e.g. "osamäärä ei olisi mikään luku (nopeuden pitäisi olla ääretön)".
- solutions.md:198 (L3-05) — "300 m/s, kaksi merkitsevää numeroa" — write $3{,}0 \cdot 10^{2}\,\text{m/s}$ so the two digits show.
## Checked
- `python3 scripts/reviews.py hash fy1-5 --exercises` = 1b1e5178b3cffb72 at start and end.
- One independent script (python3 -I): all 19 numeric answers recomputed from the task text and data, every one within tolerance of exercises.json; answers.py output agrees.
- Round-1 Polish resolved: $x$, $x_0$ replaced by $s$, $s_0$ in L2-05, L3-04, L3-05 (text, data columns, solutions); L2-05 range now 17,3–18,7 m = tolerance 0,04; L3-04 now needs the model; L3-05 now open, not MC.
- L3-04 rewritten: data exactly on 3,0 m/s (0–10 s) then 1,0 m/s; s(5 s) = 15 m, s(35 s) = 30 + 1,0·25 = 55 m (35 s not in the table, so the model is needed); 40 m : 30 s = 1,33 → 1,3 m/s, tolerance 0,03 accepts 1,33; time weights 5 s and 25 s and the rejected mean 2,0 m/s correct; Järkevyys 15 + 25 = 40 m a real check.
- L3-05 rewritten: Δs = 3,0 m every 0,010 s, least squares 300 m/s; drawing 3,0 cm up, 0,010 s · 10 cm/s = 0,10 cm across; "not exactly vertical because Δt > 0, one position per instant" is right; constant speed stated in the task; 300 m/s plausible.
- L2-05 fit slope 1,403 m/s, intercept 1,21 m, s(12 s) = 18,04 m; solution's "18 m" now without the false "18,0".
- L1-07 kind "model": fine; physics unchanged.
- Scope stays at s = s₀ + vt; no duplicates; plan +3/+3/+2 kept.
