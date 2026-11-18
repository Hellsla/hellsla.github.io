VERDICT: FAIL
CONTENT-HASH: 2787a77cd4887df2

## Blocking
- inquiry.json `ennuste-1` / `koe-1` (Major) — Prediction 1 asks the efficiency of a petrol engine, but the sim only returns the constant it is given (25 %), and koe-1's intro states "Mallin hyötysuhde $25\,\%$ on tyypillinen arvo" before the student has measured anything. koe-1 varies only t and asks for E_h : E_o = 75 %, so the experiment cannot refute any wrong option (90 %, 60 %, 5 %): it restates the answer. The lesson itself admits the sim "ei mittaa sitä". Fix: make the prediction something the experiment can decide. Use the time-independence of η (now `ennuste-2`, `optional`) as the core prediction and promote it with its experiment. Or let the student compare devices at equal P_o and rank them before seeing η. Remove the 25 % from the koe-1 intro.
- inquiry.json `johtopaatos` (`after: koe-1`) — The conclusion asks "Muuttuiko se, kun käyntiaika muuttui", but the only core prediction (`ennuste-1`) is not about time. The time-prediction, its experiment and the reflection are all `optional`. On the core path the lesson's key idea (η independent of t, E-based = P-based) is never predicted. Fix: as above.

## Polish
- lesson.md "Hyötysuhde kertoo hyödyn osuuden" — The first paragraph is about 170 words and holds four ideas (definition, ≤100 %, real devices, heater, motor). Split it, and put the table beside the "vaihtelee paljon" sentence. (Minor)
- inquiry.json `koe-1.question` — It asks for the loss share and hints at η only indirectly ("kun muistat, että…"). Ask for η itself, or both. (Minor)
- inquiry.json `ennuste-1.prompt` — "Vihje: muista Pohdinnan kuuma hehkulamppu…" nudges the answer. The hint "kuumeneeko moottori" is fine, but it also makes the 5 % option too tempting. (Minor)
- inquiry.json `tarkistus-3` is `optional`, so the core path has only a concept check and a calculation, with no check that explains. (Minor)
- lesson.md "Tässä yksinkertaistetussa mallissa… valovirta" — It sits mid-section after the lamp comparison and is easy to skip, but it is useful. Put it with the table note. (Minor)

## Checked
- Opening question (hot incandescent lamp, LED) is answered by the Sankey figure and the pair comparison.
- Scope matches the FY2 slot (η = E_a/E_o = P_a/P_o); no chain efficiencies, no FY3 content.
- The worked example has 7 stages and the units, significant figures and check are there; it is not repeated in the exercises.
- Option feedback in the checks and the Etsi virhe item repairs the misconception; the heater item tests "hyöty määräytyy tarkoituksesta".
- Exit ticket tests the core idea (η from E, P, and the power-versus-efficiency misconception).
- Finnish reads fluently; terms are consistent with the glossary.
- The captures are not available in the packet ("none yet"); the figures and 360 px are judged only from their descriptions and the deterministic checks.

## Scores
- 2 Conceptual clarity: 4 — clear, with a good "purpose defines the loss" treatment; the lamp-figure scales are accurate.
- 3 Pedagogical effectiveness: 3 — the core prediction and experiment are circular, and the time-independence is optional.
- 4 Exercise quality and variety: 4 — a good error item, a transfer task and misconception-based hints (the exercise set itself not judged).
- 5 YO readiness: 4 — a conversion, a symbolic-first solution, and sig-fig reasoning.
- 6 Experimental reasoning: 2 — the constant-η sim cannot test the prediction, and the experiment's intro discloses the value.
