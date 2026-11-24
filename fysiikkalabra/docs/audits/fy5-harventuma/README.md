# FY5 harvennus → harventuma: ennen/jälkeen

Kuvat eivät muutu ulkonäöltään: vain `aria-label` (alt-teksti) muuttuu. Piirrosten sisäiset nimiöt (`\text{harvennus}`) jätettiin ennalleen ja ovat uudelleen piirrettävien listalla.

Jälkeen-kuvat: `fy5-10-types-jalkeen.png`, `fy5-14-pitkittainen-jalkeen.png` (ennen-kuva on ulkonäöltään sama, vain nimiö on piirroksessa vielä "harvennus").

## Alt-tekstit (vain muuttuneet lauseet)
| Kuva | Ennen | Jälkeen |
|---|---|---|
| fy5-10/types (fi) | Alhaalla pitkittäinen aalto: pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harvennus). | Alhaalla pitkittäinen aalto: pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harventuma). |
| fy5-10/types (fi-easy) | Pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harvennus). | Pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harventuma). |
| fy5-14/pitkittainen (fi) | Ilman hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat tihentymiä ja harvat harvennuksia. | Ilman hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat tihentymiä ja harvat harventumia. |
| fy5-14/pitkittainen (fi-easy) | Ilman hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat tihentymiä ja harvat harvennuksia. | Ilman hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat tihentymiä ja harvat harventumia. |

## Piirrosten sisällä (ei muutettu) → uudelleen piirrettävät
- fy5-10/types: kaksi nimiötä "harvennus" (`lessons/FY5/fy5-10/figures.py` rivit 87–88; fi, fi-easy ja en käyttävät samaa piirrosta, `figures.json` kääntää nimiön).
- fy5-14/pitkittainen: yksi nimiö "harvennus" (`lessons/FY5/fy5-14/figures.py` rivi 67).
- `figures.json`-avain `"harvennus"` (fi-easy, en) on piirroksen nimiön käännösavain; vaihtuu piirroksen mukana.
