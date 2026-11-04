VERDICT: PASS
CONTENT-HASH: 55477a465de9a3d6

## Blocking

## Polish
- lesson.md:310 (theta-graph aria-label) — "n = 1,332", while the text says $n = 1{,}3315$. Carried from the fi version; the peak is 42,3° either way.

## Checked
- Round-1 blocking fixed: "Aallonpituus kertoo valon värin." is removed. Line 75 ("Väri riippuu taajuudesta, joten väri pysyy samana…") is now the only statement about colour, and the lesson is consistent. No other sentence in lesson.md or inquiry.json ties colour to the in-material wavelength.
- Round-1 polish fixed: "noin 198 000 / 196 000 km/s" (exact 198 111 / 196 053).
- One script (scratchpad sci/recompute_r2.py): worked example 34,88° / 34,47°; virhe 39,2° vs 34,5°; koe-1 Δδ 0,53…4,45° (α1 = 50°); koe-2 minimum 38,43° near 49–50°.
- Rainbow 42,30° / 40,63°, secondary 50,5° / 53,5°; siirto 25,40 mm; tarkistus-2 1946 km/s; exit ticket −8°.
- Physics kept in simplified sentences: electron-response mechanism, Newton's two prisms, antisolar point and sun-height limit, θ = 4β − 2α with derivation, prism equations with their exit condition.
- inquiry.json: one correct option per choice item, distractor feedback right, model answers agree with the theory.
- check_layout.py fy7-11 --width 340: fi-easy OK, no formula overflow.
