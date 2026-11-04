VERDICT: PASS
CONTENT-HASH: 4187dbc87c6a58fb

## Blocking

## Polish
- solutions.md fy8-5-L3-05 Vastaus b) — "alkalimetalleilla arvot ovat suurempia, koska ytimen varaus on suurempi kuin vedyllä" clashes with the screening argument just made. — Write "koska sisäkuorten elektronit eivät varjosta ytimen varausta täysin, joten valenssielektroniin vaikuttaa suurempi varaus kuin vedyssä".
- solutions.md fy8-5-L3-04 Kuvaajan lukeminen — the slope is read through the first and last raw data points, called "suoran päätepisteet". Also "kuoille" → "kuorille". — Either read two points off the fitted line (for example at 0,14 and 0,22) or call the end-point slope a check of the fitted value 13,62 eV.
- figure fy8-5/string (used by L2-06) — the labels "0 solmua / 1 solmu / 2 solmua" give away the node count that a) asks for. — Ask in a) only for the wavelengths, or remove the node-count labels from the copy shown with the task.
- solutions.md fy8-5-L2-06 Vastaus c) — "$80\,\text{Hz} \cdot \tfrac12 = 40\,\text{Hz}$" uses the m = 2 frequency before it has been computed. — Write $f_1 = \tfrac{64\,\text{m/s}}{1{,}60\,\text{m}} = 40\,\text{Hz}$.
- exercises.json fy8-5-L3-05 — Li 5,39, Na 5,14 and K 4,34 eV and the 2,10 eV Na transition are real tabulated values but are labelled "Esimerkkiaineisto". — Name a source (for example NIST ASD) and present the values as lähteellinen aineisto.

## Checked
- One-script recompute, all equal to answers.py: 50; 5,26 %; 300; 1,51; −0,544 eV; 14; 103 nm; 8; 960; 365 nm; 72,25 %; 120 Hz; 16; 15; 4235; 13,62 eV; 590,5 nm (241,2 nm).
- L2-05 histogram matches the exact 1s distribution (117/174/78/24/6/1); interpolated 90 % radius 0,145 vs 0,141 nm.
- L3-04 gives n = 3,00/4,01/5,02/5,98; the n = 7 line is 397,1 nm and the limit 365 nm.
- L3-05 configuration and trend reasoning are right; 2,10 eV < E_i.
- L2-06: 40/80/120 Hz; the node–energy analogy matches the brief.
- MC L1-06, L1-07, L2-07: one correct option each, and every feedback is right.
- Scope, notation, symbolic-first solving and rounding are fine. The levels fit and nothing duplicates an existing task. Hash is the same at start and end.
