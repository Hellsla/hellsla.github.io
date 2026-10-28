VERDICT: PASS
CONTENT-HASH: 0c12449dd247c7d9

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- inquiry.json activities[4], [12], [15] solution strings were still the dense Finnish → Periaate/Muunnokset/Vastaus/Järkevyys split into short sentences (all steps kept)
- inquiry.json activities[12].hints[2] — "kerrotaan sadalla prosentin saamiseksi" → "Kerro lopuksi tulos sadalla, niin saat prosentin."
- inquiry.json activities[2].choices[2].feedback, [3].choices[0].feedback, [11].choices[1].feedback, [14].choices[1].feedback — long sentences split / made concrete

## Polish
- Short option texts and criteria were left as in Finnish; they are already plain.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): Selkeä suomi: short sentences, terms kept (siirtohäviö, hyötysuhde, kaukolämpö), no dropped steps, hints or feedback; options and feedback still match, correct choices unambiguous; Annettu/Kysytty… labels unchanged.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked district-heating feedback (inquiry.json) and the grid-loss Reasonableness (solutions.md) against the new Finnish.
