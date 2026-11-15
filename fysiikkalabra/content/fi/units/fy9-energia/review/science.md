VERDICT: FAIL
CONTENT-HASH: 6ad4a6f43f1059e3
Review of the recognition chart (queue 9c) and the term change against the version passed at e297d1ba1b8c1dd6; full on the chart, delta on the rest.

## Blocking
- B (row 1 and ARIA_KARTTA): "suljettu järjestelmä → energia säilyy, E_alussa = E_lopussa". A closed system exchanges no matter but can exchange energy as heat and work; total energy is constant only in an isolated system. glossary.json says exactly this ("eristetty systeemi … Suljettuun systeemiin energiaa voi vielä siirtyä"), and the unit's own Kaava section says "Eristetyssä systeemissä, johon energiaa ei tule eikä josta sitä lähde". The chart contradicts both and teaches the wrong condition. Fix: "eristetty systeemi" (or "energiaa ei tule eikä lähde") in the sign and the aria-label.

## Polish
- C: "voima siirtää matkan → W = Fs": the Kaava's condition is a constant force along the motion; "liikkeen suuntainen voima" in the sign would make it explicit.
- Note for the teacher/pedagogy: "monta laitetta peräkkäin → η = η_1η_2η_3" is the Johda itse result of the Kaava section; the old map left it out on purpose (teacher 2026-11-12). Physics is right (each stage's output is the next stage's input).

## Checked
- Rows: energy over time → P = ΔE/Δt; steady power, known duration → E = Pt (Kaava: "tasaisella teholla"); kWh → 1 kWh = 1000 W·3600 s = 3,6 MJ (recomputed); useful and taken energy → η = W_a/W_o (MAFY symbols of mafy-tunnukset.tsv; aria's "annettu energia jaettuna otetulla" matches); chain → product of efficiencies (derivation in the johda block checked); fuel → Q = Hm; force over a distance → W = Fs.
- Names and symbols agree with kaavanimet.tsv; nothing outside FY9.
- ARIA_KARTTA lists the same eight rows in order with the same physics (so it carries the same "suljettu" error).
- teacher.md: only "käsitekartta" → "tunnistuskaavio". unit.md: only the figure.
