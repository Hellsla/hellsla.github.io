# Auditointi tvt-tyoselostus (2026-11-13, --audit-only)

Sisältöhash: 3336b3617eb6b37b · Tarkistukset: `guides.py check` ok.

| Arvioija | Tulos | Tila | Raportti |
|---|---|---|---|
| visual-editorial | FAIL | audit (full), ensimmäinen visuaalinen katselmointi | review/visual.md |
| science | PASS (voimassa) | ei ajettu uudelleen | review/science.md |
| pedagogy | PASS (voimassa) | ei ajettu uudelleen | review/pedagogy.md |

Pisteet (vain visuaalisen raportin antamat; muut jätetty tyhjiksi): kuvitus 4 · typografia 3 · suomen kieli 4 · saavutettavuus 4.

## Löydökset
- **Major** (visual): guide.md vaihe 4: "y = mx + b", "m on kulmakerroin ja b vakiotermi" ja "m: 4.05 ja b: 0.02" tavallisena tekstinä LaTeX-yhtälön vieressä (eri kirjaintyyppi samassa virkkeessä) → inline-matematiikaksi tai ohjelman ruutu sanatarkaksi lainaukseksi
- **Minor** (visual): kuvatekstiesimerkit suorissa lainausmerkeissä → ”…”
- **Minor** (visual): vaiheen 4 "Jos keksityillä esimerkkiarvoilla…" -virke kömpelö
- **Minor** (visual): fig-2-kaappaus tyhjä 28×28 (mahdollinen ylimääräinen elementti)
- **Minor** (visual): kuvan nimikkeet ~13 px 390 px:ssä
- **Minor** (visual): vaihe 8 yhdistää kaksi ajatusta yhteen virkkeeseen

Rajaus: kontaktilehteä ja top-kaappauksia ei avattu erikseen.

## Kolme arvokkainta korjausta
1. Vaiheen 4 symbolit matematiikkana (Major)
2. Lainausmerkit ja kömpelö virke
3. Vaiheen 8 jakaminen
