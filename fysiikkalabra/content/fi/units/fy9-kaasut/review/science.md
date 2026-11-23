VERDICT: FAIL
CONTENT-HASH: 9aa2efef9e81542c
SCOPE: full; the three new ```pysahdy boxes judged first, then unit.md, inquiry.json, teacher.md and the Sovella set s1–s9 with answers.py. Hash identical at start and end. Language: fi.

## Blocking
1. **A (definition), unit.md, second pysahdy box (Kaasun tila).** The question "Miksi absoluuttinen nollapiste on vain mallin ennuste?" says that absolute zero itself is only a model prediction. That is wrong. Absolute zero is the lowest possible temperature and the zero of the kelvin scale, whatever model is used. What the gas model predicts is that the gas's pressure or volume would fall to zero there, and the extrapolated value is the estimate. The box's own answer is about the extrapolation, so the question and the answer do not match, and a student is left thinking absolute zero is hypothetical. Fix: e.g. "Miksi suoran jatkaminen nollapaineeseen on vain kaasumallin ennuste?" and keep the answer as it is (optionally add: "Absoluuttinen nollapiste on silti todellinen alin mahdollinen lämpötila.").

## Polish
- The same box sits between "Kelvinlämpötila on" and the formula $T = \theta + 273{,}15\,\text{K}$, so it splits the sentence. It also answers a point that the paragraph under the formula only introduces afterwards. Move it after that paragraph (ends "…tiivistyy nesteeksi ennen sitä.").
- The third box repeats the sentence right after it. The physics is right (a cyclic engine, $W = Q_1 - Q_2 < Q_1$), but the repeat is redundant.
- s5 b): "Lämpötilan ja mittarin virheet ovat kumpikin noin 5–7 %". When recomputed they are 4.6 % (30 °C → 26.6 g/mol) and 5.0 % (200 kPa → 26.7 g/mol). "noin 5 %" fits.

## Checked
- Box 1: the gauge shows overpressure; $101 + 230 = 331\,\text{kPa}$ is correct and consistent with the text. Box 3: correct by the guardrail (a heat engine in a cycle).
- New raster figures: kone.webp has arrow widths of 274 : 179 : 92 px, which is 1000 : 653 : 336, so the "mittakaavassa" claim holds (1000/650/350 J). The hero image matches its alt text and makes no physics claim.
- One script recomputes every number from the task data and compares it with answers.py: the tyre example (285.8 kPa, gauge 185 kPa; teacher.md 14 % / 20 %, −25 °C → 34.3 ml); inquiry aineisto 0.0602 mol (B 0.0361), luukku 17.66 kN (54.0 with total pressure), pumppu 151.5 kPa, pallo 832 kg (3451/2619), mäntä 750 J, tarkistus-2 58.3 kW, the pump 10.3 m limit, the celsius 114 kPa and lt-4 1.07; s1 562.1 kPa / 21.19 kJ / 25.0 and 3.81 kJ / 650 kPa / 501 kPa / 0.42 m; s2 2183 mol, 34.92 kg, 485 kW, 174.6 kW, 84 %, waste 77.6 kW; s3 LSQ k 0.1351 and −279.1 °C, read −279.3, extreme lines pass every ±0.3 ml range (−264.5 / −294.4), 1.646 mmol, point 1.68 mmol, shift 11 K; s4 6.0 % (below Carnot 8.3 %); s5 25.45 g/mol, 17.2 with 311 kPa; s6 11.21 / 18.69 / 37.4 kPa, safety 5.35 / 3.21 / 1.60; s7 37.2 %, 2700 MW, 64.8 GWh, 2.33·10¹⁴ J, 11.3 K (Carnot 49.7 % > 37 %); s8 0.0602 mol, 40 %, 63.3 kPa; s9 750 J, 0.1026 mol, 1172.6 K. All agree.
- Every choice item has exactly one correct option, and the distractor feedback is right. The rubric points add up, the criteria match the solutions, s6 force diagrams pass the force-diagram checklist, the scope stays within FY3/FY4, and no data is presented as measured without a source.
