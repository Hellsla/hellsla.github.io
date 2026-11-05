VERDICT: PASS
CONTENT-HASH: 501fa6aaa0208bbd
Round: 1

## Blocking
(none)

## Polish
- exercises.json:151 (L1-09, statement 5) — the false statement uses the plain mean 9 °C; the lesson's warned mistake is the mass-weighted "ice as cold water" mean (here 13,6 °C). Its feedback says only that the mean "unohtaa sulamislämmön", but the plain mean also ignores the masses. Consider the 13,6 °C version, or add "ja massat" to the feedback.
- exercises.json:148 (L1-09, statement 4 feedback) — "Niin kauan kuin jäätä ja vettä on yhtä aikaa, lämpötila on 0 °C" could add "tasapainossa normaalipaineessa", as the lesson summary does (C-level, not required).
- lessons/FY3/fy3-14/answers.py — add L1-09 to the "multiple choice, no number" comments.

## Checked
- Recomputed: Q_v = 4190·0,25·18 = 18 855 J ≈ 19 kJ; Q_j = 334 000·0,080 = 26 720 J ≈ 27 kJ; Q_v < Q_j, so m_s = Q_v/s = 0,0565 kg ≈ 56 g melts, 24 g of ice remains, T = 0 °C. Statements 1, 3, 4 true; 2, 5 false; answer string matches.
- Boundary case per guardrail: Q_v < Q_j → ice left at 0 °C; no c_j term needed since ice is at 0 °C (stated).
- Statement 2 (mass comparison) and 5 (mean temperature) carry the chapter's own warned mistakes; each feedback gives the right reason.
- Notation Q_v = c_v m_v T_v, Q_j = s m_j, m_s as in the lesson; insulated vessel stated.
- Renders: measured at 390 px in Chromium with all feedback and the solution open: widest inline formula 263 px, within ~300 px. Physics judged from text.
- Hash identical at start and end.
