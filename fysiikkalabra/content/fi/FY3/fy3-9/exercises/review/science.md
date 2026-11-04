VERDICT: FAIL
CONTENT-HASH: 95ae4810d48b52f4

## Blocking
- exercises.json:301 (L3-04 text), solutions.md:209 and :212 — A: "ilma ei ole ehtinyt luovuttaa energiaa ympäristöön" / "energia ei ehdi siirtyä ympäristöön" / "työ jää kaasun energiaksi" describe an adiabatic compression. From 40,0 ml to 10,0 ml that gives about 700 kPa and about 240 °C. The table's 481 kPa and the answer of 76 °C fit only if a large part of the work has already left as heat, so the stated condition contradicts the data. — Fix: write "ilma on ehtinyt luovuttaa ympäristöön vain osan energiasta", "energia ei ehdi kokonaan siirtyä ympäristöön" and "osa työstä jää kaasun energiaksi". The numbers stay the same.

## Polish
- solutions.md:238 (L3-05 a) — "mittausvirheen rajoissa" → "mittausepävarmuuden rajoissa". The products fall steadily (606 → 594); say so.
- L1-07 is the third plain Boyle compression at level 1 (L1-01, L1-02); a different context or unknown would add more.
- L2-05 is tagged `graph` but asks only for ratios from the table: ask for the plot or drop the tag.
- docs/exercise-bank/FY3.md — the planned "ruiskumittaus → linearisointi" item is already L2-03, and the new L2-07 (absolute zero) replaces it. Update the plan line.
- L2-07 — the slope is read at two data points. The fit passes within 0,04 kPa of both, but the guardrail asks for points read off the line.

## Checked
- All 20 answers recomputed in one script; they agree with answers.py and the solutions (0,631 l; 126,9 kPa; 1,99 ml; −276,1 °C; 75,9 °C; 30,4 m).
- L2-05: p/T and V/T are constant to 0,3 %, while p/θ falls from 4,99 to 1,50; the process identification and the kelvin argument are right.
- L2-06: p(V + 2,0 ml) = 2400 ± 2 on every row; the error is correctly called systematic.
- L2-07: the least-squares fit gives −276,2 °C ± about 2 K, so "within uncertainty" holds; the condensation and absolute-zero wording follow the guardrails.
- L3-04: the two-step route (isoterminen, then isokoorinen) is valid, and the cooled value of 404 kPa is right.
- L3-05: hydrostatic pressure is right, the 1,5 l limit is stated as a model, the extrapolation is named, and there is no unsafe advice.
- L1-06 and L1-08: exactly one correct option each, and the feedback is right.
- Scope stays inside FY3: the gas laws, kelvins, fy3-4 hydrostatics, and work and internal energy only qualitatively.
- Hash unchanged at the start and the end.
