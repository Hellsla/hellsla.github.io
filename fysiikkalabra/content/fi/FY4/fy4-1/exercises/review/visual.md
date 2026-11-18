VERDICT: PASS
CONTENT-HASH: 2e5d53eab6b173d8

## Blocking
None.

## Polish
- [Minor] fy4-1-L3-05 Kaava — the closing "Ratkaistuna ajalle $t = \dfrac{x-x_0}{v}$" is an inline fraction (\dfrac) after a colon-less sentence; it reads fine, but a display line like the other two Kaava steps would match them. Optional.

## Checked
- Delta, solutions.md Kaava steps only (L2-06, L3-04, L3-05). The review/shots folder was missing, so I regenerated it with screenshot.py (79 captures, hash unchanged).
- Opened fy4-1-open-exercises-L2-1280-7.png (L2-06: derivation x_A = x_B -> (v_A - v_B)t = x_0B - x_0A, then display t), L3-1280-5 and -6 (L3-04: k, x = k x_ohj, v = k v_ohj, aligned two-row chain x = k x_0,ohj + k v_ohj t = x_0 + v t, then t), L3-1280-7 (L3-05: x_R = x_P, derivation, display t, x = x_0R + v_R t).
- Also opened L3-4 and L2-9..12 for the surrounding layout: the sections around the changed Kaava steps (Periaate, Muunnokset, Sijoitus, Vastaus, Järkevyys) kept their order and spacing; nothing clipped; the auto-wrapped chains are aligned at `=`; subscripts (x_{0A}, x_{0,ohj}, v_P t_0) legible; \cdot and decimal commas unchanged.
- The changed text is 1280 px only; the layout checks at 360/390/768/1280 px passed in the packet, and the longer sentences are inline maths that the page wraps like the neighbouring paragraphs.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
