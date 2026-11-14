VERDICT: PASS
CONTENT-HASH: fb0d0423c711ce05
SCOPE: delta added-exercise from caaeaa93666bca57 base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L2-09 ja L1-01) — lasku on lähes sama: L1-01 antaa kaiun ajaksi 91,0 µs (vastaus 7,01 cm), ja L2-09 lukee kuvasta 90 µs (vastaus 6,93 cm). L2-09:ssä on lisänä kuvaajan lukeminen, joten tehtävä ei ole toisto. Kerroksen paksuus (esim. A–C) olisi kuitenkin erilaisempi kysymys, kunhan se ei ole inquiry-tarkistuksen B–C.
- solutions.md (L2-09, Vastaus) — pyöristysperuste "kuten nopeudessa 1540 m/s" ei nimeä rajoittavaa tietoa. Rajoittava tieto on kuvasta luettu aika 90 µs: lukema on noin ±1 µs:n tarkka, mikä tekee noin 1 %. — Perustele kolme numeroa lukematarkkuudella.
- solutions.md (L1-09, Vastaus) — ilmaus "Aika 20 ms on sovittu tarkaksi" ei ole kurssin käytäntö. — Perustele vastaus merkitsevillä numeroilla.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 5: arvioin muutetun tehtävän L2-09 ja tehtävän L1-09.
- L2-09: d = vt/2 = 1540·90·10⁻⁶/2 m = 6,93 cm, kuten answers.py:ssä. Lukemilla 89 µs ja 91 µs saadaan 6,85 cm ja 7,01 cm, joten ±1 µs:n lukema mahtuu toleranssiin 2 %.
- Kuvassa piikki C on 90 µs:n apuviivalla. Kuvan generaattori, alt-teksti ja ratkaisu ovat yhtäpitäviä. Kuva ei kerro syvyyttä, joten se ei paljasta vastausta.
- Toisto: inquiry-tarkistus kysyy samasta kuvasta kerrosta B–C (3,08 cm, edellinen raporttini). L2-05 käyttää taulukkoa (58,9 µs ja 109,2 µs). L2-09 kysyy luun pinnan syvyyttä ihosta, eikä sitä kysy mikään muu tehtävä.
- Periaate (kaiku kulkee edestakaisin, anturi on iholla) ja järkevyystarkistus (13,9 cm/2) ovat oikein. Syvyys on suurempi kuin A:n (1,54 cm) ja B:n (3,85 cm).
- L1-09: 1402,4·0,020/2 = 14,02 m. Arvo on VERIFIED-riviltä, ja tehtävä on ennallaan.
- Kaikkien kolmen kieliversion answer, unit ja tolerance ovat samat.
