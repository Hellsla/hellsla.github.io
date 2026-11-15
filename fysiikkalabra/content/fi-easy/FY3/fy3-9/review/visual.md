VERDICT: FAIL
CONTENT-HASH: 7bdf6d7731bbc6de

## Blocking
- [Major] inquiry.json and exit-ticket.json, edited lines (open-ennusta-1280-1, open-exit-1280, open-tarkista-1280-2) — the delta converted kPa, Pa, N and kPa·ml to LaTeX but left every "ml" (and "l") volume plain in the same sentences: "Suljetussa sylinterissä on 50 ml ilmaa. Ilman paine on $100\,\text{kPa}$", "25 ml → $200\,\text{kPa}$", "40 ml ilmaa $100\,\text{kPa}$:n paineessa". The page shows sans-serif "50 ml" next to serif maths "100 kPa" and the choices "50 ml, koska…" — teacher rule 2026-11-01: every number with its unit in LaTeX, a plain one in edited text is Major — set every number+ml (about 40 places: ennusta, tutki, tarkista, exit ticket, solutions) as $50\,\text{ml}$ (litre as in the existing $\textsf{l}$ style), then re-run `lint_lesson.py`.

## Polish
- [Minor] lesson.md line 256 "10, 15, 20, 30 ja 40 ml" — same plain-unit form in untouched text; fix together.

## Checked
- Delta: open-ennusta-1280-1 (predictions with new $\text{kPa}$ typography: spacing and upright units good, mix with plain ml visible), open-tarkista-1280-2 (Laskutehtävä, hints, solution: formulas aligned, kulmakerroin $3{,}6\,\text{kPa}\cdot\textsf{l}$ reads well), open-exit-1280 (Pohdintatehtävä answer chain aligned).
- Diff read in full: only unit/number typesetting, no meaning change; layout survived, no overflow.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
