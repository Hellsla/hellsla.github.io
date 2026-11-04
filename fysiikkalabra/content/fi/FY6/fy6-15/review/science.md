VERDICT: FAIL
CONTENT-HASH: 8d554d92d33342d2

## Blocking
- lesson.md:355 (also ennuste-1 feedbacks, Yleinen virhekäsitys) — B: "Sulake ei suojaa ihmistä sähköiskulta" is absolute. The earthing section, the glossary *maadoitus* and tarkistus-3 ("miten suojamaadoitus ja sulake suojaavat … ihmistä") all say the fuse disconnects an earth fault. These contradict each other — fix: "Sulake ei huomaa ihmisen kautta kulkevaa virtaa; ihmistä se suojaa vain yhdessä suojamaadoituksen kanssa."
- lesson.md:227 — B: "suojamaadoitusjohdin aina keltavihreä" is false for old Finnish installations (other colours, PEN). Laypersons are told they may connect a luminaire — fix: "uusissa asennuksissa keltavihreä; vanhoissa värit voivat poiketa, eikä väristä päätellä jännitteettömyyttä."
- lesson.md:475 and inquiry.json:141–169 (iho table, "Kumipohjaisin kengin … 1,15 mA") — B: rubber soles appear harmless with no condition stated, which reinforces a dangerous myth. This holds only for intact, dry soles, a dry floor and one contact to earth; a hand on a tap or an earthed appliance bypasses the shoes — fix: add one sentence saying so.

## Polish
- lesson.md:224 — "Johto on mitoitettu sulakkeen nimellisvirralle" reverses fy6-16 lesson.md:185 ("sulakkeen koko valitaan johdon poikkipinta-alan mukaan"). Use fy6-16's direction.
- lesson.md:327 — Class III is "enintään 50 V vaihtojännitteellä" yet fed "akusta". Add "tai 120 V tasajännite".
- lesson.md:555 — "sulake katkaisee virran, jos kuormitus jatkuu": at 1,25 · I_s a fuse may take a long time or not trip. Say "voi laueta vasta pitkän ajan kuluttua".
- lesson.md:260 aria-label — "Ihmisen kautta ei kulje virtaa": write "vain pieni virta, kunnes sulake katkaisee".
- fy6-16 lesson.md:265 — "suojausluokitus, esimerkiksi IP54" conflicts with this chapter's glossary *suojausluokitus* (I–III); IP is the kotelointiluokka.

## Checked
- All lesson and inquiry numbers were recomputed and match: 8,7; 13,9; 22,6; 12,6; 19,6 (9,6 + 4,3 + 5,7) A; 230, 11,5 and 1,15 mA; 131 W and its mistakes; 2300 and 3680 W; 2,56.
- The body-current thresholds 0,5 / 10 / 30 / >50 mA (≈1 s) agree with IEC 60479-1, and the duration and path caveats are present.
- The RCD principle, the 30 mA limit and the L–N contact it misses are correct; the figure matches.
- Classes I–III and their symbols, and the 400 kV, 25 kV, 3 MV/m and 20 kV values are correct.
- The step-voltage, rescue and 112 advice is correct. The Tukes register and layperson list are correct, as is the exit ticket.
- The predictions have exactly one correct option each, and their feedback is sound. The fuse and RCD wording of fy6-16 otherwise agrees.
