# Auditointi fy10-hiuksen-paksuus (2026-11-13, --audit-only)

Sisältöhash: 8969dfde234e43b7 · Tarkistukset: `investigations.py check` ok.

| Arvioija | Tulos | Tila | Raportti |
|---|---|---|---|
| visual-editorial | PASS | audit (full), ensimmäinen visuaalinen katselmointi | review/visual.md |
| science | PASS (voimassa) | ei ajettu uudelleen | review/science.md |
| pedagogy | PASS (voimassa) | ei ajettu uudelleen | review/pedagogy.md |

Pisteet (vain visuaalisen raportin antamat; muut jätetty tyhjiksi): kuvitus 4 · typografia 5 · suomen kieli 5 · saavutettavuus 4.

## Löydökset
- **Minor** (visual): fig-2/4/6/8-kaappaukset ~1 px leveitä (kaappausartefakteja; tarkista screenshot.py:n kuvanumerointi)
- **Minor** (visual): pattern-kuva 390 px: "kaaviokuva, ei mittakaavassa" ja m-merkit pientä tekstiä
- **Minor** (visual): model-kuvaan lyhyt "malli, ei mittaustuloksia" -nimike
- **Minor** (visual): vihjelaatikon "Kuvasta nähdään…" tulee ennen kuvaa (ohjatussa tilassa ok)

Rajaus: top-*, open-ennusta-1280 ja muut 1280-kaappaukset ei avattu erikseen.

## Kolme arvokkainta korjausta
1. pattern-kuvan tekstikoko
2. model-kuvan nimike
3. Kuvakaappausten numerointi (työkalu)
