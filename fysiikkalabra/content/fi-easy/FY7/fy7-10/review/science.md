VERDICT: FAIL
CONTENT-HASH: a39e8dfcd20fe425

## Blocking
- lesson.md:152 (Osittainen heijastuminen) — A (causality): "Samasta syystä ikkunasta näkee illalla oman huoneensa heijasteen" ties the window reflection to the previous paragraph's reason, a large angle of incidence (grazing light). The room is seen in the window at near-normal incidence; the real reason is the one the next sentence gives (little light from outside, so the ~4 % reflected room light dominates). The fi original has no "samasta syystä" and states only that reason. Fix: drop "Samasta syystä", e.g. "Illalla ikkunasta näkee oman huoneensa heijasteen, koska ulkoa tulee vähän valoa."

## Polish
- lesson.md:150 — "järven pinta peilaa iltaisin rannan puut" keeps the fi wording where "iltaisin" suggests the time of day is the cause; the cause is the grazing view far across the lake. Fix: "kun pintaa katsoo loivasti kauas" (C if left; same polish as the fi review).

## Checked
- Simplification fidelity: inquiry.json and exit-ticket.json have the same structure, correct flags, experiment initial/locked/vary/measure keys and the same numbers as the passed fi version in every string; the rewritten sentences say the same physics.
- lesson.md: same numbers as fi in every section; the six figures are identical to fi (geometry and labels).
- One script recomputed everything: example 38,02° and 2,256·10⁸ m/s; ennuste-1 28,9°; ennuste-2 22,1° → 40,6° (×1,84), max 48,8°/24,4°; ratios 1,36/1,48; koe-2 35,2/30,9/30,3/18,5° and 0,766; virhe 0,651 → 40,6°; siirto 41,68° (25,94; 22,08; 39,9); tarkistus-2 1,470 (0,680; 1,592); nopeus 2,013 (4,47); exit 25°/50°, 1,33; R 2,0 %/4,3 %.
- mittaus fit: A = 1,4895, ΔA = 0,0162, B = −0,0041; line through (0,60; 0,89); mistakes 0,671 and 1,79.
- Split sentences keep their conditions: angles from the normal, n > 1 "näkyvälle valolle läpinäkyvissä aineissa", "samalla tulokulmalla", the oblique view in Näennäinen syvyys and tarkistus-3, frequency set by the source.
- Each choice item has exactly one correct option; distractor feedback names the real error.
- Sim strings (lang/fi-easy.json) match fi in content; the model box states its limits and calls readings model values.
