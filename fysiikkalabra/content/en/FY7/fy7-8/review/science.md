VERDICT: PASS
CONTENT-HASH: 725adfdc8c3bfd9f

## Blocking

## Polish
- assets/sims/fy7/fy7-8/sim.js:134 — the bar label `$P_\text{perille}$` is hard-coded Finnish and shows on the en page (readout below says P_arriving) — route it through __() like the readout. (Owner rule: no Finnish visible in en.)
- content/en/FY7/fy7-8/inquiry.json:53 — pending text names "the part Core idea", but the en section is "Key idea" (lang/en.json) — say "Key idea".
- scripts/review_packet.py:68 (tooling) — exercise brief empty for en; see the exercise report.

## Checked
- Every number in lesson.md, inquiry.json and exit-ticket.json matches the reviewed Finnish; the only differences are SVG label coordinates moved for longer English labels.
- Transformer mechanism (shared changing flux, equal voltage per turn, DC gives zero after switching), power conservation, rms values, laminated core for eddy currents: correct in English.
- P_h = R I² = R P²/U², and the warning that the transmission voltage is not across the line resistance (drop RI) kept intact.
- Worked example recomputed: N1 = 1980, I1 = 81.82 A → 82 A, power check 9.0 MW.
- Predictions: one correct option each; model values 2000/1000/500 A and 24/6.0/1.5 MW at 100/200/400 kV with R = 0.040 Ω/km · 150 km = 6.0 Ω recomputed; sim screenshot (1.50 MW, 0.75 %, 198.5 MW, N2:N1 = 20) agrees.
- koe-1 locks P and l and varies U only.
- virhe: 2.7·10¹⁰ W, 27 kW distractor, RI = 3.0 kV recomputed; siirto 720 kW with mistakes 1 512 500 / 2.4 / 0.72 recomputed; tarkistus-2 0.2609 A, mistakes 5.0 / 95.83 A.
- Model answers and exit ticket (11.5 V; a third of the current → a ninth of the loss) match the theory.
- Hash identical at start and end.
