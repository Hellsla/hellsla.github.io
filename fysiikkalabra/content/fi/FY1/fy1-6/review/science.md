VERDICT: PASS
CONTENT-HASH: b6c3eec0f963e833

## Blocking

## Polish
- lesson.md:170–171 — the km/h step still multiplies a bare number (`3{,}6 \cdot v`, `3{,}6 \cdot 14{,}715`) — substitute with units, e.g. `v = 14{,}715\,\text{m/s} = 14{,}715 \cdot 3{,}6\,\text{km/h} = 52{,}97\,\text{km/h}`.
- inquiry.json:335 (data, solution) — the error is written `\pm 0{,}1\,\text{m/s}` / `\pm 0{,}2\,\text{m/s}^2`; the teacher's rule writes an error as Δx — "virhe on noin $\Delta v \approx 0{,}1\,\text{m/s}$, joten $\Delta g \approx 0{,}2\,\text{m/s}^2$".
- lesson.md:185, 191 — "kevyt ja leveä kappale hidastuu eniten": a falling body in air still speeds up, only less — "ilma jarruttaa kevyttä ja leveää kappaletta eniten" / "sen nopeus kasvaa hitaimmin".
- lesson.md:191 — "$v = g\,t$ ei päde ilman ilmanvastuksen huomiotta jättämistä" is hard to parse — "$v = g\,t$ pätee vain, kun ilmanvastus voidaan jättää huomiotta".
- lessons/FY1/fy1-6/sim-spec.md — still writes "v/t" twice (not student-facing); align with the colon rule.

## Checked
- Round-1 blocking fixed: the sim readout now shows `$v : t = …$` and "`$v : t$` ei ole vielä määritelty"; calc box `v : t`; no `×`, `\times`, `δ` anywhere.
- lesson-answers.py recomputed independently: 9,81; 9,8; 11,1; 3,058; 14,715; 52,974 — all equal.
- Worked example: v = gt symbolic first, 14,715 → 15 m/s and 52,97 → 53 km/h (2 s.f. from 1,5 s, conversion from unrounded value), graph check real.
- Free-fall figure to scale (≈6,2 px/m, drops 4,9/19,6/44,1 m, 10 m bar = 62 px, arrows ∝ v); same-fall figure drop ratio 1 : 4, equal arrows; (t, v) figure points exact (6 px per m/s).
- Air model: dv/dt = g − (K/m)v², K = ½·1,2·0,47·π·0,10², v = v_T tanh(gt/v_T); at 4,0 s 0,1 kg → 10,5, 1 kg → 27,5, 10 kg → 37,5 m/s < gt = 39,2 m/s, as the model answer says.
- exp-1 (9,81, mistakes 19,6, 29,4), data task (slope 9,8; LS through origin 9,78; residuals ≤ 0,04 m/s; figure line and points to scale), siirto 11,1 → 11 m/s (29,4, 22,2, 3,7), check-2 3,06 s (11,0, 30, 0,327): correct.
- Experiments lock environment and the other parameters, vary only t or m_B; simState gives vA, vB.
- Every prediction's correct option and every feedback's physics right; Apollo 15 hammer–feather (Scott, 1971) correct.
- Scope: v = gt as a linear model, mass independence taken as an experimental result, no forces (FY1 scope).
- Hash identical at start and end.
