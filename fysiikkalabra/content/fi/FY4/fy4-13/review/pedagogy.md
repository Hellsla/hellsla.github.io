VERDICT: FAIL
CONTENT-HASH: d1d8ce15626f5d7b
## Blocking
- lesson.md:411 (Tiivistelmä) — a TAB replaced the backslash of \frac in all four formulas, so the page shows "a = fracm_2m_1+m_2 g" (capture stage-selita-390-4) — restore \frac{...}{...}.
- assets/sims/fy4/fy4-13 sim.js (force-diagram panels), inquiry.json exp-1 intro — at 390 px each diagram is ~25 px wide, arrows 10–35 px, labels ~9 px; the same at 1280 px (sim-1280). Exp-1 asks the student to watch how the lengths of \overline{T}_1 and \overline{G}_2 change, which a phone cannot show, and the diagrams are the lesson's core skill — scale each diagram to fill its panel (rectangle about a third of the panel width, labels at least 12 px) and keep the arrows to scale.
## Polish
- lesson.md Ydinajatus — the Miksi (why slower than free fall) is never stated outright; add: "a = m_2 g/(m_1+m_2) < g, koska paino kiihdyttää myös kärryä".
- lesson.md Esimerkki, stage "Kaava ratkaistuna" — jumps from two equations to a; add the line "yhteenlasku: m_2 g = (m_1+m_2)a".
- Theory and example figures at 390 px (fig-2, fig-3) — "voimakuvio: kärry" and the subscripts are about 9 px; stack the two panels on a phone or enlarge labels.
- Sim canvas, exp-2 at 390 px — "Tilannekuva" overlaps the ceiling beam, and the Tilanne select is clipped at the right (capture is 316 px wide).
- inquiry.json hook — the Pohdinta question (what pulls the cart) differs from the Miksi; fine, but link them in the reflect prompt.
## Checked
- Opening illustration matches the Miksi (cart, pulley, hanging weight, FY3-level detail); labels in figures and sim are LaTeX.
- Chapter names in prior, not ids; learn goals parallel -maan/-mään.
- Force diagrams: error, draw (check-3), equations; diagram before equations in every solution; the virhe description lists arrows, not the error.
- Prediction 1 can be refuted by exp-1; gating and feedback repair the misconception; workload one lesson with optional items.
- Example has eight stages with solution rules met; checks have misconception distractors; exit ticket tests the core idea.
- Layout 360/768/1280 tests pass; captures at 1280 show a single reading column.
