VERDICT: FAIL
CONTENT-HASH: 2241ae0d390f82f3

## Blocking
- [Major] solutions.md fy2-k1 c) Perustelu (390 px, Osa 1 stage capture 5) — the chain `1\,\text{Wh} … 15\,\text{Wh} = 15 \cdot 3600\,\text{J} = 54\,000\,\text{J} = 54\,\text{kJ}` runs past the edge of its box and is clipped after the last "=": the answer "54 kJ" is not visible on a phone — the model answer to the very point the item tests (Wh to J) loses its result; the same bug clips the final unit in FY1's k1 e) — let the chain wrap into rows after an equals sign (or start it on its own row) so nothing leaves the card.

## Polish
- [Minor] top-390/top-1280 — the banner "Luonnos: tätä oppituntia ei ole vielä tarkistettu." says "oppituntia" on an exam page (shared template); "tätä sivua" would fit.
- [Minor] header and Kokeen pisteet — "20 p", "70 p", "120 p:n" are plain text while the task cards write "$2$ p" in LaTeX; use one style.
- [Minor] tasks fy2-k2 d) and fy2-k5 d) — Finnish text uses straight quotes ("hävinnyt", "Koska hukkalämpö …"); use ”…”.
- [Minor] solutions fy2-k3 — the symbol `E_\text{pa}` (polttoaineen energia) is never named in Annettu or Kysytty; name it once, or use `E_\text{polttoaine}`.
- [Minor] fy2-k2 a) Kaava — the implication in `\eta = \tfrac{E_\text{akku}}{E_\text{verkko}} \Rightarrow E_\text{verkko} = \tfrac{E_\text{akku}}{\eta}` is broken after the arrow, so row 3 ("= E_akku/η") reads as a continuation of the first equation; break before the arrow or write the rearranged form on its own line. Also fy2-k6 table: "13 500" touches the card edge at 390 px and the header cells are left-aligned over right-aligned numbers.

## Checked
- top-390, top-1280, contact sheets 1, 2, 6, 8; Osa 1 stage captures 5, 6; Osa 2 captures 2, 6, 8, 17, 19; Osa 3 captures 1, 5, 9; Kokeen pisteet (contact 8 #96).
- Figure fy2-k4-bars (fig-1-390, also enlarged): axes titled with units, ticks readable, bars from zero, 12 bars distinct; fine. fig-2 is an empty 28 px stub.
- Exam header, structure box and point sums (20 + 2·15 + 20 = 70; 120 offered) consistent; tables (k4, k6) fit at 390 px; rubric chips, reveal states and tasks show no horizontal overflow; euro sign and units render.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
