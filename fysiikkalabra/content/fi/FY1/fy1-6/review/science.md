VERDICT: PASS
CONTENT-HASH: a74dfb2e59b19197

## Blocking

## Polish
- lesson.md:192 (Tiivistelmä) — "tunnissa 3600 m = 3,6 km" reads as if an hour held 3600 m; say "nopeudella 1 m/s kertyy tunnissa 3600 m = 3,6 km".
- inquiry.json:335 (data, solution) — error still `\pm 0{,}1\,\text{m/s}` / `\pm 0{,}2\,\text{m/s}^2`; the teacher's Δx rule: "$\Delta v \approx 0{,}1\,\text{m/s}$, joten $\Delta g \approx 0{,}2\,\text{m/s}^2$".
- lesson.md:185, 191 — "kevyt ja leveä kappale hidastuu eniten": a body falling in air still speeds up — "sen nopeus kasvaa hitaimmin"; :191 "ei päde ilman … huomiotta jättämistä" → "pätee vain, kun ilmanvastus voidaan jättää huomiotta".
- inquiry.json:503 (check-2 solution) — two colons in one sentence ("m/s²: sijoitetaan …: v ="); style only.
- lessons/FY1/fy1-6/sim-spec.md — "v/t" (not student-facing); align with the colon rule.

## Checked
- Round-3 change, lesson.md:159: 1 m/s means 3600 m = 3,6 km per 3600 s, so 1 m/s = 3,6 km/h — correct reasoning, then substituted for the unit.
- lesson.md:166–173: v = 14,715 · 1 m/s = 14,715 · 3,6 km/h = 52,97 km/h; units carried (round-2 polish fixed); 53 km/h from the unrounded value.
- inquiry.json:486–487, 503 (check-2 hints, solution): 108 · 1000 m : 3600 s = 30,0 m/s, t = 30,0 m/s : 9,81 m/s² = 3,058 → 3,06 s; mistakes 11,0, 30, 0,327 unchanged.
- lesson-answers.py recomputed: 9,81; 9,8; 11,1; 3,058; 14,715; 52,974 — equal.
- Notation: \cdot, no ×/\times/δ in lesson, inquiry, exit ticket; sim readout `v : t`.
- Figures, air model (10,5 / 37,5 m/s at 4,0 s), experiments and predictions unchanged since round-2 PASS.
- Hash identical at start and end.
