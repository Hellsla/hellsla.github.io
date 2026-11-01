VERDICT: PASS
CONTENT-HASH: afb3b91be208f94f

## Blocking
(none) Round 1 Major resolved: exit-ticket.json vastaus now reads "Muunnetaan teho kilowateiksi: sijoitetaan 1 W = 10^-3 kW, joten [chain]. Valmiustila kuluttaa [chain]". No parenthesis, no lone ")"; each display chain is introduced by a sentence and the continuation "ja kuluttaa" after the last block is clean (open-exit-1280).

## Polish
- [Minor] theory-1280-2 — the inline "40 kJ = 40 · / 1000 J = 40 000 J" still breaks after "40 ·" at 1280 px; the template fix did not catch this one (or the capture predates it). Make it a display chain or a non-breaking join.
- [Minor] lesson.md Kaava (fig-3 text) — "Olkiluoto 3 -ydinvoimalayksikön": use a non-breaking space after "3" so it cannot split at 390 px.
- [Minor] Tutki sim at 1280 (lab-1280-1) — controls interleave A and B (A select, t_A, B select, t_B, Nopeus); the t_A label wraps "= 5 min = / 0,0833 h". Group A and B in separate rows.
- [Minor] tarkista solution 4 (open-tarkista-1280-3) — Sijoitus uses a stacked "J over s" fraction cramped against the "=" rows; write 800 J/s inline.
- [Minor] Tyypillisiä tehoja table (theory-1280-2) — "Teho" header sits left of its right-hand values; align header and values the same way.

## Checked
- open-exit-1280 (the fix); contact-1 (all twelve thumbnails: intro, sim, hero, bars, E-t graph, example, stages 2-3 survive).
- open-tarkista-1280-3; theory-1280-2 (E-t graph, kWh display, table); lab-1280-1 (sim and Ennusta/Tutki layout).
- Round 1 figure and 390 px findings (fig-1/2/3, example, stages) judged as unchanged from the thumbnails; content hash changed only in the exit answer text, per the contact sheet.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
