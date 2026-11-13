# Auditointi fy10-liukukitka (2026-11-13, --audit-only)

Sisältöhash: 8e295e965fd9669d · Tarkistukset: `investigations.py check` ok.

| Arvioija | Tulos | Tila | Raportti |
|---|---|---|---|
| visual-editorial | FAIL | audit (full), ensimmäinen visuaalinen katselmointi | review/visual.md |
| science | PASS (voimassa) | ei ajettu uudelleen | review/science.md |
| pedagogy | PASS (voimassa) | ei ajettu uudelleen | review/pedagogy.md |

Pisteet (vain visuaalisen raportin antamat; muut jätetty tyhjiksi): kuvitus 4 · typografia 4 · suomen kieli 4 · saavutettavuus 4.

## Löydökset
- **Major** (visual): "mitattu kitkakerroin muuttuu noin 0,02 asteen kallistusta kohti" luetaan "0,02 astetta kohti" eikä "0,02 per aste": kallistusvirhe näyttää ~50-kertaa liian pieneltä, eikä yksikköä ole kirjoitettu LaTeXina. Esiintyy "Miksi juuri nämä akselit?" -laatikossa, Teoriaa lyhyesti -kappaleessa ja teacher.md:ssä → "0,02 per kallistusaste (1°)" kaikissa kolmessa
- **Minor** (visual): voimakuva pieni puhelimella, nimikkeet ~10 px
- **Minor** (visual): kaksi kaksoispistettä peräkkäin kallistuslauseessa
- **Minor** (visual): setup-kuvan "liikeanturi"- ja "jarru"-nimikkeet heikot
- **Minor** (visual): nopeuskuvaajan "pysähtyy" ilman asteikkomerkkiä

Rajaus: muut sivun osat ja open-ennusta vain kontaktilehdeltä; parilliset fig-kaappaukset 28×28.

## Kolme arvokkainta korjausta
1. Kallistusvirhelauseen yksikkö kolmessa paikassa (Major)
2. Voimakuvan koko ja nimikkeet
3. Kaksoispisteet
