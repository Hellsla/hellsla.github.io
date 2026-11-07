VERDICT: FAIL
CONTENT-HASH: ce8f542f0c239b34
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- content/en/FY6/fy6-1/lesson.md:83 — A (terminology): "In an ordinary short circuit the propagation delay is so small…" calls the lamp circuit a *short circuit* (oikosulku), a term the course defines in fy6-2 as a path that bypasses a component and uses for I_sc in fy6-14. The Finnish says "tavallisen lyhyessä virtapiirissä" (in a circuit of ordinary short length). — Fix: "In an ordinary circuit of short length (a few metres of wire) the propagation delay is so small…".
- content/en/FY6/fy6-1/inquiry.json:348 (tarkista 1, correct option feedback) — same error: "In a short circuit the delay is so small…" (fi: "Lyhyessä piirissä"). — Fix: "When the wires are only a few metres long, the delay is so small…".

## Polish
- none

## Checked
- lesson.md Virtapiiri and Direction-of-current paragraphs vs fi: switching change propagates quickly but not infinitely fast; free electrons already in the wire incl. filament; drift < 1 mm/s kept; no 'speed of light' claim left.
- inquiry tarkista 1: correct option and all three distractor feedbacks match fi (finite speed, electrons start almost immediately throughout the circuit); exactly one correct option.
- Diff since origin/main compared sentence by sentence with the Finnish source change; content hash checked at start and end.
