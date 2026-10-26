VERDICT: PASS
CONTENT-HASH: 35c7e28697874a1d
## Blocking

## Polish
- Sim canvas ("p (kPa)", "V (l)", "ΔU + W_k", "Q") and the DOM readout ("p = 200 kPa, ΔV = 0,00 l", "Q = 0 J, ΔU = 0 J", the "Lämpö Q = 500 J" slider label) stay plain interface text per NOTES.md §1 until the teacher decides; weakest spot of the print-quality rule, legible at 390 px.
- exp-1 Alkutila line (fy3-11-exp-exp-1-390-1.png): "lämpö Q = 500 J" and "paine p₂ = 100 kPa" still render as plain text in the capture (the table header "lämpö Q / ΔV (l)" is mixed italic and plain). If the capture is current, the generator still needs maths there. Also "paine p₂ = 100 kPa" sits beside a readout of p = 200 kPa, which can puzzle a student: say "paluupaine".
- inquiry.json pred-1: still lacks the cue "kaasu painaa mäntää voimalla pA" (round 1).
- inquiry.json exp-2 feedback: say once that the second law is an experience-based law, not something two runs prove (round 1).
- inquiry.json "suunnittele": heaviest step; workload at the upper limit of one lesson (round 1).

## Checked
- Diff is symbol-to-maths only: "$(V, p)$", "$(s, F)$", "$V$-akseli", "$1\,\text{TJ} = 10^{12}\,\text{J}$" in contribution, prior, feedbacks, howto, hints, prompts and exercise L2-01; no wording or number changed.
- No bare "(V, p)" left in inquiry.json, exercises.json or lesson.md prose (figure aria-label is plain by design).
- Answers unaffected (41,0 %, 450 J); feedback still repairs the misconceptions.
- Round-1 verdict stands: figures 1-4, staged example, experiments, exercise levels, exit ticket, Finnish, 360 px layout.
