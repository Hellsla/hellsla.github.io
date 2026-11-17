VERDICT: PASS
CONTENT-HASH: e7401741ee3560cf

## Blocking
(none)

## Polish
- [Minor] solutions.md k1 a (stage-osa-1-390-6) — the split leaves "$M_1 = \ldots$ ja" at the end of a line and the $M_2$ aligned block as a boxed display with the full stop after it; reads slightly broken but nothing is clipped — write $M_2$ as its own inline chain in the same paragraph (the page then breaks it) or give each moment its own paragraph.
- [Minor] solutions.md k1 g (stage-osa-1-390-9) — "Jos taajuus ja aallonpituus pysyisivät samoina, myös nopeus pysyisi samana, eikä taajuus muutu väliaineen vaihtuessa." mixes mood and the last clause does not follow from the first — e.g. "… myös nopeus pysyisi samana, mutta nopeus muuttuu, kun väliaine vaihtuu." "Lyhenevä aallonpituus syntyy, jos ajatellaan …" is awkward — "Aallonpituuden voisi luulla lyhenevän, jos ajattelee …".
- [Minor] solutions.md k1 b, c, h, i — several paragraphs are one short sentence ("Valitaan momenttipisteeksi oikea pukki.", "Tämä on kuvaaja B."), so the argument reads as a stack of lines; join each such sentence to its neighbour where it continues the same step.
- [Minor] solutions.md k1 h — "$0{,}60 : 0{,}40 = 1{,}5$" has no units; write "$0{,}60\,\text{m} : 0{,}40\,\text{m}$". k1 a writes "$\text{Nm}$"; "$\text{N}\cdot\text{m}$" is the form the module uses elsewhere.

## Checked
- Diff of the change: tasks.json (intro, k1a, heilurimittaus, kaiku, k7 text and source_note split into paragraphs) and solutions.md (Perustelu paragraphs of k1 a–j, k7 Periaate/Mallivastaus).
- Opened: page-390-1 (intro split into three paragraphs, reads well), page-390-3 (k1 c–e at 390 px), page-390-36, -37, -42, -50, -58 (other tasks' open solutions, unaffected), stage-osa-1-390-2, -6, -7, -8, -9, -10 (all ten k1 Perustelu blocks), stage-kokeen-pisteet-390.
- Maths displays intact at 390 px in every split step: no clipping, no red KaTeX, units upright; nothing seen overflows. k7 Periaate/Mallivastaus split (stage captures of Osa 3) not opened one by one; the layout is the same component as seen in -58.
- Figures not part of this change; not re-judged. The hash command did not accept the id, so the packet hash and shots/stamp.txt (both e7401741ee3560cf) were used.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
