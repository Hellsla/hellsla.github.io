VERDICT: FAIL
CONTENT-HASH: 7caf8e281c418c80

## Blocking
- [Critical] Koe 1 / Koe 2 simulation at 390 px (exp-exp-1-390-1, exp-exp-2-390-1) — in the experiment card the canvas is clipped (pulley and hanging mass cut off), its labels are oversized and overlap ("Tilannekuva" over $t$, "Voimakuvio: punnus" over $\overline{N}$/$\overline{G}_2$) and no force diagram is visible; sim-390 and lab-1280 are fine, so the embedding is at fault — Koe 1 asks the student to watch $\overline{T}_1$ and $\overline{G}_2$ change, impossible on a phone — resize the canvas and its label overlay to the card width and recapture (if it is a capture-timing artefact, the capture must wait for the resize).
- [Major] figures `atwood` and `tilanne` (fig-6-390, fig-5-390, theory-1280-1/-2) — the short weight arrows start at the box centre and end at or just past the box edge: in "voimakuvio: kevyempi" $\overline{G}_1$ shows only as an arrowhead under the box, in "voimakuvio: punnus" $\overline{G}_2$ mostly lies inside the box. Comparing $T$ with $G$ is the figures' whole point, and at 390 px it cannot be read — keep the common scale but make the boxes smaller (or the scale larger) so every arrow extends clearly outside its box.

## Polish
- [Minor] lesson.md Kaava — "(kg)", "(N)", "(m/s²)" in plain text after the symbols; the experiment tables' headers mix plain "m/s" with maths — write $(\text{kg})$, $(\text{N})$, $(\text{m/s}^2)$.
- [Minor] lesson.md Yleinen virhekäsitys and exit ticket 1 — "Ne vaikuttavat eri kappaleisiin mutta kuuluvat eri vuorovaikutuksiin" reads as if acting on different bodies argued against a pair → "Ne vaikuttavat eri kappaleisiin kuten voima ja vastavoima, mutta ne kuuluvat eri vuorovaikutuksiin: …". Also "$T$ supistuu pois, koska lanka on … sisäinen voima" → "$T$ kumoutuu, koska langan jännitysvoima on kappaleiden välinen sisäinen voima."
- [Minor] inquiry.json pred-2, check-1, check-3 — "langan päissä roikkuu kappaleet, joiden…" → "langan päissä roikkuvat kappaleet, joiden…".
- [Minor] inquiry.json exp-2 solution, Vastaus — "kolme merkitsevää numeroa kuten taulukon lukemissa, mutta erotuksella on vain kaksi…" contradicts itself → "$0{,}74\,\text{N}$ ylös. Erotuksessa desimaalien määrä ratkaisee: lukemat ovat sadasosan tarkkuudella, joten tulos annetaan sadasosan tarkkuudella."
- [Minor] figure `atwood` — $\overline{a}$ is drawn beside the force diagrams too, while `tilanne`, `esimerkki` and the sim's "Mallin oletukset" keep velocity and acceleration in the tilannekuva only, because they are not forces; drop the two $\overline{a}$ arrows in the force-diagram column.

## Checked
- contact-1…6; fig-1/5/6/8-390; theory-1280-1/-2/-3
- example-390-2; sim-390, sim-1280, lab-1280
- exp-exp-1-390-1/-2, exp-exp-2-390-1; open-tarkista-1280-2/-3 (check-2, check-3, exit ticket)

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 2
