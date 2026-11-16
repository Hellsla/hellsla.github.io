VERDICT: PASS
CONTENT-HASH: 3adcc392f3bc2b66

## Blocking

## Polish
- content/fi/FY4/fy4-8/exercises/solutions.md:276 (L2-10 a) — exact speeds and $1500\,\text{kg}$ (four significant figures, trailing zeros count) would allow four figures; "kolme numeroa ei lupaa liikaa" is true but not the usual rule — give $52{,}08$, $144{,}7$, $468{,}8\,\text{kJ}$ or say plainly that three are enough for the comparison.
- solutions.md:248 — $30 : 3{,}6\,\text{m/s} = 8{,}333\,\text{m/s}$ and $13{,}889\,\text{m/s}$ are rounded: "≈", not "=".
- solutions.md (L2-10 e) — $7716\,\text{J} : 0{,}05\,\text{m} = 154\,\text{kN}$ shown as "noin $150\,\text{kN}$"; fine with the one-figure distance, could say so.

## Checked
- Hash the same at the start and the end (3adcc392f3bc2b66).
- git diff since the version passed: solutions.md L2-10 Vastaus only; the d) paragraph moved first, a) now starts "Lisäksi:"; no number, formula or word otherwise changed. exercises.json and answers.py unchanged.
- The answer-box value ($s \approx 0{,}26\,\text{m}$) now on the first line of the answer step matches `answer` 0.26 (tolerance 0.05); parts a–c, e read in order after it with every part's result still present.
- All 21 numeric answers recomputed in one script with my own formulas (least-squares fits through the origin for L2-05, L2-07): equal to answers.py and inside every tolerance.
- L2-10: $E_\text{k} = 52\,083$; $144\,676$; $468\,750\,\text{J}$; ratio $9{,}00$; $F = 29\,430\,\text{N}$, $E_{\text{k}0} = 7716\,\text{J}$, $s = 0{,}2622\,\text{m}$; $a = 37{,}5\,g$; same distance at $100\,\text{km/h}$ gives exactly the weight of $12\,000\,\text{kg}$; $7{,}7\,\text{kN}$ over $1{,}0\,\text{m}$, $154\,\text{kN}$ over $0{,}05\,\text{m}$.
- L2-10 source values and quotation agree with the coordinator's verified record (read 16.11.2026); kg-as-force interpretation and constant force stated in the task; mean-force limit said.
- L2-10 c: energy to deformation and internal energy, then to the surroundings as heat; never "muuttuu lämmöksi".
- Significant figures: $80\,\text{kg}$ two (trailing zero counts) → $0{,}26\,\text{m}$, reason true.
- Multiple choice L1-06, L1-08 and statements L1-09: one correct option each, distractors wrong, feedback physics right.
- Notation ($E_{\text{k}0} + W = E_\text{k}$, $W = Fs$) as in the brief; scope FY4.
