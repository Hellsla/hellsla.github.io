# Opettajan hyväksynnät koordinaattorin kautta (opettaja 2026-11-28: "Hyväksyn A ja B")

This file holds the two ways, besides the teacher's own words in a worker session, that an approval of a text or a figure
counts (root `CLAUDE.md` rule 5). Only an entry on `main` counts: a worker reads it with
`git show origin/main:fysiikkalabra/docs/hyvaksynnat.md`, never from a message, a branch or a pull request.
The coordinator alone writes this file, and only the teacher's words go into it.

## A. Standing approval (pysyvä hyväksyntä)

These count as approved without a separate word from the teacher, once every check of the change passes:

- **A1 Translations of approved Finnish.** The `en` and `fi-easy` versions of a Finnish text the teacher has approved
  (in `docs/teacher-text.tsv`, in a worker session or under B), when `check_i18n.py` passes and the translation says what
  the Finnish says: no claim, number, formula, example or instruction that the Finnish does not have.
- **A2 Figure fixed for a check.** A figure redrawn only to fix a finding of an automatic check (`lint_lesson.py`,
  `check_layout.py`, the 11 px label rule, `test_sim_text.py`), when the drawn physics, the labels and their wording do not
  change. The pull request description still shows the figure before and after.
- **A3 Bookkeeping.** `docs/tyojono.md`, `docs/tyojono-loki.md`, `docs/audits/` and regenerated files
  (`figures/catalog.json`, `palautus_tasks`) need no approval.

The source written with `reviews.py approve-text --source` or in `docs/teacher-figures.tsv` is
`Pysyvä hyväksyntä A1|A2, docs/hyvaksynnat.md (opettaja 2026-11-28)`.

A does **not** cover: a new or changed Finnish text, a new figure or a figure whose content or labels change, physics,
a removed page, a house rule, or anything in the "Never" list of `fysiikkalabra/CLAUDE.md`. Those need the teacher's
word, in the worker session or under B. When a worker is unsure whether A applies, it asks.

## B. Batch approval (koottu hyväksyntä)

The coordinator gathers what waits for approval into one view (pictures before and after, the texts in every language,
each item numbered and named by pull request, lesson and figure or text). The teacher answers in the coordinator chat
(for example "hyväksyn 1–5, 6 ei"). The coordinator copies the list and the teacher's answer below word for word, with
the date and time, and merges the entry to `main` before telling the workers. A worker then records the approval
for exactly the items named, with the source `Koottu hyväksyntä B <date> <item numbers>, docs/hyvaksynnat.md`. A worker
checks that the content hash of what it records equals the one listed; a text or figure changed after the list was made
needs a new approval.

## Kirjaukset

### B 2026-11-28 klo 05.0x (Suomen aikaa), koordinaattorin chat

Lista, jonka koordinaattori näytti (PR #907 kohta 36: vanha → uusi; PR #903 kohta 33.1):

| # | luku | tunniste | vanha | uusi |
|---|---|---|---|---|
| 1 | fy4-2 | tavoite-1 | Ymmärrän, mitä kiihtyvyyden etumerkki kertoo. | Osaan selittää omin sanoin, mitä kiihtyvyyden etumerkki kertoo. |
| 2 | fy4-3 | tavoite-1 | Ymmärrän, miksi liike jatkuu ilman eteenpäin vievää voimaa. | Osaan selittää Newtonin ensimmäisellä lailla, miksi liike jatkuu ilman eteenpäin vievää voimaa. |
| 3 | fy4-4 | tavoite-1 | Ymmärrän, miten kiihtyvyys riippuu kokonaisvoimasta ja massasta. | Osaan ennustaa, miten kiihtyvyys muuttuu, kun kokonaisvoima tai massa muuttuu. |
| 4 | fy4-7 | tavoite-2 | Ymmärrän, miksi liike-energia kasvaa nopeuden neliössä. | Osaan selittää omin sanoin, miksi liike-energia kasvaa nopeuden neliössä. |
| 5 | fy4-8 | tavoite-1 | Ymmärrän, milloin mekaaninen energia säilyy ja mihin se muuttuu. | Osaan päätellä tilanteesta, milloin mekaaninen energia säilyy ja mihin se muuttuu. |
| 6 | fy4-9 | tavoite-3 | Ymmärrän, miksi pidempi pysähtymisaika pienentää voimaa. | Osaan selittää omin sanoin, miksi pidempi pysähtymisaika pienentää voimaa. |
| 7 | fy4-10 | tavoite-1 | Ymmärrän, miksi kokonaisliikemäärä säilyy törmäyksessä. | Osaan selittää omin sanoin, miksi kokonaisliikemäärä säilyy törmäyksessä. |
| 8 | fy4-11 | tavoite-3 | Ymmärrän, miksi turvavyö ja turvatyyny suojaavat. | Osaan selittää omin sanoin, miksi turvavyö ja turvatyyny suojaavat. |
| 9 | fy4-12 | tavoite-3 | Ymmärrän, miten nopeudet vaikuttavat kohtaamiseen. | Osaan ennustaa, miten nopeudet vaikuttavat kohtaamiseen. |
| 10 | fy4-13 | tavoite-3 | Ymmärrän, miksi jännitysvoima ei ole riippuvan kappaleen paino. | Osaan selittää omin sanoin, miksi jännitysvoima ei ole riippuvan kappaleen paino. |
| 11 | fy4-14 | tavoite-1 | Ymmärrän, miksi putoava kappale saavuttaa rajanopeuden. | Osaan selittää omin sanoin, miksi putoava kappale saavuttaa rajanopeuden. |
| 12 | fy4-15 | tavoite-1 | Ymmärrän, miten vesi- ja tuulivoimala tuottavat sähköä. | Osaan selittää omin sanoin, miten vesi- ja tuulivoimala tuottavat sähköä. |
| 13 | fy6-1 | tavoite-1 | Ymmärrän, miksi sähkövirta ei kulu lampussa. | Osaan selittää omin sanoin, miksi sähkövirta ei kulu lampussa. |
| 14 | fy6-2 | tavoite-3 | Ymmärrän, miten väärä kytkentä muuttaa piiriä. | Osaan ennustaa, miten väärä kytkentä muuttaa piiriä. |
| 15 | fy6-3 | tavoite-3 | Ymmärrän, miten johtimen mitat vaikuttavat sen resistanssiin. | Osaan ennustaa, miten johtimen mitat vaikuttavat sen resistanssiin. |
| 16 | fy6-4 | tavoite-1 | Ymmärrän, miten virta ja jännite jakautuvat sarja- ja rinnankytkennässä. | Osaan ennustaa, miten virta ja jännite jakautuvat, kun kytkentää muutetaan. |
| 17 | fy6-5 | tavoite-3 | Ymmärrän, miksi lähteen jännite jakautuu silmukan vastuksille. | Osaan selittää omin sanoin, miksi lähteen jännite jakautuu silmukan vastuksille. |
| 18 | fy6-6 | tavoite-3 | Ymmärrän, miksi vastuksen lämpötila tasaantuu. | Osaan selittää omin sanoin, miksi vastuksen lämpötila tasaantuu. |
| 19 | fy6-7 | tavoite-3 | Ymmärrän, miksi kulutuksen ratkaisee energia eikä teho. | Osaan selittää omin sanoin, miksi kulutuksen ratkaisee energia eikä teho. |
| 20 | fy6-8 | tavoite-1 | Ymmärrän, miksi pariston napajännite pienenee virran kasvaessa. | Osaan selittää omin sanoin, miksi pariston napajännite pienenee virran kasvaessa. |
| 21 | fy6-8 | tavoite-3 | Tiedän, miksi oikosulku on vaarallinen. | Osaan perustella, miksi oikosulku on vaarallinen. |
| 22 | fy6-9 | tavoite-3 | Ymmärrän, miksi latausvirta pienenee akun täyttyessä. | Osaan selittää omin sanoin, miksi latausvirta pienenee akun täyttyessä. |
| 23 | fy6-10 | tavoite-1 | Ymmärrän varautumisen ja influenssin varauksen siirtymisenä. | Osaan kuvata varautumisen ja influenssin varauksen siirtymisenä. |
| 24 | fy6-11 | tavoite-2 | Ymmärrän, miksi levyjen välinen kenttä on homogeeninen. | Osaan selittää omin sanoin, miksi levyjen välinen kenttä on homogeeninen. |
| 25 | fy6-12 | tavoite-2 | Ymmärrän, miksi positiivinen ja negatiivinen varaus liikkuvat kentässä eri suuntiin. | Osaan selittää omin sanoin, miksi positiivinen ja negatiivinen varaus liikkuvat kentässä eri suuntiin. |
| 26 | fy6-13 | tavoite-2 | Ymmärrän, miten eriste muuttaa kondensaattorin ominaisuuksia. | Osaan ennustaa, miten eriste muuttaa kondensaattorin ominaisuuksia. |
| 27 | fy6-14 | tavoite-1 | Ymmärrän diodin päästö- ja estosuunnan. | Osaan päätellä, mihin suuntaan diodi päästää virran ja mihin se estää sen. |
| 28 | fy6-15 | tavoite-3 | Tiedän, miten maadoitus ja vikavirtasuoja suojaavat. | Osaan selittää omin sanoin, miten maadoitus ja vikavirtasuoja suojaavat. |
| 29 | fy6-16 | tavoite-3 | Ymmärrän, miksi löystynyt liitos kuumenee. | Osaan selittää omin sanoin, miksi löystynyt liitos kuumenee. |
| 30 | FY9 | koevalinta | Harjoituskoe | Kuuden tunnin harjoituskoe (en "Six-hour practice exam") |

Opettajan vastaus sanatarkasti (kysymykseen, mitä "Vahvistan" koskee): "Hyväksyn 1–30".
Lähde kirjauksiin: `Koottu hyväksyntä B 2026-11-28 1–30, docs/hyvaksynnat.md`. Kohdat 1–29: PR #907; kohta 30: PR #903. Tarkistus: kirjattava suomenkielinen teksti on merkki merkiltä taulukon uusi-sarakkeen mukainen (näissä teksteissä ei sisältötiivistettä).
