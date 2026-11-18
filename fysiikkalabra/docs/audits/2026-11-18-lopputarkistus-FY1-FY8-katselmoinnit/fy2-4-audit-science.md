VERDICT: FAIL
CONTENT-HASH: 2787a77cd4887df2

## Blocking
- inquiry.json:396 (check-patteri, "Alle $100\,\%$, koska minkään laitteen hyötysuhde ei voi olla $100\,\%$.") — **A, Major**. This option's conclusion also covers the keyed "Lähes $100\,\%$". lesson.md:91 says only an ideal, lossless device reaches 100 %, so the theory supports this option, and its feedback "ei aina sen alle" contradicts the keyed "lähes". Two options can be defended. — Give it a conclusion clearly apart from the keyed one (e.g. "Noin $50\,\%$, koska johdot lämpenevät"; the feedback adds that the wires' heat also stays in the room).

## Polish
- inquiry.json:62–75 (ennuste-1 feedback) — calls 25 % "(simulaation mallin arvo)". It is a typical real value that the sim takes as input, so "tyypillinen arvo" fits better. (Minor)
- lesson.md:93–100 — the FY2 scope note asks for a named source for real values. The table names none. Add one line with a source, or say the values are approximate. (Minor)
- sim.js:48 (`nuolet`, "Nuolten paksuudet ovat suhteessa tehoihin") — the input arrow is always 100 px, so the proportion holds only within one picture. Add "saman laitteen". (Minor, B)
- lesson.md:64 — most of a filament's loss leaves as infrared radiation. The current wording is fine for FY2 (C); one clause would name the mechanism. (Minor)

## Checked
- All 31 lesson-answers.py numbers recomputed independently in one script; all agree (worked example 360/324/36 kJ, koe-1, siirto 250 W and its mistakes, tarkistus-2 80 %, virhe 30 %).
- Sankey figures to scale: lamp 120/6/114 px; pair 1,6 px/W in both lamps (96 px, 16 px, 4,8 px), so "kuusi kertaa" holds.
- Formula section names its law; the constant-power condition for $P_\text{a}/P_\text{o}$ is stated and the derivation is correct.
- Efficiency limit uses the guardrail wording; heater "lähes 100 %"; FY2 scope kept.
- Typical efficiencies plausible; load dependence stated.
- Other choice items: exactly one correct option; distractor feedback correct.
- Experiments: the adapter sets `laite` before `Po`, so 40 W and 60 kW hold; only `t` varies; simState gives Eo, Ea, Eh.
- sim.js implements $P_\text{a} = \eta P_\text{o}$, $E = Pt$; its assumptions are stated.
- Exit ticket correct (70 %, 150 J; 50 W, 150 W).
- Hash identical at start and end.

## Scores
- 1 Physics and mathematical correctness: **2** — theory, figures and numbers correct, but one task has two defensible options (A in a task).
- 6 Experimental reasoning (models): **4** — controlled variables and model assumptions are honest; the engine prediction is checked against an input value.
