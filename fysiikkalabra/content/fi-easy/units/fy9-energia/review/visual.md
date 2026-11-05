VERDICT: PASS
CONTENT-HASH: 2c058d99010374be

Visual and editorial review of `preview/fi-easy/fy9-energia.html` (built with `python3 scripts/build.py fy9-energia`),
checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element (hints, solutions,
model answers, rubrics, exit answers) opened. No console or page errors, no `.katex-error`, no unrendered `$…$` in
paragraphs, list items or table cells, no point in a decimal number inside rendered math, and no horizontal page
scroll at 390 px (scrollWidth 390; the stage bar scrolls inside itself). The six figures (hero, concept map, the
scaled 500 MW energy-flow diagram, the P₀–P₃ bar chart, the fy2-4 grid diagram, the s3 consumption graph) render
from figures.json with Finnish labels and decimal commas (3,6 MJ, η₁ = 0,90, −4,9 kWh/°C) and are legible at
390 px; their aria-labels are translated into short S2 sentences with the same numbers. Tables (task s1 devices,
s3 data, s4 options) fit at 390 px. "Luvun tärkeät käsitteet" renders after the opening with the fixed lead,
bold terms and inline LaTeX. Language is correct standard Finnish throughout.

## Blocking
None.

## Polish
1. `sovella/tasks.json` fy9-energia-s5 text (the report quote): "Keittimen arvokilvessä teho on $2200\,\text{W}$."
   reads oddly; write "Keittimen arvokilven mukaan teho on $2200\,\text{W}$."
2. `sovella/tasks.json` fy9-energia-s3 part c criterion detail: "Arvio on ekstrapolointi eli arvio mitatun alueen
   ulkopuolelta, $9\,\text{K}$ kylmimmän mittauksen ulkopuolelta." repeats "ulkopuolelta"; write "Arvio on
   ekstrapolointi eli arvio mitatun alueen ulkopuolelta: $-28\,{}^\circ\text{C}$ on $9\,\text{K}$ kylmempi kuin
   kylmin mittaus."
3. The s3 solution graph is 298 px wide at 390 px, so its tick labels are about 10 px; readable, and identical to
   the reviewed source, so no change for the translation.

## Shared issues
1. The stage bar and exit section show the English label "Exit ticket" (`lang/fi-easy.json` `inquiry.exit_ticket`
   and `optional_exit`, same as `lang/fi.json`). For S2 readers a Finnish label such as "Lähtölippu" would be
   clearer; a shared language-file decision, not this unit's.
