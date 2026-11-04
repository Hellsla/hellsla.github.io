VERDICT: FAIL
CONTENT-HASH: da8b5996f6fae213

## Blocking
- [Major] lesson.md:52-55 (section "Valo etenee säteinä", the three-angle list) — the list has no blank line before it, so it renders as one run-in paragraph: "Kulmia on kolme: – Tulevan säteen … α1. – Heijastuneen … β. – Taittuneen … α2." (seen in theory-1280-1, and the built HTML has no <ul>; the Tiivistelmä list renders correctly) — the three angles are the key vocabulary of the chapter and weak readers lose the parallel structure; stray dashes look like a defect — insert a blank line after "Kulmia on kolme:".

## Polish
- [Minor] inquiry.json simulaatio howto: "Lukemista näet kulmat…" -> "Lukemissa näet kulmat…" (carried over from the earlier report; not re-verified in this round).
- [Minor] Worked example "Sijoitus" (example-390): the aligned lines are centred instead of aligned at "="; readable, no overflow at 340 px.

## Checked
- Hash at start and end: da8b5996f6fae213. Window-reflection paragraph (theory-1280-3): clause no longer duplicated, reads correctly.
- Contact sheet 1; fig-5, fig-7, fig-9, fig-11, fig-13 (via theory-1280-1..5: interface, wavefronts, depth, graph, scene); top-390, sim-1280, example-390-1/2, lab-1280-1, open-exercises-1280-1, open-tarkista-1280-1.
- check_layout.py fy7-10 --width 340: OK in fi, en and fi-easy.
- Figures: labels all Finnish and LaTeX, ray colour consistent, graph axes with units, legend labels clear, no clipping.
- Not opened individually: hero/scene at 390, exercise levels 2-3, exit ticket.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
