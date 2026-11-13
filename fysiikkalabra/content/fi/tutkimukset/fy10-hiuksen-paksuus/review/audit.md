# Auditointi fy10-hiuksen-paksuus (2026-11-13, --audit-only)

Sisältöhash: 8969dfde234e43b7 · Tarkistukset: `investigations.py check` ok.

| Arvioija | Tulos | Tila | Raportti |
|---|---|---|---|
| visual-editorial | FAIL | audit (full), ensimmäinen visuaalinen katselmointi | review/visual.md |
| science | PASS (voimassa) | ei ajettu uudelleen | review/science.md |
| pedagogy | PASS (voimassa) | ei ajettu uudelleen | review/pedagogy.md |

Pisteet (vain visuaalisen raportin antamat; muut jätetty tyhjiksi): kuvitus 3 · typografia 4 · suomen kieli 4 · saavutettavuus 4.

## Löydökset
- **Major** (visual): "pattern"-kuva (Teoriaa lyhyesti): kertalukujen m numerot ja asteikkomerkit ovat kirkkaiden pisteiden alla, mutta teksti määrittelee m:n tummien minimien kertaluvuksi (keskimaksimin reunat ovat m = 1); kuva houkuttelee numeroimaan kirkkaita pisteitä, juuri sitä opettajan huomautusten virhekäsitystä, eikä minimejä näytetä lainkaan → siirrä merkit tummiin väleihin ja nimeä ne minimeiksi, säilytä kaaviokuvamerkintä
- **Minor** (visual): geometry-kuvan nimikkeet (hius, θ_m, säde) ~11 px puhelimella
- **Minor** (visual): model-kuvan kulmakolmion nimikkeet Δm, Δx_m harmaat ja pienet; kaava kelluu akselinimikkeen lähellä
- **Minor** (visual): Mittaa-taulukon otsakesarake 2x_m (m) kapea 390 px:ssä; tyhjällä taulukolla ei kuvatekstiä, että se on pohja
- **Minor** (visual): "Päätät itse" -kappale 120+ sanaa, "työtavassa" toistuu → yksi kappale per työtapa
- **Minor** (visual): tieteellinen huomio: pattern-kuvan keskimaksimi piirretty vain noin kaksi kertaa sivumaksimeja leveämmäksi (teksti sanoo samoin, yhdenmukainen)

Rajaus: contact-2/3 ja useimmat muut sivun osat ei avattu. Huom.: tämän tutkimuksen ensimmäinen ajo antoi PASS, mutta raporttitiedosto ei tallentunut; uusinta-ajo antoi FAIL (Major) — arvioijien välinen vaihtelu, tulos kannattaa varmistaa korjauksen yhteydessä.

## Kolme arvokkainta korjausta
1. pattern-kuvan m-merkinnät minimeille (Major)
2. geometry- ja model-kuvien nimikkeiden koko
3. Päätät itse -kappaleen jakaminen
