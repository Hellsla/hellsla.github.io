VERDICT: PASS
CONTENT-HASH: 4ef41bcb63136457

## Blocking

## Polish
- inquiry.json ennuste-2, the "Ensimmäisen mittauspisteen kohdalle" feedback — it uses 0,79 g/ml and gets about 63 g, while everywhere else the lesson uses 0,80 g/ml and 61 g. 0,79 is the least-squares slope (LS b = 62,3 g), so the numbers are not wrong. Use 0,80 g/ml (about 62 g) or write "noin 61–63 g".
- lesson.md, the slope figure's aria-label — the screen-reader text still says "k = Δy/Δx = 0,5". Write "Δy : Δx" to match the notation rule.
- ennuste-2 extends the line to V = 0, outside the measured 20–120 ml. The physical reason (the empty glass) makes this justified (a C finding). One clause, "suoraa jatketaan mitatun alueen ulkopuolelle", would tie it to the new extrapolation sentence in Lineaarinen malli.

## Checked
- The guardrail wordings are in place and consistent across the Miksi question, the theory, the kertaus feedback, the koe-3 feedback, the misconception and the Tiivistelmä:
  - "Todellisissa mittaussarjoissa … eivät yleensä sijaitse täsmälleen samalla suoralla", and no "koskaan" or "aina";
  - a fitted line may pass through a point;
  - the slope is read from two distant points on the fitted line;
  - extrapolation is only an estimate;
  - the line through the origin has a physical reason ("lähti paikasta s = 0 hetkellä t = 0").
- The heating model now states its condition (small heat losses), and the walk (tarkistus-2) and the plant (siirto) state the constant-rate assumption beyond the measured range.
- One script recomputed:
  - dataset 1: d = 0,76 / 0,12 / 0,44 m at k = 0,30 / 0,50 / 0,60 m/s; the best k through the origin is 0,49 m/s; consecutive slopes 0,2/0,8/0,5/0,3/0,5 m/s; s : t = 0,60/0,40/0,53 m/s;
  - dataset 2: d(b = 0, k = 0,80) = 61 g; best b = 61,3 g with d = 1,2 g;
  - dataset 3 (b = 80 °C): d_min = 5,80 °C at k = −1,90 °C/min; the residual signs are +, −, −, −, −, +, +, exactly the curvature the koe-3 answer names.
- Worked example: k = 8,0 °C/min, b = 20 °C, t = 2,5 min, symbolic first. The residuals are at most 0,8 °C, three on each side, and the LS fit (7,85 °C/min) agrees.
- Other answers: kuvaajasta 15 km/h (mistakes 16,7 and 0,067); siirto 20 vrk (25, 16); tarkistus-2 7,0 h (8,3, 5,5); exit ticket k = 1,5 m/s, b = 2,0 m and b = empty glass, not proportional.
- Every choice item has exactly one correct option, and every distractor's feedback is right. koe-1 and koe-3 lock b, koe-2 locks k, and simState gives d.
- The lint's FAIL in the check list is stale: lint_lesson.py now reports 0 errors and 0 warnings.
- Hash identical at start and end.
