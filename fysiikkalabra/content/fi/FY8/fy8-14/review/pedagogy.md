VERDICT: PASS
CONTENT-HASH: 1c59e4e4a38d1723

## Blocking

## Polish
- inquiry.json:`tarkistus-3` prompt — one task asks four things, and the first sentence is unclear ("vaikka röntgenkuvatun potilaan vieressä voi olla heti kuvauksen jälkeen") — split into two parts, or write: "Selitä, miksi hoitaja pysyttelee tänä aikana etäällä potilaasta, vaikka röntgenkuvatun potilaan vieressä voi olla heti kuvauksen jälkeen." -> "Selitä, miksi hoitaja pysyttelee etäällä PET-potilaasta, mutta voi olla heti röntgenkuvauksen jälkeen potilaan vieressä."
- Workload: x-ray, CT, tracers, PET, radiotherapy, industry and safety, plus the sim, three predictions, an interpret task, the example and three checks, exceeds one hour for a 17-year-old. The industry section (savuilmaisin, radiohiili, paksuusmittari) is not assessed anywhere in the core path; mark the `rontgen` interpret task or `siirto` optional, or trim the industry text.
- exit-ticket.json — both questions concern x-ray contrast and justification/optimisation; PET localisation, the lesson's opening question, is not tested. Replace one question with "Miksi yksi koinsidenssi ei riitä paikantamaan lähdettä?"
- inquiry.json:`virhe`, `ennuste-3` — the correct option is each time the longest and the only one with a complete causal clause; vary lengths so it cannot be picked by form.
- Phone, koe-1 (tutki-390-2, lab-1280-1) — the readings table is wider than its card, so the `kasvaimen kautta (%)` column is off-screen when recording; shorten the headers ("etäisyys (cm)", "kasvaimen kautta (%)") or wrap them.

## Checked
- Course goals, slot and prerequisite; full lesson text, inquiry sequence, exit ticket (packet).
- Captures: top-390, fig-1, fig-4, fig-6, fig-8, fig-10, fig-12, stage-ennusta-390-1, stage-tutki-390-1/-2, stage-tarkista-390-1, lab-1280-1.
- PET sim run in Playwright at 1280 px: N = 16, 76, 226 gave 20,4 / 14,9 / 1,0 cm, matching the stated model values; the tumour is not drawn, so the experiments can refute predictions 1 and 2.
- Predictions: feedback is gated and repairs the misconception; ennuste-3 reveals only after the theory.
- Hash at start and end: 1c59e4e4a38d1723.
