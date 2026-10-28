VERDICT: PASS
CONTENT-HASH: 92ed4655267e611e

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- figures.json — the six figure descriptions were still the dense Finnish originals → split into short sentences (figures redrawn)
- inquiry.json activities[13].solution and activities[16].solution — long Finnish solution text left as is → Periaate, Muunnokset, Vastaus and Järkevyys split into short sentences; ekstrapolointi explained
- inquiry.json learn[0], activities[1] feedback ×2, [2].choices[2], [3].choices[2–3], [10].prompt, [12].prompt and feedback ×2, [13].hints[1] and mistakes[0], [15].choices[0–1], [16].hints[1] and mistakes ×2, [17].prompt and criteria[1] — long or chained sentences → shorter sentences, same content

## Polish
- (none)

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): Selkeä suomi throughout lesson.md (already simplified), inquiry.json, exit tickets and figure texts; physics terms kept (termodynaaminen systeemi, tilanmuuttuja, absoluuttinen nollapiste, ekstrapolointi); no step, hint or feedback dropped; correct options still unambiguous; Finnish step labels unchanged; sim names (*Nopeus*, *Mitattu*, *Teoria*) match the sim.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md (new Limits-of-the-model section, dilute-gas wording, LaTeX temperatures, extrapolation wording), inquiry.json (new check-c2 item with options and feedback, renumbered titles, LaTeX temperatures, explain model answer, exit intro), exit-ticket.json (trimmed to 1 question) and the new figure description; check_i18n and the page checks pass.
