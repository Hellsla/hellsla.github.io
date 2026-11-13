# Auditointi tvt-epavarmuus (2026-11-13, --audit-only)

Sisältöhash: fd34db779eea2d90 · Tarkistukset: `guides.py check` ok.

| Arvioija | Tulos | Tila | Raportti |
|---|---|---|---|
| visual-editorial | FAIL | audit (full), ensimmäinen visuaalinen katselmointi | review/visual.md |
| science | PASS (voimassa) | ei ajettu uudelleen | review/science.md |
| pedagogy | PASS (voimassa) | ei ajettu uudelleen | review/pedagogy.md |

Pisteet (vain visuaalisen raportin antamat; muut jätetty tyhjiksi): kuvitus 3 · typografia 3 · suomen kieli 4 · saavutettavuus 3.

## Löydökset
- **Major** (visual): "Tuloksen epävarmuus ja ilmoittaminen" vaihe 2: laskurivit leikkautuvat oikeasta reunasta 390 px:ssä (Δk-rivi menettää yksikön s²/m, Δg-rivi m/s²). 1280 px:ssä sopii. Korjaus jaettuun mathlayout-rivityksessä listakohdissa, ei käsin jaettuna.
- **Minor** (visual): kuvan nimikkeet pieniä 390 px:ssä; katkoviivat lähes yhtyvät sovitussuoraan
- **Minor** (visual): fig-2-kaappaus tyhjä 28×28 (mahdollinen ylimääräinen elementti)
- **Minor** (visual): "m:n" tavallisena symbolina → $m$:n
- **Minor** (visual): vaihe 2 tiivis kappale, viisi kaavaa

Rajaus: kontaktilehtiä, page-390-4/5, page-1280-1/3/4, top-390 ei avattu.

## Kolme arvokkainta korjausta
1. Laskurivien leikkautuminen 390 px:ssä (Major, jaettu mathlayout)
2. Kuvan nimikkeiden koko ja katkoviivojen erottuvuus
3. Vaiheen 2 jakaminen
