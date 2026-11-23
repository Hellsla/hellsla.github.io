# "Avaa isoksi": ratkaisukentän leveys lyhyellä tehtävällä (opettaja 2026-11-23)

Muutos: `templates/site.css`, `.ex-focus-body.stack` (lyhyt tehtävä, lesson.js part 10). Tehtäväteksti pysyy enintään 44 rem
leveänä; ratkaisukenttä ja Abitti-työkalurivin alue käyttävät isonäkymän leveyden enintään 92 rem (sama raja kuin yläpalkilla).
Alle 1100 px ja pitkän tehtävän rinnakkaistila eivät muutu.

Kuvat (FY2 luku 6, `fy2-6`): `before-*` ennen, `after-*` jälkeen. `stack` = lyhyt tehtävä (6-1), `side` = pitkä tehtävä
(rinnakkaistila, ennallaan). 390 px: ei stack-tilaa, ennallaan.

| kuva | tehtävä | ratkaisukenttä ennen → jälkeen |
|---|---|---|
| stack-1280 | lyhyt | 704 px → 1216 px |
| stack-1920 | lyhyt | 828 px → 1656 px (92 rem) |
| side-1280, side-1920, side-390 | pitkä / puhelin | ennallaan |

Tarkistukset: `check_layout.py fy2-6` leveyksillä 360–1920, `check_a11y.py`, `test_writepad.py` (uusi tarkistus: teksti ≤ 44 rem,
kenttä leveämpi ja ≤ 92 rem, Abitti-työkalurivi ikkunan sisällä yläreunassa ja yläpalkin yläpuolella, ei sivuttaisvieritystä).
