VERDICT: PASS
CONTENT-HASH: 9cfa5cdd244942ed
Mode: delta, round 1 (new task fy1-5-L2-08, graph-choice figures pick-away/back/distance/vt; paragraph splits in L2-02, L2-07, L3-01/02/04/05)

## Blocking
(none)

## Polish
- [Minor] fy1-5-L2-08 at 1280 px — in the two-column option grid the opened feedback sits under the chosen option, so the neighbouring card is stretched to the same height and shows a large empty area — acceptable, but the feedback could span both columns.
- [Minor] fy1-5-L2-08 — option letters appear in the order D, A, C, B (fixed order in both languages); an unordered A-D reads oddly — keep the letters in reading order if the shuffle allows.

## Checked
- Rendered live with Playwright (chromium, built preview/en/fy1-5.html) at 390 px and 1280 px: task fy1-5-L2-08 before answering and with each of the four options chosen (feedback open). Opened en-390 and 1280 and fi-easy-390 captures of the opened states at readable size.
- English words in the figures: alt texts translated (figures.json), axis labels are LaTeX (t (s), s (m), Δs (m), v (m/s)), tick decimals use a point (0.5, 1.0, 1.5). Question, option labels and feedback are in the page language.
- Measured by script at both widths: no element of the card extends past the card edge, no horizontal page scroll (scrollWidth = viewport), feedback stays inside the exercise card at 390 and 1280.
- Figures: all four share axes and scale (t 0–10 s, s 0–12 m); the (t, v) and Δs options are distinguished by their axis labels; one line colour, no data/model confusion.
- From the diff and text only (not from captures): paragraph splits in L2-02, L2-07, L3-01, L3-02, L3-04, L3-05; solutions.md for L2-08. The existing 1280 exercise captures in review/shots predate or omit the new task, so they were not used for it.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
