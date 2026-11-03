VERDICT: DONE

Round-1 fixes; `check_lesson.py fy7-9` all ok.

- Visual Blocking (spectrum table clipped, heads misaligned) — `lesson.md`: the table now has three columns (Alue | Aallonpituus | Lähteitä ja käyttöä) with shorter cells, soft hyphens in the long words and a non-breaking hyphen in D‑vitamiini. Measured: it fits with no horizontal scroll at 360, 390, 768 and 1280 px (scrollWidth = clientWidth), and `check_layout` passes at 360/768/1280 with no wide-table warning. **For developer:** the heads are still offset from the body columns. The cause is the shared rule `table thead,table tbody{display:table;width:100%}` in templates/site.css: thead and tbody are laid out as two separate tables. With `display:table-row-group`, every column lines up at all four widths (tested by injecting the rule), and the table still fits. That is a template change, outside this lesson.
- Polish: microwaves make the water molecules "kääntyilemään edestakaisin"; "273,15 K" in lesson.md and in the lava hints, feedback and solution in inquiry.json; the Etsi virhe feedback now says that b·T has the unit m·K², not m; "noin 500 nm (tarkemmin 502 nm)"; sim.js header comment 750 K → 800 K.
- Not done: glossary "aallonpituus" belongs to fy5-10, not this chapter.
