VERDICT: PASS
CONTENT-HASH: e356f29b730cbfea
SCOPE: delta: new tasks s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla, with graph s8-kuvaaja) and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- [Minor] s8 c, "Vertailu": the second row of the chain is a bare "≈ 5,5 %" with no quantity; write `\dfrac{0{,}54}{9{,}81} \approx 5{,}5\,\%`.
- [Minor] s8 c, Aikaskaalan virhe: two separate calculations (`√(9,81/10,35) = 0,974` and `0,974 · 0,05 s = 0,0487 s`) are set in one block with no named left side; make two blocks or name them.
- [Minor] s8 b: say that the points read from the line are the circled ones in the graph (only the alt text does).
- [Minor] Sijoitus boxes end in ";" or ","; optional, as in the older tasks.

## Checked
- Playwright is missing, so I rendered `preview/fi-easy/fy9-mittaaminen.html` in headless Chrome at 360 px, s7 and s8 cards isolated with solutions open (own captures; graph's alt text and figure compared with the Finnish one). Opened: both task cards, s8 solution c; s7 and s8 a-b structure was checked in the Finnish render because the layout is identical.
- Language level: short sentences, one idea each ("Videosta mitataan kuulan putoamismatka s yhdeksällä hetkellä t. Hetket ovat välillä … ja niiden väli on …"; "Satunnainen lukemisvirhe ei siis selitä eroa"); the terms epävarmuus, kulmakerroin, systemaattinen virhe match the glossary and the Finnish version. Instructions are clear ("Perustele, miksi valitset tämän kuvaajan").
- Same numbers as the Finnish text in tasks, chains and graph (30,0 ± 1,2 N/m; 10,35 ± 0,15 m/s²; 15,0 ± 0,6 cm; 5,18 m/s²). The alt text is split into short sentences and names the same quantities as the task text.
- 360 px: no clipping, aligned rows wrap, and the line break "3,7-/kertainen" falls at a hyphen.
- Intro: "Tässä on kahdeksan … Kaksi tehtävää alkaa valmiista kuvaajasta. Yksi tehtävä yhdistää …" read from tasks.json; true. Not opened as a render.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
