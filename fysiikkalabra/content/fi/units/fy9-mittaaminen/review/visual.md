VERDICT: PASS
CONTENT-HASH: 44505a13028017fe
SCOPE: delta: new tasks s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla, with graph s8-kuvaaja) and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- [Minor] s8 c, "Vertailu": the second row of the chain is a bare "≈ 5,5 %" with no quantity, so the reader cannot see what it is a percentage of — write `\dfrac{0{,}54}{9{,}81} \approx 5{,}5\,\%` (it checks).
- [Minor] s8 c, Aikaskaalan virhe: the two lines in one block (`√(9,81/10,35) = 0,974` and `0,974 · 0,05 s = 0,0487 s`) are two separate calculations set as one block without a common left side; make them two blocks or give each a name (`k`, `Δt`).
- [Minor] s8 b "Kuvaajan lukeminen" does not say that the read-off points are the circled ones in the graph (only the alt text does); add "(ympyröity kuvaajaan)".
- [Minor] s7 and s8 Sijoitus: chain boxes end in ";" and "," (`= 30,0 N/m;`, `= 28,8 N/m,`); a full stop or nothing reads cleaner. Same style as the older tasks, so only if edited anyway.

## Checked
- Playwright is missing here, so I rendered the page (`preview/fy9-mittaaminen.html`) in headless Chrome at 360 px with the s7 and s8 cards isolated and every solution open (own captures, also 2.5x for the graph). Read: both task cards (text, figure, parts, skill links), the whole of s7 solution a-b, the whole of s8 solution a-c.
- s8-kuvaaja at 2.5x: axes with quantity and unit (s (m), t² (s²)), ticks 0,04…0,16 and 0,2…0,8, points blue and distinct from the black line, slope label does not touch the circles, no clipping. Alt text names (kuulan putoamismatka s, t², 5,18 m/s², 0,01 m, circled points) match the figure and the task text.
- 360 px: aligned rows wrap cleanly, no clipped formula, the two 9-column tables become two stacked tables that are readable; the rounding of results matches the data (30,0 ± 1,2; 10,35 ± 0,15; 15,0 ± 0,6).
- Intro: its text is read from tasks.json ("Kahdeksan … Kaksi tehtävää alkaa valmiista kuvaajasta"): eight tasks, and s7 and s8 are the two tasks with a given graph, so it is true; I did not open a render of the intro.
- The unit page's earlier captures (teacher-390-3, stage-sovella-390-6..9) were opened; they show the Esimerkit stage, not these tasks.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
